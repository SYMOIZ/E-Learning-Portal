from pathlib import Path

def count_lines(path):
    return len(Path(path).read_text(encoding="utf-8").splitlines())

print(count_lines("README.md"))
