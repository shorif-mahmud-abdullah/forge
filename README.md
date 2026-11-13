# Forge

An autonomous code-fixing agent. Give it a repository and an issue; it localises the
fault, writes a patch, proves the patch with tests, and opens a pull request.

It runs on **self-hosted open models** (Ollama on 2x GTX 1080 Ti), which makes
inference efficiency a first-class engineering problem rather than an afterthought.

## Status

Phase 0 — project skeleton. See [docs/PLAN.md](docs/PLAN.md).

## Requirements

- Python 3.12 (managed by `uv`)
- [uv](https://docs.astral.sh/uv/)
- Docker (sandboxed execution of agent-generated code)
- An LLM endpoint — Ollama over an SSH tunnel, or a cloud fallback

## Setup

```bash
uv sync --all-groups
uv run pre-commit install
cp .env.example .env
```

Open the tunnel to the GPU box in a separate terminal:

```bash
ssh -N gpu
```

Verify it:

```bash
curl http://localhost:11434/v1/models
```

## Commands

| Task | Command |
|---|---|
| Install | `uv sync --all-groups` |
| Lint | `uv run ruff check .` |
| Format | `uv run ruff format .` |
| Type check | `uv run mypy` |
| Test | `uv run pytest` |
| All gates | `uv run ruff check . && uv run ruff format --check . && uv run mypy && uv run pytest` |

## Layout

```
src/forge/        application package (src layout: forces installation, catches packaging bugs)
tests/            pytest suite
docs/             plan, architecture notes, learning log
docker/           sandbox and compose definitions
.github/workflows CI
```
