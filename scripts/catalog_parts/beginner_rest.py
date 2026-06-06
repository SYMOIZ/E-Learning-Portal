"""Additional topic registrations for make_full_catalog."""

from __future__ import annotations

from textwrap import dedent
from typing import Callable


def register_beginner_rest(p: Callable[..., None]) -> None:
    p(
        "Loops",
        what="Loops repeat blocks of code while a condition holds or over a sequence.",
        why="Iteration processes collections and repeated tasks without duplication.",
        where="Batch processing, reports, games, polling, data pipelines.",
        objectives=("Use for and while loops appropriately.", "Iterate sequences and ranges.", "Avoid infinite loops."),
        outcome="You process collections and repeated work with clear loop constructs.",
        industry=("Report generation", "Game loops", "IoT sampling", "Finance batch jobs"),
        concepts=(
            ("for", "Iterate over iterable objects.", "for ch in 'abc':\n    print(ch)"),
            ("while", "Repeat while condition is true.", "n = 3\nwhile n:\n    n -= 1\n    print(n)"),
            ("range", "Generate arithmetic progressions.", "for i in range(3):\n    print(i)"),
        ),
        concept="Loops automate repetition with controlled exit conditions.",
        purpose="Traverse data and repeat operations efficiently.",
        benefits="Less duplication, scalable processing, idiomatic Python.",
        use_cases="Summing lists, retry logic, parsing lines, animations.",
        best_practices="Prefer for over while when iterating sequences; use enumerate when needed.",
        mistakes="Off-by-one errors, modifying list while iterating, unbounded while True without break.",
        basic_syntax="for item in items:\n    print(item)",
        structure="init -> loop header -> body -> next item",
        pattern="for row in rows:\n    print(row)",
        beginner="for i in range(5):\n    print(i * i)",
        intermediate="total = 0\nfor value in [1, 2, 3, 4]:\n    total += value\nprint(total)",
        advanced=dedent("""\
            for index, name in enumerate(['Ada', 'Grace'], start=1):
                print(index, name)"""),
        mermaid="flowchart TD\n    A[Start Loop] --> B{More?}\n    B -->|yes| C[Body]\n    C --> B\n    B -->|no| D[Exit]",
    )

    p(
        "Nested Loops",
        what="Nested loops place one loop inside another to handle multi-dimensional iteration.",
        why="Matrices, grids, combinations, and nested records require nested iteration.",
        where="Image pixels, seat maps, cartesian products, nested JSON.",
        objectives=("Write nested for loops for 2D data.", "Control complexity with helper functions.", "Break early when possible."),
        outcome="You traverse nested structures without losing readability.",
        industry=("Graphics", "Scheduling", "E-commerce bundles", "Simulation"),
        concepts=(
            ("Outer loop", "Controls major dimension.", "for row in [[1, 2], [3]]:\n    print(row)"),
            ("Inner loop", "Processes each element in a row.", "for row in [[1, 2], [3]]:\n    for x in row:\n        print(x)"),
            ("Cartesian product", "Nested loops generate pairs.", "pairs = [(a, b) for a in range(2) for b in range(2)]\nprint(len(pairs))"),
        ),
        concept="Nested loops walk structures with more than one dimension.",
        purpose="Visit every combination or nested element systematically.",
        benefits="Straightforward for small data, easy to reason about.",
        use_cases="Multiplication tables, board games, nested categories.",
        best_practices="Extract inner body to functions; consider itertools.product.",
        mistakes="O(n^3) surprises, deep nesting without bounds, reusing loop variable names.",
        basic_syntax="for i in range(2):\n    for j in range(2):\n        print(i, j)",
        structure="outer init -> inner init -> body -> inner next -> outer next",
        pattern="for y in rows:\n    for x in y:\n        print(x)",
        beginner="for r in range(2):\n    for c in range(2):\n        print(r, c)",
        intermediate="matrix = [[1, 2], [3, 4]]\nflat = [x for row in matrix for x in row]\nprint(flat)",
        advanced=dedent("""\
            from itertools import product

            for a, b in product(['A', 'B'], [1, 2]):
                print(a, b)"""),
        mermaid="flowchart TD\n    A[Outer] --> B[Inner]\n    B --> C[Process]\n    C --> B",
    )

    p(
        "Break Continue Pass",
        what="break, continue, and pass alter loop flow or serve as placeholders.",
        why="They express early exit, skip iteration, or stub incomplete code cleanly.",
        where="Search loops, validation pipelines, protocol stubs, parsers.",
        objectives=("Use break to exit loops early.", "Use continue to skip iterations.", "Use pass for empty blocks."),
        outcome="You control loop flow precisely without awkward flags.",
        industry=("Log parsing", "Search features", "Games", "Network clients"),
        concepts=(
            ("break", "Exit the nearest enclosing loop.", "for n in range(10):\n    if n == 3:\n        break\nprint('done')"),
            ("continue", "Skip to next iteration.", "for n in range(5):\n    if n % 2 == 0:\n        continue\n    print(n)"),
            ("pass", "Null statement preserving syntax.", "def todo():\n    pass\nprint(callable(todo))"),
        ),
        concept="Flow keywords fine-tune iteration without extra state variables.",
        purpose="Express skip, stop, or stub directly in loops and classes.",
        benefits="Clearer loops, less boilerplate, valid empty blocks.",
        use_cases="Find first match, filter invalid rows, TDD stubs.",
        best_practices="Prefer functions over deeply broken loops; document pass usage.",
        mistakes="break only breaks one level, continue in wrong place, pass hiding missing logic.",
        basic_syntax="for x in xs:\n    if x < 0:\n        continue\n    print(x)",
        structure="loop -> test -> break/continue/pass -> body",
        pattern="for item in items:\n    if item is None:\n        continue\n    print(item)",
        beginner="for i in range(5):\n    if i == 3:\n        break\n    print(i)",
        intermediate="evens = []\nfor n in range(6):\n    if n % 2:\n        continue\n    evens.append(n)\nprint(evens)",
        advanced=dedent("""\
            class Parser:
                def feed(self, chunk: bytes) -> None:
                    pass


            print(hasattr(Parser(), 'feed'))"""),
        mermaid="flowchart TD\n    A[Loop] --> B{break?}\n    B -->|yes| C[Exit]\n    B -->|no| D{continue?}",
    )

    p(
        "Strings",
        what="Strings are immutable sequences of Unicode characters.",
        why="Text processing is central to APIs, logs, and user interfaces.",
        where="Web apps, document tools, NLP preprocessing, log parsers.",
        objectives=("Create and slice strings.", "Use common string methods.", "Format output with f-strings."),
        outcome="You manipulate and format text confidently in Python.",
        industry=("Web frontends", "Log analysis", "Chatbots", "Document automation"),
        concepts=(
            ("Literals", "Quoted text creates str objects.", "msg = 'hello'\nprint(msg.upper())"),
            ("Slicing", "Extract subsequences by index.", "print('Python'[0:2])"),
            ("f-strings", "Embed expressions in strings.", "name = 'Ada'\nprint(f'Hi {name}')"),
        ),
        concept="Strings are immutable Unicode text.",
        purpose="Represent and transform textual data.",
        benefits="Rich methods, easy formatting, UTF-8 by default.",
        use_cases="User names, templates, CSV fields, HTTP bodies.",
        best_practices="Prefer f-strings; avoid concatenating in tight loops.",
        mistakes="Mutating strings, poor encoding handling, O(n^2) concat.",
        basic_syntax="greeting = 'Hello'\nprint(greeting + ' World')",
        structure="create -> transform -> format -> output",
        pattern="label = f'item: {name}'\nprint(label)",
        beginner="text = '  Python  '\nprint(text.strip().lower())",
        intermediate="words = 'a,b,c'.split(',')\nprint('-'.join(words))",
        advanced=dedent("""\
            import re

            print(re.sub(r'\\d+', '#', 'Room 42'))"""),
        mermaid="flowchart LR\n    A[Text Input] --> B[Normalize]\n    B --> C[Transform]\n    C --> D[Output]",
    )

    p(
        "String Methods",
        what="String methods provide built-in operations for searching, splitting, and formatting text.",
        why="Method calls replace hand-written parsing for common text tasks.",
        where="Data cleaning, URL handling, validation, templating.",
        objectives=("Apply strip, split, join, replace, and find.", "Choose methods vs regex appropriately.", "Chain operations readably."),
        outcome="You clean and transform strings using the str API efficiently.",
        industry=("Marketing analytics", "Support tickets", "SEO tools", "Compliance redaction"),
        concepts=(
            ("strip", "Remove leading/trailing whitespace.", "print('  hi  '.strip())"),
            ("split/join", "Tokenize and reassemble strings.", "print('-'.join('a b c'.split()))"),
            ("replace", "Substitute substrings.", "print('foo-bar'.replace('-', '_'))"),
        ),
        concept="str methods operate on immutable copies.",
        purpose="Standardize text transformations.",
        benefits="Readable, fast C implementations, fewer bugs.",
        use_cases="Normalizing emails, parsing tags, masking PII.",
        best_practices="Normalize once; store canonical form; handle None before calling.",
        mistakes="Calling methods on None, locale-unaware case folding, excessive regex.",
        basic_syntax="email = ' Ada@Example.COM '\nprint(email.strip().lower())",
        structure="normalize -> tokenize -> transform -> join",
        pattern="parts = line.strip().split(',')\nprint(parts)",
        beginner="print('hello world'.title())",
        intermediate="slug = 'Hello World'.lower().replace(' ', '-')\nprint(slug)",
        advanced=dedent("""\
            from textwrap import dedent as d

            block = d('''\
                line one
                line two
            ''')
            print(block.splitlines())"""),
        mermaid="flowchart LR\n    A[Raw str] --> B[Methods]\n    B --> C[Clean str]",
    )

    p(
        "Lists",
        what="Lists are ordered, mutable sequences of arbitrary objects.",
        why="They are the default workhorse collection for ordered data.",
        where="Queues, result sets, UI lists, algorithm inputs.",
        objectives=("Create, index, slice, and mutate lists.", "Use list comprehensions.", "Copy lists safely."),
        outcome="You store and transform ordered collections fluently.",
        industry=("Inventory systems", "Analytics", "Media playlists", "Task queues"),
        concepts=(
            ("Literals", "Square brackets build lists.", "nums = [1, 2, 3]\nprint(nums[0])"),
            ("append", "Add element at end.", "items = []\nitems.append('a')\nprint(items)"),
            ("Comprehension", "Build lists from iterables.", "squares = [n * n for n in range(4)]\nprint(squares)"),
        ),
        concept="Lists are dynamic arrays of references.",
        purpose="Hold ordered, changeable sequences.",
        benefits="Versatile, fast append/pop at end, rich API.",
        use_cases="Shopping carts, timelines, batch results.",
        best_practices="Avoid using as default args; copy before mutate shared data.",
        mistakes="Shallow copy surprises, O(n) inserts at front, aliasing bugs.",
        basic_syntax="fruits = ['apple', 'banana']\nprint(len(fruits))",
        structure="create -> access -> mutate -> iterate",
        pattern="results = [transform(x) for x in data]",
        beginner="colors = ['red', 'green']\ncolors.append('blue')\nprint(colors)",
        intermediate="matrix = [[1, 2], [3, 4]]\nprint([row[0] for row in matrix])",
        advanced=dedent("""\
            from copy import deepcopy

            original = [[1], [2]]
            cloned = deepcopy(original)
            cloned[0].append(9)
            print(original, cloned)"""),
        mermaid="flowchart LR\n    A[List] --> B[Index/Slice]\n    B --> C[Mutate]\n    C --> D[Iterate]",
    )

    p(
        "List Methods",
        what="List methods mutate or query lists in place: sort, extend, pop, remove, and more.",
        why="In-place operations save memory and express intent clearly.",
        where="Sorting results, stack behavior, deduplication workflows.",
        objectives=("Use sort, reverse, extend, insert, pop, remove.", "Know which methods return None.", "Pick list vs set for uniqueness."),
        outcome="You update lists efficiently using the list API.",
        industry=("Ranking dashboards", "Undo stacks", "Batch ETL", "Leaderboards"),
        concepts=(
            ("sort", "Order list in place.", "nums = [3, 1, 2]\nnums.sort()\nprint(nums)"),
            ("pop", "Remove and return item.", "stack = [1, 2]\nprint(stack.pop())"),
            ("extend", "Add multiple items.", "a = [1]\na.extend([2, 3])\nprint(a)"),
        ),
        concept="Mutating methods update the same list object.",
        purpose="Modify ordered collections without reassigning names.",
        benefits="Performance, clarity, idiomatic Python.",
        use_cases="Priority queues, rolling windows, in-memory buffers.",
        best_practices="sorted() for new list; key= for custom ordering.",
        mistakes="Assigning sort result, modifying while iterating, pop empty list.",
        basic_syntax="values = [3, 1, 2]\nvalues.sort()\nprint(values)",
        structure="prepare list -> call method -> verify state",
        pattern="items.extend(new_batch)\nitems.sort(key=len)",
        beginner="pets = ['cat', 'dog']\npets.append('bird')\nprint(pets)",
        intermediate="data = ['b', 'a', 'c']\nprint(sorted(data))\nprint(data)",
        advanced=dedent("""\
            from bisect import insort

            scores = [10, 20, 40]
            insort(scores, 25)
            print(scores)"""),
        mermaid="flowchart LR\n    A[List] --> B[Method]\n    B --> C[Updated List]",
    )

    p(
        "Tuples",
        what="Tuples are ordered, immutable sequences often used for fixed records.",
        why="Immutability makes tuples safe dictionary keys and return values.",
        where="Coordinates, DB rows, function returns, config constants.",
        objectives=("Create tuples and unpack them.", "Use tuples as dict keys.", "Choose tuple vs list."),
        outcome="You model fixed-size records with tuples appropriately.",
        industry=("GIS", "Finance ticks", "ORM rows", "Robotics state"),
        concepts=(
            ("Literals", "Parentheses or commas create tuples.", "point = (10, 20)\nprint(point[0])"),
            ("Unpacking", "Assign elements to names.", "x, y = (3, 4)\nprint(x + y)"),
            ("Immutability", "Cannot change length or items.", "t = (1, 2)\nprint(len(t))"),
        ),
        concept="Tuples protect data from accidental mutation.",
        purpose="Represent small fixed structures.",
        benefits="Hashable, memory efficient, clear intent.",
        use_cases="RGB triples, lat/long, multi-return values.",
        best_practices="Use namedtuple or dataclass for many fields.",
        mistakes="Trying to append, confusing single-element syntax, huge tuples.",
        basic_syntax="rgb = (255, 128, 0)\nprint(rgb)",
        structure="pack values -> pass/store -> unpack/use",
        pattern="name, score = get_result()",
        beginner="dims = (1920, 1080)\nprint(dims[0] * dims[1])",
        intermediate="record = ('Ada', 36)\nprint(f'{record[0]} is {record[1]}')",
        advanced=dedent("""\
            from collections import namedtuple

            Point = namedtuple('Point', 'x y')
            print(Point(1, 2)._asdict())"""),
        mermaid="flowchart LR\n    A[Values] --> B[Tuple]\n    B --> C[Unpack/Key]",
    )

    p(
        "Sets",
        what="Sets are unordered collections of unique hashable elements.",
        why="They provide fast membership tests and set algebra.",
        where="Tag systems, deduplication, permission unions, graph nodes.",
        objectives=("Create sets and test membership.", "Apply union, intersection, difference.", "Use set comprehensions."),
        outcome="You deduplicate and compare collections with sets.",
        industry=("Ad targeting", "Security IOC lists", "Catalog tags", "Graph analytics"),
        concepts=(
            ("Literals", "Curly braces or set() constructor.", "tags = {'python', 'web'}\nprint('python' in tags)"),
            ("Uniqueness", "Duplicates are ignored.", "print(set([1, 1, 2]))"),
            ("Algebra", "Union and intersection ops.", "a = {1, 2}\nb = {2, 3}\nprint(a & b)"),
        ),
        concept="Sets enforce uniqueness with hash-based lookup.",
        purpose="Track distinct items and relationships.",
        benefits="O(1) average membership, expressive operators.",
        use_cases="Unique visitors, skill tags, anomaly detection.",
        best_practices="Use frozenset for immutable sets; beware unhashable elements.",
        mistakes="Using {} for empty set, relying on order, set of lists.",
        basic_syntax="seen = set()\nseen.add('a')\nprint(seen)",
        structure="build set -> membership/ops -> consume",
        pattern="unique = set(items)\nprint(len(unique))",
        beginner="print(set('hello'))",
        intermediate="required = {'read', 'write'}\ngranted = {'read'}\nprint(required <= granted)",
        advanced=dedent("""\
            def jaccard(a: set[str], b: set[str]) -> float:
                return len(a & b) / len(a | b)


            print(jaccard({'a', 'b'}, {'b', 'c'}))"""),
        mermaid="flowchart LR\n    A[Items] --> B[Set]\n    B --> C[Unique/Membership]",
    )

    p(
        "Dictionaries",
        what="Dictionaries map hashable keys to values for fast lookup.",
        why="Key-value storage models records, caches, and indexes naturally.",
        where="JSON-like data, configs, memoization, frequency counts.",
        objectives=("Create, access, and update dicts.", "Iterate keys, values, items.", "Use get and setdefault safely."),
        outcome="You structure associative data with dictionaries.",
        industry=("API payloads", "Session stores", "Feature flags", "Word counts"),
        concepts=(
            ("Literals", "Key:value pairs in braces.", "user = {'name': 'Ada'}\nprint(user['name'])"),
            ("get", "Safe lookup with default.", "print({'a': 1}.get('b', 0))"),
            ("items", "Iterate key-value pairs.", "for k, v in {'x': 1}.items():\n    print(k, v)"),
        ),
        concept="Dicts are hash tables mapping keys to values.",
        purpose="Associate labels with data for O(1) lookup.",
        benefits="Flexible schema, fast access, JSON-like.",
        use_cases="HTTP headers, tallies, object caches.",
        best_practices="Use dict comprehensions; avoid mutating while iterating.",
        mistakes="KeyError on missing keys, unhashable keys, relying on order before 3.7 mentally.",
        basic_syntax="scores = {'Ada': 98, 'Lin': 87}\nprint(scores['Ada'])",
        structure="build -> lookup/update -> iterate",
        pattern="count = {}\nfor word in words:\n    count[word] = count.get(word, 0) + 1",
        beginner="capitals = {'FR': 'Paris'}\nprint(capitals.get('FR'))",
        intermediate=dedent("""\
            rows = [{'id': 1, 'name': 'Ada'}, {'id': 2, 'name': 'Lin'}]
            by_id = {r['id']: r for r in rows}
            print(by_id[2])"""),
        advanced=dedent("""\
            from collections import defaultdict

            dd = defaultdict(list)
            for dept, name in [('eng', 'Ada'), ('eng', 'Lin')]:
                dd[dept].append(name)
            print(dict(dd))"""),
        mermaid="flowchart LR\n    A[Key] --> B[Hash]\n    B --> C[Value]",
    )

    p(
        "Functions",
        what="Functions are reusable blocks of code that perform a task and optionally return a value.",
        why="They reduce duplication and organize logic into testable units.",
        where="API handlers, data transforms, CLI tools, ML training loops.",
        objectives=("Define and call functions.", "Use parameters and return values.", "Apply default and keyword arguments."),
        outcome="You structure programs into composable functions.",
        industry=("Backend services", "Data engineering", "Test automation", "Quant libraries"),
        concepts=(
            ("def", "Keyword to define a function.", "def greet(name):\n    return f'Hi {name}'\nprint(greet('Ada'))"),
            ("Parameters", "Inputs declared in the definition.", "def add(a, b):\n    return a + b\nprint(add(2, 3))"),
            ("Return", "Sends a result back to the caller.", "def double(n):\n    return n * 2\nprint(double(4))"),
        ),
        concept="Functions encapsulate behavior with a clear interface.",
        purpose="Reuse logic and improve maintainability.",
        benefits="Testability, readability, modularity.",
        use_cases="Validation, formatting, API clients, business rules.",
        best_practices="Single responsibility, type hints, docstrings.",
        mistakes="Side effects in pure helpers, too many parameters.",
        basic_syntax="def double(n):\n    return n * 2",
        structure="def name(params):\n    body\n    return result",
        pattern="def process(data):\n    return transform(clean(data))",
        beginner="def greet(name):\n    print(f'Hello, {name}')\n\ngreet('World')",
        intermediate=dedent("""\
            def summarize(numbers: list[float]) -> dict[str, float]:
                return {"count": len(numbers), "total": sum(numbers)}


            print(summarize([1.5, 2.5, 3.0]))"""),
        advanced=dedent("""\
            from functools import wraps


            def log_calls(func):
                @wraps(func)
                def wrapper(*args, **kwargs):
                    result = func(*args, **kwargs)
                    print(func.__name__, 'called')
                    return result

                return wrapper


            @log_calls
            def add(a, b):
                return a + b


            print(add(1, 2))"""),
        mermaid="flowchart TD\n    A[Call] --> B[Bind Args]\n    B --> C[Body]\n    C --> D[Return]",
    )

    p(
        "Arguments and Parameters",
        what="Parameters define what a function accepts; arguments are the values passed in.",
        why="Flexible signatures support optional config, variadic input, and readable call sites.",
        where="Library APIs, frameworks, decorators, CLI wrappers.",
        objectives=("Use positional and keyword parameters.", "Apply *args and **kwargs.", "Avoid mutable default arguments."),
        outcome="You design function signatures that are safe and expressive.",
        industry=("SDK design", "Web frameworks", "Plugin systems", "Testing utilities"),
        concepts=(
            ("Defaults", "Parameters with fallback values.", "def connect(timeout=30):\n    return timeout\nprint(connect())"),
            ("Keyword args", "Call by name for clarity.", "def plot(x, y, color='blue'):\n    return (x, y, color)\nprint(plot(1, 2, color='red'))"),
            ("*args/**kwargs", "Collect extra positional/keyword args.", "def wrap(*args, **kwargs):\n    return (args, kwargs)\nprint(wrap(1, z=2))"),
        ),
        concept="Binding maps arguments to parameters at call time.",
        purpose="Let functions accept varying inputs cleanly.",
        benefits="Readable calls, extensibility, wrapper-friendly.",
        use_cases="Decorators, logging wrappers, optional flags.",
        best_practices="Keyword-only for bool flags; immutable defaults; type hints.",
        mistakes="Mutable defaults, overusing **kwargs, unclear parameter order.",
        basic_syntax="def power(base, exp=2):\n    return base ** exp",
        structure="define params -> bind at call -> execute",
        pattern="def create_user(name, *, active=True):\n    return {'name': name, 'active': active}",
        beginner="def greet(name, punctuation='!'):\n    print(f'Hello, {name}{punctuation}')\n\ngreet('Ada')",
        intermediate=dedent("""\
            def tag(*labels, **meta):
                return {'labels': labels, 'meta': meta}


            print(tag('py', 'web', year=2026))"""),
        advanced=dedent("""\
            from typing import Callable


            def twice(func: Callable[[int], int], value: int) -> int:
                return func(func(value))


            print(twice(lambda x: x + 1, 3))"""),
        mermaid="flowchart LR\n    A[Call Site] --> B[Bind Params]\n    B --> C[Function Body]",
    )

    p(
        "Return Statements",
        what="return sends a value back to the caller and exits the function.",
        why="Callers need results; early returns simplify control flow.",
        where="Calculations, parsers, validators, service methods.",
        objectives=("Return single and multiple values.", "Use early return for guards.", "Distinguish return vs print."),
        outcome="You write functions that communicate results clearly.",
        industry=("Financial calculators", "Compilers", "Auth services", "Games"),
        concepts=(
            ("Single value", "Most common return form.", "def sq(n):\n    return n * n\nprint(sq(4))"),
            ("Tuple return", "Multiple values as one object.", "def minmax(nums):\n    return min(nums), max(nums)\nprint(minmax([3, 1, 2]))"),
            ("Early return", "Exit when precondition fails.", "def safe_div(a, b):\n    if b == 0:\n        return None\n    return a / b\nprint(safe_div(4, 2))"),
        ),
        concept="return completes the function call expression.",
        purpose="Deliver outputs and stop execution when done.",
        benefits="Composable functions, clearer flow, testable outputs.",
        use_cases="Validation results, parsed tokens, status codes.",
        best_practices="Keep return types consistent; document None cases.",
        mistakes="Returning print result, inconsistent types, missing return.",
        basic_syntax="def add(a, b):\n    return a + b",
        structure="compute -> optionally early exit -> return",
        pattern="if not valid(x):\n    return None\nreturn transform(x)",
        beginner="def is_even(n):\n    return n % 2 == 0\nprint(is_even(4))",
        intermediate="def partition(nums, pivot):\n    low = [n for n in nums if n < pivot]\n    high = [n for n in nums if n >= pivot]\n    return low, high\nprint(partition([3, 1, 4, 2], 3))",
        advanced=dedent("""\
            from typing import Optional


            def find_user(users: list[dict], user_id: int) -> Optional[dict]:
                for user in users:
                    if user.get('id') == user_id:
                        return user
                return None


            print(find_user([{'id': 1}], 1))"""),
        mermaid="flowchart TD\n    A[Function] --> B{Guard?}\n    B -->|fail| C[Early Return]\n    B -->|ok| D[Return Result]",
    )

    p(
        "Scope",
        what="Scope determines where names are visible: local, enclosing, global, or builtin (LEGB).",
        why="Understanding scope prevents accidental shadowing and mutation bugs.",
        where="Closures, modules, nested functions, configuration.",
        objectives=("Trace LEGB name lookup.", "Use global/nonlocal intentionally.", "Avoid shadowing builtins."),
        outcome="You predict where assignments bind and how nested functions capture state.",
        industry=("Plugin hosts", "GUI callbacks", "Financial models", "Game engines"),
        concepts=(
            ("Local", "Names inside a function.", "def f():\n    x = 1\n    return x\nprint(f())"),
            ("Global", "Module-level names.", "count = 0\ndef inc():\n    global count\n    count += 1\ninc()\nprint(count)"),
            ("nonlocal", "Modify enclosing function variables.", "def outer():\n    total = 0\n    def inner():\n        nonlocal total\n        total += 1\n        return total\n    return inner()\nprint(outer())"),
        ),
        concept="Python resolves names outward through LEGB.",
        purpose="Control visibility and lifetime of variables.",
        benefits="Modularity, encapsulation, predictable bindings.",
        use_cases="Counters, factories, decorators, cached state.",
        best_practices="Minimize global state; prefer parameters and return values.",
        mistakes="UnboundLocalError, accidental global mutation, shadowing list/str.",
        basic_syntax="x = 'global'\ndef demo():\n    x = 'local'\n    return x\nprint(demo(), x)",
        structure="define scope -> assign -> lookup",
        pattern="def make_adder(n):\n    def add(x):\n        return x + n\n    return add",
        beginner="message = 'hi'\ndef show():\n    return message\nprint(show())",
        intermediate="def counter():\n    n = 0\n    def step():\n        nonlocal n\n        n += 1\n        return n\n    return step\nc = counter()\nprint(c(), c())",
        advanced=dedent("""\
            def multiplier(factor):
                def wrap(value):
                    return value * factor
                return wrap


            double = multiplier(2)
            print(double(5))"""),
        mermaid="flowchart TD\n    A[Name Lookup] --> B[Local]\n    B --> C[Enclosing]\n    C --> D[Global]\n    D --> E[Builtins]",
    )

    p(
        "Lambda Functions",
        what="Lambda functions are anonymous one-expression functions.",
        why="They shine as short callbacks for sort keys and functional helpers.",
        where="sorted/key=, map/filter, pandas apply, event handlers.",
        objectives=("Write simple lambda expressions.", "Use with sorted, map, filter.", "Know when def is clearer."),
        outcome="You apply lambdas appropriately without harming readability.",
        industry=("Data wrangling", "UI tooling", "Competitive programming", "Config DSLs"),
        concepts=(
            ("Syntax", "lambda params: expression.", "double = lambda x: x * 2\nprint(double(3))"),
            ("sorted key", "Customize ordering.", "pairs = [(1, 'b'), (2, 'a')]\nprint(sorted(pairs, key=lambda p: p[1]))"),
            ("map/filter", "Functional transforms.", "print(list(map(lambda x: x * 2, [1, 2, 3])))"),
        ),
        concept="Lambdas are expressions that create function objects.",
        purpose="Inline tiny functions at point of use.",
        benefits="Concise sort keys, quick transforms.",
        use_cases="Sorting records, simple predicates, callback slots.",
        best_practices="Use def for multi-line or complex logic; add types at boundaries.",
        mistakes="Over nesting lambdas, side effects inside, unreadable one-liners.",
        basic_syntax="square = lambda n: n * n\nprint(square(5))",
        structure="lambda params: expr -> pass to higher-order func",
        pattern="sorted(items, key=lambda x: x['score'], reverse=True)",
        beginner="nums = [1, 2, 3]\nprint(list(map(lambda x: x ** 2, nums)))",
        intermediate="employees = [{'name': 'Ada', 'age': 36}, {'name': 'Lin', 'age': 30}]\nprint(sorted(employees, key=lambda e: e['age']))",
        advanced=dedent("""\
            from functools import reduce

            print(reduce(lambda acc, x: acc + x, [1, 2, 3, 4], 0))"""),
        mermaid="flowchart LR\n    A[Lambda] --> B[Higher-Order Func]\n    B --> C[Result]",
    )

    p(
        "Modules",
        what="Modules are Python files that group related code and expose a namespace.",
        why="Modules organize code, enable reuse, and control what is public.",
        where="Standard library, internal packages, shared utilities.",
        objectives=("Import modules and names correctly.", "Understand __name__ and __main__.", "Structure module-level code."),
        outcome="You split programs into importable modules cleanly.",
        industry=("Monoliths", "Shared libs", "Notebooks", "Microservices"),
        concepts=(
            ("import", "Load module namespace.", "import math\nprint(math.sqrt(9))"),
            ("from import", "Bind specific names.", "from math import pi\nprint(round(pi, 2))"),
            ("__name__", "Tells if module is run or imported.", "print(__name__)"),
        ),
        concept="Modules are the unit of reuse in Python.",
        purpose="Encapsulate related functions, classes, constants.",
        benefits="Namespace control, testability, lazy loading.",
        use_cases="Utils, models, clients, constants.",
        best_practices="Explicit __all__; guard main with if __name__.",
        mistakes="Circular imports, star imports, heavy work at import time.",
        basic_syntax="import json\nprint(json.dumps({'a': 1}))",
        structure="imports -> constants -> defs -> main guard",
        pattern="if __name__ == '__main__':\n    main()",
        beginner="import datetime\nprint(datetime.date.today())",
        intermediate=dedent("""\
            import importlib.util
            spec = importlib.util.find_spec('pathlib')
            print(spec is not None)"""),
        advanced=dedent("""\
            import importlib
            math = importlib.import_module('math')
            print(math.hypot(3, 4))"""),
        mermaid="flowchart LR\n    A[module.py] --> B[import]\n    B --> C[Namespace]",
    )

    p(
        "Packages",
        what="Packages are directories of modules with an __init__.py (or namespace package).",
        why="Packages scale codebases beyond single files and define public APIs.",
        where="Libraries, services, frameworks, internal platforms.",
        objectives=("Create package layout with submodules.", "Import from packages correctly.", "Expose stable __all__ or submodules."),
        outcome="You organize multi-module projects into installable packages.",
        industry=("PyPI libraries", "Enterprise apps", "ML repos", "Platform SDKs"),
        concepts=(
            ("Package dir", "Folder with __init__.py.", "from pathlib import Path\nprint(Path('snippet_parts/_helpers.py').exists())"),
            ("Relative import", "Import within package.", "from snippet_parts._helpers import S\nprint(callable(S))"),
            ("__init__", "Runs when package imported.", "import snippet_parts\nprint(snippet_parts.__file__)"),
        ),
        concept="Packages group modules under a shared name.",
        purpose="Scale structure and distribution.",
        benefits="Clear boundaries, versioning, reuse.",
        use_cases="Web apps, SDKs, data platforms.",
        best_practices="Flat is better than nested; document public API.",
        mistakes="Deep circular imports, bloated __init__, missing pyproject.",
        basic_syntax="from snippet_parts._helpers import S",
        structure="package/ -> submodules -> __init__ exports",
        pattern="from mypkg.services import billing",
        beginner="import snippet_parts\nprint(snippet_parts.__name__)",
        intermediate=dedent("""\
            import pkgutil
            print(any(m.name == '_helpers' for m in pkgutil.iter_modules(['snippet_parts'])))"""),
        advanced=dedent("""\
            import importlib.metadata as md
            print(md.version('pip'))"""),
        mermaid="flowchart TD\n    A[Package] --> B[Submodule]\n    B --> C[Public API]",
    )

    p(
        "Date and Time",
        what="Python's datetime module models dates, times, timestamps, and timedeltas.",
        why="Scheduling, logging, billing, and analytics require correct temporal logic.",
        where="Cron jobs, audit trails, SLAs, reporting windows.",
        objectives=("Create datetime and timedelta objects.", "Format and parse ISO timestamps.", "Handle time zones with zoneinfo."),
        outcome="You perform reliable date/time calculations and formatting.",
        industry=("Fintech settlement", "SaaS billing", "Log aggregation", "Travel booking"),
        concepts=(
            ("datetime", "Calendar date and clock time.", "from datetime import datetime\nprint(datetime(2026, 6, 6).isoformat())"),
            ("timedelta", "Differences and durations.", "from datetime import timedelta\nprint(timedelta(days=7).days)"),
            ("timezone", "Aware UTC timestamps.", "from datetime import datetime, timezone\nprint(datetime.now(timezone.utc).year)"),
        ),
        concept="Use aware datetimes for distributed systems.",
        purpose="Measure, compare, and display time correctly.",
        benefits="Standard library support, ISO interoperability.",
        use_cases="Token expiry, report ranges, retry backoff.",
        best_practices="Store UTC; convert at display; use zoneinfo.",
        mistakes="Naive vs aware mixing, DST bugs, parsing locale dates loosely.",
        basic_syntax="from datetime import date\nprint(date.today())",
        structure="parse -> normalize TZ -> compute -> format",
        pattern="deadline = start + timedelta(hours=24)",
        beginner="from datetime import datetime\nprint(datetime.now().year)",
        intermediate=dedent("""\
            from datetime import datetime, timedelta
            start = datetime(2026, 1, 1)
            print((start + timedelta(days=30)).date())"""),
        advanced=dedent("""\
            from datetime import datetime
            from zoneinfo import ZoneInfo

            utc = datetime(2026, 6, 6, 12, tzinfo=ZoneInfo('UTC'))
            print(utc.astimezone(ZoneInfo('America/New_York')).hour)"""),
        mermaid="flowchart LR\n    A[Parse Time] --> B[UTC Store]\n    B --> C[Compute]\n    C --> D[Display TZ]",
    )

    p(
        "Math Module",
        what="The math module provides standard mathematical functions and constants.",
        why="It supplements built-in operators with trig, logs, rounding, and constants.",
        where="Graphics, statistics, engineering, games, ML feature prep.",
        objectives=("Import and use math functions.", "Apply ceil, floor, sqrt, log.", "Know math vs numpy boundaries."),
        outcome="You perform common numeric operations with the math module.",
        industry=("Simulation", "CAD tooling", "Quant finance", "Robotics"),
        concepts=(
            ("Constants", "pi and e.", "import math\nprint(round(math.pi, 3))"),
            ("sqrt/log", "Roots and logarithms.", "import math\nprint(math.sqrt(16), math.log2(8))"),
            ("hypot", "Distance calculations.", "import math\nprint(math.hypot(3, 4))"),
        ),
        concept="math operates on scalars (not vectorized).",
        purpose="Accurate numeric primitives for algorithms.",
        benefits="Fast, standard, no extra dependency.",
        use_cases="Distance metrics, probability, geometry.",
        best_practices="Use math.isclose for floats; prefer decimal for money.",
        mistakes="Using math on lists, domain errors on log/sqrt, float equality.",
        basic_syntax="import math\nprint(math.pow(2, 3))",
        structure="import math -> compute scalar -> combine",
        pattern="hyp = math.hypot(dx, dy)",
        beginner="import math\nprint(math.ceil(4.2))",
        intermediate="import math\nangles = [0, math.pi/2]\nprint([math.sin(a) for a in angles])",
        advanced=dedent("""\
            import math

            def sigmoid(x: float) -> float:
                return 1 / (1 + math.exp(-x))


            print(round(sigmoid(0), 4))"""),
        mermaid="flowchart LR\n    A[Scalars] --> B[math func]\n    B --> C[Result]",
    )

    p(
        "Random Module",
        what="The random module generates pseudo-random numbers and samples for simulations.",
        why="Games, sampling, shuffling, and Monte Carlo methods need controlled randomness.",
        where="A/B tests, load balancing, procedural content, QA fuzzing.",
        objectives=("Use random, randint, choice, shuffle.", "Seed RNG for reproducibility.", "Choose secrets vs random correctly."),
        outcome="You generate randomness safely for simulations and sampling.",
        industry=("Gaming", "ML data splits", "Security training", "Load testing"),
        concepts=(
            ("randint", "Random integer in range.", "import random\nprint(random.randint(1, 6))"),
            ("choice", "Pick random element.", "import random\nprint(random.choice(['red', 'blue']))"),
            ("seed", "Reproducible sequences.", "import random\nrandom.seed(0)\nprint(random.random())"),
        ),
        concept="random is deterministic given a seed.",
        purpose="Simulate uncertainty and shuffle data.",
        benefits="Simple API, reproducible tests with seed.",
        use_cases="Dice rolls, train/test split, lottery draws.",
        best_practices="Use secrets module for crypto; seed in tests only.",
        mistakes="Using random for passwords, biased sampling, forgetting seed in tests.",
        basic_syntax="import random\nprint(random.random())",
        structure="seed (optional) -> draw -> use",
        pattern="sample = random.sample(population, k=3)",
        beginner="import random\nprint(random.choice(['A', 'B', 'C']))",
        intermediate="import random\nitems = [1, 2, 3, 4]\nrandom.shuffle(items)\nprint(items)",
        advanced=dedent("""\
            import random

            def bootstrap(data: list[float], n: int) -> list[float]:
                return [random.choice(data) for _ in range(n)]


            print(bootstrap([1.0, 2.0, 3.0], 5))"""),
        mermaid="flowchart LR\n    A[Seed] --> B[RNG]\n    B --> C[Sample]",
    )

    p(
        "File Handling",
        what="File handling reads and writes persistent data using paths and file objects.",
        why="Programs must load configs, export reports, and process uploads.",
        where="ETL, logging, document pipelines, local tools.",
        objectives=("Open files with context managers.", "Read/write text and binary safely.", "Use pathlib for paths."),
        outcome="You read and write files reliably with proper encoding and cleanup.",
        industry=("Reporting", "Media processing", "Backup tools", "Compliance archives"),
        concepts=(
            ("open", "Returns file object.", "from io import StringIO\nf = StringIO('hi')\nprint(f.read())"),
            ("with", "Ensures files close.", "from tempfile import NamedTemporaryFile\nwith NamedTemporaryFile('w+', delete=False) as tmp:\n    tmp.write('data')\n    name = tmp.name\nprint(name.endswith('tmp') or len(name) > 0)"),
            ("pathlib", "OO paths.", "from pathlib import Path\np = Path('README.md')\nprint(p.suffix)"),
        ),
        concept="Files are streams; paths are pathlib.Path objects.",
        purpose="Persist and exchange data on disk.",
        benefits="Context managers, pathlib clarity, binary support.",
        use_cases="Config load, CSV export, image bytes, log rotation.",
        best_practices="Specify encoding=utf-8; use Path; handle missing files.",
        mistakes="Forgetting close, wrong newline mode, loading huge files fully.",
        basic_syntax="from pathlib import Path\nprint(Path('.').resolve())",
        structure="open path -> read/write -> atomic replace optional",
        pattern="text = Path('file.txt').read_text(encoding='utf-8')",
        beginner="from pathlib import Path\np = Path('README.md')\nprint(p.exists())",
        intermediate=dedent("""\
            from pathlib import Path
            lines = Path('README.md').read_text(encoding='utf-8').splitlines()
            print(len(lines))"""),
        advanced=dedent("""\
            from pathlib import Path

            def write_atomic(path: Path, content: str) -> None:
                tmp = path.with_suffix(path.suffix + '.tmp')
                tmp.write_text(content, encoding='utf-8')
                tmp.replace(path)


            p = Path('demo_out.txt')
            write_atomic(p, 'hello')
            print(p.read_text(encoding='utf-8'))"""),
        mermaid="flowchart LR\n    A[Path] --> B[Open]\n    B --> C[Read/Write]\n    C --> D[Close]",
    )

    p(
        "Exception Handling",
        what="Exception handling manages errors with try, except, else, and finally.",
        why="Robust programs recover from failures and preserve resources.",
        where="Network I/O, parsing, databases, user input.",
        objectives=("Catch specific exceptions.", "Raise meaningful errors.", "Use finally for cleanup."),
        outcome="You write fault-tolerant code with clear error paths.",
        industry=("Payment processing", "API gateways", "Data ingestion", "Desktop apps"),
        concepts=(
            ("try/except", "Handle expected failures.", "try:\n    int('x')\nexcept ValueError as e:\n    print(type(e).__name__)"),
            ("raise", "Signal errors upstream.", "def require_positive(n):\n    if n <= 0:\n        raise ValueError('must be positive')\nrequire_positive(1)"),
            ("finally", "Always-run cleanup.", "f = None\ntry:\n    f = open(__file__)\n    data = f.read(10)\nfinally:\n    if f:\n        f.close()\nprint(len(data))"),
        ),
        concept="Exceptions unwind the stack until a matching handler runs.",
        purpose="Separate happy path from error recovery.",
        benefits="Resource safety, clearer control flow, rich tracebacks.",
        use_cases="Retry wrappers, validation, transaction rollback.",
        best_practices="Catch specific types; chain exceptions; log context.",
        mistakes="Bare except, swallowing errors, using exceptions for flow control.",
        basic_syntax="try:\n    risky()\nexcept Exception:\n    handle()",
        structure="try -> except specific -> else -> finally",
        pattern="try:\n    return parse(data)\nexcept ParseError:\n    return default",
        beginner="try:\n    print(1 / 0)\nexcept ZeroDivisionError:\n    print('cannot divide by zero')",
        intermediate=dedent("""\
            class AppError(Exception):
                pass


            def load(value: str) -> int:
                try:
                    return int(value)
                except ValueError as exc:
                    raise AppError('bad input') from exc


            print(load('10'))"""),
        advanced=dedent("""\
            from contextlib import suppress

            with suppress(FileNotFoundError):
                open('missing.txt').read()
            print('continued')"""),
        mermaid="flowchart TD\n    A[try] --> B{Error?}\n    B -->|yes| C[except]\n    B -->|no| D[else]\n    C --> E[finally]\n    D --> E",
    )

    p(
        "Debugging Basics",
        what="Debugging basics include reading tracebacks, using print/logging, and breakpoints.",
        why="Finding root cause quickly saves hours in development and incidents.",
        where="Local dev, staging reproduction, postmortems.",
        objectives=("Read stack traces bottom-up.", "Use pdb/breakpoint().", "Form hypotheses and isolate bugs."),
        outcome="You systematically narrow down and fix defects.",
        industry=("SRE", "QA automation", "Game dev", "Enterprise apps"),
        concepts=(
            ("Traceback", "Shows call stack at error.", "import traceback\ntry:\n    1/0\nexcept ZeroDivisionError:\n    traceback.print_exc()"),
            ("breakpoint", "Interactive debugger entry.", "x = 1\nx += 1\nprint(x)"),
            ("logging", "Better than print in prod.", "import logging\nlogging.basicConfig(level=logging.INFO)\nlogging.info('check')"),
        ),
        concept="Debug loop: reproduce -> isolate -> fix -> verify.",
        purpose="Restore correct program behavior.",
        benefits="Faster fixes, fewer regressions, shared techniques.",
        use_cases="Failing tests, prod incidents, flaky jobs.",
        best_practices="Minimal repro, binary search commits, watch variables.",
        mistakes="Random changes, ignoring traceback, debugging without tests.",
        basic_syntax="import logging\nlogging.debug('state=%s', value)",
        structure="reproduce -> inspect -> hypothesize -> fix -> test",
        pattern="assert expected == actual, (expected, actual)",
        beginner="def add(a, b):\n    return a + b\nassert add(2, 3) == 5",
        intermediate=dedent("""\
            def divide(a, b):
                try:
                    return a / b
                except ZeroDivisionError:
                    return float('inf')


            print(divide(1, 0))"""),
        advanced=dedent("""\
            import logging

            logger = logging.getLogger(__name__)


            def compute(values):
                logger.debug('inputs=%r', values)
                return sum(values)


            print(compute([1, 2, 3]))"""),
        mermaid="flowchart LR\n    A[Bug Report] --> B[Repro]\n    B --> C[Inspect]\n    C --> D[Fix]\n    D --> E[Test]",
    )

    p(
        "Virtual Environments",
        what="Virtual environments isolate project dependencies from the system Python.",
        why="Isolation prevents version conflicts and makes projects reproducible.",
        where="Every professional Python project locally and in CI.",
        objectives=("Create and activate venv.", "Install packages into venv only.", "Export requirements or lockfiles."),
        outcome="You manage per-project dependencies safely.",
        industry=("Web teams", "ML labs", "CI pipelines", "Consulting deliverables"),
        concepts=(
            ("venv module", "Creates env directory.", "import venv\nprint(hasattr(venv, 'EnvBuilder'))"),
            ("pip in venv", "Installs into env site-packages.", "import site\nprint(len(site.getsitepackages()) >= 1)"),
            ("requirements.txt", "Pinned dependency list.", "from pathlib import Path\nprint(Path('README.md').exists())"),
        ),
        concept="Each venv has its own interpreter symlink and site-packages.",
        purpose="Reproducible dependency graphs per project.",
        benefits="No global pollution, easier onboarding, safer upgrades.",
        use_cases="App dev, notebooks, test matrices.",
        best_practices="Commit requirements; never pip install globally; use python -m pip.",
        mistakes="Forgetting activate, mixing conda/pip blindly, no pin files.",
        basic_syntax="import sys\nprint(sys.prefix)",
        structure="python -m venv -> activate -> pip install -r requirements",
        pattern="import sys\nprint('venv active' if sys.prefix != sys.base_prefix else 'system')",
        beginner="import sys\nprint(sys.prefix != sys.base_prefix)",
        intermediate=dedent("""\
            import sys
            print('executable:', sys.executable)
            print('prefix:', sys.prefix)"""),
        advanced=dedent("""\
            import subprocess
            import sys

            cmd = [sys.executable, '-m', 'pip', 'list', '--format=freeze']
            out = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print(len(out.stdout.splitlines()))"""),
        mermaid="flowchart LR\n    A[Project] --> B[venv]\n    B --> C[pip install]\n    C --> D[Isolated deps]",
    )

    p(
        "Basic Project Structure",
        what="Basic project structure organizes source, tests, config, and docs for maintainability.",
        why="Consistent layout helps teams navigate, test, and package code.",
        where="Every repo from tutorials to production services.",
        objectives=("Lay out src/ or package root with tests.", "Add README, requirements, and .gitignore.", "Use pyproject.toml for modern tooling."),
        outcome="You bootstrap Python projects that scale beyond one file.",
        industry=("Open source", "Agencies", "Product engineering", "Research labs"),
        concepts=(
            ("src layout", "Package under src/ avoids import confusion.", "from pathlib import Path\nprint(Path('scripts').is_dir())"),
            ("tests/", "Automated verification.", "import pathlib\nprint(pathlib.Path('scripts').exists())"),
            ("pyproject.toml", "Project metadata and tools.", "print('pyproject'[:3])"),
        ),
        concept="Structure communicates boundaries and entry points.",
        purpose="Enable testing, packaging, and collaboration.",
        benefits="Onboarding speed, CI clarity, fewer import hacks.",
        use_cases="CLI tools, libraries, microservices.",
        best_practices="One obvious README; Makefile/task runner optional; pin Python version.",
        mistakes="Flat script pile, tests not runnable, secrets in repo.",
        basic_syntax="from pathlib import Path\nprint(list(Path('.').glob('scripts/*.py'))[:1])",
        structure="README + pyproject + package + tests + scripts",
        pattern="layout = {'src': 'pkg', 'tests': 'tests', 'config': 'pyproject.toml'}\nprint(layout['src'])",
        beginner="from pathlib import Path\nprint([p.name for p in Path('scripts').glob('*.py')][:3])",
        intermediate=dedent("""\
            from pathlib import Path
            root = Path('.')
            print('has scripts:', (root / 'scripts').exists())
            print('has README:', (root / 'README.md').exists())"""),
        advanced=dedent("""\
            from pathlib import Path

            def tree(path: Path, prefix: str = '') -> None:
                entries = sorted(path.iterdir(), key=lambda p: p.name)
                for entry in entries[:5]:
                    print(prefix + entry.name)


            tree(Path('scripts'))"""),
        mermaid="flowchart TD\n    A[Repo Root] --> B[src/package]\n    A --> C[tests]\n    A --> D[pyproject.toml]\n    A --> E[README]",
    )
