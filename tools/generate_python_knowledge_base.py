#!/usr/bin/env python3
"""Generate the single-page Python knowledge base README.

The repository is documentation-first, and the requested README is large enough
that generating it keeps the topic catalog complete, consistent, and auditable.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


LEVELS: list[tuple[str, list[str]]] = [
    (
        "Level 1: Beginner",
        [
            "Introduction to Python",
            "Installing Python",
            "IDE Setup",
            "Python Syntax",
            "Variables",
            "Data Types",
            "Type Casting",
            "Input and Output",
            "Operators",
            "Conditional Statements",
            "Loops",
            "Nested Loops",
            "Break Continue Pass",
            "Strings",
            "String Methods",
            "Lists",
            "List Methods",
            "Tuples",
            "Sets",
            "Dictionaries",
            "Functions",
            "Arguments and Parameters",
            "Return Statements",
            "Scope",
            "Lambda Functions",
            "Modules",
            "Packages",
            "Date and Time",
            "Math Module",
            "Random Module",
            "File Handling",
            "Exception Handling",
            "Debugging Basics",
            "Virtual Environments",
            "Basic Project Structure",
        ],
    ),
    (
        "Level 2: Intermediate",
        [
            "Object Oriented Programming",
            "Classes",
            "Objects",
            "Constructors",
            "Encapsulation",
            "Inheritance",
            "Polymorphism",
            "Abstraction",
            "Magic Methods",
            "Iterators",
            "Generators",
            "Decorators",
            "Context Managers",
            "Regular Expressions",
            "JSON Processing",
            "CSV Processing",
            "XML Processing",
            "Logging",
            "Configuration Management",
            "Multithreading",
            "Multiprocessing",
            "Async Programming",
            "API Development",
            "API Consumption",
            "Requests Library",
            "Database Fundamentals",
            "SQLite",
            "MySQL Integration",
            "PostgreSQL Integration",
            "SQLAlchemy ORM",
            "Unit Testing",
            "Pytest",
            "Mocking",
            "Packaging Python Projects",
            "CLI Applications",
        ],
    ),
    (
        "Level 3: Advanced",
        [
            "Data Structures Internals",
            "Algorithms in Python",
            "Design Patterns",
            "SOLID Principles",
            "Memory Management",
            "Garbage Collection",
            "Python Internals",
            "Metaclasses",
            "Descriptors",
            "Concurrency",
            "Parallel Computing",
            "Distributed Systems",
            "Network Programming",
            "Socket Programming",
            "Cybersecurity Automation",
            "Web Scraping",
            "Automation Frameworks",
            "ETL Development",
            "Data Engineering",
            "Pandas",
            "NumPy",
            "PySpark",
            "Machine Learning",
            "Deep Learning",
            "NLP",
            "Computer Vision",
            "FastAPI",
            "Django",
            "Flask",
            "Microservices",
            "Docker with Python",
            "Kubernetes Integration",
            "Cloud Development",
            "AWS with Python",
            "Azure with Python",
            "GCP with Python",
            "DevOps Automation",
            "CI/CD Pipelines",
            "Performance Optimization",
            "System Design with Python",
        ],
    ),
]


FAMILY_BY_TOPIC: dict[str, str] = {}


def assign(family: str, topics: list[str]) -> None:
    for topic in topics:
        FAMILY_BY_TOPIC[topic] = family


assign("setup", ["Introduction to Python", "Installing Python", "IDE Setup", "Python Syntax"])
assign("data_model", ["Variables", "Data Types", "Type Casting", "Input and Output", "Operators"])
assign("control_flow", ["Conditional Statements", "Loops", "Nested Loops", "Break Continue Pass"])
assign(
    "collections",
    ["Strings", "String Methods", "Lists", "List Methods", "Tuples", "Sets", "Dictionaries"],
)
assign(
    "functions",
    ["Functions", "Arguments and Parameters", "Return Statements", "Scope", "Lambda Functions"],
)
assign(
    "tooling",
    [
        "Modules",
        "Packages",
        "Date and Time",
        "Math Module",
        "Random Module",
        "File Handling",
        "Exception Handling",
        "Debugging Basics",
        "Virtual Environments",
        "Basic Project Structure",
    ],
)
assign(
    "oop",
    [
        "Object Oriented Programming",
        "Classes",
        "Objects",
        "Constructors",
        "Encapsulation",
        "Inheritance",
        "Polymorphism",
        "Abstraction",
        "Magic Methods",
    ],
)
assign("iteration", ["Iterators", "Generators"])
assign("decorators_context", ["Decorators", "Context Managers"])
assign("structured_text", ["Regular Expressions", "JSON Processing", "CSV Processing", "XML Processing"])
assign("operations", ["Logging", "Configuration Management"])
assign("concurrency", ["Multithreading", "Multiprocessing", "Async Programming"])
assign("api", ["API Development", "API Consumption", "Requests Library"])
assign(
    "database",
    ["Database Fundamentals", "SQLite", "MySQL Integration", "PostgreSQL Integration", "SQLAlchemy ORM"],
)
assign("testing", ["Unit Testing", "Pytest", "Mocking"])
assign("packaging", ["Packaging Python Projects", "CLI Applications"])
assign(
    "internals",
    [
        "Data Structures Internals",
        "Memory Management",
        "Garbage Collection",
        "Python Internals",
        "Metaclasses",
        "Descriptors",
    ],
)
assign("architecture", ["Algorithms in Python", "Design Patterns", "SOLID Principles", "System Design with Python"])
assign(
    "advanced_concurrency",
    [
        "Concurrency",
        "Parallel Computing",
        "Distributed Systems",
        "Network Programming",
        "Socket Programming",
        "Performance Optimization",
    ],
)
assign(
    "security_automation",
    ["Cybersecurity Automation", "Web Scraping", "Automation Frameworks", "DevOps Automation", "CI/CD Pipelines"],
)
assign("data_engineering", ["ETL Development", "Data Engineering", "Pandas", "NumPy", "PySpark"])
assign("ai", ["Machine Learning", "Deep Learning", "NLP", "Computer Vision"])
assign("web_frameworks", ["FastAPI", "Django", "Flask", "Microservices"])
assign(
    "cloud",
    ["Docker with Python", "Kubernetes Integration", "Cloud Development", "AWS with Python", "Azure with Python", "GCP with Python"],
)


FAMILY_DETAILS: dict[str, dict[str, object]] = {
    "setup": {
        "domain": "developer environment and execution workflow",
        "where": "local machines, classrooms, notebooks, CI runners, servers, and cloud workspaces",
        "concepts": [
            ("Interpreter", "The Python executable that reads source code and runs it.", "source.py -> python -> output", 'print("Python is ready")'),
            ("Script", "A file containing repeatable Python instructions.", "task.py -> run -> result", 'Path("report.txt").write_text("done")'),
            ("Feedback Loop", "The cycle of write, run, inspect, and improve.", "edit -> execute -> observe -> refine", "python --version"),
        ],
    },
    "data_model": {
        "domain": "values, expressions, and data representation",
        "where": "business rules, forms, reports, analytics, automation scripts, and service configuration",
        "concepts": [
            ("Value", "A piece of information stored and processed by Python.", "name -> object", 'customer = "Ada"'),
            ("Type", "A category that defines allowed operations for a value.", "42:int | 3.14:float | True:bool", "isinstance(42, int)"),
            ("Expression", "A combination of values and operators that produces a result.", "inputs + operator -> result", "total = price * quantity"),
        ],
    },
    "control_flow": {
        "domain": "decision-making and repetition",
        "where": "validation, games, ETL jobs, user workflows, robotics, simulations, and data processing",
        "concepts": [
            ("Branch", "A path chosen when a condition is true or false.", "condition ? path A : path B", 'status = "pass" if score >= 70 else "retry"'),
            ("Iteration", "Repeating work over data or until a condition changes.", "collection -> repeated body", "for item in items: process(item)"),
            ("Loop Control", "Keywords that alter normal loop execution.", "continue | break | pass", "if item is None: continue"),
        ],
    },
    "collections": {
        "domain": "containers and sequence processing",
        "where": "records, API payloads, dashboards, configuration, search, recommendations, and reporting",
        "concepts": [
            ("Sequence", "An ordered container accessed by position.", "index -> element", "names[0]"),
            ("Mapping", "A key-value structure for labeled data.", "key -> value", 'profile["email"]'),
            ("Mutability", "Whether a container can change after creation.", "list changes | tuple stays fixed", "items.append('new')"),
        ],
    },
    "functions": {
        "domain": "reusable behavior and program organization",
        "where": "libraries, scripts, APIs, notebooks, automation jobs, and reusable business logic",
        "concepts": [
            ("Parameter", "A named input accepted by a function.", "caller value -> parameter", "def greet(name): ..."),
            ("Return Value", "The result sent back to the caller.", "function -> result", "return total"),
            ("Scope", "The region where a name is available.", "local name | global name", "count = len(items)"),
        ],
    },
    "tooling": {
        "domain": "standard library tools and project hygiene",
        "where": "file processing, scheduled jobs, reproducible projects, debugging sessions, and production utilities",
        "concepts": [
            ("Module", "A Python file or library that exposes reusable names.", "import module -> use function", "import math"),
            ("Boundary", "A safe edge around files, errors, environments, or packages.", "program -> external resource", "with open(path) as file: ..."),
            ("Repeatability", "A project setup that works the same way for every contributor.", "venv + requirements + structure", "python -m venv .venv"),
        ],
    },
    "oop": {
        "domain": "object-oriented modeling",
        "where": "domain models, GUI systems, service layers, frameworks, plugins, simulations, and enterprise applications",
        "concepts": [
            ("Class", "A blueprint that defines data and behavior.", "class -> objects", "class Invoice: ..."),
            ("Object", "A runtime instance with state and methods.", "object.state + object.method()", "invoice.total()"),
            ("Interface", "A behavioral contract used by multiple implementations.", "same call -> different behavior", "notifier.send(message)"),
        ],
    },
    "iteration": {
        "domain": "lazy data traversal",
        "where": "streaming files, pagination, data pipelines, memory-sensitive processing, and event systems",
        "concepts": [
            ("Iterator", "An object that returns one item at a time.", "next() -> item", "next(iter([1, 2, 3]))"),
            ("Generator", "A function that yields values lazily.", "yield -> pause -> resume", "yield row"),
            ("Laziness", "Deferring work until a value is requested.", "request -> compute next", "(x*x for x in numbers)"),
        ],
    },
    "decorators_context": {
        "domain": "behavior wrapping and resource lifecycle control",
        "where": "web routes, authorization, timing, retries, transactions, files, locks, and test fixtures",
        "concepts": [
            ("Wrapper", "Code that runs before, after, or around another callable.", "call -> wrapper -> function", "@timer"),
            ("Context", "A managed setup and cleanup boundary.", "enter -> work -> exit", "with open(path) as file: ..."),
            ("Composition", "Adding behavior without rewriting the original function.", "base behavior + concern", "cached_fetch = cache(fetch)"),
        ],
    },
    "structured_text": {
        "domain": "structured and semi-structured data exchange",
        "where": "APIs, data imports, logs, configuration, integrations, reports, and legacy enterprise systems",
        "concepts": [
            ("Pattern", "A rule for finding text with expected structure.", "text -> match groups", r"re.findall(r'\\d+', text)"),
            ("Serialization", "Converting objects into portable text.", "dict -> JSON/XML/CSV", "json.dumps(record)"),
            ("Schema Awareness", "Knowing the fields and types expected by another system.", "contract -> parser -> validation", 'record["id"]'),
        ],
    },
    "operations": {
        "domain": "runtime observability and environment-driven behavior",
        "where": "production services, CLI tools, scheduled jobs, cloud deployments, and incident response",
        "concepts": [
            ("Log Event", "A timestamped record of what the program observed or did.", "code path -> log line", 'logger.info("job finished")'),
            ("Configuration", "Values supplied outside code to alter behavior safely.", "env/file/flags -> settings", 'os.getenv("APP_ENV")'),
            ("Signal", "Actionable runtime evidence for debugging and support.", "metric + log + trace", 'logger.exception("failed")'),
        ],
    },
    "concurrency": {
        "domain": "overlapping work",
        "where": "web servers, crawlers, background jobs, data ingestion, IO-heavy tools, and CPU-heavy processing",
        "concepts": [
            ("Task", "A unit of work that can run independently.", "task queue -> workers", "executor.submit(fetch, url)"),
            ("Synchronization", "Coordination that prevents unsafe shared-state access.", "lock -> protected section", "with lock: counter += 1"),
            ("Awaitable", "An async operation that yields control while waiting.", "await IO -> resume later", "await client.get(url)"),
        ],
    },
    "api": {
        "domain": "service communication over network boundaries",
        "where": "backend services, mobile apps, SaaS integrations, data feeds, automation, and microservices",
        "concepts": [
            ("Endpoint", "A URL and method that expose a capability.", "GET /items -> response", "@app.get('/items')"),
            ("Request", "Input sent by a client to a server.", "client -> request -> service", "requests.get(url)"),
            ("Response", "Structured output returned by a service.", "service -> status + body", "return {'ok': True}"),
        ],
    },
    "database": {
        "domain": "persistent data storage and retrieval",
        "where": "web applications, analytics systems, CRMs, financial software, inventory tools, and reporting platforms",
        "concepts": [
            ("Table", "A structured collection of rows and columns.", "table -> rows -> fields", "SELECT * FROM users"),
            ("Transaction", "A group of changes committed or rolled back together.", "begin -> changes -> commit", "connection.commit()"),
            ("ORM Model", "A Python class mapped to a database table.", "class <-> table", "session.add(user)"),
        ],
    },
    "testing": {
        "domain": "verification and confidence building",
        "where": "libraries, services, CI pipelines, refactors, regulated systems, and team development",
        "concepts": [
            ("Assertion", "A statement that expected behavior is true.", "actual == expected", "assert total == 42"),
            ("Fixture", "Reusable setup for tests.", "setup -> test -> cleanup", "@pytest.fixture"),
            ("Test Double", "A replacement for a dependency during tests.", "mock -> controlled response", "mock_api.return_value = data"),
        ],
    },
    "packaging": {
        "domain": "distributable tools and command-line interfaces",
        "where": "internal automation, open source packages, developer tools, release pipelines, and operations scripts",
        "concepts": [
            ("Entry Point", "A command that starts a Python function.", "shell command -> main()", "python -m package"),
            ("Metadata", "Package information used by installers and indexes.", "name/version/dependencies", "pyproject.toml"),
            ("Argument Parsing", "Turning command-line text into structured options.", "argv -> namespace", "argparse.ArgumentParser()"),
        ],
    },
    "internals": {
        "domain": "runtime mechanics and language customization",
        "where": "frameworks, performance tuning, debugging tools, ORMs, libraries, and advanced platform engineering",
        "concepts": [
            ("Object Model", "The internal rules governing Python objects.", "name -> object -> type", "type(value)"),
            ("Lifecycle", "How objects are allocated, referenced, and released.", "create -> reference -> collect", "gc.collect()"),
            ("Protocol", "A special method contract recognized by Python.", "__len__ -> len(obj)", "def __get__(self, obj, owner): ..."),
        ],
    },
    "architecture": {
        "domain": "scalable design and problem solving",
        "where": "large services, libraries, system design interviews, enterprise platforms, and long-lived products",
        "concepts": [
            ("Algorithm", "A precise procedure for transforming input into output.", "input -> steps -> output", "sorted(items, key=len)"),
            ("Pattern", "A reusable design solution for a recurring problem.", "context -> proven structure", "Strategy(), Factory(), Adapter()"),
            ("Boundary", "A separation that keeps responsibilities clear.", "interface -> implementation", "Repository.save(entity)"),
        ],
    },
    "advanced_concurrency": {
        "domain": "high-scale execution and networked systems",
        "where": "distributed backends, data platforms, event processing, streaming systems, networking tools, and performance-critical services",
        "concepts": [
            ("Throughput", "The amount of work completed per unit of time.", "tasks / second", "pool.map(work, items)"),
            ("Coordination", "How processes, services, or nodes agree on work.", "producer -> queue -> consumers", "message_id"),
            ("Bottleneck", "The slowest resource limiting the system.", "CPU | IO | network | lock", "profile before optimizing"),
        ],
    },
    "security_automation": {
        "domain": "safe automation, scraping, and delivery workflows",
        "where": "security operations, compliance checks, release engineering, QA automation, incident response, and data collection",
        "concepts": [
            ("Policy", "A rule that automation enforces consistently.", "input -> check -> allow/deny", "if risk > threshold: alert()"),
            ("Extractor", "Code that gathers structured facts from external sources.", "page/log/API -> records", "BeautifulSoup(html)"),
            ("Pipeline", "A repeatable chain from trigger to verified outcome.", "commit -> test -> package -> deploy", "ci.yml"),
        ],
    },
    "data_engineering": {
        "domain": "analytical data processing",
        "where": "warehouses, lakes, dashboards, ML features, reporting, financial analytics, and operational intelligence",
        "concepts": [
            ("Dataset", "A structured collection prepared for analysis or processing.", "rows + columns + schema", "DataFrame(records)"),
            ("Transformation", "A rule that cleans, enriches, or reshapes data.", "raw -> curated", "df.assign(total=df.qty * df.price)"),
            ("Scale", "The ability to process data efficiently as volume grows.", "local -> distributed", "spark.read.parquet(path)"),
        ],
    },
    "ai": {
        "domain": "model-driven prediction and perception",
        "where": "recommendations, forecasting, chatbots, document search, image analysis, fraud detection, and decision support",
        "concepts": [
            ("Feature", "An input signal used by a model.", "raw data -> features", "tokens = text.split()"),
            ("Model", "A learned or programmed function that maps inputs to outputs.", "features -> prediction", "prediction = model(x)"),
            ("Evaluation", "Measuring whether predictions are reliable.", "predictions vs labels -> score", "accuracy = correct / total"),
        ],
    },
    "web_frameworks": {
        "domain": "web application and service frameworks",
        "where": "REST APIs, dashboards, admin panels, SaaS platforms, internal portals, and microservices",
        "concepts": [
            ("Route", "A URL rule connected to Python behavior.", "URL -> function/class", "@app.get('/')"),
            ("Middleware", "Reusable logic around requests and responses.", "request -> middleware -> handler", "auth middleware"),
            ("Service Boundary", "A deployable unit with clear ownership.", "API contract -> implementation", "users service"),
        ],
    },
    "cloud": {
        "domain": "containerized and cloud-native Python delivery",
        "where": "AWS, Azure, GCP, Kubernetes, serverless platforms, data jobs, APIs, and DevOps automation",
        "concepts": [
            ("Artifact", "A packaged version of code ready to run.", "source -> image/package -> deploy", "docker build ."),
            ("Runtime Environment", "The infrastructure and settings where code executes.", "container + env + secrets", "os.getenv('REGION')"),
            ("Managed Service", "A cloud capability consumed through APIs or SDKs.", "Python -> SDK -> cloud resource", "client.list_buckets()"),
        ],
    },
}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def function_name(topic: str) -> str:
    name = re.sub(r"[^a-zA-Z0-9]+", "_", topic.lower()).strip("_")
    if name and name[0].isdigit():
        name = f"topic_{name}"
    return name or "topic"


def family_for(topic: str) -> str:
    try:
        return FAMILY_BY_TOPIC[topic]
    except KeyError as exc:
        raise SystemExit(f"No family assigned for topic: {topic}") from exc


def code_block(language: str, content: str) -> str:
    return f"```{language}\n{content.rstrip()}\n```"


def table_cell(value: object) -> str:
    """Escape Markdown table separators inside generated cell content."""
    return str(value).replace("|", r"\|")


def syntax_for(topic: str, family: str) -> tuple[str, str, str]:
    fn = function_name(topic)
    if family == "setup":
        return (
            'print("Hello, Python")',
            'def main():\n    print("Run this file with python script.py")\n\n\nif __name__ == "__main__":\n    main()',
            'write code -> save file -> run interpreter -> inspect output',
        )
    if family == "data_model":
        return (
            'name = "Ada"\nage = int("36")\nis_active = True',
            'input_value = "42"\nnumber = int(input_value)\nresult = number * 2\nprint(result)',
            'capture value -> convert type if needed -> apply operator -> store result',
        )
    if family == "control_flow":
        return (
            'if score >= 70:\n    print("pass")\nelse:\n    print("practice again")',
            'for item in items:\n    if item is None:\n        continue\n    process(item)',
            'condition -> branch or loop -> optional break/continue -> result',
        )
    if family == "collections":
        return (
            'skills = ["syntax", "functions", "testing"]\nprofile = {"name": "Ada", "level": "beginner"}',
            'for skill in skills:\n    print(skill.upper())\n\nlevel = profile.get("level", "unknown")',
            'choose container -> add/read/update values -> iterate or transform',
        )
    if family == "functions":
        return (
            'def calculate_total(price, quantity):\n    return price * quantity',
            'def summarize(name, *skills, active=True, **metadata):\n    return {"name": name, "skills": skills, "active": active, **metadata}',
            'define inputs -> isolate behavior -> return output -> reuse from callers',
        )
    if family == "tooling":
        return (
            'from pathlib import Path\n\nprint(Path.cwd())',
            'from pathlib import Path\n\npath = Path("data.txt")\ntry:\n    content = path.read_text()\nexcept FileNotFoundError:\n    content = ""',
            'import tool -> protect resource boundary -> handle failure -> keep project repeatable',
        )
    if family == "oop":
        return (
            'class User:\n    pass\n\nuser = User()',
            'class Account:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n\n    def deposit(self, amount):\n        self.balance += amount',
            'model noun -> define state -> add behavior -> collaborate through methods',
        )
    if family == "iteration":
        return (
            'numbers = iter([1, 2, 3])\nprint(next(numbers))',
            'def read_batches(rows, size):\n    for index in range(0, len(rows), size):\n        yield rows[index:index + size]',
            'source -> iterator/generator -> consume one item at a time',
        )
    if family == "decorators_context":
        return (
            'with open("notes.txt", "w") as file:\n    file.write("managed safely")',
            'def trace(func):\n    def wrapper(*args, **kwargs):\n        print(f"calling {func.__name__}")\n        return func(*args, **kwargs)\n    return wrapper',
            'wrap behavior or manage resource -> run target work -> cleanup/return',
        )
    if family == "structured_text":
        return (
            'import json\n\npayload = json.loads(\'{"name": "Ada"}\')',
            'import re\n\nemails = re.findall(r"[\\w.-]+@[\\w.-]+", text)',
            'read text -> parse according to format -> validate fields -> transform output',
        )
    if family == "operations":
        return (
            'import logging\n\nlogging.info("application started")',
            'import os\n\nsettings = {\n    "env": os.getenv("APP_ENV", "development"),\n    "debug": os.getenv("DEBUG") == "1",\n}',
            'load config -> run behavior -> emit logs -> diagnose from evidence',
        )
    if family in {"concurrency", "advanced_concurrency"}:
        return (
            'from concurrent.futures import ThreadPoolExecutor\n\nwith ThreadPoolExecutor() as pool:\n    results = list(pool.map(str.upper, ["api", "db"]))',
            'import asyncio\n\nasync def main():\n    await asyncio.sleep(0.1)\n    return "done"\n\nasyncio.run(main())',
            'split work -> schedule tasks -> coordinate results -> measure bottlenecks',
        )
    if family == "api":
        return (
            'from urllib.request import urlopen\n\nwith urlopen("https://example.com") as response:\n    status = response.status',
            'def create_response(data, status=200):\n    return {"status": status, "data": data}',
            'client request -> validate input -> execute business logic -> return response',
        )
    if family == "database":
        return (
            'import sqlite3\n\nconnection = sqlite3.connect(":memory:")',
            'with sqlite3.connect("app.db") as connection:\n    connection.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")\n    connection.commit()',
            'connect -> execute query/ORM operation -> commit or rollback -> close',
        )
    if family == "testing":
        return (
            'def test_total():\n    assert 2 + 2 == 4',
            'from unittest.mock import Mock\n\nservice = Mock(return_value={"ok": True})\nassert service()["ok"] is True',
            'arrange setup -> act on code -> assert outcome -> automate in CI',
        )
    if family == "packaging":
        return (
            'def main():\n    print("tool started")',
            'import argparse\n\nparser = argparse.ArgumentParser()\nparser.add_argument("--name", default="Python")\nargs = parser.parse_args()',
            'package code -> expose command -> parse options -> return exit status',
        )
    if family == "internals":
        return (
            'value = []\nprint(type(value), id(value))',
            'import gc\n\nbefore = gc.get_count()\ngc.collect()\nafter = gc.get_count()',
            'inspect object -> understand protocol/lifecycle -> customize only when justified',
        )
    if family == "architecture":
        return (
            'def linear_search(items, target):\n    return target in items',
            'class Strategy:\n    def execute(self, value):\n        raise NotImplementedError',
            'define problem -> choose algorithm/pattern -> isolate boundaries -> validate trade-offs',
        )
    if family == "security_automation":
        return (
            'import hashlib\n\ndigest = hashlib.sha256(b"evidence").hexdigest()',
            'from html.parser import HTMLParser\n\nclass LinkParser(HTMLParser):\n    def handle_starttag(self, tag, attrs):\n        if tag == "a":\n            print(dict(attrs).get("href"))',
            'collect evidence -> validate safely -> automate repeatable checks -> report clearly',
        )
    if family == "data_engineering":
        return (
            'records = [{"qty": 2, "price": 10}]\ntotals = [row["qty"] * row["price"] for row in records]',
            'def transform(rows):\n    for row in rows:\n        yield {**row, "total": row["qty"] * row["price"]}',
            'extract source -> validate schema -> transform data -> load curated output',
        )
    if family == "ai":
        return (
            'tokens = "Python makes automation easier".lower().split()',
            'def predict_sentiment(words):\n    positive = {"good", "great", "easier"}\n    return sum(word in positive for word in words)',
            'collect data -> engineer features -> train or call model -> evaluate predictions',
        )
    if family == "web_frameworks":
        return (
            'def health_check():\n    return {"status": "ok"}',
            'def route(path):\n    def decorator(func):\n        ROUTES[path] = func\n        return func\n    return decorator\n\nROUTES = {}',
            'route request -> validate data -> call service layer -> serialize response',
        )
    if family == "cloud":
        return (
            'import os\n\nregion = os.getenv("CLOUD_REGION", "local")',
            'def build_container_command(image):\n    return ["docker", "run", "--rm", image]',
            'package artifact -> configure environment -> deploy -> observe and rollback if needed',
        )
    raise SystemExit(f"No syntax template for family: {family}")


def examples_for(topic: str, family: str) -> tuple[str, str, str]:
    fn = function_name(topic)
    beginner = f'topic = "{topic}"\nprint(f"Now learning: {{topic}}")'
    intermediate = (
        f"def build_{fn}_checklist():\n"
        f"    return [\n"
        f"        \"explain the concept\",\n"
        f"        \"write a small example\",\n"
        f"        \"identify a common mistake\",\n"
        f"    ]\n\n"
        f"for step in build_{fn}_checklist():\n"
        f"    print(step)"
    )
    advanced = (
        "from dataclasses import dataclass\n\n\n"
        "@dataclass(frozen=True)\n"
        "class LearningTopic:\n"
        "    name: str\n"
        "    level: str\n"
        "    evidence: tuple[str, ...]\n\n"
        "    def is_ready_for_project(self) -> bool:\n"
        "        return len(self.evidence) >= 3\n\n\n"
        f'topic = LearningTopic("{topic}", "{family.replace("_", " ")}", ("notes", "code", "review"))\n'
        "print(topic.is_ready_for_project())"
    )

    if family == "data_model":
        beginner = "price = 19.99\nquantity = 3\nprint(price * quantity)"
        intermediate = (
            "def invoice_total(items, tax_rate):\n"
            "    subtotal = sum(price * qty for price, qty in items)\n"
            "    return round(subtotal * (1 + tax_rate), 2)\n\n"
            "print(invoice_total([(10.0, 2), (4.5, 3)], 0.08))"
        )
    elif family == "control_flow":
        beginner = "score = 82\nif score >= 70:\n    print('pass')\nelse:\n    print('retry')"
        intermediate = (
            "orders = [120, 0, 45, 300]\n"
            "for amount in orders:\n"
            "    if amount == 0:\n"
            "        continue\n"
            "    if amount > 250:\n"
            "        print('manual review')\n"
            "        break\n"
            "    print('approved')"
        )
    elif family == "collections":
        beginner = "skills = ['strings', 'lists', 'dictionaries']\nprint(skills[0])"
        intermediate = (
            "inventory = {'laptop': 4, 'monitor': 0, 'keyboard': 12}\n"
            "available = {item: qty for item, qty in inventory.items() if qty > 0}\n"
            "print(available)"
        )
    elif family == "functions":
        beginner = "def greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('Ada'))"
        intermediate = (
            "def average(*scores):\n"
            "    if not scores:\n"
            "        return 0\n"
            "    return sum(scores) / len(scores)\n\n"
            "print(average(80, 90, 100))"
        )
    elif family == "tooling":
        beginner = "from datetime import date\n\nprint(date.today())"
        intermediate = (
            "from pathlib import Path\n\n"
            "path = Path('notes.txt')\n"
            "try:\n"
            "    print(path.read_text())\n"
            "except FileNotFoundError:\n"
            "    print('create notes.txt first')"
        )
    elif family == "oop":
        beginner = "class Course:\n    pass\n\npython = Course()\nprint(type(python).__name__)"
        intermediate = (
            "class Course:\n"
            "    def __init__(self, title):\n"
            "        self.title = title\n"
            "        self.completed = False\n\n"
            "    def mark_complete(self):\n"
            "        self.completed = True\n\n"
            "course = Course('Python')\n"
            "course.mark_complete()\n"
            "print(course.completed)"
        )
    elif family == "iteration":
        beginner = "for number in range(3):\n    print(number)"
        intermediate = (
            "def chunks(items, size):\n"
            "    for index in range(0, len(items), size):\n"
            "        yield items[index:index + size]\n\n"
            "print(list(chunks([1, 2, 3, 4], 2)))"
        )
    elif family == "decorators_context":
        beginner = "with open('example.txt', 'w') as file:\n    file.write('managed resource')"
        intermediate = (
            "def uppercase_result(func):\n"
            "    def wrapper(*args, **kwargs):\n"
            "        return func(*args, **kwargs).upper()\n"
            "    return wrapper\n\n"
            "@uppercase_result\n"
            "def label():\n"
            "    return 'python'\n\n"
            "print(label())"
        )
    elif family == "database":
        beginner = "import sqlite3\n\nconnection = sqlite3.connect(':memory:')\nprint(connection.execute('SELECT 1').fetchone()[0])"
        intermediate = (
            "import sqlite3\n\n"
            "with sqlite3.connect(':memory:') as db:\n"
            "    db.execute('CREATE TABLE users (name TEXT)')\n"
            "    db.execute('INSERT INTO users VALUES (?)', ('Ada',))\n"
            "    print(db.execute('SELECT name FROM users').fetchall())"
        )
    elif family == "testing":
        beginner = "def add(a, b):\n    return a + b\n\nassert add(2, 3) == 5"
        intermediate = (
            "from unittest.mock import Mock\n\n"
            "gateway = Mock(return_value={'status': 'ok'})\n"
            "assert gateway()['status'] == 'ok'\n"
            "gateway.assert_called_once()"
        )
    elif family in {"concurrency", "advanced_concurrency"}:
        beginner = "from concurrent.futures import ThreadPoolExecutor\n\nwith ThreadPoolExecutor() as pool:\n    print(list(pool.map(len, ['api', 'database'])))"
        intermediate = (
            "import asyncio\n\n"
            "async def fetch_name(name):\n"
            "    await asyncio.sleep(0.01)\n"
            "    return name.upper()\n\n"
            "async def main():\n"
            "    print(await asyncio.gather(fetch_name('api'), fetch_name('db')))\n\n"
            "asyncio.run(main())"
        )
    elif family == "api":
        beginner = "def response(body, status=200):\n    return {'status': status, 'body': body}\n\nprint(response({'ok': True}))"
        intermediate = (
            "from urllib.parse import urlencode\n\n"
            "params = urlencode({'page': 1, 'limit': 20})\n"
            "url = f'https://api.example.com/items?{params}'\n"
            "print(url)"
        )
    elif family == "data_engineering":
        beginner = "rows = [{'qty': 2, 'price': 10}]\nprint(rows[0]['qty'] * rows[0]['price'])"
        intermediate = (
            "def clean_orders(rows):\n"
            "    for row in rows:\n"
            "        if row['qty'] > 0:\n"
            "            yield {**row, 'total': row['qty'] * row['price']}\n\n"
            "print(list(clean_orders([{'qty': 2, 'price': 10}])))"
        )
    elif family == "ai":
        beginner = "text = 'Python powers AI systems'\ntokens = text.lower().split()\nprint(tokens)"
        intermediate = (
            "def simple_classifier(words):\n"
            "    ai_terms = {'model', 'training', 'prediction'}\n"
            "    return 'ai-related' if ai_terms & set(words) else 'general'\n\n"
            "print(simple_classifier({'model', 'accuracy'}))"
        )
    elif family == "web_frameworks":
        beginner = "def health_check():\n    return {'status': 'ok'}\n\nprint(health_check())"
        intermediate = (
            "ROUTES = {}\n\n"
            "def route(path):\n"
            "    def register(handler):\n"
            "        ROUTES[path] = handler\n"
            "        return handler\n"
            "    return register\n\n"
            "@route('/health')\n"
            "def health():\n"
            "    return {'status': 'ok'}\n\n"
            "print(ROUTES['/health']())"
        )
    elif family == "cloud":
        beginner = "import os\n\nprint(os.getenv('APP_ENV', 'local'))"
        intermediate = (
            "def deployment_manifest(image, replicas=2):\n"
            "    return {'image': image, 'replicas': replicas, 'port': 8000}\n\n"
            "print(deployment_manifest('python-api:latest'))"
        )

    return beginner, intermediate, advanced


def render_topic(topic: str, level: str) -> str:
    family = family_for(topic)
    details = FAMILY_DETAILS[family]
    domain = details["domain"]
    where = details["where"]
    concepts = details["concepts"]
    basic, structure, pattern = syntax_for(topic, family)
    beginner, intermediate, advanced = examples_for(topic, family)
    anchor = slug(topic)

    lines: list[str] = [
        f"# {topic}",
        "",
        f"> **Level:** {level} | **Domain:** {domain}",
        "",
        "## Overview",
        f"- **What is it?** {topic} is the Python discipline focused on {domain}.",
        f"- **Why is it important?** It turns isolated syntax knowledge into reliable capability for {domain}.",
        f"- **Where is it used?** {where}.",
        "",
        "## Learning Objectives",
        f"- Explain the purpose and vocabulary of **{topic}**.",
        f"- Apply the core Python patterns used in {domain}.",
        "- Recognize trade-offs, failure modes, and safe defaults.",
        f"- **Expected outcome:** create a small, reviewable Python example that demonstrates {topic.lower()} in context.",
        "",
        "## Real World Applications",
        f"- **Industry use cases:** {where.capitalize()}.",
        f"- **Business applications:** reduce manual work, improve reliability, and make {domain} easier to maintain.",
        "- **Career relevance:** strengthens portfolio projects, interview explanations, team collaboration, and production readiness.",
        "",
        "## Core Concepts",
        "",
        "| Concept | Definition | Visual Explanation | Practical Example |",
        "| --- | --- | --- | --- |",
    ]

    for concept, definition, visual, example in concepts:  # type: ignore[misc]
        lines.append(
            f"| **{table_cell(concept)}** | {table_cell(definition)} | `{table_cell(visual)}` | `{table_cell(example)}` |"
        )

    lines.extend(
        [
            "",
            "## Infographic Summary",
            "",
            "| Block | Learning Block |",
            "| --- | --- |",
            f"| 📌 Concept | **{topic}** belongs to the {domain} layer of Python mastery. |",
            f"| ⚡ Purpose | Make Python programs clearer, safer, and more useful for {domain}. |",
            "| 🔥 Benefits | Better readability, fewer bugs, stronger automation, and easier team handoff. |",
            f"| 🎯 Use Cases | Practice projects, production scripts, backend systems, analytics workflows, and {anchor.replace('-', ' ')} exercises. |",
            "| 🚀 Best Practices | Start small, name things clearly, handle errors intentionally, test behavior, and document assumptions. |",
            "| ❌ Common Mistakes | Memorizing syntax without context, skipping edge cases, overengineering early, and ignoring runtime feedback. |",
            "",
            "## Syntax Guide",
            "",
            "### Basic Syntax",
            "",
            code_block("python", basic),
            "",
            "### Standard Structure",
            "",
            code_block("python", structure),
            "",
            "### Code Pattern",
            "",
            code_block("text", pattern),
            "",
            "## Examples",
            "",
            "### Beginner Example",
            "",
            code_block("python", beginner),
            "",
            "### Intermediate Example",
            "",
            code_block("python", intermediate),
            "",
            "### Advanced Example",
            "",
            code_block("python", advanced),
            "",
            "## Workflow Diagram",
            "",
            "```mermaid",
            "flowchart LR",
            f"    A[Learn {topic}] --> B[Identify Inputs]",
            "    B --> C[Apply Python Pattern]",
            "    C --> D[Test Behavior]",
            "    D --> E[Document Result]",
            "```",
            "",
            "---",
            "",
        ]
    )
    return "\n".join(lines)


def render_header() -> str:
    total = sum(len(topics) for _, topics in LEVELS)
    lines = [
        "# PYTHON LEARNING ROADMAP",
        "",
        "> A complete README-format Python knowledge base for GitHub, NotebookLM, Obsidian, Notion, and documentation portals.",
        "",
        "## Knowledge Base Promise",
        "",
        f"- Covers **{total} requested Python topics** across beginner, intermediate, and advanced levels.",
        "- Uses a repeatable learning structure: overview, objectives, real-world value, concepts, infographic summary, syntax, examples, and Mermaid workflow diagrams.",
        "- Balances instructor clarity with practical engineering habits: small examples, explicit trade-offs, testing mindset, and production awareness.",
        "- Can be read as one long README or split into the recommended NotebookLM folder structure near the end.",
        "",
        "## How to Use This README",
        "",
        "| Learner Type | Best Path | Evidence of Progress |",
        "| --- | --- | --- |",
        "| New programmer | Read Level 1 in order and run every beginner example. | Working scripts, vocabulary notes, and small automation tasks. |",
        "| Junior developer | Review Level 1 quickly, then build Level 2 projects. | Tested functions, CLI tools, API clients, and database exercises. |",
        "| Professional engineer | Use Level 3 as an architecture and specialization map. | Production-style services, data pipelines, cloud deployments, and design explanations. |",
        "| Instructor or mentor | Assign one topic section at a time with examples and diagrams. | Student explanations, code reviews, quizzes, and mini-project demos. |",
        "",
        "## Table of Contents",
        "",
    ]
    for level_name, topics in LEVELS:
        lines.append(f"### {level_name}")
        lines.append("")
        for index, topic in enumerate(topics, start=1):
            lines.append(f"{index}. [{topic}](#{slug(topic)})")
        lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def render_level_overview(level_name: str, topics: list[str]) -> str:
    return "\n".join(
        [
            f"## {level_name}",
            "",
            "| Focus | Outcome | Topic Count |",
            "| --- | --- | --- |",
            f"| {level_name.replace(':', '')} mastery | Build progressively stronger Python skills through structured topic sections. | {len(topics)} |",
            "",
            "```mermaid",
            "flowchart TD",
            f"    A[{level_name}] --> B[Conceptual Understanding]",
            "    B --> C[Syntax Practice]",
            "    C --> D[Applied Examples]",
            "    D --> E[Project Readiness]",
            "```",
            "",
        ]
    )


def render_final_section() -> str:
    return """# FINAL SECTION

