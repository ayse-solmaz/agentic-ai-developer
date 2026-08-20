"""
Day 28 — Measure first. Fake LLM = sleep (no API bill).

Bottleneck here is waiting on the model, not Python classify.
"""

from __future__ import annotations

import time
from concurrent.futures import ThreadPoolExecutor

from yoyo_qa import classify


def fake_llm(ms: int = 200) -> None:
    """Stand-in for a slow Gemini call."""
    time.sleep(ms / 1000)


def bench_classify(n: int = 2000) -> float:
    t0 = time.perf_counter()
    for _ in range(n):
        classify("bugün ne var")
    return time.perf_counter() - t0


def sequential_three() -> float:
    t0 = time.perf_counter()
    fake_llm()
    fake_llm()
    fake_llm()
    return time.perf_counter() - t0


def parallel_three() -> float:
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(lambda _: fake_llm(), range(3)))
    return time.perf_counter() - t0


def main() -> None:
    print("Day 28 perf lab. LLM yok; sleep = yavas API.\n")

    elapsed = bench_classify()
    n = 2000
    print(f"Benchmark classify x{n}: {elapsed*1000:.1f} ms  "
          f"({n/elapsed:.0f} istek/s yerel)")

    seq = sequential_three()
    par = parallel_three()
    print(f"3 sahte LLM ardışık: {seq*1000:.0f} ms  (latency ~ toplam)")
    print(f"3 sahte LLM paralel: {par*1000:.0f} ms  (latency ~ en yavasi)")
    print("\nDarboğaz: fake_llm wait, classify degil.")
    print("Yoyo: list/remind = classify/local, bu sleep'e hic girme (Day 24).")


if __name__ == "__main__":
    main()
