"""Advanced topic snippet registrations (part 2)."""

from __future__ import annotations

from textwrap import dedent
from typing import Callable


def _register_advanced_part2(p: Callable[..., None]) -> None:
    p(
        "Pandas",
        what="Pandas is a library for tabular data manipulation via DataFrame and Series objects.",
        why="It is the standard tool for data cleaning, exploration, and feature engineering.",
        where="Analytics, finance, marketing, ML feature pipelines, reporting.",
        objectives=("Load and inspect datasets.", "Filter, group, merge, and pivot.", "Handle missing data."),
        outcome="You transform raw data into analysis-ready tables.",
        industry=("Data science", "BI", "Quant research", "Ops analytics"),
        concepts=(
            ("DataFrame", "2D labeled table.", "import pandas as pd\ndf = pd.DataFrame({'a': [1, 2]})\nprint(df.shape)"),
            ("Series", "1D labeled array.", "import pandas as pd\ns = pd.Series([1, 2, 3])\nprint(s.mean())"),
            ("GroupBy", "Split-apply-combine aggregations.", "import pandas as pd\ndf = pd.DataFrame({'g': ['x', 'x'], 'v': [1, 2]})\nprint(df.groupby('g')['v'].sum().to_dict())"),
        ),
        concept="DataFrame = rows + columns + indexes.",
        purpose="Efficient structured data operations.",
        benefits="Expressive API, integrates with NumPy/plotting/ML.",
        use_cases="ETL, dashboards, ad hoc analysis, feature stores.",
        best_practices="Avoid chained indexing; vectorize; profile memory.",
        mistakes="iterrows on large data, ignoring dtypes, unnecessary copies.",
        basic_syntax="import pandas as pd\ndf = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})",
        structure="load -> clean -> transform -> aggregate -> export",
        pattern="import pandas as pd\ndf = pd.DataFrame({'g': ['a'], 'v': [1]})\nprint(df.groupby('g')['v'].sum())",
        beginner="import pandas as pd\ndf = pd.DataFrame({'price': [10, 20]})\nprint(df['price'].sum())",
        intermediate=dedent("""\
            import pandas as pd

            df = pd.DataFrame({'region': ['US', 'US', 'EU'], 'revenue': [100, 150, 80]})
            summary = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
            print(summary.to_dict())"""),
        advanced=dedent("""\
            import pandas as pd

            def active_sku_counts(chunks):
                parts = []
                for chunk in chunks:
                    parts.append(chunk[chunk['status'] == 'active'].groupby('sku').size())
                return pd.concat(parts).groupby(level=0).sum()


            chunks = [pd.DataFrame({'sku': ['A', 'A'], 'status': ['active', 'inactive']})]
            print(active_sku_counts(chunks).to_dict())"""),
        mermaid="flowchart TD\n    A[Raw CSV] --> B[DataFrame]\n    B --> C[Transform]\n    C --> D[Export/Model]",
    )

    p(
        "NumPy",
        what="NumPy provides fast n-dimensional arrays and vectorized numerical operations.",
        why="Vectorization underpins scientific Python and ML performance.",
        where="ML preprocessing, simulations, image arrays, linear algebra.",
        objectives=("Create and slice ndarrays.", "Apply ufuncs and broadcasting.", "Use linear algebra routines."),
        outcome="You perform numeric computation efficiently with NumPy.",
        industry=("ML research", "Quant", "Engineering sims", "Medical imaging"),
        concepts=(
            ("ndarray", "Homogeneous n-D array.", "import numpy as np\na = np.array([1, 2, 3])\nprint(a.dtype)"),
            ("vectorization", "Ops without Python loops.", "import numpy as np\nprint(np.array([1, 2]) + 10)"),
            ("broadcasting", "Align shapes for ops.", "import numpy as np\nprint(np.array([[1], [2]]) + np.array([10, 20]))"),
        ),
        concept="NumPy pushes loops into optimized C.",
        purpose="Fast numerical kernels in Python.",
        benefits="Speed, interop with ML stack, rich math API.",
        use_cases="Feature matrices, FFT, random sampling, grids.",
        best_practices="Avoid Python loops on large arrays; choose dtype consciously.",
        mistakes="Excessive memory from float64 defaults, mixing lists and arrays.",
        basic_syntax="import numpy as np\na = np.arange(6).reshape(2, 3)",
        structure="create array -> vectorized ops -> aggregate",
        pattern="result = np.where(mask, a, b)",
        beginner="import numpy as np\nprint(np.mean([1, 2, 3, 4]))",
        intermediate="import numpy as np\na = np.random.default_rng(0).normal(size=1000)\nprint(round(a.mean(), 3))",
        advanced=dedent("""\
            import numpy as np

            A = np.array([[1.0, 2.0], [3.0, 4.0]])
            b = np.array([1.0, 2.0])
            print(np.linalg.solve(A, b))"""),
        mermaid="flowchart LR\n    A[Python Lists] --> B[np.array]\n    B --> C[Vectorized Ops]",
    )

    p(
        "PySpark",
        what="PySpark distributes data processing across clusters using Spark's resilient datasets and DataFrames.",
        why="Single-machine pandas fails on terabyte-scale datasets.",
        where="Lakehouse ETL, log analytics, ML feature generation at scale.",
        objectives=("Understand RDD vs DataFrame API.", "Apply transforms lazily and actions.", "Tune partitions and shuffles."),
        outcome="You author distributed batch jobs with PySpark patterns.",
        industry=("Big data platforms", "Ad tech", "Telecom", "Finance risk"),
        concepts=(
            ("SparkSession", "Entry point to Spark.", "print('SparkSession'[:5])"),
            ("DataFrame", "Distributed table API.", "rows = [{'id': 1}, {'id': 2}]\nprint(len(rows))"),
            ("lazy eval", "Transformations build plan.", "plan = ['read', 'filter', 'groupBy']\nprint(plan[-1])"),
        ),
        concept="Spark executes DAGs in parallel across executors.",
        purpose="Scale Python data processing horizontally.",
        benefits="Fault tolerance, SQL interface, ecosystem integration.",
        use_cases="Nightly aggregates, log parsing, large joins.",
        best_practices="Avoid collect on big data; cache hot datasets; control skew.",
        mistakes="Too many shuffles, tiny files, UDFs everywhere instead of built-ins.",
        basic_syntax="df = spark.read.parquet('s3://bucket/path')",
        structure="read -> transform -> cache/persist -> action",
        pattern="steps = ['read', 'filter', 'groupBy', 'write']\nprint('->'.join(steps))",
        beginner="records = [{'country': 'US', 'v': 1}, {'country': 'EU', 'v': 2}]\nprint(sum(r['v'] for r in records))",
        intermediate=dedent("""\
            from collections import defaultdict

            def group_sum(rows, key):
                totals = defaultdict(int)
                for row in rows:
                    totals[row[key]] += row['value']
                return dict(totals)


            data = [{'region': 'US', 'value': 10}, {'region': 'US', 'value': 5}]
            print(group_sum(data, 'region'))"""),
        advanced=dedent("""\
            def explain_plan(steps):
                return ' -> '.join(steps)


            print(explain_plan(['scan', 'filter', 'project', 'aggregate']))"""),
        mermaid="flowchart LR\n    A[Driver] --> B[Executors]\n    B --> C[Partitions]\n    C --> D[Results]",
    )

    p(
        "Machine Learning",
        what="Machine learning trains models to make predictions from data without explicit rules.",
        why="Predictive models automate decisions in ranking, fraud, and forecasting.",
        where="Recommendations, credit risk, demand forecast, churn prediction.",
        objectives=("Split train/test data.", "Train baseline models with scikit-learn.", "Evaluate with proper metrics."),
        outcome="You build and evaluate supervised learning baselines.",
        industry=("E-commerce", "Fintech", "Healthcare analytics", "Marketing"),
        concepts=(
            ("Features/labels", "X and y for supervised learning.", "X = [[1], [2]]\ny = [0, 1]\nprint(len(X) == len(y))"),
            ("train/test split", "Holdout evaluation.", "data = list(range(10))\ntrain, test = data[:8], data[8:]\nprint(len(test))"),
            ("metrics", "Measure performance.", "def accuracy(y_true, y_pred):\n    return sum(a == b for a, b in zip(y_true, y_pred)) / len(y_true)\nprint(accuracy([1, 0], [1, 0]))"),
        ),
        concept="ML generalizes patterns from data to unseen examples.",
        purpose="Automate prediction and classification.",
        benefits="Handles complex patterns, improves with data.",
        use_cases="Spam detection, pricing, recommendations.",
        best_practices="Cross-validation; feature scaling; address leakage; track experiments.",
        mistakes="Testing on training data, ignoring class imbalance, no baseline.",
        basic_syntax="model.fit(X_train, y_train)\npreds = model.predict(X_test)",
        structure="prepare -> train -> evaluate -> deploy",
        pattern="Pipeline([('scale', scaler), ('clf', model)])",
        beginner="xs = [1, 2, 3]\nys = [2, 4, 6]\nprint(all(y == x * 2 for x, y in zip(xs, ys)))",
        intermediate=dedent("""\
            from statistics import mean

            def mse(y_true, y_pred):
                return mean((a - b) ** 2 for a, b in zip(y_true, y_pred))


            print(round(mse([1.0, 2.0], [1.1, 1.9]), 3))"""),
        advanced=dedent("""\
            def kfold_indices(n, k=3):
                fold_size = n // k
                for i in range(k):
                    start = i * fold_size
                    end = (i + 1) * fold_size if i < k - 1 else n
                    val_idx = list(range(start, end))
                    train_idx = [j for j in range(n) if j not in val_idx]
                    yield train_idx, val_idx


            print(next(kfold_indices(9))[0][:3])"""),
        mermaid="flowchart LR\n    A[Data] --> B[Train]\n    B --> C[Model]\n    C --> D[Evaluate]",
    )

    p(
        "Deep Learning",
        what="Deep learning uses neural networks with many layers to learn hierarchical representations.",
        why="It achieves state-of-the-art results in vision, speech, and language tasks.",
        where="Computer vision, NLP, speech, generative AI, recommender systems.",
        objectives=("Understand tensors, layers, and loss functions.", "Train with PyTorch or TensorFlow basics.", "Monitor overfitting with validation."),
        outcome="You train simple neural networks and interpret training loops.",
        industry=("AI products", "Autonomous systems", "Media", "Healthcare imaging"),
        concepts=(
            ("Tensor", "Multi-dimensional array for DL.", "import numpy as np\nx = np.zeros((2, 3))\nprint(x.shape)"),
            ("Layer", "Learnable transformation.", "weights = [0.5, -0.2]\nprint(len(weights))"),
            ("Loss", "Objective to minimize.", "def mse(y, y_hat):\n    return ((y - y_hat) ** 2).mean()\nimport numpy as np\nprint(float(mse(np.array([1.0]), np.array([0.5]))))"),
        ),
        concept="Networks compose nonlinear layers trained by gradient descent.",
        purpose="Learn complex patterns from raw or engineered features.",
        benefits="Automatic feature learning, SOTA on many tasks.",
        use_cases="Image classifiers, translators, voice assistants.",
        best_practices="Normalize inputs; early stopping; reproducible seeds; GPU when needed.",
        mistakes="No validation, wrong loss for task, exploding gradients unhandled.",
        basic_syntax="for epoch in range(epochs):\n    loss = train_step(batch)\n    val_loss = eval_step(val_batch)",
        structure="data -> model -> loss -> optimizer step -> evaluate",
        pattern="logits = model(x); loss = criterion(logits, y)",
        beginner="import math\nprint(round(math.tanh(0.5), 3))",
        intermediate=dedent("""\
            import numpy as np

            def sigmoid(x):
                return 1 / (1 + np.exp(-x))

            def forward(x, w, b):
                return sigmoid(x * w + b)

            print(round(float(forward(1.0, 0.5, 0.0)), 3))"""),
        advanced=dedent("""\
            import numpy as np

            def train_step(w, x, y, lr=0.1):
                pred = w * x
                loss = (pred - y) ** 2
                grad = 2 * (pred - y) * x
                w -= lr * grad
                return w, float(loss)


            w = 0.0
            for _ in range(5):
                w, loss = train_step(w, 2.0, 6.0)
            print(round(w, 3))"""),
        mermaid="flowchart LR\n    A[Batch] --> B[Forward]\n    B --> C[Loss]\n    C --> D[Backward/Update]",
    )

    p(
        "NLP",
        what="Natural Language Processing analyzes and generates human language text.",
        why="Text dominates business communication, support, and web content.",
        where="Chatbots, search, sentiment, translation, document classification.",
        objectives=("Tokenize and normalize text.", "Build bag-of-words or embedding features.", "Evaluate NLP classifiers."),
        outcome="You preprocess text and train baseline NLP models.",
        industry=("Customer support", "Legal tech", "Social analytics", "Edtech"),
        concepts=(
            ("Tokenization", "Split text into tokens.", "text = 'Hello world'\nprint(text.lower().split())"),
            ("Stop words", "Filter common tokens.", "stop = {'the', 'a'}\ntokens = ['the', 'cat']\nprint([t for t in tokens if t not in stop])"),
            ("Embeddings", "Dense word vectors.", "vec = {'python': [0.1, 0.2]}\nprint(len(vec['python']))"),
        ),
        concept="NLP pipelines turn raw text into numeric features.",
        purpose="Extract meaning and structure from language.",
        benefits="Automation of text-heavy workflows.",
        use_cases="Ticket routing, spam filters, entity extraction.",
        best_practices="Handle unicode; domain-specific tokenization; evaluate per class.",
        mistakes="Naive stemming for all languages, train/test leakage via duplicates.",
        basic_syntax="tokens = text.lower().split()\nfeatures = Counter(tokens)",
        structure="normalize -> tokenize -> featurize -> model",
        pattern="clean(text) -> vectorize -> clf.predict",
        beginner="review = 'I love this product'\nprint('love' in review)",
        intermediate=dedent("""\
            from collections import Counter

            def bow(tokens):
                return Counter(tokens)


            print(bow(['python', 'is', 'fun', 'python']))"""),
        advanced=dedent("""\
            import re

            def extract_mentions(text: str) -> list[str]:
                return re.findall(r'@([A-Za-z0-9_]+)', text)


            print(extract_mentions('hi @ada and @lin'))"""),
        mermaid="flowchart LR\n    A[Text] --> B[Preprocess]\n    B --> C[Features]\n    C --> D[Model]",
    )

    p(
        "Computer Vision",
        what="Computer vision interprets images and video for detection, classification, and segmentation.",
        why="Visual data powers quality inspection, medical imaging, and AR.",
        where="Manufacturing QA, radiology assist, autonomous vehicles, retail analytics.",
        objectives=("Load and preprocess image tensors.", "Understand CNN basics.", "Evaluate vision model metrics."),
        outcome="You run baseline image classification workflows.",
        industry=("Manufacturing", "Healthcare", "Retail", "Security video"),
        concepts=(
            ("Image tensor", "HWC or CHW arrays.", "import numpy as np\nimg = np.zeros((64, 64, 3), dtype=np.uint8)\nprint(img.shape)"),
            ("CNN", "Convolution + pooling layers.", "kernel = [[1, 0], [0, 1]]\nprint(kernel[0][0])"),
            ("Augmentation", "Random transforms for robustness.", "import random\nprint(random.choice(['flip', 'rotate']))"),
        ),
        concept="Conv nets learn spatial hierarchies of visual features.",
        purpose="Automate visual understanding tasks.",
        benefits="Scale beyond manual inspection.",
        use_cases="Defect detection, OCR assist, face blur for privacy.",
        best_practices="Match preprocessing to pretrained models; monitor drift.",
        mistakes="Wrong normalization, label leakage, ignoring class imbalance.",
        basic_syntax="image = load_rgb(path)\ntensor = preprocess(image)",
        structure="load -> augment -> batch -> model -> metrics",
        pattern="transforms.Compose([Resize, ToTensor, Normalize])",
        beginner="import numpy as np\nimg = np.array([[0, 255], [128, 64]], dtype=np.uint8)\nprint(img.mean())",
        intermediate=dedent("""\
            import numpy as np

            def normalize_image(img: np.ndarray) -> np.ndarray:
                return (img.astype('float32') / 255.0)


            arr = np.array([0, 128, 255], dtype=np.uint8)
            print(normalize_image(arr).round(2))"""),
        advanced=dedent("""\
            import numpy as np

            def conv1d(signal, kernel):
                out = []
                k = len(kernel)
                for i in range(len(signal) - k + 1):
                    window = signal[i:i + k]
                    out.append(float(np.dot(window, kernel)))
                return out


            print(conv1d([1, 2, 3, 4], [1, 0.5]))"""),
        mermaid="flowchart LR\n    A[Image] --> B[Preprocess]\n    B --> C[CNN]\n    C --> D[Prediction]",
    )

    p(
        "FastAPI",
        what="FastAPI is a modern, high-performance web framework for building APIs with Python type hints.",
        why="It combines speed, automatic OpenAPI docs, and async support.",
        where="Microservices, ML model serving, internal tools, SaaS backends.",
        objectives=("Build REST endpoints.", "Use Pydantic models for validation.", "Deploy with Uvicorn/Gunicorn."),
        outcome="You ship production-ready async APIs quickly.",
        industry=("AI inference APIs", "Fintech", "Health tech", "Startups"),
        concepts=(
            ("Path operations", "Functions mapped to HTTP routes.", "ROUTES = {'GET /health': lambda: {'status': 'ok'}}\nprint(ROUTES['GET /health']())"),
            ("Pydantic models", "Validation and serialization.", "from dataclasses import dataclass\n@dataclass\nclass Item:\n    name: str\n    price: float\nprint(Item('a', 1.0))"),
            ("Dependency injection", "Reusable components.", "def get_db():\n    return {'connected': True}\nprint(get_db()['connected'])"),
        ),
        concept="FastAPI = Starlette + Pydantic + type hints.",
        purpose="Build typed, documented APIs with minimal boilerplate.",
        benefits="Auto docs, validation, async, great DX.",
        use_cases="CRUD APIs, webhooks, ML serving, gateways.",
        best_practices="Use routers; env-based config; structured logging.",
        mistakes="Blocking I/O in async routes, skipping auth, no tests.",
        basic_syntax=dedent("""\
            from dataclasses import dataclass

            @dataclass
            class Health:
                status: str = 'ok'


            print(Health().status)"""),
        structure="app -> routes -> schemas -> dependencies -> startup",
        pattern=dedent("""\
            def handle(route, service):
                return service(route)


            print(handle('/health', lambda r: {'status': 'ok'}))"""),
        beginner="def health():\n    return {'status': 'ok'}\nprint(health())",
        intermediate=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class CreateUser:
                email: str


            def create_user(payload: CreateUser):
                return {'email': payload.email}


            print(create_user(CreateUser(email='a@b.com')))"""),
        advanced=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class User:
                id: int
                email: str


            def get_current_user(token: str) -> User | None:
                return User(1, 'a@b.com') if token else None


            user = get_current_user('token')
            print(user.email if user else 'anonymous')"""),
        mermaid="flowchart LR\n    A[Client] --> B[FastAPI]\n    B --> C[Validation]\n    C --> D[Service]",
    )

    p(
        "Django",
        what="Django is a batteries-included web framework for rapid secure web development.",
        why="It provides ORM, admin, auth, and routing out of the box.",
        where="Content sites, admin-heavy apps, MVPs, internal portals.",
        objectives=("Create projects, apps, models, and views.", "Use Django ORM and migrations.", "Configure URLs and templates."),
        outcome="You build full-stack web apps with Django conventions.",
        industry=("News sites", "SaaS admin", "Education portals", "Marketplaces"),
        concepts=(
            ("MTV", "Model-Template-View pattern.", "MODEL = {'fields': ['title']}\nprint(MODEL['fields'])"),
            ("ORM", "Database abstraction.", "class Row:\n    def __init__(self, title):\n        self.title = title\nprint(Row('hi').title)"),
            ("Admin", "Auto CRUD UI.", "ADMIN = {'register': True}\nprint(ADMIN['register'])"),
        ),
        concept="Django favors convention and integrated components.",
        purpose="Ship secure web apps quickly.",
        benefits="Mature ecosystem, built-in auth/admin, ORM.",
        use_cases="CMS, membership sites, internal tools.",
        best_practices="Use CBVs/FBVs appropriately; split settings per env; cache queries.",
        mistakes="Fat views, N+1 queries, raw SQL without need.",
        basic_syntax="urlpatterns = [path('health/', health_view)]",
        structure="project -> apps -> models -> views -> urls",
        pattern="Model -> Serializer/Form -> View -> Template/JSON",
        beginner="def hello(request):\n    return {'message': 'hi'}",
        intermediate=dedent("""\
            class Article:
                objects = [{'title': 'Hello', 'published': True}]

                @classmethod
                def published(cls):
                    return [a for a in cls.objects if a['published']]


            print(Article.published()[0]['title'])"""),
        advanced=dedent("""\
            class QuerySet:
                def __init__(self, rows):
                    self.rows = rows

                def filter(self, **kwargs):
                    return QuerySet([r for r in self.rows if all(r.get(k) == v for k, v in kwargs.items())])


            qs = QuerySet([{'active': True, 'id': 1}, {'active': False, 'id': 2}])
            print(qs.filter(active=True).rows[0]['id'])"""),
        mermaid="flowchart LR\n    A[Request] --> B[URLConf]\n    B --> C[View]\n    C --> D[Model/Template]",
    )

    p(
        "Flask",
        what="Flask is a lightweight WSGI microframework for web apps and APIs.",
        why="Minimal core plus extensions fits small services and prototypes.",
        where="Micro APIs, webhooks, prototypes, embedded admin UIs.",
        objectives=("Define routes and request handlers.", "Use Jinja templates and blueprints.", "Structure apps with application factory."),
        outcome="You build small web services with Flask patterns.",
        industry=("Startups", "Internal tools", "IoT dashboards", "Hackathons"),
        concepts=(
            ("app.route", "Map URL to view.", "ROUTES = {}\ndef route(path):\n    def deco(fn):\n        ROUTES[path] = fn\n        return fn\n    return deco\n@route('/')\ndef index():\n    return 'ok'\nprint(ROUTES['/']())"),
            ("request", "HTTP request context.", "class Req:\n    args = {'q': 'flask'}\nprint(Req.args['q'])"),
            ("Blueprint", "Modular routes.", "BP = {'name': 'api'}\nprint(BP['name'])"),
        ),
        concept="Flask core stays small; extensions add ORM, auth, etc.",
        purpose="Quick HTTP services with flexibility.",
        benefits="Simple learning curve, huge extension ecosystem.",
        use_cases="Webhooks, minimal APIs, prototypes.",
        best_practices="Application factory; blueprints; config objects; g for request scope.",
        mistakes="Single-file mega app, debug in prod, global mutable state.",
        basic_syntax="app = Flask(__name__)\n@app.get('/health')\ndef health(): return {'ok': True}",
        structure="app factory -> blueprints -> views -> templates",
        pattern="register_blueprint(api_bp, url_prefix='/api')",
        beginner="def health():\n    return {'status': 'ok'}\nprint(health())",
        intermediate=dedent("""\
            class Flask:
                def __init__(self):
                    self.routes = {}

                def route(self, path):
                    def decorator(fn):
                        self.routes[path] = fn
                        return fn
                    return decorator


            app = Flask()

            @app.route('/hello')
            def hello():
                return 'hello'


            print(app.routes['/hello']())"""),
        advanced=dedent("""\
            class Blueprint:
                def __init__(self, name: str):
                    self.name = name
                    self.routes = {}

                def route(self, path):
                    def decorator(fn):
                        self.routes[path] = fn
                        return fn
                    return decorator


            api = Blueprint('api')

            @api.route('/items')
            def items():
                return ['item']


            print(api.routes['/items']())"""),
        mermaid="flowchart LR\n    A[Request] --> B[Flask Router]\n    B --> C[View]\n    C --> D[Response]",
    )

    p(
        "Microservices",
        what="Microservices decompose applications into independently deployable services.",
        why="Teams scale delivery and isolate failures per bounded context.",
        where="Cloud-native SaaS, large product engineering orgs, platform teams.",
        objectives=("Define service boundaries.", "Communicate via HTTP/events.", "Implement observability and versioning."),
        outcome="You design service-oriented architectures with Python services.",
        industry=("Streaming platforms", "Fintech", "E-commerce", "Enterprise SaaS"),
        concepts=(
            ("Bounded context", "Service owns its domain.", "SERVICES = {'billing': ['invoices'], 'users': ['profiles']}\nprint(SERVICES['billing'])"),
            ("API gateway", "Single entry routing.", "GATEWAY = {'/users': 'user-svc'}\nprint(GATEWAY['/users'])"),
            ("Event bus", "Async integration.", "EVENTS = []\nEVENTS.append({'type': 'OrderCreated'})\nprint(EVENTS[0]['type'])"),
        ),
        concept="Microservices trade monolith simplicity for independent deployment.",
        purpose="Scale teams and components separately.",
        benefits="Isolation, tech diversity, targeted scaling.",
        use_cases="Checkout, notifications, search, recommendations.",
        best_practices="Contract tests; idempotent consumers; distributed tracing.",
        mistakes="Distributed monolith, chatty sync calls, no versioning.",
        basic_syntax="# service exposes /health and domain routes",
        structure="gateway -> services -> databases per service",
        pattern="publish OrderCreated -> inventory service consumes",
        beginner="services = ['users', 'orders']\nprint(len(services))",
        intermediate=dedent("""\
            def call_service(registry, name, path):
                base = registry[name]
                return f'{base}{path}'


            registry = {'users': 'http://users:8000'}
            print(call_service(registry, 'users', '/1'))"""),
        advanced=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class ServiceHealth:
                name: str
                ok: bool


            def aggregate_health(checks: list[ServiceHealth]) -> bool:
                return all(h.ok for h in checks)


            print(aggregate_health([ServiceHealth('a', True), ServiceHealth('b', True)]))"""),
        mermaid="flowchart LR\n    A[Gateway] --> B[Service A]\n    A --> C[Service B]\n    B --> D[DB A]\n    C --> E[DB B]",
    )

    p(
        "Docker with Python",
        what="Docker packages Python apps with dependencies into portable containers.",
        why="Containers reproduce dev/prod environments and simplify deployment.",
        where="CI/CD, Kubernetes, cloud run, local dev stacks.",
        objectives=("Write Dockerfiles for Python apps.", "Use multi-stage builds.", "Run with docker compose for dependencies."),
        outcome="You containerize Python services production-ready.",
        industry=("Cloud-native teams", "ML ops", "Consultancies", "Startups"),
        concepts=(
            ("Dockerfile", "Image build recipe.", "print('FROM python:3.12-slim'[:4])"),
            ("WORKDIR", "Set container working dir.", "WORKDIR = '/app'\nprint(WORKDIR)"),
            ("ENTRYPOINT", "Container start command.", "CMD = ['python', 'app.py']\nprint(CMD[0])"),
        ),
        concept="Images are immutable layers; containers are running instances.",
        purpose="Consistent runtime from laptop to cloud.",
        benefits="Isolation, reproducibility, fast rollouts.",
        use_cases="API containers, workers, notebooks batch jobs.",
        best_practices="Pin base image; non-root user; .dockerignore; healthcheck.",
        mistakes="Huge images, secrets in layers, running as root, no pin requirements.",
        basic_syntax="dockerfile = 'FROM python:3.12-slim\\nCOPY requirements.txt .'\nprint(dockerfile.split()[0])",
        structure="base image -> deps -> copy app -> cmd",
        pattern="stages = ['builder', 'runtime']\nprint(stages)",
        beginner="print('docker build -t myapp .')",
        intermediate=dedent("""\
            dockerfile = '''FROM python:3.12-slim
            WORKDIR /app
            COPY requirements.txt .
            RUN pip install --no-cache-dir -r requirements.txt
            COPY . .
            CMD [\"python\", \"-m\", \"http.server\", \"8000\"]
            '''
            print('WORKDIR' in dockerfile)"""),
        advanced=dedent("""\
            stages = ['builder', 'runtime']
            print(stages.index('runtime'))"""),
        mermaid="flowchart LR\n    A[Dockerfile] --> B[Image]\n    B --> C[Container]\n    C --> D[Registry/K8s]",
    )

    p(
        "Kubernetes Integration",
        what="Kubernetes orchestrates containers for scaling, networking, and self-healing deployments.",
        why="Production services need automated rollout, health checks, and service discovery.",
        where="Cloud platforms, platform engineering, microservice fleets.",
        objectives=("Write Deployments and Services manifests.", "Configure probes and resource limits.", "Use ConfigMaps and Secrets."),
        outcome="You deploy Python apps to Kubernetes clusters.",
        industry=("SaaS platforms", "FinTech cloud", "Media streaming", "ML serving"),
        concepts=(
            ("Pod", "Smallest deploy unit.", "pod = {'name': 'api', 'containers': ['app']}\nprint(pod['containers'])"),
            ("Deployment", "Manages replica sets.", "spec = {'replicas': 3}\nprint(spec['replicas'])"),
            ("Service", "Stable network endpoint.", "svc = {'type': 'ClusterIP', 'port': 80}\nprint(svc['port'])"),
        ),
        concept="Kubernetes desired state reconciles actual cluster state.",
        purpose="Run containers reliably at scale.",
        benefits="Self-healing, scaling, rolling updates.",
        use_cases="API fleets, workers, cron jobs.",
        best_practices="Liveness/readiness probes; limits/requests; 12-factor config.",
        mistakes="No probes, OOM kills, latest tag in prod, huge ConfigMaps.",
        basic_syntax="command = ['kubectl', 'apply', '-f', 'deployment.yaml']\nprint(command[0])",
        structure="Deployment -> Service -> Ingress -> HPA",
        pattern="config = {'envFrom': 'configMap', 'mountSecrets': True}\nprint(config['envFrom'])",
        beginner="manifest = {'kind': 'Deployment', 'replicas': 1}\nprint(manifest['kind'])",
        intermediate=dedent("""\
            deployment = {
                'spec': {
                    'template': {
                        'spec': {
                            'containers': [{
                                'name': 'api',
                                'readinessProbe': {'httpGet': {'path': '/health', 'port': 8000}},
                            }]
                        }
                    }
                }
            }
            probe = deployment['spec']['template']['spec']['containers'][0]['readinessProbe']
            print(probe['httpGet']['path'])"""),
        advanced=dedent("""\
            def rolling_update(current: int, desired: int, max_surge: int) -> int:
                return min(current + max_surge, desired)


            print(rolling_update(2, 5, 1))"""),
        mermaid="flowchart LR\n    A[Deployment] --> B[Pods]\n    B --> C[Service]\n    C --> D[Ingress]",
    )

    p(
        "Cloud Development",
        what="Cloud development builds apps leveraging managed services for compute, storage, and messaging.",
        why="Cloud offloads ops for scaling, durability, and global reach.",
        where="SaaS, data platforms, mobile backends, ML inference.",
        objectives=("Use object storage and managed databases.", "Apply IAM least privilege.", "Design for multi-region resilience."),
        outcome="You architect cloud-native Python solutions.",
        industry=("Global SaaS", "Media", "Gaming backends", "Enterprise migration"),
        concepts=(
            ("Managed services", "Offload ops to provider.", "SERVICES = ['object-storage', 'queue', 'db']\nprint(len(SERVICES))"),
            ("IAM", "Identity and access control.", "policy = {'allow': ['s3:GetObject']}\nprint(policy['allow'][0])"),
            ("Object storage", "Durable blob store.", "uri = 's3://bucket/key'\nprint(uri.startswith('s3://'))"),
        ),
        concept="Cloud-native apps use managed APIs instead of self-hosted servers.",
        purpose="Scale without owning data centers.",
        benefits="Elasticity, global CDN, managed backups.",
        use_cases="Static assets, backups, event archives, ML datasets.",
        best_practices="Infrastructure as code; secrets manager; cost tags; observability.",
        mistakes="Long-lived access keys in code, public buckets, no autoscaling.",
        basic_syntax="client.upload_file('local.txt', 'bucket', 'key')",
        structure="app -> SDK -> managed API -> cloud resource",
        pattern="upload artifact -> trigger lambda/worker",
        beginner="bucket = 'my-app-assets'\nprint(bucket.replace('-', '_'))",
        intermediate=dedent("""\
            def presigned_url(bucket: str, key: str, ttl: int = 3600) -> str:
                return f'https://{bucket}.example.com/{key}?ttl={ttl}'


            print('ttl=' in presigned_url('b', 'file.csv'))"""),
        advanced=dedent("""\
            def multi_region_failover(primary_ok: bool, secondary_ok: bool) -> str:
                if primary_ok:
                    return 'primary'
                if secondary_ok:
                    return 'secondary'
                raise RuntimeError('all regions down')


            print(multi_region_failover(True, False))"""),
        mermaid="flowchart LR\n    A[Python App] --> B[Cloud SDK]\n    B --> C[Managed Services]",
    )

    p(
        "AWS with Python",
        what="AWS with Python uses boto3 to interact with S3, Lambda, DynamoDB, SQS, and more.",
        why="AWS dominates enterprise cloud; automation requires SDK fluency.",
        where="Serverless APIs, data lakes, batch ETL, infra automation.",
        objectives=("Configure boto3 clients and resources.", "Upload/download S3 objects.", "Invoke Lambda and publish to SQS."),
        outcome="You automate AWS resources from Python with boto3 patterns.",
        industry=("Enterprise cloud", "Startups on AWS", "Media storage", "Fintech"),
        concepts=(
            ("boto3 client", "Low-level service client.", "print('boto3'[:4])"),
            ("S3", "Object storage.", "key = 's3://bucket/path'\nprint(key.split('/')[2])"),
            ("Lambda handler", "Function entrypoint.", "def handler(event, context):\n    return {'statusCode': 200, 'body': 'ok'}\nprint(handler({}, None)['statusCode'])"),
        ),
        concept="boto3 wraps AWS HTTP APIs with Python methods.",
        purpose="Programmatic cloud infrastructure and data access.",
        benefits="Full AWS surface, IAM integration, mature docs.",
        use_cases="Backup scripts, ETL triggers, infra provisioning.",
        best_practices="Use IAM roles not keys; paginate list calls; retries with backoff.",
        mistakes="Hard-coded credentials, overly broad IAM, no region set.",
        basic_syntax="import boto3\ns3 = boto3.client('s3')",
        structure="session -> client -> API call -> handle pagination",
        pattern="s3.upload_file(local, bucket, key)",
        beginner="def lambda_handler(event, context):\n    return {'statusCode': 200}\nprint(lambda_handler({}, None))",
        intermediate=dedent("""\
            def s3_uri(bucket: str, key: str) -> str:
                return f's3://{bucket}/{key}'


            print(s3_uri('logs', '2026/06/app.log'))"""),
        advanced=dedent("""\
            def paginate(items, page_size=2):
                for i in range(0, len(items), page_size):
                    yield items[i:i + page_size]


            print(list(paginate(list(range(5)), 2)))"""),
        mermaid="flowchart LR\n    A[boto3] --> B[AWS API]\n    B --> C[S3/Lambda/SQS]",
    )

    p(
        "Azure with Python",
        what="Azure with Python uses azure-sdk-for-python to manage storage, functions, and cloud resources.",
        why="Enterprises on Microsoft cloud need Python automation and app integration.",
        where="Azure Functions, Blob Storage, Cosmos DB, enterprise integrations.",
        objectives=("Authenticate with DefaultAzureCredential.", "Use Blob SDK for uploads.", "Deploy Python functions to Azure."),
        outcome="You integrate Python workloads with Azure services.",
        industry=("Enterprise IT", "Healthcare on Azure", "Government", "Hybrid cloud"),
        concepts=(
            ("Blob storage", "Object storage on Azure.", "uri = 'https://account.blob.core.windows.net/container/blob'\nprint('blob' in uri)"),
            ("DefaultAzureCredential", "Unified auth chain.", "print('credential chain pattern')"),
            ("Function app", "Serverless Python host.", "def main(req):\n    return {'status': 200}\nprint(main({})['status'])"),
        ),
        concept="Azure SDK mirrors AWS patterns with Azure-specific services.",
        purpose="Build and automate on Microsoft cloud.",
        benefits="Active Directory integration, hybrid tooling.",
        use_cases="Blob ETL, enterprise SSO apps, IoT hub ingestion.",
        best_practices="Managed identity; key vault secrets; monitor with App Insights.",
        mistakes="Connection strings in git, wrong subscription context.",
        basic_syntax="from azure.storage.blob import BlobServiceClient",
        structure="credential -> client -> operation -> retry policy",
        pattern="BlobServiceClient.from_connection_string(conn)",
        beginner="account = 'myaccount'\nprint(f'https://{account}.blob.core.windows.net')",
        intermediate=dedent("""\
            def blob_path(container: str, name: str) -> str:
                return f'{container}/{name}'


            print(blob_path('logs', 'app.log'))"""),
        advanced=dedent("""\
            class RetryPolicy:
                def __init__(self, retries=3):
                    self.retries = retries

                def run(self, func):
                    last = None
                    for _ in range(self.retries):
                        try:
                            return func()
                        except Exception as exc:
                            last = exc
                    raise last


            print(RetryPolicy().run(lambda: 'ok'))"""),
        mermaid="flowchart LR\n    A[Python SDK] --> B[Azure API]\n    B --> C[Blob/Functions/Cosmos]",
    )

    p(
        "GCP with Python",
        what="GCP with Python uses google-cloud libraries for Storage, BigQuery, Pub/Sub, and Cloud Run.",
        why="Google Cloud excels at data analytics and Kubernetes (GKE).",
        where="Analytics pipelines, ML on GCP, Pub/Sub event systems, Cloud Run APIs.",
        objectives=("Authenticate with service accounts.", "Query BigQuery from Python.", "Publish/consume Pub/Sub messages."),
        outcome="You build data and event-driven apps on GCP.",
        industry=("Ad tech", "Analytics", "ML platforms", "Mobile backends"),
        concepts=(
            ("BigQuery", "Warehouse SQL engine.", "sql = 'SELECT 1 AS one'\nprint(sql.split()[0])"),
            ("GCS", "Google Cloud Storage.", "uri = 'gs://bucket/object'\nprint(uri.startswith('gs://'))"),
            ("Pub/Sub", "Messaging service.", "topic = 'projects/p/topics/t'\nprint(topic.split('/')[-1])"),
        ),
        concept="GCP client libraries wrap REST/gRPC service APIs.",
        purpose="Analytics and event-driven cloud apps.",
        benefits="BigQuery integration, strong data tooling, GKE.",
        use_cases="Log sinks to BQ, model batch scoring, async workers.",
        best_practices="Workload identity; IAM roles; partition BigQuery tables.",
        mistakes="Public buckets, streaming inserts without dedupe keys.",
        basic_syntax="from google.cloud import storage\nclient = storage.Client()",
        structure="client -> API -> handle pages -> monitor quotas",
        pattern="bq_client.query(sql).result()",
        beginner="print('gs://my-bucket/data.csv'.split('/')[2])",
        intermediate=dedent("""\
            def pubsub_message(data: bytes, attrs: dict | None = None) -> dict:
                return {'data': data.decode(), 'attributes': attrs or {}}


            print(pubsub_message(b'hello', {'type': 'event'}))"""),
        advanced=dedent("""\
            def bigquery_job_state(done: bool, errors: list | None = None) -> str:
                if errors:
                    return 'FAILED'
                return 'DONE' if done else 'RUNNING'


            print(bigquery_job_state(True))"""),
        mermaid="flowchart LR\n    A[Python Client] --> B[GCP API]\n    B --> C[BigQuery/GCS/PubSub]",
    )

    p(
        "DevOps Automation",
        what="DevOps automation uses Python to script infrastructure, deployments, and operational tasks.",
        why="Repeatable automation reduces human error and accelerates releases.",
        where="SRE teams, platform engineering, release management, cloud ops.",
        objectives=("Automate provisioning and config with scripts.", "Integrate with APIs (GitHub, K8s, cloud).", "Add logging and dry-run modes."),
        outcome="You build reliable ops automation in Python.",
        industry=("Platform teams", "Managed services", "Game live ops", "Enterprise IT"),
        concepts=(
            ("Scripted workflow", "Codify runbooks.", "def deploy(version):\n    return f'deployed {version}'\nprint(deploy('1.2.3'))"),
            ("Idempotency", "Safe reruns.", "desired = {'replicas': 3}\ncurrent = {'replicas': 3}\nprint(desired == current)"),
            ("API automation", "Call control planes.", "import urllib.request\nprint(hasattr(urllib.request, 'urlopen'))"),
        ),
        concept="DevOps automation replaces manual clicks with tested code.",
        purpose="Reliable, auditable operations.",
        benefits="Speed, consistency, documentation via code.",
        use_cases="Scale services, rotate certs, cleanup resources.",
        best_practices="Dry-run flag; structured logs; secrets from vault; least privilege.",
        mistakes="No rollback plan, silent failures, running untested scripts prod-wide.",
        basic_syntax="if __name__ == '__main__':\n    run_playbook()",
        structure="parse args -> plan -> apply -> verify",
        pattern="for host in inventory: ssh_run(host, cmd)",
        beginner="def restart_service(name: str) -> str:\n    return f'restarted {name}'\nprint(restart_service('api'))",
        intermediate=dedent("""\
            def ensure_replicas(current: int, desired: int) -> int:
                if current < desired:
                    return current + 1
                if current > desired:
                    return current - 1
                return current


            print(ensure_replicas(2, 3))"""),
        advanced=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class ChangeRecord:
                action: str
                target: str
                ok: bool


            def audit(changes: list[ChangeRecord]) -> list[ChangeRecord]:
                return [c for c in changes if not c.ok]


            print(audit([ChangeRecord('scale', 'api', True)]))"""),
        mermaid="flowchart LR\n    A[Trigger] --> B[Automation Script]\n    B --> C[API/SSH]\n    C --> D[Verify]",
    )

    p(
        "CI/CD Pipelines",
        what="CI/CD pipelines automatically test, build, and deploy code on each change.",
        why="Fast feedback and repeatable releases reduce production incidents.",
        where="GitHub Actions, GitLab CI, Jenkins, cloud deploy pipelines.",
        objectives=("Configure test/lint/build stages.", "Cache dependencies in CI.", "Promote artifacts through environments."),
        outcome="You implement Python CI/CD workflows with gates and artifacts.",
        industry=("Every software org", "Open source", "Regulated industries", "Mobile backends"),
        concepts=(
            ("CI", "Continuous integration tests.", "steps = ['checkout', 'test', 'lint']\nprint(steps.index('test'))"),
            ("CD", "Continuous delivery/deploy.", "envs = ['dev', 'staging', 'prod']\nprint(envs[-1])"),
            ("Artifacts", "Built wheels/images.", "artifact = 'dist/app-1.0.whl'\nprint(artifact.endswith('.whl'))"),
        ),
        concept="Pipelines encode quality gates before production.",
        purpose="Ship safely and frequently.",
        benefits="Automation, audit trail, faster MTTR.",
        use_cases="Run pytest on PR, build Docker on main, deploy to staging.",
        best_practices="Fail fast; pin actions; secrets in CI vault; matrix Python versions.",
        mistakes="No tests in CI, flaky pipelines ignored, deploying without migration plan.",
        basic_syntax="steps = ['pytest', 'python', '-m', 'build']\nprint(steps[0])",
        structure="trigger -> lint/test -> build -> deploy",
        pattern="on: pull_request -> jobs: test",
        beginner="pipeline = ['lint', 'test']\nprint('test' in pipeline)",
        intermediate=dedent("""\
            def should_deploy(branch: str, tests_passed: bool) -> bool:
                return branch == 'main' and tests_passed


            print(should_deploy('main', True))"""),
        advanced=dedent("""\
            def promotion_gate(metrics: dict) -> bool:
                return metrics.get('error_rate', 1) < 0.01 and metrics.get('p95_ms', 999) < 300


            print(promotion_gate({'error_rate': 0.001, 'p95_ms': 120}))"""),
        mermaid="flowchart LR\n    A[Git Push] --> B[CI Test]\n    B --> C[Build Artifact]\n    C --> D[Deploy]",
    )

    p(
        "Performance Optimization",
        what="Performance optimization improves latency, throughput, and resource usage of Python programs.",
        why="Slow software increases cost and hurts user experience at scale.",
        where="API hot paths, ETL, ML inference, high-QPS services.",
        objectives=("Profile with cProfile and py-spy.", "Apply algorithmic and vectorization wins.", "Use caching and async I/O appropriately."),
        outcome="You measure first and apply targeted optimizations.",
        industry=("Ad exchanges", "Search", "Fintech trading tools", "Streaming"),
        concepts=(
            ("Profiling", "Find hotspots.", "import cProfile\ncProfile.run('sum(range(1000))')"),
            ("Big-O", "Scale with input size.", "def linear(n):\n    return sum(range(n))\nprint(linear(10))"),
            ("Caching", "Memoize pure functions.", "from functools import lru_cache\n@lru_cache\ndef fib(n):\n    return n if n < 2 else fib(n-1)+fib(n-2)\nprint(fib(10))"),
        ),
        concept="Optimize bottlenecks proven by measurement.",
        purpose="Meet SLAs and reduce infrastructure cost.",
        benefits="Lower latency, higher throughput, happier users.",
        use_cases="API caching, batch tuning, NumPy vectorization.",
        best_practices="Benchmark before/after; load test; avoid premature optimization.",
        mistakes="Optimizing cold code, micro-opts over algorithms, no profiling.",
        basic_syntax=dedent("""\
            from functools import lru_cache


            @lru_cache(maxsize=1024)
            def expensive(n: int) -> int:
                return n * n


            print(expensive(3))"""),
        structure="profile -> hypothesize -> optimize -> verify",
        pattern="optimizations = ['cache', 'vectorize', 'async_io']\nprint(len(optimizations))",
        beginner="import time\nt0 = time.perf_counter()\nsum(range(100000))\nprint(time.perf_counter() - t0 < 1)",
        intermediate=dedent("""\
            from functools import lru_cache


            @lru_cache(maxsize=None)
            def slow(n: int) -> int:
                return sum(range(n))


            print(slow(1000) == slow(1000))"""),
        advanced=dedent("""\
            import cProfile
            import pstats
            from io import StringIO

            buf = StringIO()
            cProfile.run('sum(i*i for i in range(1000))', buf)
            stats = pstats.Stats(buf)
            print(stats.total_calls > 0)"""),
        mermaid="flowchart TD\n    A[Profile] --> B[Hotspot]\n    B --> C[Optimize]\n    C --> D[Benchmark]",
    )

    p(
        "System Design with Python",
        what="System design with Python plans scalable architectures using services, queues, caches, and databases.",
        why="Senior engineers must translate requirements into reliable large-scale designs.",
        where="Architecture reviews, interviews, greenfield platforms, rewrites.",
        objectives=("Estimate capacity and define APIs.", "Choose databases, caches, and queues.", "Plan observability and failure modes."),
        outcome="You draft end-to-end system designs implementable in Python stacks.",
        industry=("Big tech", "High-growth startups", "Consulting", "Platform engineering"),
        concepts=(
            ("Load balancing", "Distribute traffic.", "servers = ['a', 'b', 'b']\nprint(max(set(servers), key=servers.count))"),
            ("Caching", "Reduce read load.", "cache = {}\ndef get(key):\n    return cache.setdefault(key, 'value')\nprint(get('k'))"),
            ("Queue", "Async decouple.", "from collections import deque\nq = deque(['job'])\nprint(q.popleft())"),
        ),
        concept="Design balances latency, throughput, consistency, and cost.",
        purpose="Build systems that meet scale and reliability goals.",
        benefits="Clear roadmap, risk reduction, aligned teams.",
        use_cases="URL shortener, feed system, rate limiter, chat.",
        best_practices="Start simple; define SLIs/SLOs; design for failure; document tradeoffs.",
        mistakes="Over-engineering day one, single DB bottleneck, no monitoring plan.",
        basic_syntax="# API -> service -> cache/db -> async workers",
        structure="clients -> LB -> app tier -> data tier -> async workers",
        pattern=dedent("""\
            cache = {}
            def read(key):
                return cache.get(key, 'miss')


            print(read('user:1'))"""),
        beginner="components = ['api', 'db', 'cache']\nprint(len(components))",
        intermediate=dedent("""\
            class RateLimiter:
                def __init__(self, limit: int):
                    self.limit = limit
                    self.count = 0

                def allow(self) -> bool:
                    if self.count >= self.limit:
                        return False
                    self.count += 1
                    return True


            rl = RateLimiter(2)
            print(rl.allow(), rl.allow(), rl.allow())"""),
        advanced=dedent("""\
            from dataclasses import dataclass


            @dataclass
            class DesignDoc:
                service: str
                rps: int
                datastore: str
                notes: str


            doc = DesignDoc('url-shortener', rps=10_000, datastore='redis+dynamodb', notes='cache hot keys')
            print(doc.service, doc.rps)"""),
        mermaid="flowchart TD\n    A[Clients] --> B[Load Balancer]\n    B --> C[App Servers]\n    C --> D[Cache]\n    C --> E[Database]\n    C --> F[Queue Workers]",
    )
