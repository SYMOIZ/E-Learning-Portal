"""Intermediate topic snippet registrations."""

from __future__ import annotations

from textwrap import dedent
from typing import Callable


def register_intermediate(p: Callable[..., None]) -> None:
    p(
        "Object Oriented Programming",
        what="OOP organizes code around objects that combine data and behavior.",
        why="It models real-world entities and scales large codebases.",
        where="Web frameworks, game engines, enterprise apps, SDK design.",
        objectives=("Design classes and objects.", "Apply encapsulation, inheritance, polymorphism.", "Choose OOP vs functional patterns."),
        outcome="You design maintainable class hierarchies.",
        industry=("Django models", "Fintech domains", "Simulation software", "Game engines"),
        concepts=(
            ("Class", "Blueprint for objects.", "class User:\n    pass\nprint(User)"),
            ("Object", "Instance of a class.", "class Box:\n    pass\nb = Box()\nprint(type(b).__name__)"),
            ("Method", "Function bound to an object.", "class Greeter:\n    def hi(self):\n        return 'hello'\nprint(Greeter().hi())"),
        ),
        concept="Objects bundle state and behavior.",
        purpose="Structure complex domains clearly.",
        benefits="Reuse, abstraction, team scalability.",
        use_cases="ORM models, payment systems, inventory systems.",
        best_practices="Composition over inheritance, small public APIs.",
        mistakes="God classes, deep inheritance trees, anemic models.",
        basic_syntax="class Dog:\n    def bark(self):\n        return 'woof'",
        structure="class -> instantiate -> call methods",
        pattern="class Service:\n    def run(self):\n        return self.execute()",
        beginner=dedent("""\
            class Rectangle:
                def __init__(self, w, h):
                    self.w, self.h = w, h

                def area(self):
                    return self.w * self.h


            print(Rectangle(4, 5).area())"""),
        intermediate=dedent("""\
            from abc import ABC, abstractmethod


            class Notifier(ABC):
                @abstractmethod
                def send(self, message: str) -> None:
                    raise NotImplementedError


            class EmailNotifier(Notifier):
                def send(self, message: str) -> None:
                    print(f"EMAIL: {message}")


            EmailNotifier().send('hi')"""),
        advanced=dedent("""\
            class ValidatedModel:
                def __setattr__(self, name, value):
                    if name.startswith('_'):
                        return super().__setattr__(name, value)
                    if name == 'age' and value < 0:
                        raise ValueError('age must be non-negative')
                    super().__setattr__(name, value)


            obj = ValidatedModel()
            obj.age = 30
            print(obj.age)"""),
        mermaid="flowchart LR\n    A[Class] --> B[Constructor]\n    B --> C[Object]\n    C --> D[Methods]",
    )

    p(
        "Classes",
        what="Classes define attributes and methods shared by all instances of a type.",
        why="They encapsulate data and behavior for a cohesive abstraction.",
        where="Domain models, widgets, service clients, test doubles.",
        objectives=("Declare class attributes and methods.", "Use @classmethod and @staticmethod.", "Document public interface."),
        outcome="You implement classes that represent domain concepts clearly.",
        industry=("ORM entities", "UI components", "Robotics control", "Billing"),
        concepts=(
            ("class statement", "Creates a type object.", "class Point:\n    x = 0\nprint(Point.x)"),
            ("instance attrs", "Per-object state via self.", "class Counter:\n    def __init__(self):\n        self.n = 0\nprint(Counter().n)"),
            ("methods", "Functions receiving self.", "class Calc:\n    def add(self, a, b):\n        return a + b\nprint(Calc().add(2, 3))"),
        ),
        concept="Classes are factories for objects with shared behavior.",
        purpose="Define reusable types with state and operations.",
        benefits="Encapsulation, polymorphism, IDE support.",
        use_cases="Users, orders, sensors, handlers.",
        best_practices="Keep classes focused; prefer dataclasses for data containers.",
        mistakes="Too many responsibilities, public mutable everything.",
        basic_syntax="class Account:\n    def __init__(self, owner):\n        self.owner = owner",
        structure="attrs -> __init__ -> methods -> repr/str optional",
        pattern="class Model:\n    def validate(self):\n        return True",
        beginner="class Person:\n    def __init__(self, name):\n        self.name = name\nprint(Person('Ada').name)",
        intermediate=dedent("""\
            class Temperature:
                def __init__(self, celsius: float):
                    self.celsius = celsius

                @property
                def fahrenheit(self) -> float:
                    return self.celsius * 9 / 5 + 32


            print(Temperature(100).fahrenheit)"""),
        advanced=dedent("""\
            from dataclasses import dataclass, field


            @dataclass
            class Cart:
                items: list[str] = field(default_factory=list)

                def add(self, sku: str) -> None:
                    self.items.append(sku)


            c = Cart()
            c.add('ABC')
            print(c.items)"""),
        mermaid="flowchart LR\n    A[class] --> B[__init__]\n    B --> C[instance]",
    )

    p(
        "Objects",
        what="Objects are instances of classes with their own attribute values.",
        why="Runtime entities carry state that differs per instance.",
        where="Every OOP system—UI nodes, DB rows, device handles.",
        objectives=("Instantiate classes.", "Access and mutate instance state.", "Compare identity vs equality."),
        outcome="You create and interact with objects confidently.",
        industry=("CRM records", "IoT devices", "Game entities", "API resources"),
        concepts=(
            ("Instantiation", "Call class to create object.", "class Node:\n    pass\nn = Node()\nprint(isinstance(n, Node))"),
            ("self", "Reference to current instance.", "class A:\n    def id(self):\n        return id(self)\nprint(A().id())"),
            ("identity", "is checks same object.", "a = []\nb = a\nprint(a is b)"),
        ),
        concept="Objects are class instances with unique state.",
        purpose="Represent individual entities at runtime.",
        benefits="Natural modeling, mutable state when needed.",
        use_cases="Shopping cart line items, connected users.",
        best_practices="Validate invariants in __init__; use properties.",
        mistakes="Shared mutable class attrs, confusing is vs ==.",
        basic_syntax="obj = MyClass()\nobj.value = 1",
        structure="construct -> configure -> invoke methods",
        pattern="user = User(name='Ada')\nuser.activate()",
        beginner="class Book:\n    def __init__(self, title):\n        self.title = title\nprint(Book('Python').title)",
        intermediate=dedent("""\
            class Wallet:
                def __init__(self, balance=0.0):
                    self.balance = balance

                def deposit(self, amount: float) -> None:
                    self.balance += amount


            w = Wallet()
            w.deposit(10)
            print(w.balance)"""),
        advanced=dedent("""\
            class Singleton:
                _instance = None

                def __new__(cls):
                    if cls._instance is None:
                        cls._instance = super().__new__(cls)
                    return cls._instance


            print(Singleton() is Singleton())"""),
        mermaid="flowchart LR\n    A[Class()] --> B[Object State]\n    B --> C[Methods]",
    )

    p(
        "Constructors",
        what="Constructors initialize new objects, primarily via __init__ in Python.",
        why="Proper initialization enforces invariants and required dependencies.",
        where="Models, clients, widgets, connection wrappers.",
        objectives=("Implement __init__ with parameters.", "Use default and keyword-only args.", "Avoid heavy work in __init__ when possible."),
        outcome="You build objects that start in valid, predictable states.",
        industry=("ORM models", "SDK clients", "Hardware drivers", "UI widgets"),
        concepts=(
            ("__init__", "Sets up instance after creation.", "class Item:\n    def __init__(self, sku):\n        self.sku = sku\nprint(Item('A1').sku)"),
            ("__new__", "Creates instance before __init__.", "class T:\n    def __new__(cls):\n        return super().__new__(cls)\nprint(T())"),
            ("post-init", "dataclass __post_init__ hook.", "from dataclasses import dataclass\n@dataclass\nclass R:\n    w: int\n    h: int\n    area: int = 0\n    def __post_init__(self):\n        self.area = self.w * self.h\nprint(R(3,4).area)"),
        ),
        concept="__init__ configures self; __new__ allocates the instance.",
        purpose="Guarantee valid starting state.",
        benefits="Fewer invalid objects, clearer APIs.",
        use_cases="DB models, API tokens, config objects.",
        best_practices="Keep __init__ cheap; inject dependencies; validate early.",
        mistakes="I/O in __init__, too many params, subclass __init__ bugs.",
        basic_syntax="class User:\n    def __init__(self, email):\n        self.email = email",
        structure="__new__ (rare) -> __init__ -> ready object",
        pattern="def __init__(self, repo):\n    self.repo = repo",
        beginner="class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\nprint(Point(1, 2).x)",
        intermediate=dedent("""\
            class Connection:
                def __init__(self, dsn: str, *, timeout: int = 30):
                    self.dsn = dsn
                    self.timeout = timeout


            print(Connection('sqlite://', timeout=10).timeout)"""),
        advanced=dedent("""\
            class Buffer:
                def __init__(self, data: bytes):
                    if not data:
                        raise ValueError('empty buffer')
                    self._data = data

                @property
                def size(self) -> int:
                    return len(self._data)


            print(Buffer(b'abc').size)"""),
        mermaid="flowchart LR\n    A[Call Class] --> B[__new__]\n    B --> C[__init__]\n    C --> D[Ready Object]",
    )

    p(
        "Encapsulation",
        what="Encapsulation hides internal state and exposes a controlled public interface.",
        why="It protects invariants and reduces coupling between components.",
        where="Libraries, domain models, API clients, device drivers.",
        objectives=("Use private-by-convention _attrs.", "Expose @property for controlled access.", "Design minimal public methods."),
        outcome="You prevent accidental misuse of internal object state.",
        industry=("Payment vaults", "Medical records", "Embedded firmware APIs", "SaaS SDKs"),
        concepts=(
            ("Name mangling", "Double underscore alters name.", "class A:\n    def __init__(self):\n        self.__secret = 1\n    def get(self):\n        return self.__secret\nprint(A().get())"),
            ("property", "Getter/setter as attribute.", "class Circle:\n    def __init__(self, r):\n        self.radius = r\n    @property\n    def diameter(self):\n        return self.radius * 2\nprint(Circle(3).diameter)"),
            ("Public API", "Document supported methods.", "class Service:\n    def run(self):\n        return self._execute()\n    def _execute(self):\n        return 'ok'\nprint(Service().run())"),
        ),
        concept="Encapsulation separates interface from implementation.",
        purpose="Protect data integrity and enable refactoring.",
        benefits="Safer changes, clearer contracts, fewer bugs.",
        use_cases="Bank accounts, validated configs, cached clients.",
        best_practices="Properties over getters; don't over-mangle; be consistent.",
        mistakes="Everything public, leaky abstractions, property side effects.",
        basic_syntax="class Account:\n    def __init__(self):\n        self._balance = 0.0",
        structure="private state -> properties -> public methods",
        pattern="value = obj.value  # property-backed access",
        beginner="class Counter:\n    def __init__(self):\n        self._n = 0\n    def inc(self):\n        self._n += 1\n    def value(self):\n        return self._n\nc = Counter(); c.inc(); print(c.value())",
        intermediate=dedent("""\
            class Email:
                def __init__(self, address: str):
                    self.address = address.lower()

                @property
                def domain(self) -> str:
                    return self.address.split('@', 1)[1]


            print(Email('Ada@Example.com').domain)"""),
        advanced=dedent("""\
            class RateLimiter:
                def __init__(self, limit: int):
                    self._limit = limit
                    self._count = 0

                def allow(self) -> bool:
                    if self._count >= self._limit:
                        return False
                    self._count += 1
                    return True


            rl = RateLimiter(2)
            print(rl.allow(), rl.allow(), rl.allow())"""),
        mermaid="flowchart LR\n    A[Client] --> B[Public API]\n    B --> C[Private State]",
    )

    p(
        "Inheritance",
        what="Inheritance lets a subclass reuse and extend a base class.",
        why="Shared behavior avoids duplication; specialization models subtypes.",
        where="Framework hooks, UI kits, exception hierarchies, plugins.",
        objectives=("Subclass and override methods.", "Call super() correctly.", "Prefer composition when reuse is shallow."),
        outcome="You extend existing classes without breaking Liskov expectations.",
        industry=("Web frameworks", "Game engines", "Enterprise ERP", "Test fixtures"),
        concepts=(
            ("Subclass", "class Child(Parent).", "class Animal:\n    def speak(self):\n        return 'sound'\nclass Dog(Animal):\n    def speak(self):\n        return 'woof'\nprint(Dog().speak())"),
            ("super()", "Delegate to parent implementation.", "class B:\n    def val(self):\n        return 1\nclass C(B):\n    def val(self):\n        return super().val() + 1\nprint(C().val())"),
            ("MRO", "Method resolution order.", "class A:\n    def f(self):\n        return 'A'\nclass B(A):\n    pass\nprint(B().f())"),
        ),
        concept="Inheritance is an is-a relationship between types.",
        purpose="Reuse and specialize behavior.",
        benefits="DRY, polymorphic collections, framework extension.",
        use_cases="Custom exceptions, model subclasses, auth backends.",
        best_practices="Shallow trees; override thoughtfully; document contracts.",
        mistakes="Fragile base class, super misuse, deep hierarchies.",
        basic_syntax="class Employee(Person):\n    def role(self):\n        return 'staff'",
        structure="base -> override -> super optional",
        pattern="class Admin(User):\n    def permissions(self):\n        return super().permissions() | {'admin'}",
        beginner="class Bird:\n    def move(self):\n        return 'fly'\nclass Penguin(Bird):\n    def move(self):\n        return 'swim'\nprint(Penguin().move())",
        intermediate=dedent("""\
            class Logger:
                def log(self, msg: str) -> None:
                    print(msg)


            class TimestampLogger(Logger):
                def log(self, msg: str) -> None:
                    super().log(f'[ts] {msg}')


            TimestampLogger().log('start')"""),
        advanced=dedent("""\
            class Shape:
                def area(self) -> float:
                    raise NotImplementedError


            class Square(Shape):
                def __init__(self, side: float):
                    self.side = side

                def area(self) -> float:
                    return self.side ** 2


            print(Square(4).area())"""),
        mermaid="flowchart TD\n    A[Base Class] --> B[Subclass]\n    B --> C[Override Method]",
    )

    p(
        "Polymorphism",
        what="Polymorphism lets different types respond to the same interface.",
        why="Callers depend on behavior, not concrete classes.",
        where="Duck typing, protocols, plugin systems, strategy pattern.",
        objectives=("Write code against shared interfaces.", "Use duck typing safely.", "Combine polymorphism with ABCs or Protocols."),
        outcome="You write flexible code that accepts multiple implementations.",
        industry=("Payment providers", "Cloud storage drivers", "Notification channels", "ML backends"),
        concepts=(
            ("Duck typing", "If it quacks, use it.", "class Duck:\n    def quack(self):\n        return 'quack'\ndef speak(bird):\n    return bird.quack()\nprint(speak(Duck()))"),
            ("Override", "Subclass provides own version.", "class A:\n    def run(self):\n        return 1\nclass B(A):\n    def run(self):\n        return 2\nprint(B().run())"),
            ("Protocol", "Structural typing.", "from typing import Protocol\nclass Runner(Protocol):\n    def run(self) -> int: ...\nclass Job:\n    def run(self) -> int:\n        return 42\ndef start(r: Runner) -> int:\n    return r.run()\nprint(start(Job()))"),
        ),
        concept="Polymorphism emphasizes behavior over concrete type.",
        purpose="Decouple callers from implementations.",
        benefits="Extensibility, testing with fakes, cleaner APIs.",
        use_cases="Strategies, serializers, renderers.",
        best_practices="Small interfaces; type hints with Protocol; test all impls.",
        mistakes="isinstance chains everywhere, violating LSP, hidden requirements.",
        basic_syntax="def render(doc):\n    return doc.to_html()",
        structure="interface -> multiple impls -> caller uses interface",
        pattern="for handler in handlers:\n    handler.process(event)",
        beginner="class Cat:\n    def sound(self):\n        return 'meow'\nclass Dog:\n    def sound(self):\n        return 'woof'\nprint([C().sound() for C in (Cat, Dog)])",
        intermediate=dedent("""\
            class JSONRenderer:
                def render(self, data: dict) -> str:
                    import json
                    return json.dumps(data)


            class XMLRenderer:
                def render(self, data: dict) -> str:
                    return '<root/>'


            def export(renderer, payload):
                return renderer.render(payload)


            print(export(JSONRenderer(), {'a': 1}))"""),
        advanced=dedent("""\
            from typing import Protocol


            class SupportsClose(Protocol):
                def close(self) -> None: ...


            def cleanup(resource: SupportsClose) -> None:
                resource.close()


            class FileLike:
                def close(self) -> None:
                    print('closed')


            cleanup(FileLike())"""),
        mermaid="flowchart LR\n    A[Caller] --> B[Interface]\n    B --> C[Impl A]\n    B --> D[Impl B]",
    )

    p(
        "Abstraction",
        what="Abstraction hides complexity behind simpler interfaces.",
        why="Teams work at appropriate levels without knowing every detail.",
        where="APIs, ORMs, cloud SDKs, hardware abstraction layers.",
        objectives=("Define abstract base classes.", "Hide implementation details.", "Document contracts clearly."),
        outcome="You expose only what clients need while refactoring internals freely.",
        industry=("Cloud SDKs", "Database layers", "GUI toolkits", "Compiler frontends"),
        concepts=(
            ("ABC", "Abstract base class enforces methods.", "from abc import ABC, abstractmethod\nclass Repo(ABC):\n    @abstractmethod\n    def get(self, id: int): ...\nclass MemRepo(Repo):\n    def get(self, id: int):\n        return {'id': id}\nprint(MemRepo().get(1))"),
            ("Facade", "Simple wrapper over subsystems.", "class Storage:\n    def save(self, text: str) -> None:\n        open('out.txt', 'w').write(text)\nStorage().save('hi')"),
            ("Interface segregation", "Small focused interfaces.", "class Reader:\n    def read(self):\n        return 'data'\nprint(Reader().read())"),
        ),
        concept="Abstraction emphasizes what, not how.",
        purpose="Manage complexity and enable change.",
        benefits="Faster client dev, safer refactors, clearer modules.",
        use_cases="Payment gateway facade, storage adapter, ML pipeline stage.",
        best_practices="Stable public APIs; version breaking changes; tests on contracts.",
        mistakes="Leaking internals, giant interfaces, abstract everything.",
        basic_syntax="class API:\n    def fetch(self):\n        return self._request()",
        structure="public facade -> private implementation",
        pattern="class Service:\n    def run(self):\n        return self._pipeline()",
        beginner="class Clock:\n    def now_iso(self):\n        from datetime import datetime, timezone\n        return datetime.now(timezone.utc).isoformat()\nprint(Clock().now_iso()[:4])",
        intermediate=dedent("""\
            from abc import ABC, abstractmethod


            class PaymentGateway(ABC):
                @abstractmethod
                def charge(self, amount: float) -> str:
                    raise NotImplementedError


            class FakeGateway(PaymentGateway):
                def charge(self, amount: float) -> str:
                    return f'charged {amount:.2f}'


            print(FakeGateway().charge(9.99))"""),
        advanced=dedent("""\
            class Database:
                def __init__(self):
                    self._connected = True

                def query(self, sql: str) -> list[tuple]:
                    return [('row',)] if self._connected else []


            class UserRepository:
                def __init__(self, db: Database):
                    self._db = db

                def list_users(self) -> list[tuple]:
                    return self._db.query('SELECT 1')


            print(UserRepository(Database()).list_users())"""),
        mermaid="flowchart LR\n    A[Client] --> B[Abstract API]\n    B --> C[Hidden Impl]",
    )

    p(
        "Magic Methods",
        what="Magic methods (dunders) customize operator and protocol behavior.",
        why="They make user-defined objects feel like built-ins.",
        where="Domain models, containers, context managers, iterators.",
        objectives=("Implement __repr__, __str__, __len__, __eq__.", "Support context manager and iteration protocols.", "Avoid overloading operators without need."),
        outcome="You make classes Pythonic and interoperable with syntax.",
        industry=("Numeric libs", "Custom collections", "ORM fields", "Simulation"),
        concepts=(
            ("__repr__", "Unambiguous debug representation.", "class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __repr__(self):\n        return f'Point({self.x}, {self.y})'\nprint(repr(Point(1,2)))"),
            ("__eq__", "Value equality.", "class V:\n    def __init__(self, n):\n        self.n = n\n    def __eq__(self, other):\n        return isinstance(other, V) and self.n == other.n\nprint(V(1) == V(1))"),
            ("__len__", "Support len(obj).", "class Bag:\n    def __init__(self, items):\n        self.items = items\n    def __len__(self):\n        return len(self.items)\nprint(len(Bag([1,2])))"),
        ),
        concept="Dunders hook into Python data model.",
        purpose="Integrate objects with language features.",
        benefits="Readable syntax, less boilerplate at call sites.",
        use_cases="Vectors, stacks, money types, smart paths.",
        best_practices="Keep semantics intuitive; document equality/hash contract.",
        mistakes="Broken __hash__ with mutable __eq__, surprising operators.",
        basic_syntax="def __repr__(self):\n    return f'MyObj({self.id})'",
        structure="identify protocol -> implement dunders -> test",
        pattern="def __enter__(self):\n    return self",
        beginner="class Title:\n    def __init__(self, text):\n        self.text = text\n    def __str__(self):\n        return self.text.upper()\nprint(str(Title('hi')))",
        intermediate=dedent("""\
            class Stack:
                def __init__(self):
                    self._items = []

                def push(self, item):
                    self._items.append(item)

                def __len__(self):
                    return len(self._items)


            s = Stack()
            s.push(1)
            print(len(s))"""),
        advanced=dedent("""\
            class Vector:
                def __init__(self, x: float, y: float):
                    self.x, self.y = x, y

                def __add__(self, other: 'Vector') -> 'Vector':
                    return Vector(self.x + other.x, self.y + other.y)

                def __repr__(self) -> str:
                    return f'Vector({self.x}, {self.y})'


            print(Vector(1, 2) + Vector(3, 4))"""),
        mermaid="flowchart LR\n    A[Object] --> B[Magic Method]\n    B --> C[Python Syntax]",
    )

    p(
        "Iterators",
        what="Iterators expose __iter__ and __next__ to produce elements lazily.",
        why="Lazy iteration saves memory on large or infinite sequences.",
        where="File scanning, streaming APIs, custom collections, pipelines.",
        objectives=("Use iter() and next().", "Implement iterator protocol.", "Understand StopIteration."),
        outcome="You build lazy sequence producers and consumers.",
        industry=("Log streaming", "Genomics pipelines", "Market data feeds", "Pagination"),
        concepts=(
            ("__iter__", "Returns iterator object.", "data = [1, 2]\nit = iter(data)\nprint(next(it))"),
            ("__next__", "Produces next value or raises StopIteration.", "class Countdown:\n    def __init__(self, n):\n        self.n = n\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.n <= 0:\n            raise StopIteration\n        self.n -= 1\n        return self.n + 1\nprint(list(Countdown(3)))"),
            ("StopIteration", "Signals exhaustion.", "it = iter([])\ntry:\n    next(it)\nexcept StopIteration:\n    print('done')"),
        ),
        concept="Iterators generate values on demand.",
        purpose="Traverse data without loading all at once.",
        benefits="Memory efficient, composable pipelines.",
        use_cases="CSV row scan, socket read loop, paginated API.",
        best_practices="Separate iterable from iterator when reused; handle StopIteration.",
        mistakes="Non-resetting iterators, confusing iterable vs iterator.",
        basic_syntax="for item in iterable:\n    print(item)",
        structure="__iter__ -> __next__ loop -> StopIteration",
        pattern="it = iter(source)\nwhile True:\n    try:\n        item = next(it)\n    except StopIteration:\n        break\n    print(item)",
        beginner="it = iter(['a', 'b'])\nprint(next(it), next(it))",
        intermediate=dedent("""\
            class Range:
                def __init__(self, n):
                    self.n = n
                    self.i = 0

                def __iter__(self):
                    return self

                def __next__(self):
                    if self.i >= self.n:
                        raise StopIteration
                    value = self.i
                    self.i += 1
                    return value


            print(list(Range(3)))"""),
        advanced=dedent("""\
            def line_generator(path: str):
                with open(path, encoding='utf-8') as handle:
                    for line in handle:
                        yield line.rstrip('\\n')


            print(sum(1 for _ in line_generator('README.md')))"""),
        mermaid="flowchart LR\n    A[Iterable] --> B[Iterator]\n    B --> C[next()]",
    )

    p(
        "Generators",
        what="Generators are iterators created by functions with yield.",
        why="They simplify lazy pipelines with readable syntax.",
        where="Streaming transforms, pagination, infinite sequences, coroutine precursors.",
        objectives=("Write generator functions with yield.", "Use yield from for delegation.", "Chain generator pipelines."),
        outcome="You implement memory-efficient data pipelines with generators.",
        industry=("ETL streaming", "Observability pipelines", "Audio processing", "Crawler fetch queues"),
        concepts=(
            ("yield", "Pauses function retaining state.", "def gen():\n    yield 1\n    yield 2\nprint(list(gen()))"),
            ("generator expr", "Like list comp but lazy.", "g = (x * x for x in range(3))\nprint(sum(g))"),
            ("yield from", "Delegate to sub-generator.", "def a():\n    yield from range(2)\nprint(list(a()))"),
        ),
        concept="Generators produce values lazily via yield.",
        purpose="Stream processing with minimal memory.",
        benefits="Simple syntax, composable stages, fast startup.",
        use_cases="Log tailers, batch readers, fibonacci stream.",
        best_practices="Document exhaustion; close generators when needed.",
        mistakes="Mixing return values with yield confusingly, not iterating once.",
        basic_syntax="def count_to(n):\n    for i in range(n):\n        yield i",
        structure="produce -> yield -> resume -> StopIteration",
        pattern="def read_chunks(f):\n    while True:\n        chunk = f.read(1024)\n        if not chunk:\n            break\n        yield chunk",
        beginner="def evens(n):\n    for i in range(n):\n        if i % 2 == 0:\n            yield i\nprint(list(evens(6)))",
        intermediate=dedent("""\
            def moving_average(values, size=3):
                window = []
                for value in values:
                    window.append(value)
                    if len(window) == size:
                        yield sum(window) / size
                        window.pop(0)


            print(list(moving_average([1, 2, 3, 4, 5])))"""),
        advanced=dedent("""\
            def pipeline(*stages):
                def run(source):
                    gen = source
                    for stage in stages:
                        gen = stage(gen)
                    yield from gen

                return run


            def double(iterable):
                for x in iterable:
                    yield x * 2


            print(list(pipeline(double)(iter([1, 2, 3]))))"""),
        mermaid="flowchart LR\n    A[Generator] --> B[yield]\n    B --> C[Consumer for-loop]",
    )

    p(
        "Decorators",
        what="Decorators wrap functions or classes to extend behavior without modifying their source.",
        why="Cross-cutting concerns like logging, timing, auth belong in decorators.",
        where="Web frameworks, CLI, testing, caching layers.",
        objectives=("Write function decorators with functools.wraps.", "Create parameterized decorators.", "Stack decorators safely."),
        outcome="You add reusable behavior around callables cleanly.",
        industry=("Web APIs", "Auth middleware", "Performance tooling", "Feature flags"),
        concepts=(
            ("@syntax", "Syntactic sugar for wrapping.", "def deco(f):\n    def wrap(*a, **k):\n        return f(*a, **k)\n    return wrap\n@deco\ndef hi():\n    return 'hi'\nprint(hi())"),
            ("wraps", "Preserve metadata.", "from functools import wraps\ndef deco(f):\n    @wraps(f)\n    def wrap():\n        return f()\n    return wrap\n@deco\ndef work():\n    'doc'\n    return 1\nprint(work.__name__)"),
            ("Param decorator", "Decorator factory.", "def repeat(n):\n    def deco(f):\n        def wrap():\n            return [f() for _ in range(n)]\n        return wrap\n    return deco\n@repeat(2)\ndef one():\n    return 1\nprint(one())"),
        ),
        concept="Decorators are higher-order functions applying wrappers.",
        purpose="Inject before/after logic around callables.",
        benefits="DRY, composable, framework-friendly.",
        use_cases="Timing, retries, access control, memoization.",
        best_practices="Use wraps; keep wrappers thin; type the wrapped callable.",
        mistakes="Forgetting wraps, decorator order confusion, heavy work at import.",
        basic_syntax="def logged(func):\n    def wrapper(*args, **kwargs):\n        print('call', func.__name__)\n        return func(*args, **kwargs)\n    return wrapper",
        structure="define wrapper -> apply with @ -> preserve metadata",
        pattern=dedent("""\
            def view():
                return 'ok'


            print(view())"""),
        beginner=dedent("""\
            def uppercase(func):
                def wrapper(text):
                    return func(text).upper()
                return wrapper

            @uppercase
            def greet(name):
                return f'hello {name}'

            print(greet('ada'))"""),
        intermediate=dedent("""\
            from functools import wraps


            def retry(times: int):
                def decorator(func):
                    @wraps(func)
                    def wrapper(*args, **kwargs):
                        last = None
                        for _ in range(times):
                            try:
                                return func(*args, **kwargs)
                            except Exception as exc:
                                last = exc
                        raise last

                    return wrapper

                return decorator


            @retry(3)
            def flaky():
                return 'ok'


            print(flaky())"""),
        advanced=dedent("""\
            import time
            from functools import wraps


            def timed(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    start = time.perf_counter()
                    result = func(*args, **kwargs)
                    print(f'{func.__name__} took {time.perf_counter() - start:.4f}s')
                    return result

                return wrapper


            @timed
            def compute(n: int) -> int:
                return sum(range(n))


            print(compute(1000))"""),
        mermaid="flowchart LR\n    A[Function] --> B[Decorator]\n    B --> C[Wrapped Callable]",
    )

    p(
        "Context Managers",
        what="Context managers setup and teardown resources with the with statement.",
        why="Guaranteed cleanup prevents leaks even when errors occur.",
        where="Files, locks, DB transactions, temporary directories.",
        objectives=("Use with for files and locks.", "Implement __enter__/__exit__.", "Use contextlib.contextmanager."),
        outcome="You manage resources safely with with blocks.",
        industry=("Database apps", "Concurrent services", "Infra automation", "Desktop apps"),
        concepts=(
            ("with", "Calls __enter__ and __exit__.", "from contextlib import contextmanager\n@contextmanager\ndef tag(name):\n    print(f'<{name}>')\n    yield\n    print(f'</{name}>')\nwith tag('p'):\n    print('hi')"),
            ("__exit__", "Receives exception info.", "class Demo:\n    def __enter__(self):\n        return self\n    def __exit__(self, exc_type, exc, tb):\n        print('cleanup', exc_type is None)\n        return False\nwith Demo():\n    pass"),
            ("contextmanager", "Generator-based manager.", "from contextlib import contextmanager\n@contextmanager\ndef opened(path):\n    f = open(path, encoding='utf-8')\n    try:\n        yield f\n    finally:\n        f.close()\nwith opened('README.md') as fh:\n    print(fh.readline()[:5])"),
        ),
        concept="Context managers pair acquisition with release.",
        purpose="Deterministic setup/teardown.",
        benefits="Exception-safe cleanup, readable scope.",
        use_cases="Transactions, temp dirs, timing blocks.",
        best_practices="Avoid suppressing exceptions unless intended; keep __exit__ fast.",
        mistakes="Manual open/close, swallowing errors, re-entrant locks misuse.",
        basic_syntax="with open('file.txt', encoding='utf-8') as f:\n    data = f.read()",
        structure="__enter__ -> body -> __exit__",
        pattern="with lock:\n    mutate_shared_state()",
        beginner="from contextlib import suppress\nwith suppress(ValueError):\n    int('x')\nprint('ok')",
        intermediate=dedent("""\
            from contextlib import contextmanager


            @contextmanager
            def temporary(value: str):
                print('set', value)
                try:
                    yield value
                finally:
                    print('unset', value)


            with temporary('config') as cfg:
                print('use', cfg)"""),
        advanced=dedent("""\
            import threading


            class LockGuard:
                def __init__(self, lock: threading.Lock):
                    self.lock = lock

                def __enter__(self):
                    self.lock.acquire()
                    return self

                def __exit__(self, exc_type, exc, tb):
                    self.lock.release()
                    return False


            lock = threading.Lock()
            with LockGuard(lock):
                print('critical section')"""),
        mermaid="flowchart TD\n    A[with] --> B[__enter__]\n    B --> C[Body]\n    C --> D[__exit__]",
    )

    from catalog_parts.intermediate_part2 import _register_intermediate_part2

    _register_intermediate_part2(p)
