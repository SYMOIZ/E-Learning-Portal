# CSV Processing

## Overview

- **What is it?** CSV processing reads and writes comma-separated tabular files.
- **Why is it important?** Spreadsheets and legacy systems still exchange CSV widely.
- **Where is it used?** Finance exports, marketing lists, ETL staging, reports.

## Learning Objectives

- **Skills gained:** Practical command of CSV Processing.
- **Concepts covered:**

- Use csv.reader and csv.DictReader.
- Write rows with csv.writer.
- Handle headers and dialects.

- **Expected outcome:** You import and export tabular CSV data reliably.

## Real World Applications

- Accounting
- Retail analytics
- HR systems
- Science datasets

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### reader

- **Definition:** Iterate rows as lists.
- **Visual explanation:** `reader` → process → result
- **Practical example:**

```python
import csv
from io import StringIO
rows = list(csv.reader(StringIO('a,b\n1,2')))
print(rows)
```

### DictReader

- **Definition:** Rows as dicts by header.
- **Visual explanation:** `DictReader` → process → result
- **Practical example:**

```python
import csv
from io import StringIO
r = csv.DictReader(StringIO('name,score\nAda,99'))
print(list(r)[0]['name'])
```

### writer

- **Definition:** Serialize rows.
- **Visual explanation:** `writer` → process → result
- **Practical example:**

```python
import csv
from io import StringIO
buf = StringIO()
w = csv.writer(buf)
w.writerow(['x', 'y'])
print(buf.getvalue().strip())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | CSV is text rows with delimiter-separated fields. |
| ⚡ Purpose | Interchange tabular data simply. |
| 🔥 Benefits | Universal, streaming-friendly, stdlib module. |
| 🎯 Use Cases | Sales exports, survey results, bulk imports. |
| 🚀 Best Practices | Use DictReader; specify newline=''; handle encoding. |
| ❌ Common Mistakes | Locale comma issues, not quoting embedded commas, huge memory load. |

## Syntax Guide

### Basic Syntax

```python
import csv
with open('data.csv', newline='', encoding='utf-8') as f:
    rows = list(csv.reader(f))
```

### Standard Structure

```python
open -> reader/writer -> process rows
```

### Code Pattern

```python
for row in csv.DictReader(f):
    handle(row)
```

## Examples

### Beginner Example

```python
import csv
from io import StringIO

print(list(csv.reader(StringIO('id,name\n1,Ada'))))
```

### Intermediate Example

```python
import csv
from io import StringIO

source = StringIO('sku,qty\nA1,2\nB2,1\n')
total = sum(int(row['qty']) for row in csv.DictReader(source))
print(total)
```

### Advanced Example

```python
import csv
from io import StringIO

def filter_rows(text: str, min_qty: int) -> list[dict]:
    rows = csv.DictReader(StringIO(text))
    return [r for r in rows if int(r['qty']) >= min_qty]


data = 'sku,qty\nA,5\nB,1\n'
print(filter_rows(data, 2))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[CSV File] --> B[Reader]
    B --> C[Rows]
    C --> D[Process]
```

---
