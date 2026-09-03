"""
Day 87 — Business model lab (no LLM). Price covers TCO. Jail stays on free tier.

Do not sell "no HITL, fully autonomous" as the SKU.
"""

from __future__ import annotations

from proto_lab import self_modify

TCO_CENT = 14
MARGIN = 2
PLANS = {
    "free": {"jail": True, "hitl": True, "price": 0},
    "pro": {"jail": True, "hitl": True, "price": TCO_CENT * MARGIN},
}


def price_ok(price: int, tco: int = TCO_CENT) -> bool:
    return price >= tco


def sell(sku: str) -> dict:
    if sku == "autonomous_no_hitl":
        return {"ok": False, "error": "unsafe_sku"}
    plan = PLANS.get(sku)
    if not plan:
        return {"ok": False, "error": "unknown"}
    return {"ok": True, **plan}


def demo() -> None:
    print("Day 87 biz lab. TCO + margin. Jail on free. No LLM.\n")

    print("A) free tier still has jail")
    print(" ", sell("free"))
    print("  jail_locked:", self_modify("check_input")["error"])

    print("\nB) price covers TCO")
    p = sell("pro")["price"]
    print("  pro_price:", p, "covers_tco:", price_ok(p))
    print("  too_cheap:", price_ok(1))

    print("\nC) no HITL SKU is not sold")
    print(" ", sell("autonomous_no_hitl"))


if __name__ == "__main__":
    demo()
