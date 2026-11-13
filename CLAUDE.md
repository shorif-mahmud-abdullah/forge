# Forge — working agreement

This file is loaded automatically by Claude Code in any session opened in this
repository, on any machine. It is the project's memory. Keep it current.

## What this project is

An autonomous code-fixing agent. Input: a repository plus an issue. Output: a
patch that is proven by tests, submitted as a pull request. Scored on a subset of
SWE-bench Lite.

It is also a deliberate learning vehicle for: RAG, agent development, agentic AI,
MCP, LLM fine-tuning, and production DevOps.

## Who is building it

Shorif, learning this stack intensively. Self-rated levels:

| Python | Git | SQL | React | Docker | Linux CLI | async/await |
|---|---|---|---|---|---|---|
| 4/5 | 3/5 | 2/5 | 1/5 | 1.5/5 | 2.5/5 | 1/5 |

Implications: **Docker and async need real teaching** (both are load-bearing here).
**React is near zero** — scaffold the frontend, let him learn by modifying it.
SQL is taught from the ground up when Postgres/pgvector arrive.

## How to work with him — non-negotiable

Every new topic follows this loop. Never lead with code.

1. **Concept** — what problem it solves, why it exists, trade-offs. No code.
2. **Checkpoint** — ask 2-3 questions. If he can't answer, go back to 1.
3. **Design** — present options with a recommendation; he decides.
4. **Build** — state up front which parts he writes and which you write. He always
   gets the conceptually interesting part; you take boilerplate and glue.
5. **Review & measure** — review his code honestly. Record a number.
6. **Log** — append a few sentences to `docs/learning-log/`.

Be direct. Say when something is a bad idea. Do not pad with praise.

## Hard constraints

- **No paid LLM API.** Inference runs on an office GPU box reached over SSH:
  `ssh -N gpu` tunnels `localhost:11434` to Ollama there. Models available include
  `qwen3.5:9b`, `qwen3:14b`, `gemma3:12b`.
- **Hardware: 2x GTX 1080 Ti, 11 GB each. Pascal, compute capability 6.1.**
  No tensor cores. FP16 runs at 1/64 of FP32 rate. No FlashAttention, no Unsloth,
  unreliable bitsandbytes 4-bit. CUDA 13 dropped Pascal — pin PyTorch to a cu12x
  build with `sm_61` kernels.
- **Therefore: train on Kaggle (2x T4, 30 h/week free), serve on the office GPUs.**
- **Fine-tuning teacher must be `qwen3:14b` (Apache 2.0), never Gemini/Groq output** —
  cloud provider terms restrict using outputs to train models.
- Context length, not model size, is the VRAM battle. A 9B model at 32k context needs
  roughly 4-5 GB of KV cache on top of 6.6 GB of weights. Knobs: split across both
  GPUs, or `OLLAMA_KV_CACHE_TYPE=q8_0`.
- Qwen3 emits large `reasoning` blocks by default. Control thinking mode explicitly;
  an unguarded "hello" cost 896 completion tokens.
- No company data in this repo. Public or synthetic only.

## Timeline

Ten-day sprint, roughly 90 hours, ending 2026-11-22. See `docs/PLAN.md` for the
day-by-day breakdown and current position. Fine-tuning is expected to land on days
11-14 because it needs trace data that only exists once the system runs.

## Conventions

- `src/` layout. Package is `forge`.
- `uv` for dependencies; `uv.lock` is committed and authoritative.
- Config only through `forge.config.Settings` (pydantic-settings, `FORGE_` prefix).
  Never hardcode a URL, model name or key.
- ruff + mypy `strict` + pytest must all pass before a commit. `pre-commit` enforces it.
- Conventional commits (`feat:`, `fix:`, `docs:`, `chore:`). Feature branch per phase,
  PR into `main`.

## Commands

```bash
uv sync --all-groups                 # install
uv run pytest                        # tests
uv run mypy                          # types
uv run ruff check . && uv run ruff format --check .
ssh -N gpu                           # tunnel to Ollama
```
