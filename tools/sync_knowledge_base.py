#!/usr/bin/env python3
"""Build the canonical single-page README from topic-level lessons.

Topic files in ``Python-Mastery/{Beginner,Intermediate,Advanced}`` are the
maintainable source for lesson bodies. This command preserves the root README's
front matter and final career section, regenerates the complete topic index,
and replaces all lesson sections in level order.
"""

from __future__ import annotations

from curriculum_manifest import (
    DESTINATION,
    LEVELS,
    ROOT,
    SOURCE,
    complete_topic_index,
    topic_filename,
)


def lesson_body(level: str, number: int, topic: str) -> str:
    """Read one topic file and remove split-edition navigation."""
    path = DESTINATION / level / topic_filename(number, topic)
    document = path.read_text(encoding="utf-8")
    start_marker = f"# {topic}\n"
    start = document.find(start_marker)
    if start < 0:
        raise ValueError(f"{path.relative_to(ROOT)} is missing {start_marker.strip()}")

    footer = document.rfind("\n---\n")
    if footer < start:
        raise ValueError(f"{path.relative_to(ROOT)} is missing its footer separator")
    return document[start:footer].rstrip()


def build_level(level_number: int, level: str) -> str:
    lessons = []
    for number, topic in enumerate(LEVELS[level], start=1):
        body = lesson_body(level, number, topic)
        lessons.append(
            f"{body}\n\n[Back to complete topic index](#complete-topic-index)"
        )
    joined = "\n\n---\n\n".join(lessons)
    return f"## Level {level_number}: {level}\n\n---\n\n{joined}"


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    lessons_start = source.find("## Level 1: Beginner")
    final_start = source.find("# FINAL SECTION")
    if lessons_start < 0 or final_start < 0 or final_start <= lessons_start:
        raise ValueError("README does not contain the expected level and final markers")

    prefix = source[:lessons_start].rstrip()
    index_marker = "## Complete Topic Index"
    index_start = prefix.find(index_marker)
    if index_start < 0:
        raise ValueError("README is missing the Complete Topic Index heading")
    prefix = f"{prefix[:index_start].rstrip()}\n\n{complete_topic_index()}\n"
    final_section = source[final_start:].lstrip()
    levels = [
        build_level(level_number, level)
        for level_number, level in enumerate(LEVELS, start=1)
    ]
    output = (
        f"{prefix}\n\n"
        f"{'\n\n---\n\n'.join(levels)}\n\n"
        f"---\n\n{final_section.rstrip()}\n"
    )
    SOURCE.write_text(output, encoding="utf-8")

    topic_total = sum(len(topics) for topics in LEVELS.values())
    print(f"Synchronized {topic_total} topic lessons into {SOURCE.name}")


if __name__ == "__main__":
    main()