## Complete Python Roadmap

| Phase | Core Focus | Build Evidence | Readiness Signal |
| --- | --- | --- | --- |
| Beginner | Syntax, values, control flow, collections, functions, files, exceptions, and environments. | Scripts, notes, small calculators, file utilities, and debugging exercises. | You can write and explain a small Python program without copying blindly. |
| Intermediate | OOP, iterators, decorators, data formats, logging, concurrency, APIs, databases, tests, packages, and CLIs. | Tested modules, API clients, database-backed tools, packages, and automation utilities. | You can design maintainable Python components and verify them with tests. |
| Advanced | Internals, algorithms, architecture, distributed systems, security, data engineering, AI, web frameworks, cloud, DevOps, and performance. | Production-style systems, pipelines, services, containers, cloud integrations, and design documents. | You can choose Python architecture intentionally and justify trade-offs. |

```mermaid
flowchart LR
    A[Beginner Foundations] --> B[Intermediate Engineering]
    B --> C[Advanced Production Systems]
    C --> D[Specialized Career Tracks]
    D --> E[Portfolio + Interviews + Real Delivery]
```

## Python Career Paths

| Career Path | Python Strengths Needed | Portfolio Evidence |
| --- | --- | --- |
| Python Developer | Core syntax, OOP, packaging, testing, APIs, databases, and CLI tools. | Reusable package, tested CLI app, API integration, and documentation. |
| Backend Engineer | Web frameworks, database design, API contracts, testing, logging, security, deployment, and performance. | FastAPI/Django/Flask service with auth, persistence, tests, Docker, and CI. |
| Data Engineer | ETL, SQL, Pandas, PySpark, orchestration, data quality, cloud storage, and pipelines. | Batch pipeline, validation checks, warehouse model, and scheduled workflow. |
| AI Engineer | NumPy, Pandas, ML, deep learning, NLP, computer vision, APIs, evaluation, and deployment. | Model training notebook, inference API, metrics report, and monitoring plan. |
| DevOps Engineer | Automation, scripting, CI/CD, Docker, Kubernetes, cloud SDKs, observability, and reliability. | Deployment automation, CI workflow, infrastructure script, and runbook. |
| Cybersecurity Engineer | Secure coding, automation, parsing, web scraping, APIs, logging, incident response, and evidence handling. | Security scanner, log analyzer, alert pipeline, and safe reporting workflow. |

