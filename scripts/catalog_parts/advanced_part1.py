"""Advanced topic snippet registrations (part 1)."""

from __future__ import annotations

from textwrap import dedent
from typing import Callable


def _register_advanced_part1(p: Callable[..., None]) -> None:
    p(
        "Data Structures Internals",
        what="Data structures internals explain how Python lists, dicts, and sets are implemented.",
        why="Understanding internals guides performance and memory decisions.",
        where="High-scale services, competitive programming, library authors.",
        objectives=("Explain dynamic arrays and hash tables at high level.", "Know amortized costs of list/dict ops.", "Choose structures based on access patterns."),
        outcome="You reason about Python collection performance accurately.",
        industry=("High-frequency systems", "Database engines", "Game servers", "ML infra"),
        concepts=(
            ("Dynamic array", "Lists over-allocate for append.", "items = []\nitems.append(1)\nprint(len(items))"),
            ("Hash table", "Dicts map keys via hashing.", "d = {'a': 1}\nprint('a' in d)"),
            ("Load factor", "Dicts resize when crowded.", "print(len({i: i for i in range(1000)}))"),
        ),
        concept="CPython collections trade memory for speed with tuned C implementations.",
        purpose="Pick the right structure and avoid hidden costs.",
        benefits="Predictable performance, fewer production surprises.",
        use_cases="Caches, indexes, buffers, queues.",
        best_practices="Use deque for FIFO; set for membership; pre-size when known.",
        mistakes="Assuming list insert is O(1), using dict as ordered log without need.",
        basic_syntax="from collections import deque\nq = deque([1, 2])\nq.append(3)",
        structure="analyze access pattern -> pick structure -> benchmark",
        pattern="needs_membership = True\nprint('set' if needs_membership else 'list')",
        beginner="from collections import deque\nprint(deque([1, 2, 3])[0])",
        intermediate=dedent("""\
            import sys

            small = {}
            big = {i: i for i in range(1000)}
            print(sys.getsizeof(small) < sys.getsizeof(big))"""),
        advanced=dedent("""\
            from collections import OrderedDict

            cache = OrderedDict()
            cache['a'] = 1
            cache['b'] = 2
            cache.move_to_end('a')
            print(list(cache.keys()))"""),
        mermaid="flowchart LR\n    A[Operation] --> B[List/Dict/Set]\n    B --> C[CPython C API]",
    )

    p(
        "Algorithms in Python",
        what="Algorithms in Python implement classic CS techniques for searching, sorting, and graphs.",
        why="Correct algorithms reduce time and memory at scale.",
        where="Interviews, data pipelines, routing, recommendation engines.",
        objectives=("Implement search and sort algorithms.", "Analyze Big-O complexity.", "Use heapq and bisect when appropriate."),
        outcome="You choose and implement algorithms suited to problem constraints.",
        industry=("Big tech", "Logistics", "Ads ranking", "Bioinformatics"),
        concepts=(
            ("Binary search", "Divide sorted space.", "def bs(a, t):\n    lo, hi = 0, len(a) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if a[mid] == t: return mid\n        if a[mid] < t: lo = mid + 1\n        else: hi = mid - 1\n    return -1\nprint(bs([1,3,5], 3))"),
            ("Sorting", "Order elements.", "print(sorted([3, 1, 2]))"),
            ("heapq", "Priority queue heap.", "import heapq\nh = [3, 1, 2]\nheapq.heapify(h)\nprint(heapq.heappop(h))"),
        ),
        concept="Algorithm choice depends on n, constraints, and constants.",
        purpose="Solve problems within time/memory budgets.",
        benefits="Scalability, predictable latency.",
        use_cases="Top-K, scheduling, shortest path, dedupe.",
        best_practices="Use stdlib bisect/heapq; benchmark; document complexity.",
        mistakes="O(n^2) on large n, wrong assumptions about sorted input.",
        basic_syntax="import heapq\nheapq.heappush(heap, item)",
        structure="model problem -> choose algo -> implement -> test edge cases",
        pattern="import heapq\nh = [3, 1, 2]\nheapq.heapify(h)\nprint(heapq.heappop(h))",
        beginner="print(sorted(['b', 'a', 'c']))",
        intermediate=dedent("""\
            import bisect

            nums = [1, 3, 5, 7]
            print(bisect.bisect_left(nums, 5))"""),
        advanced=dedent("""\
            from collections import deque


            def bfs(graph, start):
                seen = {start}
                queue = deque([start])
                order = []
                while queue:
                    node = queue.popleft()
                    order.append(node)
                    for nei in graph.get(node, []):
                        if nei not in seen:
                            seen.add(nei)
                            queue.append(nei)
                return order


            print(bfs({'A': ['B'], 'B': ['C']}, 'A'))"""),
        mermaid="flowchart TD\n    A[Problem] --> B[Algorithm Choice]\n    B --> C[Implementation]\n    C --> D[Complexity Check]",
    )

    p(
        "Design Patterns",
        what="Design patterns are reusable solutions to common software design problems.",
        why="Shared vocabulary speeds design discussions and avoids reinventing wheels.",
        where="Enterprise apps, frameworks, large teams, maintainability-focused code.",
        objectives=("Apply factory, strategy, observer, and adapter patterns.", "Map patterns to Python idioms.", "Avoid pattern overuse."),
        outcome="You structure code with proven design patterns when they fit.",
        industry=("Enterprise Java/Python shops", "SDK design", "Plugin architectures", "Games"),
        concepts=(
            ("Strategy", "Interchangeable algorithms.", "class Add:\n    def apply(self, a, b):\n        return a + b\nprint(Add().apply(2, 3))"),
            ("Factory", "Centralize object creation.", "def user_factory(kind):\n    return {'admin': dict(role='admin'), 'guest': dict(role='guest')}[kind]\nprint(user_factory('admin'))"),
            ("Observer", "Publish/subscribe.", "class Bus:\n    def __init__(self):\n        self.listeners = []\n    def subscribe(self, fn):\n        self.listeners.append(fn)\n    def emit(self, msg):\n        for fn in self.listeners:\n            fn(msg)\nb = Bus()\nb.subscribe(lambda m: None)\nb.emit('hi')"),
        ),
        concept="Patterns name recurring structure, not copy-paste code.",
        purpose="Improve flexibility and maintainability.",
        benefits="Team communication, extensibility.",
        use_cases="Payment strategies, notification bus, adapters for legacy APIs.",
        best_practices="Prefer simplicity; use patterns with clear pain point.",
        mistakes="Pattern obsession, unnecessary abstraction layers.",
        basic_syntax=dedent("""\
            class Strategy:
                def apply(self, value):
                    return value


            print(Strategy().apply(1))"""),
        structure="identify variation -> encapsulate -> compose",
        pattern="context.set_strategy(concrete_strategy)",
        beginner=dedent("""\
            class Greeter:
                def greet(self, name):
                    return f'Hello, {name}'


            print(Greeter().greet('Ada'))"""),
        intermediate=dedent("""\
            class Logger:
                def log(self, msg: str) -> None:
                    print(msg)


            class Service:
                def __init__(self, logger: Logger):
                    self.logger = logger

                def run(self):
                    self.logger.log('running')


            Service(Logger()).run()"""),
        advanced=dedent("""\
            from typing import Callable


            class EventEmitter:
                def __init__(self):
                    self._handlers: dict[str, list[Callable]] = {}

                def on(self, event: str, handler: Callable) -> None:
                    self._handlers.setdefault(event, []).append(handler)

                def emit(self, event: str, payload):
                    for handler in self._handlers.get(event, []):
                        handler(payload)


            bus = EventEmitter()
            bus.on('created', lambda p: print('event', p))
            bus.emit('created', {'id': 1})"""),
        mermaid="flowchart LR\n    A[Problem] --> B[Pattern]\n    B --> C[Components]",
    )

    p(
        "SOLID Principles",
        what="SOLID principles guide object-oriented design for maintainable systems.",
        why="They reduce coupling and make change safer in large codebases.",
        where="Enterprise services, domain-driven design, long-lived products.",
        objectives=("Explain SRP, OCP, LSP, ISP, DIP.", "Recognize violations in Python code.", "Refactor toward SOLID incrementally."),
        outcome="You evaluate designs using SOLID as a checklist.",
        industry=("Enterprise software", "Banking platforms", "Healthcare systems", "B2B SaaS"),
        concepts=(
            ("SRP", "One reason to change per class.", "class ReportWriter:\n    def write(self, text):\n        return text.upper()\nprint(ReportWriter().write('a'))"),
            ("OCP", "Open for extension, closed for modification.", "class Tax:\n    def rate(self):\n        return 0.1\nclass ReducedTax(Tax):\n    def rate(self):\n        return 0.05\nprint(ReducedTax().rate())"),
            ("DIP", "Depend on abstractions.", "class Repo:\n    def save(self, data):\n        return data\nclass Service:\n    def __init__(self, repo: Repo):\n        self.repo = repo\nprint(Service(Repo()).repo.save(1))"),
        ),
        concept="SOLID favors composable, testable modules.",
        purpose="Manage complexity as systems grow.",
        benefits="Easier testing, safer refactors, clearer boundaries.",
        use_cases="Plugin systems, policy engines, multi-tenant apps.",
        best_practices="Small classes; inject dependencies; program to interfaces.",
        mistakes="God objects, concrete imports everywhere, inheritance abuse.",
        basic_syntax="# depend on Protocol/ABC interfaces, not concrete classes",
        structure="define abstraction -> implement -> inject",
        pattern=dedent("""\
            class Service:
                def __init__(self, repo):
                    self.repo = repo


            print(Service(repo=object()))"""),
        beginner="class Formatter:\n    def fmt(self, x):\n        return str(x)\nprint(Formatter().fmt(1))",
        intermediate=dedent("""\
            from typing import Protocol


            class Notifier(Protocol):
                def send(self, message: str) -> None: ...


            class EmailNotifier:
                def send(self, message: str) -> None:
                    print(message)


            def notify(user: str, notifier: Notifier) -> None:
                notifier.send(f'hello {user}')


            notify('Ada', EmailNotifier())"""),
        advanced=dedent("""\
            class DiscountPolicy:
                def discount(self, total: float) -> float:
                    return total


            class VIPDiscount(DiscountPolicy):
                def discount(self, total: float) -> float:
                    return total * 0.9


            class Checkout:
                def __init__(self, policy: DiscountPolicy):
                    self.policy = policy

                def total(self, amount: float) -> float:
                    return self.policy.discount(amount)


            print(Checkout(VIPDiscount()).total(100))"""),
        mermaid="flowchart TD\n    A[SOLID] --> B[SRP]\n    A --> C[OCP]\n    A --> D[LSP]\n    A --> E[ISP]\n    A --> F[DIP]",
    )

    p(
        "Memory Management",
        what="Memory management covers how Python allocates, uses, and releases object memory.",
        why="Memory leaks and bloat cause crashes and cost in production.",
        where="Long-running services, data processing, ML training, embedded Python.",
        objectives=("Understand object sizes and references.", "Use sys.getsizeof and tracemalloc.", "Break reference cycles thoughtfully."),
        outcome="You diagnose and reduce memory usage in Python programs.",
        industry=("Streaming ETL", "Web workers", "Scientific computing", "Ad tech"),
        concepts=(
            ("References", "Names point to objects.", "import sys\na = []\nb = a\nprint(sys.getrefcount(a) > 1)"),
            ("getsizeof", "Shallow object size.", "import sys\nprint(sys.getsizeof([]))"),
            ("tracemalloc", "Track allocations.", "import tracemalloc\ntracemalloc.start()\nx = [0] * 1000\nprint(tracemalloc.get_traced_memory()[0] > 0)"),
        ),
        concept="CPython uses reference counting plus cyclic GC.",
        purpose="Use memory efficiently and avoid leaks.",
        benefits="Stability, lower cloud bills, faster caches.",
        use_cases="Batch jobs, caches, image/audio buffers.",
        best_practices="Profile before optimizing; use generators; weakref caches.",
        mistakes="Global caches without bounds, circular refs with __del__, huge lists.",
        basic_syntax="import sys\nsys.getsizeof(obj)",
        structure="measure -> identify hotspots -> reduce retention",
        pattern="for chunk in read_chunks(): process(chunk)",
        beginner="import sys\nprint(sys.getsizeof('hello'))",
        intermediate=dedent("""\
            import tracemalloc

            tracemalloc.start()
            data = bytearray(10_000)
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            print(peak > current)"""),
        advanced=dedent("""\
            import gc

            gc.set_threshold(700, 10, 10)
            objects = [{} for _ in range(100)]
            del objects
            print(gc.collect() >= 0)"""),
        mermaid="flowchart LR\n    A[Objects] --> B[Refcount]\n    B --> C[GC Cycles]\n    C --> D[Free Memory]",
    )

    p(
        "Garbage Collection",
        what="Garbage collection reclaims memory from unreachable objects, especially cycles.",
        why="Reference cycles alone would leak memory without cyclic GC.",
        where="Graphs, linked structures, long-lived caches, ORM identity maps.",
        objectives=("Explain refcount vs generational GC.", "Use gc module for debugging.", "Design to minimize cycles."),
        outcome="You understand when Python frees objects and how to debug retention.",
        industry=("Game servers", "Graph analytics", "Desktop apps", "ORM-heavy web apps"),
        concepts=(
            ("refcount", "Immediate reclaim when zero.", "import sys\nobj = object()\nprint(sys.getrefcount(obj) >= 2)"),
            ("gc.collect", "Force collection.", "import gc\nprint(isinstance(gc.collect(), int))"),
            ("generations", "GC generations 0/1/2.", "import gc\nprint(len(gc.get_threshold()) == 3)"),
        ),
        concept="Generational GC tracks container objects in cycles.",
        purpose="Reclaim cyclic garbage automatically.",
        benefits="Less manual memory management than C.",
        use_cases="Linked lists, parent/child trees, observer graphs.",
        best_practices="Use weakref for caches; avoid __del__ complexity.",
        mistakes="Creating unbounded cycles, disabling GC without reason.",
        basic_syntax="import gc\ngc.collect()",
        structure="allocate -> use -> dereference -> GC runs",
        pattern="import weakref\nweakref.ref(obj)",
        beginner="import gc\nprint(gc.isenabled())",
        intermediate=dedent("""\
            import gc

            class Node:
                def __init__(self):
                    self.ref = None

            a = Node()
            b = Node()
            a.ref = b
            b.ref = a
            del a, b
            print(gc.collect() >= 0)"""),
        advanced=dedent("""\
            import weakref


            class Cache:
                def __init__(self):
                    self._items = {}

                def set(self, key, value):
                    self._items[key] = weakref.ref(value)

                def get(self, key):
                    ref = self._items.get(key)
                    return ref() if ref else None


            c = Cache()
            obj = {'a': 1}
            c.set('k', obj)
            print(c.get('k'))"""),
        mermaid="flowchart TD\n    A[Objects] --> B{Reachable?}\n    B -->|no| C[GC Collect]\n    B -->|yes| D[Keep]",
    )

    p(
        "Python Internals",
        what="Python internals cover bytecode, the evaluation loop, and CPython implementation details.",
        why="Internals explain performance characteristics and debugging mysteries.",
        where="Performance tuning, compiler tooling, advanced debugging, C extensions.",
        objectives=("Inspect bytecode with dis.", "Explain frame objects and namespaces.", "Understand GIL at high level."),
        outcome="You read dis output and understand how CPython executes code.",
        industry=("Language tooling", "High-performance Python", "Security research", "Compiler dev"),
        concepts=(
            ("bytecode", "Stack machine instructions.", "import dis\ndis.dis('a=1')"),
            ("frame", "Execution frame with locals.", "def f():\n    x = 1\n    return x\nprint(f())"),
            ("GIL", "Global interpreter lock.", "import sys\nprint(hasattr(sys, 'version'))"),
        ),
        concept="CPython compiles to bytecode interpreted by the eval loop.",
        purpose="Deepen mental model of Python execution.",
        benefits="Better optimization instincts, clearer profiling.",
        use_cases="Hot path optimization, custom profilers, REPL tools.",
        best_practices="Profile first; consider PyPy/C extensions for hot loops.",
        mistakes="Micro-optimizing without measurement, fighting the GIL blindly.",
        basic_syntax="import dis\ndis.dis(func)",
        structure="source -> compile -> bytecode -> eval loop",
        pattern="dis.dis(compile('x=1', '<s>', 'exec'))",
        beginner="import dis\ndis.dis(lambda x: x + 1)",
        intermediate=dedent("""\
            import dis


            def add(a, b):
                return a + b


            dis.dis(add)"""),
        advanced=dedent("""\
            import types

            code = compile('result = 40 + 2', '<string>', 'exec')
            namespace = {}
            exec(code, namespace)
            print(namespace['result'])"""),
        mermaid="flowchart LR\n    A[Source] --> B[Compile]\n    B --> C[Bytecode]\n    C --> D[Eval Loop]",
    )

    p(
        "Metaclasses",
        what="Metaclasses are classes that create classes, hooking into class construction.",
        why="Frameworks use metaclasses for ORMs, validation, and API registries.",
        where="Django models, dataclass-like codegen, plugin registration, singletons.",
        objectives=("Explain type and class creation.", "Write a simple metaclass.", "Know when class decorators suffice."),
        outcome="You understand metaclass use cases and implement simple ones.",
        industry=("Web frameworks", "Code generators", "Enterprise DSLs", "Testing frameworks"),
        concepts=(
            ("type", "Default metaclass.", "class A: pass\nprint(type(A))"),
            ("__new__", "Metaclass creates class.", "class Meta(type):\n    def __new__(mcls, name, bases, ns):\n        ns['tag'] = name.lower()\n        return super().__new__(mcls, name, bases, ns)\nclass A(metaclass=Meta): pass\nprint(A.tag)"),
            ("__init__", "Initialize created class.", "class Meta(type):\n    def __init__(cls, name, bases, ns):\n        super().__init__(name, bases, ns)\n        cls.created = True\nclass B(metaclass=Meta): pass\nprint(B.created)"),
        ),
        concept="Metaclasses customize class object creation.",
        purpose="Framework-level automation and enforcement.",
        benefits="Centralized registration, enforced conventions.",
        use_cases="ORM field collection, API route tables, interface enforcement.",
        best_practices="Prefer simpler hooks first; document heavily.",
        mistakes="Metaclass for everything, incomprehensible MRO interactions.",
        basic_syntax=dedent("""\
            class Meta(type):
                pass


            class MyClass(metaclass=Meta):
                pass


            print(MyClass.__name__)"""),
        structure="metaclass __new__/__init__ -> class object",
        pattern=dedent("""\
            class Registry(type):
                registry = {}

                def __new__(mcls, name, bases, namespace):
                    cls = super().__new__(mcls, name, bases, namespace)
                    registry = mcls.registry
                    registry[name] = cls
                    return cls


            print(callable(Registry))"""),
        beginner="print(type(int))",
        intermediate=dedent("""\
            class PluginMeta(type):
                plugins = {}

                def __new__(mcls, name, bases, namespace):
                    cls = super().__new__(mcls, name, bases, namespace)
                    if name != 'PluginBase':
                        mcls.plugins[name] = cls
                    return cls


            class PluginBase(metaclass=PluginMeta):
                pass


            class EmailPlugin(PluginBase):
                pass


            print('EmailPlugin' in PluginMeta.plugins)"""),
        advanced=dedent("""\
            class SingletonMeta(type):
                _instances = {}

                def __call__(cls, *args, **kwargs):
                    if cls not in cls._instances:
                        cls._instances[cls] = super().__call__(*args, **kwargs)
                    return cls._instances[cls]


            class Config(metaclass=SingletonMeta):
                def __init__(self):
                    self.env = 'prod'


            print(Config() is Config())"""),
        mermaid="flowchart LR\n    A[metaclass] --> B[class object]\n    B --> C[instances]",
    )

    p(
        "Descriptors",
        what="Descriptors implement __get__, __set__, or __delete__ to customize attribute access.",
        why="They power properties, ORM fields, and validated attributes.",
        where="Frameworks, data models, lazy computed fields, cached attributes.",
        objectives=("Implement descriptor protocol.", "Understand data vs non-data descriptors.", "Use property as descriptor shortcut."),
        outcome="You control attribute access with descriptors and properties.",
        industry=("ORMs", "Validation libraries", "Game engines", "Financial models"),
        concepts=(
            ("__get__", "Customize read.", "class D:\n    def __get__(self, obj, owner):\n        return 42\nclass A:\n    x = D()\nprint(A().x)"),
            ("__set__", "Customize write.", "class Positive:\n    def __set__(self, obj, value):\n        if value < 0: raise ValueError\n        obj._v = value\n    def __get__(self, obj, owner):\n        return obj._v\nclass Account:\n    balance = Positive()\na = Account()\na.balance = 10\nprint(a.balance)"),
            ("property", "Built-in descriptor.", "class C:\n    def __init__(self):\n        self._n = 0\n    @property\n    def n(self):\n        return self._n\nprint(C().n)"),
        ),
        concept="Descriptors intercept dot access on classes.",
        purpose="Reuse attribute logic across classes.",
        benefits="DRY validation, lazy loading, typed fields.",
        use_cases="Validated setters, cached properties, ORM columns.",
        best_practices="Use property first; descriptor for reuse across classes.",
        mistakes="Infinite recursion in __get__, confusing data descriptor priority.",
        basic_syntax=dedent("""\
            class Desc:
                def __get__(self, obj, owner=None):
                    return 42


            class Host:
                value = Desc()


            print(Host().value)"""),
        structure="define descriptor -> assign to class -> access via instance",
        pattern=dedent("""\
            class Model:
                @property
                def field(self):
                    return self._field


            m = Model()
            m._field = 1
            print(m.field)"""),
        beginner=dedent("""\
            class Echo:
                def __get__(self, obj, owner):
                    return 'echo'


            class Host:
                msg = Echo()


            print(Host().msg)"""),
        intermediate=dedent("""\
            class Typed:
                def __init__(self, name, expected_type):
                    self.name = name
                    self.expected_type = expected_type

                def __set_name__(self, owner, name):
                    self.name = name

                def __get__(self, obj, owner):
                    return obj.__dict__.get(self.name)

                def __set__(self, obj, value):
                    if not isinstance(value, self.expected_type):
                        raise TypeError('wrong type')
                    obj.__dict__[self.name] = value


            class User:
                age = Typed('age', int)


            u = User()
            u.age = 30
            print(u.age)"""),
        advanced=dedent("""\
            class LazyProperty:
                def __init__(self, func):
                    self.func = func
                    self.name = func.__name__

                def __get__(self, obj, owner):
                    if obj is None:
                        return self
                    value = self.func(obj)
                    setattr(obj, self.name, value)
                    return value


            class Data:
                @LazyProperty
                def expensive(self):
                    return sum(range(1000))


            d = Data()
            print(d.expensive == d.expensive)"""),
        mermaid="flowchart LR\n    A[obj.attr] --> B[Descriptor __get__]\n    B --> C[Value]",
    )

    p(
        "Concurrency",
        what="Concurrency coordinates multiple tasks making progress without necessarily running in parallel.",
        why="Users expect responsive systems during I/O and background work.",
        where="Web servers, UI backends, job orchestration, streaming.",
        objectives=("Contrast concurrency vs parallelism.", "Combine threads and async appropriately.", "Use queues for producer/consumer."),
        outcome="You design systems where tasks overlap safely.",
        industry=("Realtime dashboards", "Chat", "Trading feeds", "IoT hubs"),
        concepts=(
            ("Concurrency", "Tasks interleave progress.", "import asyncio\nasync def task():\n    return 1\nprint(asyncio.run(task()))"),
            ("Parallelism", "Simultaneous CPU execution.", "print('use multiprocessing for CPU parallel')"),
            ("Queue", "Coordinate workers.", "from queue import Queue\nq = Queue()\nq.put(1)\nprint(q.get())"),
        ),
        concept="Concurrency manages many tasks; parallelism uses multiple cores.",
        purpose="Improve throughput and responsiveness.",
        benefits="Better resource utilization, smoother UX.",
        use_cases="Download managers, job workers, server request handling.",
        best_practices="Match tool to workload; bound queues; monitor backlog.",
        mistakes="Threads for CPU-bound, unbounded task spawning, no backpressure.",
        basic_syntax="queue.put(item)\nitem = queue.get()",
        structure="producers -> queue -> consumers",
        pattern="asyncio.create_task(coro)",
        beginner="from queue import Queue\nq = Queue()\nq.put('job')\nprint(q.get())",
        intermediate=dedent("""\
            import asyncio

            async def worker(name, delay):
                await asyncio.sleep(delay)
                return name

            async def main():
                results = await asyncio.gather(worker('a', 0.01), worker('b', 0.01))
                print(sorted(results))

            asyncio.run(main())"""),
        advanced=dedent("""\
            import threading
            from queue import Queue


            def consumer(q: Queue, out: list):
                while True:
                    item = q.get()
                    if item is None:
                        break
                    out.append(item * 2)
                    q.task_done()


            q = Queue()
            out = []
            t = threading.Thread(target=consumer, args=(q, out))
            t.start()
            q.put(21)
            q.put(None)
            t.join()
            print(out)"""),
        mermaid="flowchart LR\n    A[Tasks] --> B[Scheduler]\n    B --> C[Workers]",
    )

    p(
        "Parallel Computing",
        what="Parallel computing executes computations simultaneously across cores or machines.",
        why="CPU-heavy workloads need parallelism to meet latency SLAs.",
        where="NumPy, multiprocessing, Spark, GPU offload, simulation.",
        objectives=("Use process pools for CPU parallelism.", "Partition data for workers.", "Understand Amdahl's law limits."),
        outcome="You scale CPU-bound Python workloads across cores.",
        industry=("Quant", "Rendering", "Scientific HPC", "ML feature gen"),
        concepts=(
            ("Process pool", "Multiple interpreters.", "from concurrent.futures import ProcessPoolExecutor\nprint(ProcessPoolExecutor)"),
            ("map", "Apply func across inputs.", "print(list(map(lambda x: x * 2, [1, 2, 3])))"),
            ("chunking", "Split data for workers.", "data = list(range(10))\nchunks = [data[i:i+3] for i in range(0, len(data), 3)]\nprint(len(chunks))"),
        ),
        concept="Parallelism requires independent work units and merges results.",
        purpose="Reduce wall-clock time for heavy compute.",
        benefits="Faster batch jobs, higher hardware utilization.",
        use_cases="Monte Carlo, image filters, large transforms.",
        best_practices="Minimize IPC; profile serial vs parallel; pick chunk sizes.",
        mistakes="Tiny tasks overhead, pickle overhead, no speedup due to serial sections.",
        basic_syntax="with ProcessPoolExecutor() as pool:\n    pool.map(func, items)",
        structure="partition -> map workers -> reduce results",
        pattern="pool.map(process_chunk, chunks)",
        beginner="print(sum(map(lambda x: x * x, range(5))))",
        intermediate=dedent("""\
            from concurrent.futures import ProcessPoolExecutor


            def square(n: int) -> int:
                return n * n


            if __name__ == '__main__':
                with ProcessPoolExecutor(max_workers=2) as pool:
                    print(list(pool.map(square, range(4))))"""),
        advanced=dedent("""\
            def parallel_sum(numbers, workers=2):
                size = len(numbers) // workers or 1
                chunks = [numbers[i:i + size] for i in range(0, len(numbers), size)]
                partials = [sum(chunk) for chunk in chunks]
                return sum(partials)


            print(parallel_sum(list(range(10)), workers=2))"""),
        mermaid="flowchart LR\n    A[Input Data] --> B[Partition]\n    B --> C[Workers]\n    C --> D[Reduce]",
    )

    p(
        "Distributed Systems",
        what="Distributed systems coordinate multiple nodes over unreliable networks.",
        why="Scale and fault tolerance require multiple machines and services.",
        where="Microservices, Kafka pipelines, cloud storage, global SaaS.",
        objectives=("Explain CAP tradeoffs at high level.", "Design idempotent workers and retries.", "Use message queues and service discovery."),
        outcome="You reason about failure modes in distributed Python systems.",
        industry=("Cloud platforms", "Streaming", "Global e-commerce", "Fintech"),
        concepts=(
            ("Idempotency", "Safe retries.", "def charge(idempotency_key, amount):\n    seen = set()\n    if idempotency_key in seen:\n        return 'duplicate'\n    seen.add(idempotency_key)\n    return f'charged {amount}'\nprint(charge('k1', 10))"),
            ("Timeouts", "Bound waiting.", "import socket\nsocket.setdefaulttimeout(5.0)\nprint(socket.getdefaulttimeout())"),
            ("Message queue", "Async decoupling.", "QUEUE = []\nQUEUE.append({'task': 1})\nprint(QUEUE.pop(0))"),
        ),
        concept="Network partitions and latency are inevitable.",
        purpose="Build reliable multi-node applications.",
        benefits="Scale, isolation, geographic distribution.",
        use_cases="Order processing, event buses, crawl fleets.",
        best_practices="Design for failure; observability; sagas; idempotent handlers.",
        mistakes="Single point of failure, no retries, distributed monolith coupling.",
        basic_syntax="# worker consumes message -> process -> ack",
        structure="producer -> queue -> consumer -> store",
        pattern=dedent("""\
            def retry_delay(attempt: int, base: float = 0.1) -> float:
                return base * (2 ** attempt)


            print(retry_delay(2))"""),
        beginner="jobs = []\njobs.append('email')\nprint(jobs.pop())",
        intermediate=dedent("""\
            def handle_event(event, processed: set):
                event_id = event['id']
                if event_id in processed:
                    return 'skipped'
                processed.add(event_id)
                return 'handled'


            print(handle_event({'id': '1'}, set()))"""),
        advanced=dedent("""\
            import hashlib


            def shard_for(key: str, num_shards: int) -> int:
                digest = hashlib.md5(key.encode(), usedforsecurity=False).hexdigest()
                return int(digest, 16) % num_shards


            print(shard_for('user-42', 8))"""),
        mermaid="flowchart LR\n    A[Service A] --> B[Queue]\n    B --> C[Service B]\n    C --> D[Database]",
    )

    p(
        "Network Programming",
        what="Network programming sends and receives data over TCP/IP and application protocols.",
        why="Distributed apps communicate via sockets, HTTP, and messaging.",
        where="Clients, servers, proxies, IoT gateways, custom protocols.",
        objectives=("Understand IP, ports, TCP vs UDP.", "Use socket API basics.", "Handle timeouts and buffering."),
        outcome="You implement basic network clients and servers in Python.",
        industry=("Telecom", "Gaming netcode", "IoT", "Custom protocols"),
        concepts=(
            ("TCP", "Reliable stream.", "import socket\nprint(socket.SOCK_STREAM)"),
            ("UDP", "Datagram protocol.", "import socket\nprint(socket.SOCK_DGRAM)"),
            ("socket", "Endpoint abstraction.", "import socket\ns = socket.socket()\nprint(type(s).__name__)"),
        ),
        concept="Sockets are the foundation beneath HTTP and many protocols.",
        purpose="Move bytes between hosts reliably or quickly.",
        benefits="Full control, custom protocols, low-level tooling.",
        use_cases="Echo server, metrics agent, device firmware comms.",
        best_practices="Set timeouts; handle partial reads; close sockets in finally.",
        mistakes="Blocking forever, no framing, ignoring endianness in binary protocols.",
        basic_syntax="import socket\nsock = socket.create_connection(('example.com', 80), timeout=5)",
        structure="create socket -> connect/bind -> send/recv -> close",
        pattern="with socket.create_connection(addr) as s: s.sendall(data)",
        beginner="import socket\nprint(socket.gethostname())",
        intermediate=dedent("""\
            import socket

            def recv_all(sock, size: int) -> bytes:
                chunks = []
                while len(b''.join(chunks)) < size:
                    chunk = sock.recv(size - len(b''.join(chunks)))
                    if not chunk:
                        break
                    chunks.append(chunk)
                return b''.join(chunks)


            print(callable(recv_all))"""),
        advanced=dedent("""\
            import selectors
            import socket


            def echo_server():
                sel = selectors.DefaultSelector()
                sock = socket.socket()
                sock.bind(('127.0.0.1', 0))
                sock.listen()
                sel.register(sock, selectors.EVENT_READ)
                return sock, sel


            s, sel = echo_server()
            print(s.getsockname()[1] > 0)
            s.close()
            sel.close()"""),
        mermaid="flowchart LR\n    A[Client Socket] --> B[Network]\n    B --> C[Server Socket]",
    )

    p(
        "Socket Programming",
        what="Socket programming implements clients and servers using BSD sockets API.",
        why="Low-level control is needed for custom services and performance-sensitive I/O.",
        where="Chat servers, game servers, proxies, embedded agents.",
        objectives=("Build TCP echo client/server.", "Handle bind/listen/accept.", "Use non-blocking or asyncio streams."),
        outcome="You write minimal socket-based networked programs.",
        industry=("Multiplayer games", "VPN tooling", "Industrial IoT", "Media streaming"),
        concepts=(
            ("bind/listen", "Server waits for connections.", "import socket\ns = socket.socket()\ns.bind(('127.0.0.1', 0))\nprint(s.getsockname()[1] > 0)\ns.close()"),
            ("connect", "Client initiates TCP.", "import socket\ns = socket.socket()\ntry:\n    s.connect(('127.0.0.1', 9))\nexcept OSError:\n    pass\nfinally:\n    s.close()"),
            ("send/recv", "Transfer bytes.", "import socket\na, b = socket.socketpair()\na.send(b'ping')\nprint(b.recv(4))"),
        ),
        concept="Stream sockets deliver ordered byte pipes.",
        purpose="Implement custom network endpoints.",
        benefits="Minimal dependencies, full protocol control.",
        use_cases="Echo, heartbeat, binary framing, LAN tools.",
        best_practices="Use asyncio streams for many connections; always timeout.",
        mistakes="No message framing, one recv equals one message assumption.",
        basic_syntax="sock.sendall(b'data')\ndata = sock.recv(1024)",
        structure="socket -> bind/connect -> send/recv loop -> shutdown",
        pattern=dedent("""\
            class Server:
                def accept(self):
                    return 'connection'


            class Client:
                def connect(self):
                    return 'connected'


            print(Server().accept(), Client().connect())"""),
        beginner=dedent("""\
            import socket

            client, server = socket.socketpair()
            client.send(b'hello')
            print(server.recv(5))"""),
        intermediate=dedent("""\
            import socket


            def run_echo_once():
                server = socket.socket()
                server.bind(('127.0.0.1', 0))
                server.listen(1)
                port = server.getsockname()[1]
                client = socket.socket()
                client.connect(('127.0.0.1', port))
                conn, _ = server.accept()
                conn.sendall(b'pong')
                print(client.recv(4))
                conn.close()
                client.close()
                server.close()


            run_echo_once()"""),
        advanced=dedent("""\
            import asyncio


            async def handle(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
                data = await reader.read(100)
                writer.write(data.upper())
                await writer.drain()
                writer.close()


            async def main():
                server = await asyncio.start_server(handle, '127.0.0.1', 0)
                addr = server.sockets[0].getsockname()
                reader, writer = await asyncio.open_connection(*addr)
                writer.write(b'hi')
                await writer.drain()
                print((await reader.read(10)).decode())
                writer.close()
                server.close()


            asyncio.run(main())"""),
        mermaid="flowchart TD\n    A[Server bind/listen] --> B[accept]\n    B --> C[recv/send loop]",
    )

    p(
        "Cybersecurity Automation",
        what="Cybersecurity automation uses Python to orchestrate scans, parsing, and response workflows.",
        why="Security teams must scale repetitive analysis and enrichment tasks.",
        where="SOAR platforms, vuln management, log enrichment, phishing analysis.",
        objectives=("Parse logs and IOCs with Python.", "Call security APIs safely.", "Automate repeatable playbooks."),
        outcome="You build Python automations that support security operations.",
        industry=("SOC teams", "MSSP", "AppSec", "Compliance automation"),
        concepts=(
            ("IOC parsing", "Extract indicators.", "import re\nline = '1.2.3.4 failed login'\nprint(re.findall(r'\\d+\\.\\d+\\.\\d+\\.\\d+', line))"),
            ("Hashing", "Fingerprint files.", "import hashlib\nprint(hashlib.sha256(b'data').hexdigest()[:8])"),
            ("Automation script", "Schedule repeatable tasks.", "def run_playbook():\n    return ['parsed', 'enriched']\nprint(run_playbook())"),
        ),
        concept="Automate verify-enrich-respond loops with scripts.",
        purpose="Reduce manual toil and response time.",
        benefits="Consistency, speed, audit trails.",
        use_cases="Phish triage, CVE ticket creation, firewall rule audits.",
        best_practices="Least privilege creds; validate inputs; log actions; dry-run mode.",
        mistakes="Running unverified scripts as root, storing secrets in code.",
        basic_syntax="import hashlib\nhashlib.sha256(data).hexdigest()",
        structure="ingest -> parse -> enrich -> ticket/action",
        pattern="for alert in alerts:\n    enrich(alert)\n    if severity(alert): escalate(alert)",
        beginner="import re\nprint(bool(re.search(r'ERROR', 'ERROR login failed')))",
        intermediate=dedent("""\
            import hashlib


            def file_sha256(path: str) -> str:
                h = hashlib.sha256()
                with open(path, 'rb') as f:
                    for chunk in iter(lambda: f.read(8192), b''):
                        h.update(chunk)
                return h.hexdigest()


            print(len(file_sha256(__file__)) == 64)"""),
        advanced=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class Alert:
                ip: str
                severity: int


            def triage(alerts: list[Alert]) -> list[Alert]:
                return sorted([a for a in alerts if a.severity >= 7], key=lambda a: -a.severity)


            print(triage([Alert('1.2.3.4', 8), Alert('5.6.7.8', 3)]))"""),
        mermaid="flowchart LR\n    A[Alert Feed] --> B[Parser]\n    B --> C[Enrichment]\n    C --> D[Response]",
    )

    p(
        "Web Scraping",
        what="Web scraping extracts structured data from HTML and HTTP responses.",
        why="Public data powers research, monitoring, and competitive intelligence when permitted.",
        where="Price monitoring, news aggregation, lead gen (compliant), archival.",
        objectives=("Fetch pages responsibly with timeouts.", "Parse HTML with BeautifulSoup or lxml.", "Respect robots.txt and rate limits."),
        outcome="You extract structured fields from web pages ethically and robustly.",
        industry=("Market intelligence", "SEO", "Research", "Compliance monitoring"),
        concepts=(
            ("HTTP fetch", "Retrieve page content.", "HTML = '<html><title>Hi</title></html>'\nprint('Hi' in HTML)"),
            ("HTML parse", "Navigate DOM tree.", "from html.parser import HTMLParser\nclass P(HTMLParser):\n    def handle_starttag(self, tag, attrs):\n        self.tag = tag\np = P()\np.feed('<div></div>')\nprint(p.tag)"),
            ("CSS/selectors", "Target elements.", "from html.parser import HTMLParser\nprint('title' in '<title>x</title>')"),
        ),
        concept="Scraping = fetch + parse + normalize + store.",
        purpose="Turn web pages into datasets.",
        benefits="Automation of manual copy/paste research.",
        use_cases="Product prices, job listings, metadata harvest.",
        best_practices="Rate limit; identify bot; check Terms of Service; cache.",
        mistakes="Ignoring robots, brittle regex-only parsing, no backoff.",
        basic_syntax="html = fetch(url)\nsoup.select('h1.title')",
        structure="fetch -> parse -> extract -> validate -> save",
        pattern="for page in pages:\n    for item in parse(page):\n        store(item)",
        beginner="title = 'Sample'\nprint(title.lower())",
        intermediate=dedent("""\
            from html.parser import HTMLParser


            class TitleParser(HTMLParser):
                def __init__(self):
                    super().__init__()
                    self.in_title = False
                    self.title = ''

                def handle_starttag(self, tag, attrs):
                    if tag == 'title':
                        self.in_title = True

                def handle_data(self, data):
                    if self.in_title:
                        self.title += data

                def handle_endtag(self, tag):
                    if tag == 'title':
                        self.in_title = False


            parser = TitleParser()
            parser.feed('<html><title>Hello</title></html>')
            print(parser.title)"""),
        advanced=dedent("""\
            import time


            class RateLimiter:
                def __init__(self, min_interval: float):
                    self.min_interval = min_interval
                    self.last = 0.0

                def wait(self):
                    now = time.monotonic()
                    elapsed = now - self.last
                    if elapsed < self.min_interval:
                        time.sleep(self.min_interval - elapsed)
                    self.last = time.monotonic()


            limiter = RateLimiter(0.01)
            limiter.wait()
            print('fetched')"""),
        mermaid="flowchart LR\n    A[HTTP GET] --> B[HTML]\n    B --> C[Parser]\n    C --> D[Data]",
    )

    p(
        "Automation Frameworks",
        what="Automation frameworks structure reusable test and RPA-style automation (Selenium, Playwright, Robot).",
        why="Ad-hoc scripts become unmaintainable without page objects and reporting.",
        where="QA automation, browser testing, IT RPA, regression suites.",
        objectives=("Organize tests with page object model.", "Use fixtures and waits properly.", "Integrate automation into CI."),
        outcome="You build maintainable automation suites with frameworks.",
        industry=("QA teams", "SaaS releases", "E-commerce", "Banking UAT"),
        concepts=(
            ("Page Object", "Encapsulate UI locators.", "class LoginPage:\n    def username(self):\n        return '#user'\nprint(LoginPage().username())"),
            ("Waits", "Handle async UI.", "import time\ntime.sleep(0)\nprint('ready')"),
            ("Test runner", "Execute suite.", "TESTS = [lambda: True]\nprint(all(t() for t in TESTS))"),
        ),
        concept="Frameworks separate test logic from UI details.",
        purpose="Reliable repeatable automation at scale.",
        benefits="Maintainability, parallel runs, reporting plugins.",
        use_cases="Smoke tests, checkout flows, admin consoles.",
        best_practices="Stable selectors; explicit waits; screenshot on failure.",
        mistakes="sleep-only sync, duplicated selectors, flaky shared state.",
        basic_syntax="page.click('#submit')\nassert page.text('#msg') == 'OK'",
        structure="pages -> tests -> runner -> reports",
        pattern=dedent("""\
            class LoginPage:
                def open(self):
                    return self

                def login(self, user, password):
                    return user


            print(LoginPage().open().login('ada', 'secret'))"""),
        beginner="def test_true():\n    assert True\ntest_true()",
        intermediate=dedent("""\
            class HomePage:
                def __init__(self, driver):
                    self.driver = driver

                def title(self):
                    return self.driver.get('title')


            class FakeDriver:
                def get(self, key):
                    return {'title': 'Home'}[key]


            print(HomePage(FakeDriver()).title())"""),
        advanced=dedent("""\
            class TestCase:
                def __init__(self, name, fn):
                    self.name = name
                    self.fn = fn

                def run(self):
                    try:
                        self.fn()
                        return self.name, True
                    except AssertionError:
                        return self.name, False


            suite = [TestCase('login', lambda: True)]
            print([tc.run() for tc in suite])"""),
        mermaid="flowchart LR\n    A[Test Runner] --> B[Page Objects]\n    B --> C[Browser Driver]",
    )

    p(
        "ETL Development",
        what="ETL development extracts, transforms, and loads data between systems.",
        why="Business analytics requires clean consolidated datasets from many sources.",
        where="Warehouses, lakes, marketing ops, finance reporting.",
        objectives=("Design idempotent batch pipelines.", "Validate and quarantine bad records.", "Track lineage and batch metadata."),
        outcome="You implement reliable Python ETL jobs.",
        industry=("Data teams", "Retail analytics", "Healthcare reporting", "Ad tech"),
        concepts=(
            ("Extract", "Read from source.", "rows = [{'id': 1, 'v': 'a'}]\nprint(len(rows))"),
            ("Transform", "Clean and reshape.", "clean = [{**r, 'v': r['v'].upper()} for r in rows]\nprint(clean[0]['v'])"),
            ("Load", "Write to destination.", "dest = []\ndest.extend(clean)\nprint(dest[0]['id'])"),
        ),
        concept="ETL moves data with quality gates.",
        purpose="Feed analytics and downstream apps.",
        benefits="Repeatable batches, auditable transforms.",
        use_cases="Nightly sales sync, CRM to warehouse, log aggregation.",
        best_practices="Schema contracts; dead-letter queues; incremental loads.",
        mistakes="No validation, non-idempotent loads, silent row drops.",
        basic_syntax="for row in extract():\n    load(transform(row))",
        structure="extract -> validate -> transform -> load -> audit",
        pattern="batch_id = uuid4(); process(batch_id)",
        beginner="source = [1, 2, None]\nclean = [x for x in source if x is not None]\nprint(clean)",
        intermediate=dedent("""\
            def transform_rows(rows):
                for row in rows:
                    if row.get('amount', 0) < 0:
                        continue
                    yield {**row, 'amount': float(row['amount'])}


            print(list(transform_rows([{'amount': '10'}, {'amount': '-1'}])))"""),
        advanced=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class BatchMeta:
                batch_id: str
                row_count: int


            def load_with_meta(rows, batch_id: str) -> BatchMeta:
                materialized = list(rows)
                return BatchMeta(batch_id=batch_id, row_count=len(materialized))


            print(load_with_meta([{'id': 1}], 'b1'))"""),
        mermaid="flowchart LR\n    A[Source] --> B[Transform]\n    B --> C[Validate]\n    C --> D[Destination]",
    )

    p(
        "Data Engineering",
        what="Data engineering builds reliable pipelines, storage layers, and serving paths for analytics and ML.",
        why="Raw data must become trustworthy tables and features at scale.",
        where="Lakehouses, warehouses, streaming platforms, feature stores.",
        objectives=("Design batch and streaming pipelines.", "Apply partitioning and schema evolution.", "Monitor data quality SLAs."),
        outcome="You architect data platforms with Python components.",
        industry=("Tech unicorns", "Finance", "Healthcare analytics", "Retail"),
        concepts=(
            ("Pipeline", "Orchestrated stages.", "stages = ['extract', 'transform', 'load']\nprint('->'.join(stages))"),
            ("Partitioning", "Split data by key/date.", "parts = {'2026-06-06': [1, 2]}\nprint(list(parts))"),
            ("Lineage", "Track data origin.", "meta = {'source': 'crm', 'batch': '001'}\nprint(meta['source'])"),
        ),
        concept="Data engineering connects sources to trustworthy datasets.",
        purpose="Enable analytics and ML with quality and scale.",
        benefits="Single source of truth, reusable pipelines.",
        use_cases="Daily marts, CDC streams, feature pipelines.",
        best_practices="Idempotent jobs; observability; contract tests on schemas.",
        mistakes="Tight coupling to one tool, no backfills, missing monitoring.",
        basic_syntax="orchestrator.run(dag_id='daily_sales')",
        structure="ingest -> bronze -> silver -> gold",
        pattern=dedent("""\
            def merge_upserts(rows, event_date: str):
                return [dict(r, event_date=event_date) for r in rows]


            print(merge_upserts([{'id': 1}], '2026-06-06'))"""),
        beginner="events = [{'user': 'a', 'ts': 1}, {'user': 'b', 'ts': 2}]\nprint(len(events))",
        intermediate=dedent("""\
            from collections import defaultdict

            def aggregate_by_user(events):
                totals = defaultdict(int)
                for event in events:
                    totals[event['user']] += 1
                return dict(totals)


            print(aggregate_by_user([{'user': 'a'}, {'user': 'a'}, {'user': 'b'}]))"""),
        advanced=dedent("""\
            def validate_schema(row: dict, required: set[str]) -> dict:
                missing = required - row.keys()
                if missing:
                    raise ValueError(f'missing {missing}')
                return row


            print(validate_schema({'id': 1, 'name': 'Ada'}, {'id', 'name'}))"""),
        mermaid="flowchart TD\n    A[Sources] --> B[Ingestion]\n    B --> C[Processing]\n    C --> D[Serving Layer]",
    )
