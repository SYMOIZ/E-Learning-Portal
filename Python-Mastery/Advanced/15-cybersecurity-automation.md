# Cybersecurity Automation

## Overview

- **What is it?** Cybersecurity automation uses Python to orchestrate scans, parsing, and response workflows.
- **Why is it important?** Security teams must scale repetitive analysis and enrichment tasks.
- **Where is it used?** SOAR platforms, vuln management, log enrichment, phishing analysis.

## Learning Objectives

- **Skills gained:** Practical command of Cybersecurity Automation.
- **Concepts covered:**

- Parse logs and IOCs with Python.
- Call security APIs safely.
- Automate repeatable playbooks.

- **Expected outcome:** You build Python automations that support security operations.

## Real World Applications

- SOC teams
- MSSP
- AppSec
- Compliance automation

- **Business applications:** Automate workflows, reduce manual errors, accelerate delivery.
- **Career relevance:** Required knowledge for Python roles from junior developer to senior engineer.

## Core Concepts

### IOC parsing

- **Definition:** Extract indicators.
- **Visual explanation:** `IOC parsing` → process → result
- **Practical example:**

```python
import re
line = '1.2.3.4 failed login'
print(re.findall(r'\d+\.\d+\.\d+\.\d+', line))
```

### Hashing

- **Definition:** Fingerprint files.
- **Visual explanation:** `Hashing` → process → result
- **Practical example:**

```python
import hashlib
print(hashlib.sha256(b'data').hexdigest()[:8])
```

### Automation script

- **Definition:** Schedule repeatable tasks.
- **Visual explanation:** `Automation script` → process → result
- **Practical example:**

```python
def run_playbook():
    return ['parsed', 'enriched']
print(run_playbook())
```

## Infographic Summary

| Block | Summary |
| --- | --- |
| 📌 Concept | Automate verify-enrich-respond loops with scripts. |
| ⚡ Purpose | Reduce manual toil and response time. |
| 🔥 Benefits | Consistency, speed, audit trails. |
| 🎯 Use Cases | Phish triage, CVE ticket creation, firewall rule audits. |
| 🚀 Best Practices | Least privilege creds; validate inputs; log actions; dry-run mode. |
| ❌ Common Mistakes | Running unverified scripts as root, storing secrets in code. |

## Syntax Guide

### Basic Syntax

```python
import hashlib
hashlib.sha256(data).hexdigest()
```

### Standard Structure

```python
ingest -> parse -> enrich -> ticket/action
```

### Code Pattern

```python
for alert in alerts:
    enrich(alert)
    if severity(alert): escalate(alert)
```

## Examples

### Beginner Example

```python
import re
print(bool(re.search(r'ERROR', 'ERROR login failed')))
```

### Intermediate Example

```python
import hashlib


def file_sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


print(len(file_sha256(__file__)) == 64)
```

### Advanced Example

```python
from dataclasses import dataclass


@dataclass
class Alert:
    ip: str
    severity: int


def triage(alerts: list[Alert]) -> list[Alert]:
    return sorted([a for a in alerts if a.severity >= 7], key=lambda a: -a.severity)


print(triage([Alert('1.2.3.4', 8), Alert('5.6.7.8', 3)]))
```

## Workflow Diagram

```mermaid
flowchart LR
    A[Alert Feed] --> B[Parser]
    B --> C[Enrichment]
    C --> D[Response]
```

---