## Python Developer Roadmap

```mermaid
flowchart TD
    A[Syntax and Data Types] --> B[Functions and Modules]
    B --> C[OOP and Testing]
    C --> D[Packaging and CLI Tools]
    D --> E[APIs and Databases]
    E --> F[Portfolio Libraries]
```

## Backend Engineer Roadmap

```mermaid
flowchart TD
    A[HTTP and API Design] --> B[FastAPI Django or Flask]
    B --> C[Databases and ORM]
    C --> D[Authentication and Authorization]
    D --> E[Testing Logging and Monitoring]
    E --> F[Docker CI/CD and Cloud Deployment]
```

## Data Engineer Roadmap

```mermaid
flowchart TD
    A[Python Files CSV JSON XML] --> B[SQL and Databases]
    B --> C[Pandas and NumPy]
    C --> D[ETL and Data Quality]
    D --> E[PySpark and Distributed Processing]
    E --> F[Cloud Data Pipelines]
```

## AI Engineer Roadmap

```mermaid
flowchart TD
    A[Math Python NumPy Pandas] --> B[Machine Learning]
    B --> C[Deep Learning]
    C --> D[NLP and Computer Vision]
    D --> E[Evaluation and Experiment Tracking]
    E --> F[Model APIs and Production Monitoring]
```

