"""Beginner topic snippets."""
from textwrap import dedent
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "snippet_parts"))
from _helpers import S

SNIPPETS = {
    'Introduction to Python': S(
        'Python is a high-level, interpreted language prized for readable syntax and a vast ecosystem.',
        'It powers web backends, data science, automation, AI, and DevOps with one of the largest communities.',
        'Startups, enterprises, research labs, fintech, healthcare analytics, and cloud platforms.',
        ("Explain Python's design philosophy and ecosystem.", 'Compare Python to other languages for common workloads.', 'Identify domains where Python excels.'),
        'You can explain why Python fits a project and where it belongs in a tech stack.',
        ('Web services', 'Data pipelines', 'ML platforms', 'Security automation'),
        (('Interpreted Execution', 'Source runs via the interpreter.', "print('Hello, Python!')"), ('Standard Library', 'Rich modules ship with Python.', "import json\nprint(json.dumps({'ok': True}))"), ('Dynamic Typing', 'Types determined at runtime.', "x = 10\nx = 'ten'\nprint(x)")),
        'Python is interpreted, dynamically typed, and multi-paradigm.',
        'Ship solutions quickly with readable code and strong libraries.',
        'Fast prototyping, huge community, cross-platform, excellent for teams.',
        'APIs, ETL, notebooks, scripting, AI/ML, test automation.',
        'Follow PEP 8, use virtual environments, prefer clarity over cleverness.',
        'Assuming Python is slow for every task, ignoring version pins, skipping tests.',
        'print("Hello, Python!")',
        dedent('''\
def main():
    print('Learning Python')

if __name__ == '__main__':
    main()
        '''),
        dedent('''\
import json
print(json.dumps({'status': 'ok'}))
        '''),
        'print("Python is fun!")',
        dedent('''\
domains = ['web', 'data', 'automation', 'ai']
for d in domains:
    print(f'Python powers {d}')
        '''),
        dedent('''\
from dataclasses import dataclass
@dataclass(frozen=True)
class LanguageProfile:
    name: str
    typing: str
print(LanguageProfile('Python', 'dynamic'))
        '''),
        dedent('''\
flowchart TD
    A[Write Code] --> B[Interpreter]
    B --> C[Output]
        '''),
    ),
    'Installing Python': S(
        'Installing Python means obtaining the interpreter, pip, and tooling on your system.',
        'Correct installs prevent version conflicts.',
        'Laptops, CI runners, Docker images, cloud VMs.',
        ('Install Python 3.x safely.', 'Verify python and pip.', 'Choose venv or pyenv.'),
        'You confirm a working Python environment from the shell.',
        ('Onboarding', 'CI images', 'Containers', 'Education'),
        (('Interpreter', 'Executes .py files.', 'import sys\nprint(sys.version_info.major >= 3)'), ('pip', 'Installs packages.', "import importlib.util\nprint(importlib.util.find_spec('pip') is not None)"), ('venv', 'Isolated envs.', "import venv\nprint(hasattr(venv, 'EnvBuilder'))")),
        'Install = interpreter + pip + tooling.',
        'Run Python reliably on any machine.',
        'Reproducible dev setups.',
        'Local dev, servers, notebooks.',
        'Pin versions, use venv.',
        'Global pip installs, PATH issues.',
        dedent('''\
import sys
print(sys.executable)
        '''),
        '# download -> install -> verify -> venv',
        dedent('''\
import sys
print(sys.version.split()[0])
        '''),
        dedent('''\
import platform
print(platform.python_version())
        '''),
        dedent('''\
import sys
print(sys.executable)
print(sys.version)
        '''),
        dedent('''\
import subprocess, sys
r=subprocess.run([sys.executable,'-m','pip','--version'],capture_output=True,text=True)
print(r.stdout.strip())
        '''),
        dedent('''\
flowchart LR
    A[Download]-->B[Install]-->C[Verify]-->D[venv]
        '''),
    ),
    'IDE Setup': S(
        'IDE setup configures editor, interpreter, linting, and debugging.',
        'Tooling catches errors early.',
        'VS Code, PyCharm, Neovim, cloud IDEs.',
        ('Pick a Python editor.', 'Attach venv interpreter.', 'Enable lint/format/debug.'),
        'You have a productive Python workspace.',
        ('Teams', 'Remote dev', 'Bootcamps', 'OSS'),
        (('Interpreter', 'Points to venv Python.', 'import sys\nprint(sys.executable)'), ('LSP', 'Autocomplete and diagnostics.', 'import typing\nprint(typing.__name__)'), ('Debugger', 'Inspect running code.', 'x=1\nx+=1\nprint(x)')),
        'IDE = editor + LSP + debugger.',
        'Reduce friction writing Python.',
        'Faster navigation and feedback.',
        'Daily feature work.',
        'One venv per repo.',
        'Using system Python globally.',
        "print('IDE ready')",
        '# editor -> venv -> lint -> debug',
        dedent('''\
import sys
print(sys.executable)
        '''),
        dedent('''\
import sys
print(sys.version.split()[0])
        '''),
        dedent('''\
def greet(n:str)->str: return f'Hello, {n}'
print(greet('Dev'))
        '''),
        dedent('''\
import sys
print('Interpreter:', sys.executable)
        '''),
        dedent('''\
flowchart LR
    A[Folder]-->B[venv]-->C[LSP]-->D[Run]
        '''),
    ),
    'Python Syntax': S(
        'Python syntax defines statements, blocks, and expressions.',
        'Valid syntax is prerequisite to all logic.',
        'Scripts, notebooks, tests, modules.',
        ('Use indentation and colons.', 'Write expressions and comments.', 'Read SyntaxError tracebacks.'),
        'You write valid Python without syntax failures.',
        ('Apps', 'Notebooks', 'Ops scripts', 'Tests'),
        (('Indentation', 'Defines blocks.', "if True:\n    print('ok')"), ('for loop', 'Iteration syntax.', 'for i in range(3):\n    print(i)'), ('Comments', 'Ignored lines.', '# note\nx=1\nprint(x)')),
        'Significant whitespace, readable keywords.',
        'Express structure without braces.',
        'Less boilerplate.',
        'All Python programs.',
        '4 spaces, PEP 8.',
        'Tabs mixed with spaces.',
        dedent('''\
name="Ada"
print(name)
        '''),
        'imports -> defs -> main',
        '[v*v for v in [1,2,3]]',
        'print("Syntax matters")',
        'print([v*v for v in [1,2,3]])',
        dedent('''\
from typing import Iterator
def count(n:int)->Iterator[int]:
    for i in range(n): yield i
print(list(count(4)))
        '''),
        dedent('''\
flowchart TD
    A[Source]-->B[Parser]-->C[Execute]
        '''),
    ),
    'Variables': S(
        'Variables are names referencing objects in memory.',
        'They store program state.',
        'All Python programs.',
        ('Assign and reassign.', 'Use snake_case.', 'Understand references.'),
        'You model state with clear names.',
        ('Business logic', 'ETL', 'Games', 'Finance'),
        (('Assignment', 'Bind name to object.', 'score=100\nprint(score)'), ('Rebinding', 'Point to new object.', 'score+=10\nprint(score)'), ('Naming', 'snake_case style.', "user_email='a@b.com'\nprint(user_email)")),
        'Names label objects.',
        'Store and update data.',
        'Readable state.',
        'Counters, configs, input.',
        'Descriptive names.',
        'Shadowing builtins.',
        dedent('''\
name='Ada'
age=36
        '''),
        'declare -> use -> update',
        dedent('''\
total=price*quantity
print(total)
        '''),
        dedent('''\
x=5
y=3
print(x+y)
        '''),
        dedent('''\
first,*rest=[1,2,3]
print(first,rest)
        '''),
        dedent('''\
from typing import Final
MAX:Final=3
print(MAX)
        '''),
        dedent('''\
flowchart LR
    A[Assign]-->B[Object]-->C[Use]
        '''),
    ),
}
