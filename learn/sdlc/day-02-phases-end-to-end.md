# Day 2 — Classic Phases End to End

## Phase inputs & outputs

| Phase | Input | Output |
|-------|-------|--------|
| Requirements | user needs/business goals | requirements document |
| Design | requirements document | technical design doc |
| Implementation | technical design doc | working source code |
| Testing | working source code | test report/bug list |
| Deployment | working source code (tested & approved) | live version in production |
| Maintenance | live version in production | update/patch records |

## Handoffs & Definition of Done

### Design → Implementation
**Done means:** The technical design document is finished and approved by the team.
**What passes to devs:** The technical design doc, API diagrams, and technical constraints/decisions.

### Testing → Release (Deployment)
**Done means:** All critical bugs found during testing are fixed and closed, and the team lead approves the release.
**What passes to release:** tested build, test report, release approval, version tag

## Roles snapshot

| Role | Heavily influences these phases | What they do (1 line) |
|------|--------------------------------|-------------------------|
| PM / PO | Requirements | Specify user needs and business goals |
| Designer | Design | Create the architecture and technical design |
| Developer | Implementation | Turn the design into working source code |
| QA | Testing | Test the code and produce the bug list / test report |
| DevOps | Deployment, Maintenance | Release the software to production and keep it running smoothly |


## Mini timeline (small feature example)

**Feature:** "WhatsApp nickname"

| Step | Phase | What happens |
|------|-------|--------------|
| 1 | Requirements | Team decides users need custom nicknames |
| 2 | Design | Plan where nickname shows and who can edit it |
| 3 | Implementation | Developers code the nickname feature |
| 4 | Testing | QA checks limits, empty names, conflicts |
| 5 | Deployment | Feature is released to all users |
| 6 | Maintenance | Bugs are fixed, small improvements added |