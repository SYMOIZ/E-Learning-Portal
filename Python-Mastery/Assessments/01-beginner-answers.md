# Beginner Checkpoint Answers

[← Checkpoint](./01-beginner-checkpoint.md) · [Assessments](./README.md)

## Short answers

1. A variable is a name in a namespace. The object is the value that name currently references. Rebinding the name does not change the object, and two names can reference one object. Lesson: [Variables](../Beginner/05-variables.md).
2. Strings are immutable. Item assignment would change an existing string object, which Python refuses. `upper()` returns a new string and leaves the original bound name unchanged. Lesson: [Strings](../Beginner/14-strings.md).
3. Use a tuple when the record's length and meaning are fixed, such as `(latitude, longitude)`, or when the record must be hashable and used as a dictionary key. Use a list when the collection grows or shrinks. Lesson: [Tuples](../Beginner/18-tuples.md).
4. `break` leaves the loop. `continue` skips the rest of the current iteration. `pass` does nothing and is a placeholder. Lesson: [Break Continue Pass](../Beginner/13-break-continue-pass.md).
5. A mutable default is created once, when the function is defined, and then shared by later calls. Use `None` and create a new list inside the function. Lesson: [Arguments and Parameters](../Beginner/22-arguments-and-parameters.md).
6. It returns `None`. Lesson: [Return Statements](../Beginner/23-return-statements.md).
7. It isolates a project's interpreter and third-party packages from other projects, so dependency versions do not collide. Lesson: [Virtual Environments](../Beginner/34-virtual-environments.md).
8. The file is closed when the block exits, including when an exception propagates. Lesson: [File Handling](../Beginner/31-file-handling.md).

## Code-reading answers

### Item 9

```text
ADA
ada
```

`upper()` returns a new string. `name` still references `"ada"`.

### Item 10

```text
['a']
['b']
```

Each call receives a fresh list because the default is `None` and the list is created inside the function.

### Item 11

```text
1 0
```

The assignment inside `bump` creates a local name. The global `count` stays `0`. Lesson: [Scope](../Beginner/24-scope.md).

### Item 12

```text
5
```

`"cake"` is missing, so `.get` contributes `0`. Tea and bread contribute `3 + 2`. Lesson: [Dictionaries](../Beginner/20-dictionaries.md).

## Score guide

Count one point per numbered item. For code items, the full printed result must match. Review any lesson linked beside a miss, then retake only those items tomorrow.
