# Beginner Syntax Cheat Sheet

[← Cheat sheets](./README.md) · [Beginner lessons](../Beginner/01-introduction-to-python.md)

## Names, Types, and IO

```python
name = "Ada"
count = 3
ratio = 1.5
active = True
print(f"{name} ran {count} drills")
text = "42"
number = int(text)
```

| Goal | Pattern |
| --- | --- |
| Bind a name | `name = value` |
| Convert types | `int()`, `float()`, `str()`, `bool()` |
| Read terminal text | `input("prompt: ")` |
| Format output | `f"{name}: {value:.2f}"` |

## Control Flow

```python
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "C"

for item in items:
    if item == "skip":
        continue
    if item == "stop":
        break
    process(item)
```

## Collections

| Type | Create | Typical use |
| --- | --- | --- |
| `list` | `items = ["a", "b"]` | Ordered, mutable sequence |
| `tuple` | `point = (3, 4)` | Fixed record |
| `set` | `seen = {"a", "b"}` | Unique membership |
| `dict` | `row = {"id": 1}` | Keyed lookup |

## Functions, Files, Failures

```python
def total(values: list[int]) -> int:
    return sum(values)

try:
    with open("notes.txt", encoding="utf-8") as handle:
        text = handle.read()
except FileNotFoundError:
    text = ""
```

Related lessons: [Variables](../Beginner/05-variables.md), [Loops](../Beginner/11-loops.md), [Functions](../Beginner/21-functions.md), [File Handling](../Beginner/31-file-handling.md), [Exception Handling](../Beginner/32-exception-handling.md).
