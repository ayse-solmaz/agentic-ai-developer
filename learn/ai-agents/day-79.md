# Day 79 — IoT and Edge Agents

**Status:** Done (2026-09-03)  
**Phase:** 76–80 Specialized Agents (II) — day 4

## Goal

Local threshold, works offline. Actuators on an allowlist. Unlock is HITL. Inject is not a command.

## Dictionary (plain)

| Term | Meaning |
|------|---------|
| IoT agent | Sensors + allowlisted actuators |
| Edge computing | Decide next to the device; offline ok |
| Resource constraints | Rule/small model, not ToT every tick |
| Real-time | Event → action now |

## Practice

- [edge_lab.py](./practice/edge_lab.py)

## Check (your run)

| Piece | Result |
|-------|--------|
| A | `fan_on` |
| B | `fan_on` offline |
| C | `HITL_act` |
| D | `deny` |
| E | `block` |

## Next

Day 80 — phase 76–80 review.
