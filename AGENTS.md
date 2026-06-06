# AGENTS.md

Guidance for AI agents working in this repository.

## Project overview

**E-Learning Portal** is a Python learning knowledge base containing:

- `README.md` — complete Python Learning Roadmap (~110 topics, 3 levels)
- `Python-Mastery/` — per-topic markdown files for NotebookLM, Obsidian, and Notion
- `A Smarter Way to Learn Python .pdf` — supplementary static learning material

## Cursor Cloud specific instructions

### Services

| Service | Status | Notes |
|---------|--------|-------|
| Web app / API | Not present | Knowledge base is static markdown |
| Database / cache | Not present | No external services required |
| Static PDF resource | Present | At repo root |

### Regenerating the knowledge base

If topic content in `scripts/topic_snippets.py` changes:

```bash
python3 scripts/generate_knowledge_base.py
```

This updates `README.md` and all files under `Python-Mastery/`.

### Development workflow

- **Dependencies:** None required for markdown. Python 3.12+ needed only to run the generator.
- **Lint / test / build:** No application tests. Validate generator output with the command above.
- **Run:** No dev server. Optional PDF smoke test documented in previous setup.

### Tooling available on the VM

Python 3.12+ and Node.js 22+ are available system-wide.
