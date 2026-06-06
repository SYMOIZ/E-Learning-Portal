from pathlib import Path
from typing import Iterable

def load_keywords(path: Path) -> set[str]:
    return {line.strip().lower() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}

def filter_records(records: Iterable[str], keywords: set[str]) -> list[str]:
    return [record for record in records if record.lower() in keywords]