## DevOps Engineer Roadmap

```mermaid
flowchart TD
    A[Python Automation Scripts] --> B[CLI Tools and Config]
    B --> C[Docker with Python]
    C --> D[CI/CD Pipelines]
    D --> E[Kubernetes Integration]
    E --> F[AWS Azure or GCP Automation]
```

## Cybersecurity Engineer Roadmap

```mermaid
flowchart TD
    A[Python Scripting] --> B[Regex Parsing and Logs]
    B --> C[Network and Socket Programming]
    C --> D[Cybersecurity Automation]
    D --> E[Web Scraping and API Evidence]
    E --> F[Detection Reporting and Response]
```

## Recommended Folder Structure for NotebookLM

```text
Python-Mastery/
│
├── Beginner/
│   ├── 01-Introduction-to-Python.md
│   ├── 02-Python-Syntax.md
│   ├── 03-Variables.md
│   └── ...
│
├── Intermediate/
│   ├── 01-OOP.md
│   ├── 02-Decorators.md
│   ├── 03-Generators.md
│   └── ...
│
├── Advanced/
│   ├── 01-Design-Patterns.md
│   ├── 02-Metaclasses.md
│   ├── 03-Data-Engineering.md
│   └── ...
│
├── Infographics/
├── CheatSheets/
├── Interview-Questions/
├── Projects/
├── Roadmaps/
└── README.md
```

