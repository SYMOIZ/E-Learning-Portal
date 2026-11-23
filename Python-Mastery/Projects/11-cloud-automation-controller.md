# Cloud Automation Controller

[← Project catalog](./README.md) · [Cloud Development](../Advanced/33-cloud-development.md)

**Level:** Advanced  
**Lessons:** configuration, security hygiene, automation, CI

## Problem

A platform team wants a Python command that plans a safe infrastructure change, prints the plan, and applies it only when an operator passes an explicit flag.

## Non-goals

- No privilege escalation.
- No storage of long-lived keys in source code.
- No destructive cleanup of unknown resources.

## Requirements

- Default to dry-run output.
- Read credentials from the environment or a cloud identity mechanism, never from the repository.
- Refuse to continue when the target account or project does not match an allowlist.
- Document the minimum permission the automation needs.

## Starter

```python
def plan(desired, actual):
    changes = []
    for name, value in desired.items():
        if actual.get(name) != value:
            changes.append({"name": name, "to": value})
    return changes


def apply_changes(changes, enabled):
    if not enabled:
        return {"applied": False, "planned": changes}
    return {"applied": True, "planned": changes}


def main():
    desired = {"log_retention_days": 30}
    actual = {"log_retention_days": 7}
    changes = plan(desired, actual)
    print(apply_changes(changes, enabled=False))


if __name__ == "__main__":
    main()
```

## Acceptance checks

- The default command prints a plan and changes nothing.
- A target outside the allowlist exits with an error before any SDK call.
- Tests cover dry-run and allowlist rejection without cloud credentials.
- The README lists the required permission and an example plan.

## Extension

Emit a machine-readable plan file that a CI job can archive.
