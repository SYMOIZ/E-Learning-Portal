# NotebookLM, Obsidian, and Notion Import Guide

[← Study guides](./README.md) · [Knowledge base](../README.md)

This knowledge base is Markdown-first. Each of the 110 topic files is a self-contained lesson with overview, objectives, applications, core concepts, infographic blocks, syntax, three examples, and a Mermaid workflow.

## Recommended Folder Structure

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
├── Study-Guides/
└── README.md
```

Upload or clone this folder as-is. Do not flatten Beginner, Intermediate, and Advanced into one directory; NotebookLM and Obsidian both benefit from the level split.

## NotebookLM

1. Create a notebook named **Python Mastery**.
2. Add sources in this order so retrieval stays grounded:
   - `Python-Mastery/README.md`
   - `Python-Mastery/Beginner/` (all 35 files)
   - `Python-Mastery/Intermediate/` (all 35 files)
   - `Python-Mastery/Advanced/` (all 40 files)
   - `Python-Mastery/Roadmaps/` if you want career-path answers
   - one study guide (`12-week-plan.md` or `24-week-plan.md`)
3. Ask questions that name a topic, for example: “Explain generators using the intermediate and advanced examples.”
4. Keep the root single-page `README.md` **out** of the same notebook if you already imported the split lessons; the two editions duplicate the same 110 topics.

### Source Selection Tips

| Goal | Sources to enable |
| --- | --- |
| Learn one topic | That topic file only |
| Compare related topics | 2–5 sibling files, such as Lists + List Methods |
| Career planning | `Roadmaps/` plus `Projects/README.md` |
| Interview prep | Topic file plus `Interview-Questions/README.md` |

## Obsidian

1. Open `Python-Mastery/` as a vault, or copy it into an existing vault.
2. Start from `README.md` as the map of content.
3. Graph view works because lessons use relative Markdown links, not bare filenames.
4. Mermaid diagrams render in Reading View.
5. Optional: pin `Study-Guides/12-week-plan.md` or `24-week-plan.md` in the sidebar as a daily note index.

Do not add YAML frontmatter to topic files. The sync tool treats `# Topic Name` through the footer separator as the canonical lesson body.

## Notion

1. Import the `Python-Mastery` folder with **Import → Markdown**.
2. Keep subpages nested under Beginner, Intermediate, and Advanced.
3. Notion may not render Mermaid; keep the fenced `mermaid` blocks as source diagrams, or paste them into a Mermaid-capable block.
4. Turn `Projects/README.md` and `Roadmaps/README.md` into linked databases if you want status tracking.

## GitHub and Documentation Portals

- GitHub renders relative links, tables, infographic emoji blocks, and Mermaid.
- MkDocs, Docusaurus, and similar portals can map `Python-Mastery/` as a docs root.
- The repository root `README.md` remains the single-page edition for full-text search.

## Quality Checklist After Import

- [ ] 110 topic files are present (35 / 35 / 40).
- [ ] Each topic still has one Mermaid workflow.
- [ ] Career roadmaps still include a **Demonstrate** column.
- [ ] Relative links such as `[Installing Python →](../Beginner/02-installing-python.md)` still resolve.
