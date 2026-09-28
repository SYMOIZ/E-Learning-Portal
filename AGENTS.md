# AGENTS.md

Guidance for AI agents working in this repository.

## Project overview

**E-Learning Portal** is currently a documentation-focused Python learning repository. It contains:

- `Python-Mastery/` — maintainable topic-by-topic knowledge base (110 lessons: 35 Beginner, 35 Intermediate, 40 Advanced) plus Infographics, CheatSheets, Glossary, Assessments, Interview-Questions, Projects, Roadmaps, and Study-Guides
- `README.md` — complete single-page synchronized edition of the same curriculum
- `python-learning-roadmap/` — older nested deep-dive companion curriculum
- `tools/` — `sync_knowledge_base.py` and `validate_knowledge_base.py` for README parity and quality checks
- `A Smarter Way to Learn Python .pdf` — static Python learning material (241 pages)

There is no application source code, package manifests, Docker configuration, or CI setup yet.

## Cursor Cloud specific instructions

### Services

| Service | Status | Notes |
|---------|--------|-------|
| Web app / API | Not present | Nothing to start or hot-reload |
| Database / cache | Not present | No external services required |
| Static PDF resource | Present | Readable at repo root; no server needed for local file access |

### Development workflow

- **Dependencies:** None to install. The VM update script is a no-op (`true`).
- **Lint / test / build:** After editing topic lessons under `Python-Mastery/`, run:
  - `python3 tools/sync_knowledge_base.py` — rebuild root `README.md` from topic files
  - `python3 tools/validate_knowledge_base.py` — require 110 topics, section structure, example AST syntax, self-contained example `NameError` checks, Mermaid blocks, roadmaps, study guides, cheat sheets, infographic maps, glossary, checkpoints, project briefs, and relative links
- **Run:** There is no dev server. Prefer the validators above plus `git status` / PDF checks until an app is scaffolded.
- **Canonical lesson source:** Edit files in `Python-Mastery/{Beginner,Intermediate,Advanced}/` first; treat root `README.md` as the generated single-page mirror.

### Validating the learning resource

To confirm the PDF asset is intact:

```bash
file "A Smarter Way to Learn Python .pdf"
```

Expected output includes `PDF document` and `241 page(s)`.

To serve the static asset over HTTP (optional smoke test only):

```bash
python3 -m http.server 8080
```

Then fetch with `curl -I http://127.0.0.1:8080/A%20Smarter%20Way%20to%20Learn%20Python%20.pdf` and expect `HTTP/1.0 200 OK`.

### When adding an application later

Document in this file:

1. Required services and startup commands (with ports)
2. Environment variables (`.env.example`)
3. Non-obvious setup steps (migrations, seed data, etc.)

Refer to `Python-Mastery/README.md`, the root `README.md`, and `python-learning-roadmap/README.md` first once application setup instructions are added.

### Tooling available on the VM

Python 3.12+ and Node.js 22+ are available system-wide for future scaffolding. No project-specific version pins exist yet.
