"""Shared helper for snippet part modules."""

from __future__ import annotations


def S(
    what: str,
    why: str,
    where: str,
    objectives: tuple[str, str, str],
    outcome: str,
    industry: tuple[str, str, str, str],
    concepts: tuple[tuple[str, str, str], tuple[str, str, str], tuple[str, str, str]],
    concept: str,
    purpose: str,
    benefits: str,
    use_cases: str,
    best_practices: str,
    mistakes: str,
    basic_syntax: str,
    structure: str,
    pattern: str,
    beginner: str,
    intermediate: str,
    advanced: str,
    mermaid: str,
) -> dict:
    return {
        "what": what,
        "why": why,
        "where": where,
        "objectives": list(objectives),
        "outcome": outcome,
        "industry": list(industry),
        "concepts": list(concepts),
        "concept": concept,
        "purpose": purpose,
        "benefits": benefits,
        "use_cases": use_cases,
        "best_practices": best_practices,
        "mistakes": mistakes,
        "basic_syntax": basic_syntax,
        "structure": structure,
        "pattern": pattern,
        "beginner": beginner,
        "intermediate": intermediate,
        "advanced": advanced,
        "mermaid": mermaid,
    }
