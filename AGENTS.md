# AGENTS.md

Guidance for AI agents working in this repository.

## Project overview

**E-Learning Portal** is currently a placeholder repository. It contains:

- `README.md` — project title only
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
- **Lint / test / build:** No scripts exist. Skip unless new tooling is added to the repo.
- **Run:** There is no dev server. Validate changes with `git status` and file checks until an app is scaffolded.

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

Refer to the root `README.md` first once it includes setup instructions.

### Tooling available on the VM

Python 3.12+ and Node.js 22+ are available system-wide for future scaffolding. No project-specific version pins exist yet.
