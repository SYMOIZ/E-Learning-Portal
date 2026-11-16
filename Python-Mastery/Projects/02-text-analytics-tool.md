# Text Analytics Tool

[← Project catalog](./README.md) · [Dictionaries](../Beginner/20-dictionaries.md)

**Level:** Beginner  
**Lessons:** strings, string methods, dictionaries, functions, files

## Problem

An editor wants word counts for a plain-text note, including a top-word list and a defined result for an empty file.

## Non-goals

- No stemming or language detection.
- No network calls.

## Requirements

- Normalize case and ignore empty tokens.
- Count words with a dictionary.
- Return the five most common words, ties broken alphabetically.
- An empty document returns an empty list and a total of zero.

## Starter

```python
def tokenize(text):
    cleaned = []
    for raw in text.casefold().split():
        token = "".join(char for char in raw if char.isalpha())
        if token:
            cleaned.append(token)
    return cleaned


def counts(tokens):
    tally = {}
    for token in tokens:
        tally[token] = tally.get(token, 0) + 1
    return tally


def top_words(tally, limit=5):
    ranked = sorted(tally.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:limit]


def main():
    sample = "Cats cats, and dogs."
    tally = counts(tokenize(sample))
    print(top_words(tally))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- `"Cats cats, and dogs."` counts `cats` twice.
- Punctuation stuck to a word does not create a separate token.
- Empty input prints `[]`.
- The report states the total token count.

## Extension

Accept a file path and write the report as CSV.
