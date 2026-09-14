"""Shared curriculum manifest for generation and validation tools."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "README.md"
DESTINATION = ROOT / "Python-Mastery"

LEVELS: dict[str, list[str]] = {
    "Beginner": [
        "Introduction to Python",
        "Installing Python",
        "IDE Setup",
        "Python Syntax",
        "Variables",
        "Data Types",
        "Type Casting",
        "Input and Output",
        "Operators",
        "Conditional Statements",
        "Loops",
        "Nested Loops",
        "Break Continue Pass",
        "Strings",
        "String Methods",
        "Lists",
        "List Methods",
        "Tuples",
        "Sets",
        "Dictionaries",
        "Functions",
        "Arguments and Parameters",
        "Return Statements",
        "Scope",
        "Lambda Functions",
        "Modules",
        "Packages",
        "Date and Time",
        "Math Module",
        "Random Module",
        "File Handling",
        "Exception Handling",
        "Debugging Basics",
        "Virtual Environments",
        "Basic Project Structure",
    ],
    "Intermediate": [
        "Object Oriented Programming",
        "Classes",
        "Objects",
        "Constructors",
        "Encapsulation",
        "Inheritance",
        "Polymorphism",
        "Abstraction",
        "Magic Methods",
        "Iterators",
        "Generators",
        "Decorators",
        "Context Managers",
        "Regular Expressions",
        "JSON Processing",
        "CSV Processing",
        "XML Processing",
        "Logging",
        "Configuration Management",
        "Multithreading",
        "Multiprocessing",
        "Async Programming",
        "API Development",
        "API Consumption",
        "Requests Library",
        "Database Fundamentals",
        "SQLite",
        "MySQL Integration",
        "PostgreSQL Integration",
        "SQLAlchemy ORM",
        "Unit Testing",
        "Pytest",
        "Mocking",
        "Packaging Python Projects",
        "CLI Applications",
    ],
    "Advanced": [
        "Data Structures Internals",
        "Algorithms in Python",
        "Design Patterns",
        "SOLID Principles",
        "Memory Management",
        "Garbage Collection",
        "Python Internals",
        "Metaclasses",
        "Descriptors",
        "Concurrency",
        "Parallel Computing",
        "Distributed Systems",
        "Network Programming",
        "Socket Programming",
        "Cybersecurity Automation",
        "Web Scraping",
        "Automation Frameworks",
        "ETL Development",
        "Data Engineering",
        "Pandas",
        "NumPy",
        "PySpark",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "Computer Vision",
        "FastAPI",
        "Django",
        "Flask",
        "Microservices",
        "Docker with Python",
        "Kubernetes Integration",
        "Cloud Development",
        "AWS with Python",
        "Azure with Python",
        "GCP with Python",
        "DevOps Automation",
        "CI/CD Pipelines",
        "Performance Optimization",
        "System Design with Python",
    ],
}

REQUIRED_SECTIONS = (
    "Overview",
    "Learning Objectives",
    "Real World Applications",
    "Core Concepts",
    "Infographic Summary",
    "Syntax Guide",
    "Examples",
    "Workflow Diagram",
)


def slugify(value: str) -> str:
    """Return a filesystem-safe, readable topic slug."""
    import re

    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def github_heading_slug(value: str) -> str:
    """Return a GitHub-compatible heading anchor for an ASCII topic title."""
    import re

    slug = re.sub(r"[^\w\s-]", "", value.casefold(), flags=re.UNICODE)
    return re.sub(r"\s+", "-", slug.strip())


def topic_filename(number: int, topic: str) -> str:
    """Return the numbered filename for a topic."""
    return f"{number:02d}-{slugify(topic)}.md"


def complete_topic_index() -> str:
    """Return the single-page README topic index with in-page and split links."""
    lines = [
        "## Complete Topic Index",
        "",
        "Jump to a lesson in this single-page edition, or open the split NotebookLM document.",
        "",
    ]
    labels = {
        "Beginner": "Beginner lessons (35)",
        "Intermediate": "Intermediate lessons (35)",
        "Advanced": "Advanced lessons (40)",
    }
    for level, topics in LEVELS.items():
        lines.append(f"### {labels[level]}")
        lines.append("")
        lines.append("| # | Topic | Split lesson |")
        lines.append("| ---: | --- | --- |")
        for number, topic in enumerate(topics, start=1):
            split_path = f"./Python-Mastery/{level}/{topic_filename(number, topic)}"
            lines.append(
                f"| {number:02d} | [{topic}](#{github_heading_slug(topic)}) | "
                f"[Open]({split_path}) |"
            )
        lines.append("")
    return "\n".join(lines).rstrip()
