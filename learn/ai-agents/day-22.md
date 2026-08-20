# Day 22 — Multi-Modal Agents: Vision and Audio

**Status:** Done (2026-08-20)  
**Phase:** 21–25 Orchestration & Operations — day 2

## Goal

Ingest **images** (VLM) and treat **audio** as transcribe-then-text so Yoyo stays a text workflow after ingest.

## Concepts

| Term | Meaning |
|------|---------|
| Multi-modal | Text, image, audio, video as inputs |
| VLM | Model that reads pixels and text together |
| Transcription | Speech → written text before the usual agent |

## Practice

- [vision_agent.py](./practice/vision_agent.py) — local VLM, jail = `practice/media/`
- Demo bands PNG generated on first run (`media/demo_bands.png`)

Happy path (`9e8bb2cc`): left blue, middle white/light, right red.  
Jail (`dd905a3a`): `win.ini` → `ok: false`, extension rejected (no model call for that file).

VLM also labeled the bands as the French flag — extra inference, not in the pixels as text. Ground the next step (add_task) on colors/layout, not on a guessed proper noun.

## Audio (concept, same pipeline)

`kayıt → transkript → özet / action items → HITL → tools`. Do not log raw audio or secrets.

## Security smell-check

No remote image URLs (SSRF). Size cap 5 MB. Path jail. User text still goes through `check_input`. Screenshots can carry prompt-injection text — treat image-derived instructions as untrusted.

## Next

Day 23 — Agent security and privacy (injection, leakage, tool auth).
