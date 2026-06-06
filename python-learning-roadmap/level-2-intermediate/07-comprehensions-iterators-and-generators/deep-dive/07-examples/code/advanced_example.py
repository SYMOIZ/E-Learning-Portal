from pathlib import Path

def matching_lines(path: Path, keyword: str):
    with path.open(encoding="utf-8") as file:
        for line in file:
            if keyword in line:
                yield line.rstrip()