## Documentation Portal Checklist

| Platform | Recommendation |
| --- | --- |
| GitHub | Keep Mermaid diagrams enabled and use the table of contents anchors for navigation. |
| NotebookLM | Split by level and topic when source limits require smaller files. |
| Obsidian | Convert topic headings into notes and cross-link career roadmaps. |
| Notion | Import sections as pages under Beginner, Intermediate, Advanced, and Roadmaps. |
| Documentation portals | Use the same section structure for predictable learner navigation. |
"""


def build_readme() -> str:
    assigned_topics = set(FAMILY_BY_TOPIC)
    all_topics = [topic for _, topics in LEVELS for topic in topics]
    missing = sorted(set(all_topics) - assigned_topics)
    extra = sorted(assigned_topics - set(all_topics))
    if missing or extra:
        raise SystemExit(f"Topic catalog mismatch. Missing={missing}; extra={extra}")

    sections = [render_header()]
    for level_name, topics in LEVELS:
        sections.append(render_level_overview(level_name, topics))
        for topic in topics:
            sections.append(render_topic(topic, level_name))
    sections.append(render_final_section())
    return "\n".join(sections).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the Python knowledge base README.")
    parser.add_argument("--check", action="store_true", help="Fail if README.md is not up to date.")
    args = parser.parse_args()

    content = build_readme()
    if args.check:
        current = README.read_text(encoding="utf-8")
        if current != content:
            print("README.md is not up to date. Run tools/generate_python_knowledge_base.py.")
            return 1
        print("README.md is up to date.")
        return 0

    README.write_text(content, encoding="utf-8")
    print(f"Wrote {README.relative_to(ROOT)} with {len(content.splitlines())} lines.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
