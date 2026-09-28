# Quiz Engine

[← Project catalog](./README.md) · [Functions](../Beginner/21-functions.md)

**Level:** Beginner  
**Lessons:** conditionals, loops, lists, dictionaries, functions, modules

## Problem

A study group wants a quiz runner that scores answers and reprints the questions a learner missed.

## Non-goals

- No timer.
- No remote question bank.

## Requirements

- Store questions as data, not as copied `if` blocks.
- Compare answers after stripping surrounding space and ignoring case.
- Return the score and the missed prompts.
- A quiz with no questions scores zero.

## Starter

```python
def normalize(answer):
    return answer.strip().casefold()


def grade(questions, responses):
    missed = []
    correct = 0
    for question in questions:
        given = responses.get(question["id"], "")
        if normalize(given) == normalize(question["answer"]):
            correct += 1
        else:
            missed.append(question["prompt"])
    return {"score": correct, "missed": missed}


def main():
    questions = [
        {"id": "types", "prompt": "Immutable sequence?", "answer": "tuple"},
    ]
    print(grade(questions, {"types": " Tuple "}))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- Surrounding spaces and different case still count as correct.
- A wrong answer appears in `missed` and does not increase `score`.
- Missing response keys count as wrong.
- Questions live in one module and grading lives in another.

## Extension

Shuffle question order with an explicit `random.Random` seed so the quiz is repeatable in tests.
