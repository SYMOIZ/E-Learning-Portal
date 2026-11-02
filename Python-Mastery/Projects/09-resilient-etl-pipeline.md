# Resilient ETL Pipeline

[← Project catalog](./README.md) · [ETL Development](../Advanced/18-etl-development.md)

**Level:** Advanced  
**Lessons:** data engineering, files or dataframes, quality checks, idempotency

## Problem

A daily export must be cleaned, checked, and loaded so an operator can rerun the same file after a crash without duplicating facts.

## Non-goals

- No scraping of sites that disallow automation.
- No silent dropping of invalid rows.

## Requirements

- Extract records from CSV or JSON.
- Reject rows that miss a required field and write them to a quarantine report.
- Load valid rows with an upsert key or a replaceable batch id.
- Record the source file name and row count in a short lineage note.

## Starter

```python
def split_rows(rows, required):
    valid = []
    quarantine = []
    for row in rows:
        if all(row.get(field) not in (None, "") for field in required):
            valid.append(row)
        else:
            quarantine.append(row)
    return valid, quarantine


def main():
    rows = [
        {"id": "1", "amount": "5"},
        {"id": "", "amount": "9"},
    ]
    valid, quarantine = split_rows(rows, ["id", "amount"])
    print(len(valid), len(quarantine))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- Reprocessing the same batch keeps the same loaded row count.
- A quarantined row is visible in the report and absent from the load table.
- The pipeline can resume after a simulated failure between transform and load.
- The README states the batch boundary and the upsert key.

## Extension

Add a numeric range check and count how many rows fail each rule.
