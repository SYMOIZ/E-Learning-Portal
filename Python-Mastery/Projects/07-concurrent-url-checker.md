# Concurrent URL Checker

[← Project catalog](./README.md) · [Async Programming](../Intermediate/22-async-programming.md)

**Level:** Intermediate  
**Lessons:** threads or asyncio, timeouts, exceptions, collections

## Problem

A documentation owner wants to know which public URLs in a list respond successfully, without starting an unbounded number of requests.

## Non-goals

- No crawling beyond the supplied list.
- No authentication bypass.
- No aggressive retry storms.

## Requirements

- Accept URLs from a file.
- Limit in-flight checks to a configured maximum.
- Apply a per-request timeout.
- Print a summary of success, failure, and timeout counts.

## Starter

```python
def summarize(results):
    summary = {"ok": 0, "error": 0}
    for result in results:
        key = "ok" if result["ok"] else "error"
        summary[key] += 1
    return summary


def main():
    sample = [
        {"url": "https://example.com", "ok": True},
        {"url": "https://example.com/missing", "ok": False},
    ]
    print(summarize(sample))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- More URLs than the concurrency limit still finish.
- A timeout is counted separately from a successful status.
- Tests use a fake fetcher so they stay offline.
- The tool documents a polite default delay or concurrency cap.

## Extension

Write failures as structured log events with the URL host and status, not the full response body.
