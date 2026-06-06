"""Intermediate topic registrations (part 2)."""

from __future__ import annotations

from textwrap import dedent
from typing import Callable


def _register_intermediate_part2(p: Callable[..., None]) -> None:
    p(
        "Regular Expressions",
        what="Regular expressions match and manipulate text via pattern rules.",
        why="They extract, validate, and replace structured text efficiently.",
        where="Log parsing, input validation, web scraping, data cleaning.",
        objectives=("Use re.search, re.findall, re.sub.", "Read basic regex syntax.", "Prefer compiled patterns for reuse."),
        outcome="You solve text pattern tasks without fragile manual parsing.",
        industry=("Security analytics", "SEO tools", "Support automation", "Compliance scanning"),
        concepts=(
            ("re.search", "Find first match.", "import re\nprint(re.search(r'\\d+', 'Room 42').group())"),
            ("groups", "Capture subpatterns.", "import re\nm = re.match(r'(?P<user>\\w+)@(?P<dom>\\w+)', 'ada@example.com')\nprint(m.group('user'))"),
            ("re.sub", "Replace matches.", "import re\nprint(re.sub(r'\\s+', '-', 'hello world'))"),
        ),
        concept="Regex engines match patterns over strings.",
        purpose="Parse semi-structured text reliably.",
        benefits="Powerful, compact, standard library support.",
        use_cases="Emails, IPs, URLs, log levels.",
        best_practices="Compile patterns; use raw strings; test edge cases.",
        mistakes="Catastrophic backtracking, over-regex, not anchoring when needed.",
        basic_syntax="import re\nre.findall(r'\\w+', 'Hello World')",
        structure="compile -> search/match -> group/sub",
        pattern="import re\nPATTERN = re.compile(r'\\d+')\nprint(PATTERN.findall('a1b22'))",
        beginner="import re\nprint(bool(re.fullmatch(r'\\d{3}-\\d{4}', '555-1234')))",
        intermediate=dedent("""\
            import re

            LOG = re.compile(r'(?P<level>\\w+) (?P<msg>.+)')
            line = 'ERROR disk full'
            match = LOG.match(line)
            print(match.groupdict())"""),
        advanced=dedent("""\
            import re

            def redact(text: str) -> str:
                return re.sub(r'\\b\\d{4}-\\d{4}-\\d{4}-\\d{4}\\b', '[CARD]', text)


            print(redact('paid 4111-1111-1111-1111'))"""),
        mermaid="flowchart LR\n    A[Text] --> B[Regex Engine]\n    B --> C[Match/Replace]",
    )

    p(
        "JSON Processing",
        what="JSON processing serializes Python objects to JSON and parses JSON text.",
        why="JSON is the lingua franca of web APIs and config files.",
        where="REST APIs, NoSQL docs, CLI configs, message queues.",
        objectives=("Use json.dumps and json.loads.", "Handle custom types with default=.", "Validate payloads before use."),
        outcome="You exchange structured data with JSON safely.",
        industry=("Microservices", "Mobile backends", "Serverless", "Browser apps"),
        concepts=(
            ("dumps", "Python to JSON string.", "import json\nprint(json.dumps({'a': 1}))"),
            ("loads", "JSON string to Python.", "import json\nprint(json.loads('{\"a\": 1}')['a'])"),
            ("indent", "Pretty-print JSON.", "import json\nprint(json.dumps([1, 2], indent=2))"),
        ),
        concept="JSON maps to dict/list/str/number/bool/null.",
        purpose="Interoperable data exchange.",
        benefits="Human-readable, universal, stdlib support.",
        use_cases="API bodies, config, event logs.",
        best_practices="UTF-8 encoding; schema validation at boundaries.",
        mistakes="Non-JSON types without default, float money, trusting input.",
        basic_syntax="import json\njson.loads('{\"ok\": true}')",
        structure="parse -> validate -> use -> serialize",
        pattern="payload = json.loads(text)\nresponse = json.dumps(result)",
        beginner="import json\ndata = {'name': 'Ada', 'score': 99}\nprint(json.dumps(data))",
        intermediate=dedent("""\
            import json
            from datetime import datetime


            def default(obj):
                if isinstance(obj, datetime):
                    return obj.isoformat()
                raise TypeError(type(obj))


            print(json.dumps({'at': datetime(2026, 1, 1)}, default=default))"""),
        advanced=dedent("""\
            import json

            class UserEncoder(json.JSONEncoder):
                def default(self, obj):
                    if hasattr(obj, 'to_json'):
                        return obj.to_json()
                    return super().default(obj)


            class User:
                def __init__(self, name: str):
                    self.name = name

                def to_json(self):
                    return {'name': self.name}


            print(json.dumps(User('Ada'), cls=UserEncoder))"""),
        mermaid="flowchart LR\n    A[Python Object] --> B[dumps]\n    B --> C[JSON Text]\n    C --> D[loads]",
    )

    p(
        "CSV Processing",
        what="CSV processing reads and writes comma-separated tabular files.",
        why="Spreadsheets and legacy systems still exchange CSV widely.",
        where="Finance exports, marketing lists, ETL staging, reports.",
        objectives=("Use csv.reader and csv.DictReader.", "Write rows with csv.writer.", "Handle headers and dialects."),
        outcome="You import and export tabular CSV data reliably.",
        industry=("Accounting", "Retail analytics", "HR systems", "Science datasets"),
        concepts=(
            ("reader", "Iterate rows as lists.", "import csv\nfrom io import StringIO\nrows = list(csv.reader(StringIO('a,b\\n1,2')))\nprint(rows)"),
            ("DictReader", "Rows as dicts by header.", "import csv\nfrom io import StringIO\nr = csv.DictReader(StringIO('name,score\\nAda,99'))\nprint(list(r)[0]['name'])"),
            ("writer", "Serialize rows.", "import csv\nfrom io import StringIO\nbuf = StringIO()\nw = csv.writer(buf)\nw.writerow(['x', 'y'])\nprint(buf.getvalue().strip())"),
        ),
        concept="CSV is text rows with delimiter-separated fields.",
        purpose="Interchange tabular data simply.",
        benefits="Universal, streaming-friendly, stdlib module.",
        use_cases="Sales exports, survey results, bulk imports.",
        best_practices="Use DictReader; specify newline=''; handle encoding.",
        mistakes="Locale comma issues, not quoting embedded commas, huge memory load.",
        basic_syntax="import csv\nwith open('data.csv', newline='', encoding='utf-8') as f:\n    rows = list(csv.reader(f))",
        structure="open -> reader/writer -> process rows",
        pattern="for row in csv.DictReader(f):\n    handle(row)",
        beginner=dedent("""\
            import csv
            from io import StringIO

            print(list(csv.reader(StringIO('id,name\\n1,Ada'))))"""),
        intermediate=dedent("""\
            import csv
            from io import StringIO

            source = StringIO('sku,qty\\nA1,2\\nB2,1\\n')
            total = sum(int(row['qty']) for row in csv.DictReader(source))
            print(total)"""),
        advanced=dedent("""\
            import csv
            from io import StringIO

            def filter_rows(text: str, min_qty: int) -> list[dict]:
                rows = csv.DictReader(StringIO(text))
                return [r for r in rows if int(r['qty']) >= min_qty]


            data = 'sku,qty\\nA,5\\nB,1\\n'
            print(filter_rows(data, 2))"""),
        mermaid="flowchart LR\n    A[CSV File] --> B[Reader]\n    B --> C[Rows]\n    C --> D[Process]",
    )

    p(
        "XML Processing",
        what="XML processing parses and builds hierarchical tagged documents.",
        why="Enterprise systems, SOAP, RSS, and config still use XML.",
        where="Legacy integrations, Android layouts, publishing pipelines.",
        objectives=("Parse XML with ElementTree.", "Navigate elements and attributes.", "Build XML safely."),
        outcome="You read and produce XML without fragile string concat.",
        industry=("Telecom", "Publishing", "Government", "Enterprise ERP"),
        concepts=(
            ("ElementTree", "Parse XML to tree.", "import xml.etree.ElementTree as ET\nroot = ET.fromstring('<item id=\"1\">A</item>')\nprint(root.tag, root.attrib)"),
            ("find/findall", "Query child elements.", "import xml.etree.ElementTree as ET\nroot = ET.fromstring('<root><a/><b/></root>')\nprint(len(root.findall('.')))"),
            ("tostring", "Serialize element.", "import xml.etree.ElementTree as ET\ne = ET.Element('note')\nprint(ET.tostring(e, encoding='unicode')[:5])"),
        ),
        concept="XML is a tree of tagged nodes with attributes.",
        purpose="Structured document interchange.",
        benefits="Schema validation (XSD), namespaces, mature tooling.",
        use_cases="RSS feeds, SOAP envelopes, config files.",
        best_practices="Use ElementTree; avoid XML external entities; validate schema.",
        mistakes="String templating XML, billion laughs, no namespaces handling.",
        basic_syntax="import xml.etree.ElementTree as ET\nET.parse('file.xml')",
        structure="parse -> traverse -> mutate -> write",
        pattern="for child in root.findall('record'):\n    process(child)",
        beginner=dedent("""\
            import xml.etree.ElementTree as ET

            xml = '<catalog><book id=\"bk1\"/></catalog>'
            root = ET.fromstring(xml)
            print(root[0].tag)"""),
        intermediate=dedent("""\
            import xml.etree.ElementTree as ET

            data = '''<users><user name=\"Ada\"/><user name=\"Lin\"/></users>'''
            names = [u.attrib['name'] for u in ET.fromstring(data).findall('user')]
            print(names)"""),
        advanced=dedent("""\
            import xml.etree.ElementTree as ET


            def build_order(order_id: str, sku: str) -> str:
                root = ET.Element('order', id=order_id)
                item = ET.SubElement(root, 'item', sku=sku)
                item.text = '1'
                return ET.tostring(root, encoding='unicode')


            print(build_order('100', 'ABC')[:20])"""),
        mermaid="flowchart LR\n    A[XML Text] --> B[Parser]\n    B --> C[Element Tree]",
    )

    p(
        "Logging",
        what="Logging records structured runtime events with levels and handlers.",
        why="Print statements fail in production; logs enable observability.",
        where="Servers, batch jobs, libraries, debugging production.",
        objectives=("Configure logging levels and handlers.", "Log with context and exceptions.", "Use module loggers."),
        outcome="You instrument apps with production-grade logs.",
        industry=("SRE", "Backend platforms", "Data pipelines", "Security ops"),
        concepts=(
            ("getLogger", "Named logger hierarchy.", "import logging\nlog = logging.getLogger(__name__)\nlog.warning('warn')"),
            ("levels", "DEBUG INFO WARNING ERROR CRITICAL.", "import logging\nprint(logging.INFO)"),
            ("exception", "Log traceback.", "import logging\nlogging.basicConfig(level=logging.ERROR)\ntry:\n    1/0\nexcept ZeroDivisionError:\n    logging.exception('fail')"),
        ),
        concept="Loggers emit records processed by handlers/formatters.",
        purpose="Trace behavior and diagnose failures.",
        benefits="Levels, rotation, structured fields, filtering.",
        use_cases="Request tracing, audit trails, metrics hooks.",
        best_practices="Log to stdout in containers; include correlation ids; no secrets.",
        mistakes="Root logger misconfig, logging in tight loops, sensitive data in logs.",
        basic_syntax="import logging\nlogging.info('message')",
        structure="configure -> getLogger -> log events",
        pattern="logger.info('user=%s action=%s', user, action)",
        beginner="import logging\nlogging.basicConfig(level=logging.INFO)\nlogging.info('started')",
        intermediate=dedent("""\
            import logging

            logger = logging.getLogger('billing')
            logger.setLevel(logging.DEBUG)
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
            logger.addHandler(handler)
            logger.info('invoice created')"""),
        advanced=dedent("""\
            import logging
            from logging.handlers import RotatingFileHandler

            logger = logging.getLogger('app')
            handler = RotatingFileHandler('app.log', maxBytes=1024, backupCount=2)
            logger.addHandler(handler)
            logger.error('rotated log example')"""),
        mermaid="flowchart LR\n    A[Logger] --> B[Handler]\n    B --> C[Formatter]\n    C --> D[Output]",
    )

    p(
        "Configuration Management",
        what="Configuration management loads settings from env vars, files, and defaults.",
        why="Apps must behave differently per environment without code changes.",
        where="12-factor apps, microservices, CLI tools, notebooks.",
        objectives=("Load env with os.environ.", "Parse .env and YAML/TOML safely.", "Layer defaults < file < env."),
        outcome="You externalize settings with clear precedence rules.",
        industry=("Cloud SaaS", "Kubernetes apps", "ML training jobs", "Mobile backends"),
        concepts=(
            ("os.environ", "Process environment variables.", "import os\nos.environ['APP_MODE'] = 'test'\nprint(os.environ.get('APP_MODE'))"),
            ("defaults", "Fallback values.", "import os\nDEBUG = os.environ.get('DEBUG', '0') == '1'\nprint(DEBUG)"),
            ("dataclass settings", "Typed config object.", "from dataclasses import dataclass\n@dataclass\nclass Settings:\n    host: str = 'localhost'\n    port: int = 8000\nprint(Settings().port)"),
        ),
        concept="Configuration separates policy from code.",
        purpose="Deploy same artifact to many environments.",
        benefits="Security (secrets via env), flexibility, testability.",
        use_cases="DB URLs, API keys, feature flags.",
        best_practices="Never commit secrets; validate on startup; document variables.",
        mistakes="Hard-coded prod URLs, silent missing env, no typing.",
        basic_syntax="import os\nAPI_KEY = os.environ.get('API_KEY', '')",
        structure="defaults -> file -> env overrides -> validate",
        pattern="settings = Settings.from_env()",
        beginner="import os\nprint(os.environ.get('PATH') is not None)",
        intermediate=dedent("""\
            import os
            from dataclasses import dataclass


            @dataclass
            class Config:
                database_url: str
                debug: bool


            cfg = Config(database_url=os.getenv('DATABASE_URL', 'sqlite://'), debug=os.getenv('DEBUG') == '1')
            print(cfg.database_url)"""),
        advanced=dedent("""\
            import json
            from pathlib import Path


            def load_settings(path: Path) -> dict:
                data = json.loads(path.read_text(encoding='utf-8'))
                data.update({k.lower(): v for k, v in __import__('os').environ.items() if k.startswith('APP_')})
                return data


            print('keys' in load_settings.__name__ or callable(load_settings))"""),
        mermaid="flowchart TD\n    A[Defaults] --> B[File Config]\n    B --> C[Env Overrides]\n    C --> D[App]",
    )

    p(
        "Multithreading",
        what="Multithreading runs concurrent threads within one process sharing memory.",
        why="Threads overlap I/O wait times for network and disk workloads.",
        where="Socket servers, downloaders, UI backends, parallel I/O.",
        objectives=("Start threads with threading module.", "Protect shared state with locks.", "Know GIL limits on CPU-bound work."),
        outcome="You parallelize I/O-bound tasks with threads safely.",
        industry=("Web crawlers", "Chat servers", "Monitoring agents", "Desktop apps"),
        concepts=(
            ("Thread", "Concurrent execution unit.", "import threading\ndef work():\n    print('run')\nt = threading.Thread(target=work)\nt.start()\nt.join()"),
            ("Lock", "Mutual exclusion.", "import threading\nlock = threading.Lock()\ncount = 0\ndef inc():\n    global count\n    with lock:\n        count += 1\ninc()\nprint(count)"),
            ("ThreadPoolExecutor", "Managed pool.", "from concurrent.futures import ThreadPoolExecutor\nwith ThreadPoolExecutor(max_workers=2) as ex:\n    print(list(ex.map(lambda x: x * 2, [1, 2, 3])))"),
        ),
        concept="Threads share memory; locks coordinate access.",
        purpose="Concurrent I/O and responsiveness.",
        benefits="Simple shared state, low overhead for I/O.",
        use_cases="Parallel HTTP fetches, worker queues.",
        best_practices="Avoid shared mutable state; use queues; pool executors.",
        mistakes="CPU-bound threading, deadlocks, race conditions.",
        basic_syntax="threading.Thread(target=func, args=(1,)).start()",
        structure="define worker -> start threads -> join",
        pattern="with ThreadPoolExecutor() as pool:\n    pool.map(fn, items)",
        beginner=dedent("""\
            import threading

            def hello():
                print('hello from thread')

            t = threading.Thread(target=hello)
            t.start()
            t.join()"""),
        intermediate=dedent("""\
            import threading

            counter = {'n': 0}
            lock = threading.Lock()

            def worker():
                with lock:
                    counter['n'] += 1

            threads = [threading.Thread(target=worker) for _ in range(5)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()
            print(counter['n'])"""),
        advanced=dedent("""\
            from concurrent.futures import ThreadPoolExecutor, as_completed


            def fetch(n: int) -> int:
                return n * n


            with ThreadPoolExecutor(max_workers=4) as pool:
                futures = [pool.submit(fetch, i) for i in range(6)]
                results = [f.result() for f in as_completed(futures)]
            print(sorted(results))"""),
        mermaid="flowchart LR\n    A[Main Thread] --> B[Worker Threads]\n    B --> C[Shared State + Locks]",
    )

    p(
        "Multiprocessing",
        what="Multiprocessing spawns separate processes to bypass the GIL for CPU work.",
        why="True parallelism for CPU-bound Python tasks requires processes.",
        where="Data crunching, image processing, scientific compute, batch jobs.",
        objectives=("Use multiprocessing.Process and Pool.", "Pass data via queues and pipes.", "Guard entry with if __name__ == '__main__'."),
        outcome="You parallelize CPU-bound workloads across cores.",
        industry=("Quant analytics", "Video encoding", "ML preprocessing", "Simulation"),
        concepts=(
            ("Process", "Independent Python interpreter.", "import multiprocessing as mp\ndef f(x):\n    return x + 1\nif __name__ == '__main__':\n    p = mp.Process(target=f, args=(1,))\n    p.start()\n    p.join()"),
            ("Pool", "Worker process pool.", "from multiprocessing import Pool\nif __name__ == '__main__':\n    with Pool(2) as pool:\n        print(pool.map(lambda x: x * 2, [1, 2, 3]))"),
            ("Queue", "Inter-process messaging.", "from multiprocessing import Process, Queue\ndef worker(q):\n    q.put('done')\nif __name__ == '__main__':\n    q = Queue()\n    p = Process(target=worker, args=(q,))\n    p.start()\n    print(q.get())\n    p.join()"),
        ),
        concept="Processes have separate memory spaces.",
        purpose="CPU parallelism and isolation.",
        benefits="Uses multiple cores, fault isolation.",
        use_cases="Monte Carlo, batch transforms, parallel tests.",
        best_practices="Protect main; pick spawn on Windows; minimize large pickles.",
        mistakes="Forgetting main guard, huge shared objects, too many processes.",
        basic_syntax="if __name__ == '__main__':\n    Process(target=work).start()",
        structure="spawn workers -> communicate -> join",
        pattern="with Pool(n) as pool:\n    pool.map(func, data)",
        beginner=dedent("""\
            from multiprocessing import Process


            def double(x):
                print(x * 2)


            if __name__ == '__main__':
                p = Process(target=double, args=(21,))
                p.start()
                p.join()"""),
        intermediate=dedent("""\
            from multiprocessing import Pool


            def square(x: int) -> int:
                return x * x


            if __name__ == '__main__':
                with Pool(2) as pool:
                    print(pool.map(square, range(5)))"""),
        advanced=dedent("""\
            from concurrent.futures import ProcessPoolExecutor


            def fib(n: int) -> int:
                a, b = 0, 1
                for _ in range(n):
                    a, b = b, a + b
                return a


            if __name__ == '__main__':
                with ProcessPoolExecutor(max_workers=2) as ex:
                    print(list(ex.map(fib, [10, 12, 14])))"""),
        mermaid="flowchart LR\n    A[Parent Process] --> B[Child Processes]\n    B --> C[Results via Queue/Pool]",
    )

    p(
        "Async Programming",
        what="Async programming coordinates many I/O tasks with async/await and an event loop.",
        why="It scales concurrent network I/O without thread-per-connection overhead.",
        where="Web servers, websockets, chat, microservices, IoT gateways.",
        objectives=("Define async def and await coroutines.", "Run asyncio.run main loops.", "Gather concurrent tasks."),
        outcome="You build concurrent I/O services with asyncio.",
        industry=("Real-time APIs", "Streaming platforms", "Telecom", "Fintech feeds"),
        concepts=(
            ("async def", "Defines coroutine function.", "async def hi():\n    return 'hi'"),
            ("await", "Pause until awaitable completes.", "import asyncio\nasync def main():\n    await asyncio.sleep(0)\n    return 1\nprint(asyncio.run(main()))"),
            ("gather", "Run tasks concurrently.", "import asyncio\nasync def work(n):\n    return n\nasync def main():\n    print(await asyncio.gather(work(1), work(2)))\nasyncio.run(main())"),
        ),
        concept="Event loop schedules awaitable tasks cooperatively.",
        purpose="High concurrency for I/O-bound workloads.",
        benefits="Low memory vs threads, structured concurrency primitives.",
        use_cases="HTTP clients, websockets, background workers.",
        best_practices="Never block loop; use asyncio.to_thread for blocking code.",
        mistakes="Blocking calls in async routes, unhandled task exceptions.",
        basic_syntax=dedent("""\
            import asyncio


            async def main():
                return 'done'


            print(asyncio.run(main()))"""),
        structure="create coroutines -> schedule -> await results",
        pattern="await asyncio.gather(*tasks)",
        beginner=dedent("""\
            import asyncio

            async def greet(name: str) -> str:
                return f'Hello, {name}'

            print(asyncio.run(greet('Ada')))"""),
        intermediate=dedent("""\
            import asyncio

            async def fetch(n: int) -> int:
                await asyncio.sleep(0.01)
                return n * 2

            async def main():
                results = await asyncio.gather(*(fetch(i) for i in range(3)))
                print(results)

            asyncio.run(main())"""),
        advanced=dedent("""\
            import asyncio

            async def producer(queue: asyncio.Queue[int]) -> None:
                for i in range(3):
                    await queue.put(i)
                await queue.put(-1)

            async def consumer(queue: asyncio.Queue[int]) -> list[int]:
                items = []
                while True:
                    item = await queue.get()
                    if item == -1:
                        break
                    items.append(item * 2)
                return items

            async def main():
                q: asyncio.Queue[int] = asyncio.Queue()
                prod = asyncio.create_task(producer(q))
                result = await consumer(q)
                await prod
                print(result)

            asyncio.run(main())"""),
        mermaid="flowchart LR\n    A[Event Loop] --> B[Task 1]\n    A --> C[Task 2]\n    B --> D[Await I/O]",
    )

    p(
        "API Development",
        what="API development builds HTTP (or RPC) interfaces for clients and services.",
        why="APIs expose business capabilities to web and mobile clients and other services.",
        where="SaaS products, mobile backends, partner integrations, ML serving.",
        objectives=("Design RESTful routes and status codes.", "Validate request/response schemas.", "Implement auth and error handling."),
        outcome="You ship documented, testable HTTP APIs.",
        industry=("Fintech APIs", "Health platforms", "E-commerce", "Internal platforms"),
        concepts=(
            ("Routes", "Map paths to handlers.", "ROUTES = {'/health': lambda: {'status': 'ok'}}\nprint(ROUTES['/health']())"),
            ("Status codes", "Communicate outcome.", "STATUS = {200: 'OK', 404: 'Not Found'}\nprint(STATUS[200])"),
            ("Schema validation", "Reject bad payloads early.", "payload = {'email': 'a@b.com'}\nassert 'email' in payload"),
        ),
        concept="APIs are contracts between producer and consumer.",
        purpose="Enable interoperable software integration.",
        benefits="Decoupling, multi-client support, monetization.",
        use_cases="CRUD resources, webhooks, public developer platforms.",
        best_practices="Version APIs; paginate lists; consistent errors; OpenAPI docs.",
        mistakes="Breaking changes, no auth, leaking stack traces.",
        basic_syntax="def get_user(user_id: int) -> dict:\n    return {'id': user_id}",
        structure="router -> handler -> service -> repository",
        pattern=dedent("""\
            def read_item(item_id: int) -> dict:
                return {'id': item_id}


            print(read_item(1))"""),
        beginner=dedent("""\
            def create_response(data: dict, status: int = 200) -> dict:
                return {'status': status, 'data': data}


            print(create_response({'ok': True}))"""),
        intermediate=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class User:
                id: int
                email: str


            USERS = {1: User(1, 'a@b.com')}


            def get_user(user_id: int) -> User:
                if user_id not in USERS:
                    raise KeyError('not found')
                return USERS[user_id]


            print(get_user(1).email)"""),
        advanced=dedent("""\
            from http.server import BaseHTTPRequestHandler, HTTPServer


            class Handler(BaseHTTPRequestHandler):
                def do_GET(self):
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(b'{"status":"ok"}')


            def run_server():
                server = HTTPServer(('127.0.0.1', 0), Handler)
                host, port = server.server_address
                print(f'listening {port}')
                server.handle_request()


            run_server()"""),
        mermaid="flowchart LR\n    A[Client] --> B[API Gateway]\n    B --> C[Handler]\n    C --> D[Service/DB]",
    )

    p(
        "API Consumption",
        what="API consumption calls external HTTP/JSON services from Python clients.",
        why="Most apps integrate payment, maps, auth, and data providers via APIs.",
        where="Mobile backends, ETL, automation, partner integrations.",
        objectives=("Perform GET/POST with proper headers.", "Handle timeouts and retries.", "Parse and validate responses."),
        outcome="You integrate third-party APIs reliably.",
        industry=("Travel aggregators", "Marketing stacks", "Ops automation", "Open banking"),
        concepts=(
            ("GET request", "Fetch resources.", "import urllib.request\nwith urllib.request.urlopen('https://example.com') as r:\n    print(r.status)"),
            ("JSON body", "Parse response content.", "import json\nprint(json.loads('{\"ok\": true}')['ok'])"),
            ("errors", "Check status codes.", "class APIError(Exception):\n    pass\nraise APIError('404')"),
        ),
        concept="Clients must treat remote APIs as unreliable external dependencies.",
        purpose="Compose services into richer applications.",
        benefits="Faster feature delivery, leverage best-in-class vendors.",
        use_cases="Stripe charges, Slack posts, weather data.",
        best_practices="Set timeouts; exponential backoff; cache idempotent reads.",
        mistakes="No timeout, no retry limits, trusting response shape.",
        basic_syntax="import urllib.request\nurllib.request.urlopen(url, timeout=5)",
        structure="build request -> send -> handle status -> parse",
        pattern="response = client.get('/users/1')\nresponse.raise_for_status()",
        beginner=dedent("""\
            import json
            import urllib.request

            class DummyResponse:
                def read(self):
                    return b'{"value": 42}'

            data = json.loads(DummyResponse().read())
            print(data['value'])"""),
        intermediate=dedent("""\
            import json
            import urllib.error
            import urllib.request


            def fetch_json(url: str) -> dict:
                try:
                    with urllib.request.urlopen(url, timeout=5) as resp:
                        return json.loads(resp.read().decode())
                except urllib.error.HTTPError as exc:
                    return {'error': exc.code}


            print('error' in fetch_json('https://example.com') or True)"""),
        advanced=dedent("""\
            import time


            def retry_get(fetch, attempts=3, delay=0.01):
                last = None
                for _ in range(attempts):
                    try:
                        return fetch()
                    except Exception as exc:
                        last = exc
                        time.sleep(delay)
                raise last


            print(retry_get(lambda: {'ok': True}))"""),
        mermaid="flowchart LR\n    A[Python Client] --> B[HTTP Request]\n    B --> C[Remote API]\n    C --> D[Parsed Data]",
    )

    p(
        "Requests Library",
        what="Requests is a popular HTTP client library with a friendly API.",
        why="It simplifies headers, sessions, JSON, and auth compared to urllib.",
        where="Scripts, data ingestion, tests hitting HTTP services.",
        objectives=("Use requests.get/post with params and JSON.", "Reuse Session for cookies/headers.", "Handle timeouts and exceptions."),
        outcome="You call HTTP APIs ergonomically with requests.",
        industry=("Data ingestion", "QA automation", "Internal tools", "Prototyping"),
        concepts=(
            ("get/post", "HTTP verbs.", "import requests\nprint(hasattr(requests, 'get'))"),
            ("json=", "Send JSON bodies.", "payload = {'a': 1}\nprint(payload['a'])"),
            ("Session", "Persistent client.", "class Session:\n    def __init__(self):\n        self.headers = {}\ns = Session()\ns.headers['UA'] = 'demo'\nprint(s.headers['UA'])"),
        ),
        concept="Requests wraps HTTP into Pythonic calls.",
        purpose="Fast, readable HTTP client code.",
        benefits="Sessions, auth helpers, streaming, timeouts.",
        use_cases="REST integrations, health checks, scrapers (respect robots).",
        best_practices="Always set timeout; use sessions; verify TLS in prod.",
        mistakes="No timeout, ignoring response.ok, huge response in memory.",
        basic_syntax="import requests\nrequests.get('https://example.com', timeout=5)",
        structure="Session -> request -> raise_for_status -> json()",
        pattern="with requests.Session() as s:\n    s.get(url)",
        beginner="import requests\nprint(requests.__version__[:1].isdigit())",
        intermediate=dedent("""\
            class FakeResponse:
                status_code = 200

                def json(self):
                    return {'ok': True}


            def fake_get(url, timeout=5):
                return FakeResponse()


            print(fake_get('https://example.com').json())"""),
        advanced=dedent("""\
            class RetryClient:
                def __init__(self, getter, retries=3):
                    self.getter = getter
                    self.retries = retries

                def get(self, url):
                    last = None
                    for _ in range(self.retries):
                        try:
                            resp = self.getter(url)
                            if resp.status_code < 500:
                                return resp
                        except Exception as exc:
                            last = exc
                    raise last


            class Resp:
                status_code = 200


            print(RetryClient(lambda u: Resp()).get('/').status_code)"""),
        mermaid="flowchart LR\n    A[requests] --> B[HTTP]\n    B --> C[Response]",
    )

    p(
        "Database Fundamentals",
        what="Database fundamentals cover relational models, SQL, transactions, and connections.",
        why="Persistent structured storage underpins most applications.",
        where="CRUD apps, analytics, auth systems, inventory, billing.",
        objectives=("Explain tables, keys, and relationships.", "Write basic SELECT/INSERT/UPDATE.", "Understand ACID transactions."),
        outcome="You design and query relational data confidently.",
        industry=("Banking", "Retail", "Healthcare records", "SaaS multitenant"),
        concepts=(
            ("Table", "Rows and columns.", "ROW = {'id': 1, 'name': 'Ada'}\nprint(ROW['name'])"),
            ("Primary key", "Unique row identifier.", "ids = {1, 2}\nassert len(ids) == 2"),
            ("Transaction", "All-or-nothing changes.", "balance = 100\nbalance -= 30\nassert balance == 70"),
        ),
        concept="Relational DBs store normalized data queried with SQL.",
        purpose="Durable, queryable structured storage.",
        benefits="Consistency, joins, mature tooling.",
        use_cases="Users, orders, ledgers, inventory.",
        best_practices="Use migrations; index wisely; least privilege credentials.",
        mistakes="N+1 queries, no transactions, string-built SQL (injection).",
        basic_syntax="SQL = 'SELECT id, name FROM users WHERE active = 1'\nprint(SQL.split()[0])",
        structure="connect -> cursor -> execute -> commit/rollback",
        pattern="BEGIN -> statements -> COMMIT",
        beginner="SQL = 'SELECT 1 AS one'\nprint(SQL.split()[0])",
        intermediate=dedent("""\
            def transfer(balance: dict, src: str, dst: str, amount: float) -> None:
                if balance[src] < amount:
                    raise ValueError('insufficient funds')
                balance[src] -= amount
                balance[dst] += amount


            b = {'A': 100.0, 'B': 0.0}
            transfer(b, 'A', 'B', 40)
            print(b)"""),
        advanced=dedent("""\
            class Transaction:
                def __init__(self, conn):
                    self.conn = conn

                def __enter__(self):
                    self.conn['in_tx'] = True
                    return self.conn

                def __exit__(self, exc_type, exc, tb):
                    self.conn['in_tx'] = False
                    self.conn['committed'] = exc_type is None
                    return False


            conn = {'in_tx': False, 'committed': False}
            with Transaction(conn):
                conn['rows'] = 1
            print(conn['committed'])"""),
        mermaid="flowchart LR\n    A[App] --> B[Connection]\n    B --> C[SQL]\n    C --> D[DB]",
    )

    p(
        "SQLite",
        what="SQLite is a serverless embedded SQL database in a single file.",
        why="It is ideal for local apps, prototypes, tests, and edge devices.",
        where="Mobile apps, desktop tools, unit tests, small web apps.",
        objectives=("Connect with sqlite3 module.", "Execute SQL safely with parameters.", "Use context managers for connections."),
        outcome="You persist data locally with SQLite and Python.",
        industry=("Mobile", "IoT gateways", "Developer tools", "Testing"),
        concepts=(
            ("connect", "Open database file.", "import sqlite3\nconn = sqlite3.connect(':memory:')\nprint(type(conn).__name__)"),
            ("parameterized SQL", "Prevent injection.", "import sqlite3\nconn = sqlite3.connect(':memory:')\nconn.execute('CREATE TABLE t (id INTEGER)')\nconn.execute('INSERT INTO t VALUES (?)', (1,))\nprint(conn.execute('SELECT id FROM t').fetchone()[0])"),
            ("row factory", "Dict-like rows.", "import sqlite3\nconn = sqlite3.connect(':memory:')\nconn.row_factory = sqlite3.Row\nprint(callable(conn.row_factory))"),
        ),
        concept="SQLite runs in-process without separate server.",
        purpose="Lightweight relational persistence.",
        benefits="Zero config, fast for small/medium data, portable file.",
        use_cases="App cache DB, integration tests, prototypes.",
        best_practices="Use WAL mode for concurrency; migrate schema; backup file.",
        mistakes="Writing SQL with f-strings, no indexes, huge blobs in DB.",
        basic_syntax="import sqlite3\nconn = sqlite3.connect('app.db')",
        structure="connect -> execute -> commit -> close",
        pattern="conn.execute('SELECT id FROM users WHERE id=?', (user_id,))",
        beginner=dedent("""\
            import sqlite3

            conn = sqlite3.connect(':memory:')
            conn.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)')
            conn.execute('INSERT INTO users (name) VALUES (?)', ('Ada',))
            print(conn.execute('SELECT name FROM users').fetchone()[0])"""),
        intermediate=dedent("""\
            import sqlite3

            with sqlite3.connect(':memory:') as conn:
                conn.execute('CREATE TABLE items (sku TEXT, qty INTEGER)')
                conn.executemany('INSERT INTO items VALUES (?, ?)', [('A', 2), ('B', 1)])
                total = conn.execute('SELECT SUM(qty) FROM items').fetchone()[0]
                print(total)"""),
        advanced=dedent("""\
            import sqlite3

            def init(conn: sqlite3.Connection) -> None:
                conn.execute('CREATE TABLE IF NOT EXISTS audit (id INTEGER PRIMARY KEY AUTOINCREMENT, msg TEXT)')
                conn.commit()


            conn = sqlite3.connect(':memory:')
            init(conn)
            conn.execute('INSERT INTO audit (msg) VALUES (?)', ('created',))
            print(conn.execute('SELECT COUNT(*) FROM audit').fetchone()[0])"""),
        mermaid="flowchart LR\n    A[Python] --> B[sqlite3]\n    B --> C[.db file]",
    )

    p(
        "MySQL Integration",
        what="MySQL integration connects Python apps to MySQL/MariaDB servers.",
        why="MySQL powers many web stacks and hosted relational workloads.",
        where="LAMP/LEMP stacks, WordPress backends, SaaS multitenant DBs.",
        objectives=("Connect with a DB-API driver.", "Use parameterized queries.", "Manage connection pools in production."),
        outcome="You read and write MySQL data safely from Python.",
        industry=("Web hosting", "E-commerce", "Content platforms", "Internal CRMs"),
        concepts=(
            ("DB-API", "PEP 249 cursor pattern.", "class Cursor:\n    def execute(self, sql, params=()):\n        return sql, params\nc = Cursor()\nprint(c.execute('SELECT ?', (1,))[1])"),
            ("Connection string", "Host, user, database.", "DSN = {'host': 'localhost', 'database': 'app'}\nprint(DSN['database'])"),
            ("Pool", "Reuse connections.", "POOL = []\ndef acquire():\n    return POOL[0] if POOL else object()\nprint(acquire())"),
        ),
        concept="Drivers translate Python calls to MySQL protocol.",
        purpose="Remote relational storage at scale.",
        benefits="Mature ecosystem, replication, hosting support.",
        use_cases="Web apps, reporting replicas, CMS data.",
        best_practices="Use mysqlclient or PyMySQL; SSL; least privilege user.",
        mistakes="SQL injection, no connection timeout, storing plaintext passwords.",
        basic_syntax="conn = connect(host='localhost', user='app', password='***', database='app')",
        structure="pool -> connection -> cursor -> commit",
        pattern="cursor.execute('SELECT * FROM users WHERE id=%s', (user_id,))",
        beginner="CONFIG = {'driver': 'mysql', 'host': '127.0.0.1'}\nprint(CONFIG['driver'])",
        intermediate=dedent("""\
            def query_users(cursor, active_only=True):
                sql = 'SELECT id, email FROM users'
                if active_only:
                    sql += ' WHERE active = 1'
                return cursor.execute(sql)


            class Cur:
                def execute(self, sql):
                    return [('1', 'a@b.com')]


            print(query_users(Cur()))"""),
        advanced=dedent("""\
            class MySQLPool:
                def __init__(self, size: int = 5):
                    self._size = size
                    self._in_use = 0

                def connection(self):
                    if self._in_use >= self._size:
                        raise RuntimeError('pool exhausted')
                    self._in_use += 1
                    return self

                def close(self):
                    self._in_use -= 1


            pool = MySQLPool(2)
            conn = pool.connection()
            conn.close()
            print(pool._in_use)"""),
        mermaid="flowchart LR\n    A[Python App] --> B[Driver]\n    B --> C[MySQL Server]",
    )

    p(
        "PostgreSQL Integration",
        what="PostgreSQL integration connects Python to advanced open-source RDBMS features.",
        why="Postgres offers JSONB, extensions, and strong SQL compliance.",
        where="SaaS platforms, geospatial apps, analytics, Django stacks.",
        objectives=("Connect with psycopg.", "Use transactions and RETURNING.", "Leverage Postgres types from Python."),
        outcome="You integrate Python services with PostgreSQL effectively.",
        industry=("SaaS", "Geospatial", "Data warehouses", "Fintech ledgers"),
        concepts=(
            ("psycopg", "Popular Postgres adapter.", "print('psycopg'[:5])"),
            ("JSONB", "Document columns in SQL.", "import json\nprint(json.dumps({'a': 1}))"),
            ("RETURNING", "Get inserted rows.", "SQL = 'INSERT INTO t (name) VALUES (%s) RETURNING id'\nprint('RETURNING' in SQL)"),
        ),
        concept="Drivers map Python types to Postgres types.",
        purpose="Robust transactional storage with rich SQL.",
        benefits="Extensions, CTEs, strong consistency, JSONB.",
        use_cases="Multi-tenant SaaS, GIS, event sourcing.",
        best_practices="Use connection pools; migrations; explain analyze slow queries.",
        mistakes="Not closing connections, serializing JSON manually wrong, superuser in app.",
        basic_syntax="conn = psycopg.connect('postgresql://user:pass@localhost/db')",
        structure="connect -> cursor -> execute -> commit",
        pattern=dedent("""\
            class Connection:
                def transaction(self):
                    return self

                def execute(self, sql):
                    return []


            conn = Connection()
            with conn.transaction():
                rows = conn.execute('SELECT 1')
            print(rows)"""),
        beginner="DSN = 'postgresql://localhost/app'\nprint(DSN.startswith('postgresql'))",
        intermediate=dedent("""\
            def insert_user(repo, email: str) -> int:
                return repo.execute('INSERT INTO users(email) VALUES (%s) RETURNING id', (email,))


            class Repo:
                def execute(self, sql, params):
                    return 42


            print(insert_user(Repo(), 'a@b.com'))"""),
        advanced=dedent("""\
            class PGTransaction:
                def __init__(self, conn):
                    self.conn = conn

                def __enter__(self):
                    self.conn['tx'] = True
                    return self.conn

                def __exit__(self, exc_type, exc, tb):
                    self.conn['tx'] = False
                    self.conn['ok'] = exc_type is None
                    return False


            c = {'tx': False, 'ok': False}
            with PGTransaction(c):
                c['work'] = True
            print(c['ok'])"""),
        mermaid="flowchart LR\n    A[Python] --> B[psycopg]\n    B --> C[PostgreSQL]",
    )

    p(
        "SQLAlchemy ORM",
        what="SQLAlchemy ORM maps Python classes to database tables and queries.",
        why="It reduces boilerplate SQL and eases schema evolution.",
        where="Web apps, data services, admin tools, migration-heavy systems.",
        objectives=("Declare mapped classes and sessions.", "Query with Session.query or select().", "Manage migrations with Alembic."),
        outcome="You persist domain objects with SQLAlchemy patterns.",
        industry=("Django-adjacent services", "Enterprise apps", "Internal tools", "Analytics apps"),
        concepts=(
            ("Engine", "Connection factory.", "class Engine:\n    def connect(self):\n        return {'connected': True}\nprint(Engine().connect())"),
            ("Session", "Unit of work.", "class Session:\n    def add(self, obj):\n        self.obj = obj\ns = Session()\ns.add({'id': 1})\nprint(s.obj)"),
            ("Mapped class", "Class <-> table.", "class User:\n    __tablename__ = 'users'\n    id = 1\nprint(User.__tablename__)"),
        ),
        concept="ORM translates objects to SQL and back.",
        purpose="Productive relational persistence in Python.",
        benefits="Composable queries, connection pooling, dialect abstraction.",
        use_cases="User models, orders, reporting entities.",
        best_practices="Explicit sessions; avoid lazy loading N+1; use Alembic.",
        mistakes="Session leaks, implicit autoflush surprises, god models.",
        basic_syntax="session.add(obj)\nsession.commit()",
        structure="engine -> sessionmaker -> session -> query/commit",
        pattern="with Session(engine) as session:\n    session.add(user)",
        beginner=dedent("""\
            class User:
                def __init__(self, email: str):
                    self.email = email


            user = User('a@b.com')
            print(user.email)"""),
        intermediate=dedent("""\
            class Repository:
                def __init__(self, session):
                    self.session = session

                def create_user(self, email: str):
                    user = {'email': email}
                    self.session['users'] = self.session.get('users', []) + [user]
                    return user


            session = {}
            repo = Repository(session)
            print(repo.create_user('a@b.com'))"""),
        advanced=dedent("""\
            class UnitOfWork:
                def __init__(self):
                    self.new = []
                    self.dirty = []

                def register_new(self, entity):
                    self.new.append(entity)

                def commit(self):
                    saved = len(self.new) + len(self.dirty)
                    self.new.clear()
                    self.dirty.clear()
                    return saved


            uow = UnitOfWork()
            uow.register_new({'id': 1})
            print(uow.commit())"""),
        mermaid="flowchart LR\n    A[Mapped Class] --> B[Session]\n    B --> C[Engine]\n    C --> D[Database]",
    )

    p(
        "Unit Testing",
        what="Unit testing verifies small units of code behave as expected automatically.",
        why="Tests prevent regressions and document intended behavior.",
        where="Every professional Python codebase and CI pipeline.",
        objectives=("Write tests with unittest or pytest.", "Use assertions and test cases.", "Organize tests mirroring package structure."),
        outcome="You protect core logic with fast automated unit tests.",
        industry=("SaaS", "Libraries", "Quant systems", "Safety-critical tooling"),
        concepts=(
            ("test function", "Assert expected behavior.", "def test_add():\n    assert 1 + 1 == 2\ntest_add()"),
            ("TestCase", "unittest grouping.", "import unittest\nclass Tests(unittest.TestCase):\n    def test_true(self):\n        self.assertTrue(True)\nunittest.main(argv=[''], exit=False)"),
            ("arrange-act-assert", "Test structure.", "def test_double():\n    value = 2\n    result = value * 2\n    assert result == 4\ntest_double()"),
        ),
        concept="Unit tests isolate one behavior per test.",
        purpose="Catch bugs early and enable refactoring.",
        benefits="Confidence, living documentation, safer CI.",
        use_cases="Pure functions, validators, parsers.",
        best_practices="One assertion focus; descriptive names; fast tests.",
        mistakes="Testing implementation details, flaky tests, no CI run.",
        basic_syntax="def test_something():\n    assert func() == expected",
        structure="arrange -> act -> assert",
        pattern="result = system_under_test(input)\nassert result == expected",
        beginner="def inc(x):\n    return x + 1\nassert inc(2) == 3",
        intermediate=dedent("""\
            import unittest


            def is_palindrome(text: str) -> bool:
                cleaned = text.lower().replace(' ', '')
                return cleaned == cleaned[::-1]


            class PalindromeTests(unittest.TestCase):
                def test_palindrome(self):
                    self.assertTrue(is_palindrome('Level'))


            unittest.main(argv=[''], exit=False, verbosity=0)"""),
        advanced=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class TestResult:
                name: str
                passed: bool


            def run_tests(cases):
                return [TestResult(name, fn()) for name, fn in cases]


            print(run_tests([('ok', lambda: True)]))"""),
        mermaid="flowchart LR\n    A[Code Change] --> B[Run Tests]\n    B --> C{Pass?}\n    C -->|yes| D[Merge]\n    C -->|no| E[Fix]",
    )

    p(
        "Pytest",
        what="Pytest is a flexible testing framework with simple tests and powerful fixtures.",
        why="It reduces boilerplate versus unittest and has rich plugin ecosystem.",
        where="Open source Python, FastAPI/Django projects, libraries.",
        objectives=("Write test_ functions and assert.", "Use fixtures for setup/teardown.", "Parametrize tests for edge cases."),
        outcome="You build expressive test suites with pytest.",
        industry=("Web APIs", "PyPI packages", "Data platforms", "ML pipelines"),
        concepts=(
            ("test_ prefix", "Auto-discovered tests.", "def test_sum():\n    assert sum([1, 2]) == 3\ntest_sum()"),
            ("fixtures", "Reusable setup.", "def sample_data():\n    return [1, 2, 3]\nassert len(sample_data()) == 3"),
            ("parametrize", "Multiple inputs.", "cases = [(1, 2), (2, 4)]\nfor n, expected in cases:\n    assert n * 2 == expected"),
        ),
        concept="Pytest collects tests and runs with rich reporting.",
        purpose="Productive testing with minimal ceremony.",
        benefits="Fixtures, plugins, clear failures, parametrize.",
        use_cases="API tests, unit tests, snapshot testing.",
        best_practices="Use conftest.py; mark slow tests; isolate I/O.",
        mistakes="Shared mutable fixtures, testing order dependence.",
        basic_syntax="def test_example():\n    assert True",
        structure="fixtures -> test functions -> pytest runner",
        pattern=dedent("""\
            class Client:
                def post(self, path, json=None):
                    return {'path': path, 'json': json}


            def test_user_creation(client):
                return client.post('/users', json={'email': 'a@b.com'})


            print(test_user_creation(Client()))"""),
        beginner="def test_upper():\n    assert 'hi'.upper() == 'HI'\ntest_upper()",
        intermediate=dedent("""\
            def pytest_style_double(n):
                return n * 2


            def test_double():
                assert pytest_style_double(3) == 6"""),
        advanced=dedent("""\
            def parametrize(cases):
                def decorator(func):
                    def runner():
                        for args in cases:
                            func(*args)
                    return runner
                return decorator


            @parametrize([(2, 4), (3, 6)])
            def test_double(n, expected):
                assert n * 2 == expected


            test_double()"""),
        mermaid="flowchart LR\n    A[pytest] --> B[Collect Tests]\n    B --> C[Fixtures]\n    C --> D[Run/Report]",
    )

    p(
        "Mocking",
        what="Mocking replaces real dependencies with test doubles during unit tests.",
        why="Tests must be isolated from networks, databases, and non-determinism.",
        where="Unit tests for services, API clients, time, randomness.",
        objectives=("Use unittest.mock.Mock and patch.", "Assert calls and return values.", "Avoid over-mocking internal details."),
        outcome="You test components in isolation with controlled dependencies.",
        industry=("Microservices", "SDK development", "Payment integrations", "CI pipelines"),
        concepts=(
            ("Mock", "Fake object with methods.", "from unittest.mock import Mock\nm = Mock(return_value=42)\nprint(m())"),
            ("patch", "Replace symbol temporarily.", "from unittest.mock import patch\nwith patch('builtins.len', return_value=3):\n    print(len([]))"),
            ("assert_called", "Verify interactions.", "from unittest.mock import Mock\nm = Mock()\nm.save('x')\nm.save.assert_called_once_with('x')"),
        ),
        concept="Mocks simulate collaborators with controlled behavior.",
        purpose="Isolate unit under test.",
        benefits="Fast, deterministic tests without external systems.",
        use_cases="API client tests, DB repository tests, clock control.",
        best_practices="Mock boundaries not internals; verify outcomes and key calls.",
        mistakes="Mocking everything, brittle call assertions, patching wrong path.",
        basic_syntax="from unittest.mock import Mock\nservice = Mock()\nservice.fetch.return_value = {'ok': True}",
        structure="patch dependency -> exercise code -> assert behavior",
        pattern=dedent("""\
            from unittest.mock import patch


            def flow(mock_call):
                mock_call.return_value = {'ok': True}
                return mock_call()


            with patch('builtins.len', return_value=3):
                print(flow(len))"""),
        beginner=dedent("""\
            from unittest.mock import Mock

            repo = Mock()
            repo.get.return_value = {'id': 1}
            print(repo.get(1)['id'])"""),
        intermediate=dedent("""\
            from unittest.mock import patch


            def send_email(client, to: str):
                return client.post('/email', json={'to': to})


            class FakeClient:
                def post(self, path, json=None):
                    return {'path': path, 'json': json}


            with patch('builtins.print'):
                result = send_email(FakeClient(), 'a@b.com')
            print(result['json']['to'])"""),
        advanced=dedent("""\
            from unittest.mock import MagicMock


            def process(payment_gateway, amount: float) -> str:
                receipt = payment_gateway.charge(amount)
                return receipt['id']


            gateway = MagicMock()
            gateway.charge.return_value = {'id': 'rcpt_123'}
            print(process(gateway, 10.0))"""),
        mermaid="flowchart LR\n    A[Unit Under Test] --> B[Mock Dependency]\n    B --> C[Controlled Response]",
    )

    p(
        "Packaging Python Projects",
        what="Packaging Python projects prepares installable distributions with metadata and entry points.",
        why="Packaging enables pip install, versioning, and publishing to PyPI.",
        where="Open source libraries, internal packages, CLI tools.",
        objectives=("Configure pyproject.toml with build backend.", "Declare dependencies and optional extras.", "Build wheels and sdist."),
        outcome="You build and publish Python packages correctly.",
        industry=("PyPI ecosystem", "Enterprise internal PyPI", "CLI products", "SDK vendors"),
        concepts=(
            ("pyproject.toml", "Project metadata and tools.", "print('[project]' in '[project]\\nname=\"demo\"')"),
            ("wheel", "Built distribution format.", "print('whl' in 'package-1.0-py3-none-any.whl')"),
            ("entry points", "Console scripts.", "ENTRY = {'console_scripts': ['mycli=mypkg.cli:main']}\nprint(ENTRY['console_scripts'][0].split('=')[0])"),
        ),
        concept="Build backends produce standardized artifacts.",
        purpose="Share and install Python code reliably.",
        benefits="Version pinning, dependency resolution, script installation.",
        use_cases="Libraries, CLIs, plugins.",
        best_practices="Semantic versioning; README on PyPI; classifiers; license file.",
        mistakes="Missing MANIFEST/pyproject deps, not testing install in clean venv.",
        basic_syntax="[project]\nname = \"my-package\"\nversion = \"0.1.0\"",
        structure="src layout -> pyproject -> build -> publish",
        pattern="commands = ['python', '-m', 'build']\nprint(' '.join(commands))",
        beginner="from pathlib import Path\nprint(Path('scripts/generate_all_snippets.py').exists())",
        intermediate=dedent("""\
            METADATA = {
                'name': 'demo_pkg',
                'version': '0.1.0',
                'dependencies': ['requests>=2.0'],
            }
            print(METADATA['name'])"""),
        advanced=dedent("""\
            def build_console_script(module: str, func: str = 'main') -> str:
                return f'{module.split('.')[-1]}={module}:{func}'


            print(build_console_script('myapp.cli'))"""),
        mermaid="flowchart LR\n    A[Source] --> B[build]\n    B --> C[wheel/sdist]\n    C --> D[pip install]",
    )

    p(
        "CLI Applications",
        what="CLI applications expose commands via terminal interfaces using argparse, click, or typer.",
        why="Operators and developers automate workflows from the shell.",
        where="DevOps tools, data utilities, codegen, admin tasks.",
        objectives=("Parse args and subcommands.", "Provide --help and sensible defaults.", "Return proper exit codes."),
        outcome="You ship user-friendly command-line tools in Python.",
        industry=("SRE tooling", "Data ops", "Security scanners", "Build systems"),
        concepts=(
            ("argparse", "Stdlib CLI parser.", "import argparse\np = argparse.ArgumentParser()\np.add_argument('name')\nargs = p.parse_args(['Ada'])\nprint(args.name)"),
            ("subcommands", "Nested CLI verbs.", "COMMANDS = {'run': lambda: 0, 'status': lambda: 0}\nprint(COMMANDS['run']())"),
            ("exit codes", "Signal success/failure.", "import sys\nsys.exit(0)"),
        ),
        concept="CLI = argv parsing + action + exit status.",
        purpose="Automate tasks from terminal and scripts.",
        benefits="Scriptable, remote-friendly, fast iteration.",
        use_cases="Deploy tools, ETL triggers, db migrations.",
        best_practices="Support --help; validate input; log to stderr; test CLI.",
        mistakes="Printing only help on error, no exit codes, hidden global state.",
        basic_syntax="if __name__ == '__main__':\n    main()",
        structure="parse args -> dispatch command -> exit code",
        pattern="parser = argparse.ArgumentParser()\nparser.parse_args()",
        beginner=dedent("""\
            import sys

            if len(sys.argv) > 1:
                print(f'Hello, {sys.argv[1]}')
            else:
                print('Hello, world')"""),
        intermediate=dedent("""\
            import argparse


            def main(argv=None):
                parser = argparse.ArgumentParser(description='Greet users')
                parser.add_argument('name')
                args = parser.parse_args(argv)
                print(f'Hello, {args.name}')


            main(['Ada'])"""),
        advanced=dedent("""\
            import argparse


            def build_parser():
                parser = argparse.ArgumentParser(prog='tool')
                sub = parser.add_subparsers(dest='command', required=True)
                run = sub.add_parser('run')
                run.add_argument('--dry-run', action='store_true')
                return parser


            args = build_parser().parse_args(['run', '--dry-run'])
            print(args.command, args.dry_run)"""),
        mermaid="flowchart LR\n    A[argv] --> B[Parser]\n    B --> C[Command Handler]\n    C --> D[Exit Code]",
    )
