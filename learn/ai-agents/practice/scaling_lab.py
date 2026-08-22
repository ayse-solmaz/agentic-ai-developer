"""
Day 39 — Scaling & performance lab (no real LLM bill).

Ideas under test:
  cache     = same question → skip fake LLM (latency + cost)
  route     = local / cheap / expensive (Day 24)
  load test = concurrent workers → throughput + latency percentiles
  scale     = vertical (bigger box) vs horizontal (more replicas) — printed as design note

Uses hierarchical_yoyo.handle for local paths; fake_llm sleep for "model" work.
"""

from __future__ import annotations

import statistics
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from threading import Lock

from hierarchical_yoyo import handle
from yoyo_qa import cache_key, classify, est_tokens

# --- lab knobs -------------------------------------------------------------

FAKE_LLM_MS = 120  # stand-in for one model round-trip
CACHE_TTL_SEC = 3600
USD_PER_1K = 0.002  # fake expensive-tier price for cost math
WORKERS = 8
LOAD_N = 40


@dataclass
class CacheEntry:
    text: str
    saved_at: float


@dataclass
class RunStats:
    latencies_ms: list[float] = field(default_factory=list)
    cache_hits: int = 0
    llm_calls: int = 0
    est_usd: float = 0.0
    ok: int = 0
    fail: int = 0
    routes: dict[str, int] = field(default_factory=dict)

    def add(self, *, ms: float, hit: bool, llm: int, usd: float, success: bool, route: str) -> None:
        self.latencies_ms.append(ms)
        if hit:
            self.cache_hits += 1
        self.llm_calls += llm
        self.est_usd += usd
        if success:
            self.ok += 1
        else:
            self.fail += 1
        self.routes[route] = self.routes.get(route, 0) + 1


_cache: dict[str, CacheEntry] = {}
_cache_lock = Lock()
_stats_lock = Lock()


def fake_llm(question: str) -> str:
    """Slow, billable stand-in. Never call a real API in this lab."""
    time.sleep(FAKE_LLM_MS / 1000)
    return f"[fake-llm] kısa cevap: {question[:40]}"


def cached_answer(question: str, *, use_cache: bool) -> tuple[str, bool, int, float, str, bool]:
    """
    Returns: text, cache_hit, llm_calls, est_usd, route, ok
    """
    kind = classify(question)
    if kind == "block":
        return "blocked", False, 0, 0.0, "block", False

    if kind == "local":
        raw = handle(question)
        return (
            str(raw.get("text", "")),
            False,
            0,
            0.0,
            str(raw.get("route", "local")),
            bool(raw.get("ok")),
        )

    # cheap / expensive → model path (fake), with optional cache
    key = cache_key(question)
    now = time.time()
    if use_cache:
        with _cache_lock:
            hit = _cache.get(key)
            if hit and now - hit.saved_at < CACHE_TTL_SEC:
                return hit.text, True, 0, 0.0, f"{kind}+cache", True

    calls = 2 if kind == "expensive" else 1
    # one sleep models "one round-trip"; expensive counts 2× cost without 2× wait
    text = fake_llm(question)
    if kind == "expensive":
        text = "[tot×2] " + text
    tokens = est_tokens(question) + est_tokens(text)
    usd = round((tokens / 1000) * USD_PER_1K * calls, 6)

    if use_cache:
        with _cache_lock:
            _cache[key] = CacheEntry(text=text, saved_at=now)

    return text, False, calls, usd, kind, True


def one_request(question: str, *, use_cache: bool, stats: RunStats) -> None:
    t0 = time.perf_counter()
    _text, hit, llm, usd, route, ok = cached_answer(question, use_cache=use_cache)
    ms = (time.perf_counter() - t0) * 1000
    with _stats_lock:
        stats.add(ms=ms, hit=hit, llm=llm, usd=usd, success=ok, route=route)


def load_mix(n: int) -> list[str]:
    """
    Mix for load test:
      ~50% repeated FAQ (cache wins)
      ~25% local (0 LLM)
      ~15% unique cheap
      ~10% expensive / block
    """
    faq = "yoyo nedir ve ne ise yarar"
    local = "bugün ne var"
    qs: list[str] = []
    for i in range(n):
        r = i % 10
        if r < 5:
            qs.append(faq)
        elif r < 8:
            qs.append(local)
        elif r == 8:
            qs.append(f"ucuz soru numarasi {i}")
        else:
            qs.append("planla dengeli gun tot")
    return qs


def run_load(label: str, questions: list[str], *, use_cache: bool, workers: int) -> RunStats:
    stats = RunStats()
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futs = [pool.submit(one_request, q, use_cache=use_cache, stats=stats) for q in questions]
        for f in as_completed(futs):
            f.result()
    wall = time.perf_counter() - t0
    report(label, stats, wall, workers)
    return stats


def pct(sorted_vals: list[float], p: float) -> float:
    if not sorted_vals:
        return 0.0
    idx = min(len(sorted_vals) - 1, int(round((p / 100) * (len(sorted_vals) - 1))))
    return sorted_vals[idx]


def report(label: str, stats: RunStats, wall_s: float, workers: int) -> None:
    n = len(stats.latencies_ms) or 1
    lat = sorted(stats.latencies_ms)
    print(f"\n=== {label}  (workers={workers}) ===")
    print(f"requests:     {n}")
    print(f"ok / fail:    {stats.ok} / {stats.fail}")
    print(f"wall_s:       {wall_s:.3f}")
    print(f"throughput:   {n / wall_s:.1f} req/s")
    print(f"latency_ms:   avg={statistics.mean(lat):.1f}  p50={pct(lat, 50):.1f}  p95={pct(lat, 95):.1f}")
    print(f"cache_hits:   {stats.cache_hits}  ({100 * stats.cache_hits / n:.0f}%)")
    print(f"llm_calls:    {stats.llm_calls}")
    print(f"est_usd:      {stats.est_usd:.6f}")
    print(f"routes:       {dict(sorted(stats.routes.items()))}")


def design_notes() -> None:
    print(
        """
--- Scaling design (agent API @ ~1000 req/min) ---
Horizontal: more API replicas behind a load balancer (stateless ask handlers).
            Shared cache (Redis) so every replica sees FAQ hits.
Vertical:   bigger CPU/RAM on one box - helps local classify; does NOT multiply LLM QPS.
Bottleneck: almost always the model / rate limits, not Python.
Optimize:   route local first -> cache FAQ -> cheaper model -> batch -> then scale out.
Load test:  find the knee (errors up or p95 up) before users do.
"""
    )


def main() -> None:
    global _cache
    qs = load_mix(LOAD_N)
    print("Day 39 scaling lab. Fake LLM sleep = billable wait. No API keys used.\n")
    print(f"load mix: {LOAD_N} requests, workers={WORKERS}, fake_llm={FAKE_LLM_MS}ms")

    _cache = {}
    cold = run_load("A) cold (no cache)", qs, use_cache=False, workers=WORKERS)

    _cache = {}
    warm = run_load("B) warm (cache ON)", qs, use_cache=True, workers=WORKERS)

    design_notes()

    saved_calls = cold.llm_calls - warm.llm_calls
    saved_usd = cold.est_usd - warm.est_usd
    print("--- Check ---")
    print(f"LLM calls saved by cache: {saved_calls}  (cold {cold.llm_calls} -> warm {warm.llm_calls})")
    print(f"Est USD saved:            {saved_usd:.6f}")
    print("Expect: warm cache_hits > 0, warm throughput >= cold, warm est_usd <= cold.")


if __name__ == "__main__":
    main()
