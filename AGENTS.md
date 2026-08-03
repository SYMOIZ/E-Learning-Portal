# AGENTS.md

Guidance for AI agents working in this repository.

## Project overview

**E-Learning Portal** is a documentation-focused Python learning repository. It contains:

- `README.md` — canonical single-page Python Learning Roadmap (110 topics across 3 levels)
- `Python-Mastery/` — topic-by-topic knowledge base for NotebookLM, Obsidian, Notion, and docs portals
- `python-learning-roadmap/` — nested deep-dive companion curriculum with practice questions
- `tools/` — sync and validation scripts for the knowledge base
- `A Smarter Way to Learn Python .pdf` — static Python learning material (241 pages)

There is no application source code, package manifests, Docker configuration, or CI setup yet.

## Knowledge base layout

```text
Python-Mastery/
├── Beginner/              # 35 topic documents
├── Intermediate/          # 35 topic documents
├── Advanced/              # 40 topic documents
├── Infographics/
├── CheatSheets/
├── Interview-Questions/
├── Projects/
├── Roadmaps/
└── README.md
```

Topic files in `Python-Mastery/{Beginner,Intermediate,Advanced}` are the maintainable lesson source. The root `README.md` is the synchronized single-page edition.

## Cursor Cloud specific instructions

### Services

| Service | Status | Notes |
|---------|--------|-------|
| Web app / API | Not present | Nothing to start or hot-reload |
| Database / cache | Not present | No external services required |
| Static PDF resource | Present | Readable at repo root; no server needed for local file access |

### Development workflow

- **Dependencies:** None to install. The VM update script is a no-op (`true`).
- **Lint / test / build:** No application scripts exist. For knowledge-base edits, run the tools below.
- **Run:** There is no dev server. Validate documentation changes with the knowledge-base tools and `git status`.

### Knowledge base maintenance

After editing topic lessons:

```bash
python3 tools/sync_knowledge_base.py
python3 tools/validate_knowledge_base.py
```

Validation checks 110 topic files, required sections and infographic labels, root/split parity, Python example AST syntax, Mermaid blocks, final roadmaps, relative links, and PDF presence.

Weekly automation branches often start without `Python-Mastery/`. Prefer restoring from the latest complete knowledge-base branch rather than regenerating from scratch when content already exists.

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

Refer to the root `README.md` and `Python-Mastery/README.md` first once application setup instructions are added.

### Tooling available on the VM

Python 3.12+ and Node.js 22+ are available system-wide for future scaffolding. No project-specific version pins exist yet.
