# AGENTS.md

Guidance for AI agents working in this repository.

## Project overview

**E-Learning Portal** is currently a documentation-focused Python learning repository. It contains:

- `README.md` — complete single-page Python learning roadmap
- `Python-Mastery/` — 110 topic-level lessons plus indexes for portable documentation imports
- `python-learning-roadmap/` — nested curriculum directory with level and topic README files
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
- **Build:** Run `python3 tools/sync_knowledge_base.py` after editing topic files to update the single-page root README.
- **Validate:** Run `python3 tools/validate_knowledge_base.py` to check topic coverage, required sections, Python syntax, diagrams, roadmaps, and relative links.
- **Run:** There is no dev server. Validate documentation changes with the commands above and `git status`.

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

Refer to the root `README.md` and `python-learning-roadmap/README.md` first once application setup instructions are added.

### Tooling available on the VM

Python 3.12+ and Node.js 22+ are available system-wide for future scaffolding. No project-specific version pins exist yet.
