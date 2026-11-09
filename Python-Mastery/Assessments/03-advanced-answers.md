# Advanced Checkpoint Answers

[← Checkpoint](./03-advanced-checkpoint.md) · [Assessments](./README.md)

## Short answers

1. CPython's GIL allows only one thread to execute Python bytecode at a time. Threads help when they release the GIL during blocking I/O or some native extensions. CPU-bound Python loops need processes, vectorized native code, or a different runtime. Lesson: [Concurrency](../Advanced/10-concurrency.md).
2. Reference counting frees an object when its count hits zero. Two objects that reference each other can keep a count above zero even when the rest of the program cannot reach them. The cyclic garbage collector finds those unreachable cycles. Lesson: [Garbage Collection](../Advanced/06-garbage-collection.md).
3. Re-running the load with the same input does not duplicate business rows. Typical designs upsert on a natural key, store a processed-batch id, or write to a partition that is replaced atomically. Lesson: [ETL Development](../Advanced/18-etl-development.md).
4. `__slots__` can shrink millions of small objects by omitting a per-instance `__dict__`. Skip it when instances need arbitrary attributes, when you have not measured memory, or when multiple inheritance and slots conflict. Lesson: [Memory Management](../Advanced/05-memory-management.md).
5. A descriptor is an object stored on a class that customizes what happens when code gets, sets, or deletes the attribute on an instance. Lesson: [Descriptors](../Advanced/09-descriptors.md).
6. Anyone who can pull the image can read the secret, and rotating the secret requires a rebuild. Supply secrets at runtime from a secret manager or environment injected by the platform. Lesson: [Docker with Python](../Advanced/31-docker-with-python.md).
7. You give up a single atomic commit. One service can commit while the other fails, so you need an outbox, retry, or compensating action and you must tolerate a temporary mismatch. Lesson: [Distributed Systems](../Advanced/12-distributed-systems.md).
8. Latency, CPU, allocation rate, or queue time that you measured on a realistic input. A hot function in a profiler outranks a hunch about Big-O. Lesson: [Performance Optimization](../Advanced/39-performance-optimization.md).

## Code-reading answers

### Item 9

```text
[('a', 2)]
```

`most_common(1)` returns a one-item list of `(character, count)` pairs. `a` occurs twice.

### Item 10

```text
3
```

`Positive.__set__` accepts `3` and stores it on `_quantity`. `__get__` returns that stored value. A non-positive quantity would raise `ValueError` before the print.

### Item 11

```text
8
```

The cache fills bottom-up: `fib(6)` is `8`. The dictionary is the memoization table.

### Item 12

```text
['ok', 'error']
```

The second event with id `a` is skipped. Statuses are kept from the first time each id is seen.

## Score guide

Count one point per numbered item. A miss on items 3, 6, or 7 is a design miss: reread the linked lesson and rewrite the answer in your own words before you pick an advanced [project brief](../Projects/).
