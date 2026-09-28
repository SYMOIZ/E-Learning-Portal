# Intermediate Checkpoint Answers

[← Checkpoint](./02-intermediate-checkpoint.md) · [Assessments](./README.md)

## Short answers

1. Prefer composition when the new type *uses* another object and should not inherit that object's entire contract. Inheritance fits a true subtype that can stand in for the parent. Composition keeps coupling at the methods you actually call. Lesson: [Object Oriented Programming](../Intermediate/01-object-oriented-programming.md).
2. A generator produces values lazily and can represent a stream larger than memory. You give up random access, `len` unless you count yourself, and a second pass unless you recreate the generator. Lesson: [Generators](../Intermediate/11-generators.md).
3. It copies the original callable's name, docstring, and related metadata onto the wrapper. Without it, tracebacks, help text, and decorators that look at `__name__` see the wrapper instead of the function you wrote. Lesson: [Decorators](../Intermediate/12-decorators.md).
4. Parameters are sent separately from the SQL text, so user input cannot change the statement's shape. An f-string can turn input such as quotes or comments into extra SQL. Lesson: [Database Fundamentals](../Intermediate/26-database-fundamentals.md).
5. Choose `asyncio` when the work is mostly waiting on the network and the client library is async, so one thread can interleave many waits. Threads still fit blocking clients, but thousands of threads cost memory and scheduling. Bound concurrency either way. Lesson: [Async Programming](../Intermediate/22-async-programming.md).
6. Log when the local operation has handled the failure and an operator needs the diagnostic. Propagate when the caller must decide, retry, or abort a larger transaction. Logging and then swallowing an error hides broken work. Lesson: [Logging](../Intermediate/18-logging.md).
7. A mock can return the happy path the test expects even if the real collaborator has a different signature, error, or side effect. Over-mocking tests the mock setup. Prefer fakes for important boundaries and reserve mocks for true externals. Lesson: [Mocking](../Intermediate/33-mocking.md).
8. Name, version, dependencies, entry points, and supported Python versions belong in project metadata such as `pyproject.toml`. Business modules should stay importable without performing packaging side effects. Lesson: [Packaging Python Projects](../Intermediate/34-packaging-python-projects.md).

## Code-reading answers

### Item 9

```text
2
```

`inc` returns the same instance, so the second call updates the same `value`.

### Item 10

```text
[('a', 'A'), ('b', 'B')]
```

`list` exhausts the generator. Each yield is a tuple of the original item and its uppercase form.

### Item 11

```text
docu
```

A class that defines `__call__` produces callable instances. The slice keeps the first four characters.

### Item 12

```text
[('a', 5), ('b', 1)]
```

Amounts accumulate by key. `sorted` orders the pairs by key because strings sort alphabetically.

## Score guide

Count one point per numbered item. Restudy the linked lesson for any miss before you start an intermediate [project brief](../Projects/).
