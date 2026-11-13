# Forge — 10-day sprint plan

Target: **2026-11-13 to 2026-11-22**, roughly 90 hours.
Scope decision: **balanced** — touch every learning goal, get most of them properly,
accept a modest benchmark number rather than a competitive one.

## What "done" means on day 10

A working end-to-end system: an agent that takes a real issue, localises the fault,
patches it, proves the patch with tests, and reports a measured score on a small
benchmark subset — served by a self-hosted model, exposed over an API and a minimal
UI, with its own MCP server, running in CI.

Explicitly **not** in scope for the 10 days: a competitive SWE-bench score, a polished
frontend, Kubernetes, Terraform, deep observability, LangGraph in depth.

## Day by day

| Day | Date | Hours | Focus |
|---|---|---|---|
| 1 | Fri 13 Nov | ~3 | **Phase 0** repo, uv, ruff/mypy/pytest, pre-commit, CI. async/await primer. |
| 2 | Sat 14 Nov | ~16 | **Phase 1** LLM gateway: provider abstraction, async httpx, streaming, retries, structured output. **Phase 2** tool-calling protocol and agent loop v1, written from scratch. |
| 3 | Sun 15 Nov | ~16 | **Phase 3** Docker sandbox for untrusted code. Tools: read, search, edit, run. Loop hardening: step limits, timeouts, error recovery. |
| 4 | Mon 16 Nov | ~5 | **Phase 4** code indexing — tree-sitter AST parsing, symbol and import graph. |
| 5 | Tue 17 Nov | ~5 | **Phase 5** retrieval and fault localisation. Embeddings, pgvector, hybrid search. |
| 6 | Wed 18 Nov | ~5 | **Phase 6** verification loop: reproduce, patch, test, self-repair. |
| 7 | Thu 19 Nov | ~5 | **Phase 7** eval harness, benchmark subset, **first number**. Trace logging. |
| 8 | Fri 20 Nov | ~5 | **Phase 8** FastAPI backend, Postgres persistence of runs and traces. |
| 9 | Sat 21 Nov | ~16 | **Phase 9** MCP server exposing Forge tools + MCP client consuming an external server. **Phase 10** minimal frontend (scaffolded). |
| 10 | Sun 22 Nov | ~16 | **Phase 11** Docker Compose, CI eval gate, observability, inference routing (Relay), writeup. |
| 11-14 | stretch | — | **Fine-tuning**: curate traces, LoRA on Kaggle T4s, merge, GGUF, serve via Ollama, measure against baseline. |

## Risks

- **Slow inference eats schedule.** Every agent test takes minutes on a 1080 Ti.
  Budget 30% more than feels necessary. Iterate against a tiny benchmark subset.
- **Fatigue.** 5-6 hours after a full work day, ten days running. One sick day
  breaks the plan; keep slack.
- **Context window.** Code is token-heavy. Expect to fight KV cache limits by day 3.

## Current position

Day 1 — Phase 0 complete.
