# API Data Synchronizer

[← Project catalog](./README.md) · [API Consumption](../Intermediate/24-api-consumption.md)

**Level:** Intermediate  
**Lessons:** HTTP clients, JSON, configuration, exceptions, logging

## Problem

An operations script must copy a page of public JSON records into a local file and survive a single transient failure without duplicating rows.

## Non-goals

- No credential scraping.
- No bypass of access controls or rate limits.
- No private or personal data.

## Requirements

- Read the base URL and output path from configuration, not hard-coded secrets.
- Retry one failed GET with a short backoff, then log the final failure.
- Upsert local rows by a stable `id` field.
- Treat a non-JSON body as an error and leave the previous file unchanged.

## Starter

```python
def upsert(existing, incoming):
    merged = {item["id"]: item for item in existing}
    for item in incoming:
        merged[item["id"]] = item
    return list(merged.values())


def main():
    current = [{"id": "a", "name": "Ada"}]
    incoming = [{"id": "a", "name": "Ada Lovelace"}, {"id": "b", "name": "Grace"}]
    print(upsert(current, incoming))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- Re-running the same payload does not increase the row count.
- A changed name for an existing `id` replaces the old record.
- Tests pass a fake HTTP client, so the suite does not need the network.
- Logs include the attempt number and exclude response bodies that might contain personal data.

## Extension

Honor a `Retry-After` header when the server provides one.
