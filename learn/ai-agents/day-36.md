# Day 36 — Containerization and Orchestration

**Status:** Done (2026-08-22)  
**Phase:** 36–40 Production Deployment — day 1

## Goal

Package Yoyo so it runs the same way outside the laptop venv: image + runtime config (keys outside the image).

## Check (your run)

- `docker compose build` → `Image yoyo-arch:day36 Built`
- `docker compose run --rm yoyo` →  
  `routes: ['hierarchy', 'hierarchy', 'hierarchy', 'block', 'out_of_domain', 'unhandled']`

## Files

- [Dockerfile](./practice/Dockerfile)
- [docker-compose.yml](./practice/docker-compose.yml)
- [requirements-docker.txt](./practice/requirements-docker.txt)
- [.dockerignore](./practice/.dockerignore)

## Next

Day 37 — expose the agent as an API (REST).
