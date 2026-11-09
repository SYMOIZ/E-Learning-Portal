# Beginner Checkpoint

[← Assessments](./README.md) · [Answer key](./01-beginner-answers.md)

Close the lessons. Write answers in a notes file, then score them.

## Short answers

1. What is the difference between a variable and the object it names?
2. Why can you append to a list but not assign a new character into a string with `text[0] = "A"`?
3. When is a tuple a better record than a list?
4. What do `break`, `continue`, and `pass` each do inside a loop?
5. Why is `def add(item, bucket=[]):` a defect?
6. What does a function return if it has no `return` statement?
7. What problem does a virtual environment solve?
8. What does `with open(path, encoding="utf-8") as handle:` guarantee if an exception is raised while reading?

## Read the code

Write the printed result for each program. Do not run it yet.

### Item 9

```python
name = "ada"
print(name.upper())
print(name)
```

### Item 10

```python
def add(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(add("a"))
print(add("b"))
```

### Item 11

```python
count = 0

def bump():
    count = 1
    return count

print(bump(), count)
```

### Item 12

```python
prices = {"tea": 3, "bread": 2}
total = 0
for item in ("tea", "cake", "bread"):
    total += prices.get(item, 0)
print(total)
```

When you are finished, open the [answer key](./01-beginner-answers.md).
