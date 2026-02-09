# Learning Python, 6th Edition — Granular Content Summary

**Mark Lutz, O'Reilly Media, 2025 · ~1,268 pages · Python 3.x focus**

> This document describes *what each section covers and teaches*, and to what level of detail, at the granularity of every heading in the book's Table of Contents. It is intended as a reference index for a project context. Every chapter also ends with a Chapter Summary, Quiz, and Answers section (omitted from this summary as they are pedagogical apparatus, not new content). Each Part ends with programming exercises (solutions in Appendix B).

---

## Preface

### Python
Positions Python in the broader programming landscape. Notes its growth, popularity, and breadth of application domains.

### This Book
Explains the book's scope: a comprehensive tutorial of the Python *core language* only — not libraries, frameworks, or application domains. States the target audience (beginners to intermediate) and the pedagogical approach (incremental, example-heavy, with quizzes and exercises).

### This Edition
Describes what's new in the 6th edition. Updated for Python 3.11+ features including `match`/`case`, exception groups, `tomllib`, and other modern additions. Notes removal of Python 2.x coverage.

### Media Choices
Discusses the book's availability in print, ebook, and Safari/O'Reilly online formats.

### Updates and Examples
Explains where to find code examples, errata, and updates online.

### Conventions and Reuse
Describes typographic conventions used (font for code, italics for new terms, etc.) and permissions for reuse.

### Acknowledgments
Credits contributors, reviewers, and the O'Reilly team.

---

## Part I. Getting Started

Orientation section. Covers why Python exists, how its execution model works, and how to get code running. No actual Python programming is taught — this is context and setup.

---

### Chapter 1. A Python Q&A Session

High-level motivational overview of Python. No code is written; the chapter is entirely expository, answering common newcomer questions.

#### Why Do People Use Python?
Frames the two main reasons people adopt Python: software quality and developer productivity.

##### Software Quality
Explains Python's emphasis on readability, coherence, and maintainability — the "one obvious way" philosophy. Notes OOP, functional support, and code reuse features.

##### Developer Productivity
Discusses Python's conciseness relative to C/C++/Java (typically 1/3 to 1/5 the code). Notes the rapid development cycle (no compile/link steps).

#### Is Python a "Scripting Language"?
Addresses the common misconception. Argues Python is a general-purpose language that also works well for scripting. Brief discussion of the term's baggage.

#### OK, but What's the Downside?
Honest treatment of Python's main limitation: execution speed relative to compiled languages like C. Notes mitigations (C extensions, PyPy, Cython, critical-path optimisation). Brief.

#### Who Uses Python Today?
Surveys Python's adoption across industries: Google, YouTube, Instagram, Dropbox, Netflix, NASA, finance, etc. Brief name-drop overview.

#### What Can I Do with Python?
Survey of Python's application domains. Each subsection is a brief paragraph.

##### Systems Programming
OS interfaces, file/directory tools, process management, shell scripting replacement.

##### GUIs and UIs
tkinter (ships with Python), Qt (PyQt, PySide), wxPython, Kivy for mobile.

##### Internet and Web Scripting
Sockets, CGI, Django, Flask, Pyramid, XML/JSON parsing, web scraping.

##### Component Integration
C/C++ integration via ctypes, SWIG, Cython; COM on Windows; Jython for Java; IronPython for .NET.

##### Database Access
pickle, shelve, SQLite (built-in), MySQL/PostgreSQL adapters, SQLAlchemy ORM, MongoDB drivers.

##### Rapid Prototyping
Python's suitability for prototyping systems that may later be partially reimplemented in C.

##### Numeric and Scientific Programming
NumPy, SciPy, pandas, Matplotlib, scikit-learn, Jupyter. Brief overview of the ecosystem.

##### And More: AI, Games, Images, QA, Excel, Apps…
Catch-all: TensorFlow/PyTorch, Pygame, Pillow, testing frameworks, openpyxl, Electron-like tools. One paragraph.

#### What Are Python's Technical Strengths?
Enumerates Python's core technical characteristics. Each subsection is 1–2 paragraphs.

##### It's Object-Oriented and Functional
Notes support for OOP (classes, inheritance, operator overloading) and functional tools (generators, comprehensions, closures, map/filter/reduce).

##### It's Free and Open
Open-source under the PSF license. Free to use, distribute, and embed commercially.

##### It's Portable
Runs on Windows, macOS, Linux, Android, iOS, embedded systems. Same code across platforms (mostly).

##### It's Powerful
Dynamic typing, automatic memory management, large standard library, third-party ecosystem, introspection, metaprogramming.

##### It's Mixable
Easily integrated with C, C++, Java, .NET, and other languages for performance or legacy interop.

##### It's Relatively Easy to Use
Compared to C++/Java: no compilation, simpler syntax, interactive REPL for experimentation.

##### It's Relatively Easy to Learn
Simpler than many alternatives; the book argues Python is learnable by beginners in weeks.

---

### Chapter 2. How Python Runs Programs

Explains the internal execution model. Moderate technical depth — covers the compilation-to-bytecode pipeline without getting into CPython internals.

#### Introducing the Python Interpreter
Describes the Python interpreter as both the software you install and the runtime engine. Explains it reads source, compiles to bytecode, and runs it on the PVM.

#### Program Execution
Describes the two perspectives on what happens when you run a `.py` file.

##### The Programmer's View
You write `.py` text files and run them. Python handles everything else. Simple view.

##### Python's View
Detailed: source → bytecode compilation (`.pyc` files in `__pycache__`), then bytecode execution on the Python Virtual Machine (PVM). Explains `.pyc` caching, timestamp-based recompilation, and that the PVM is not a separate program but a loop inside the interpreter.

#### Execution-Model Variations
Covers alternative implementations and deployment modes.

##### Python Implementation Alternatives
CPython (the default C implementation), PyPy (with JIT compiler — notes speed gains), Jython (Java), IronPython (.NET), Stackless (microthreads). Brief description and current status of each.

##### Standalone Executables
Tools that bundle Python code into self-contained executables: PyInstaller, cx_Freeze, Nuitka. Explains these embed the interpreter and bytecode — they don't truly compile to machine code.

##### Future Possibilities
Speculates on JIT compilation in CPython (3.13+ experimental), Mojo, and other ongoing performance work. Brief.

---

### Chapter 3. How You Run Programs

Comprehensive practical chapter covering every method of launching Python code. The most hands-on chapter in Part I.

#### Installing Python
Brief guidance on getting Python installed. Notes that many systems come with Python pre-installed. Points to python.org and Appendix A for platform-specific details.

#### Interactive Code
Covers the interactive REPL (Read-Eval-Print Loop) in detail.

##### Starting an Interactive REPL
How to launch `python` or `python3` from a terminal/command prompt. What the `>>>` prompt means.

##### Where to Run: Code Folders
Advice on where to create and store script files. Working directory considerations.

##### What Not to Type: Prompts and Comments
Clarifies that `>>>` and `...` are prompts displayed by Python, not things you type. Notes `#` comments.

##### Other Python REPLs
Mentions IPython, bpython, ptpython as enhanced interactive shells with features like syntax highlighting and tab completion.

##### Running Code Interactively
Demonstrates typing expressions and statements at the `>>>` prompt. Shows how results are auto-printed, how multi-line statements work (the `...` continuation prompt), and how to handle compound statements interactively.

##### Why the Interactive Prompt?
Explains use cases: quick testing, exploring APIs, learning, debugging. Notes limitations: code is not saved, only single statements, no real editing.

#### Program Files
Covers running Python from saved `.py` files.

##### A First Script
Creates a simple `script1.py` file with print statements. Shows the file's contents and expected output.

##### Running Files with Command Lines
Demonstrates `python script1.py` from a system shell. Covers the working directory, PATH, and file extension conventions.

##### Command-Line Usage Variations
Covers: running with full paths, the `-m` module flag, command-line arguments (`sys.argv`), stdin piping, and the `-c` flag for inline code.

#### Other Ways to Run Files
Surveys alternative execution methods beyond the command line.

##### Clicking and Tapping File Icons
Running `.py` files by double-clicking on Windows/macOS. Notes the "flash and disappear" problem and how to address it (adding `input()` at the end, or using `.pyw` on Windows).

##### The IDLE Graphical User Interface
Covers IDLE (ships with Python): launching, the shell window, the editor window, running scripts via Run > Run Module, syntax colouring, basic debugging. Moderate detail.

##### Other IDEs for Python
Brief survey: VS Code, PyCharm, Spyder, Thonny, Eclipse+PyDev, Komodo. Notes features like integrated debugging, project management, and version control.

##### Smartphone Apps
Notes Python can run on phones via apps like Pythonista (iOS), QPython (Android), Pydroid (Android), and Termux. Brief.

##### WebAssembly for Browsers
Mentions Pyodide and PyScript for running Python in web browsers via WebAssembly. Brief overview.

##### Jupyter Notebooks for Science
Describes Jupyter's notebook interface: cells of code and markdown, inline output, popularity in data science. Brief.

##### Ahead-of-Time Compilers for Speed
Mentions Cython, Nuitka, and mypyc as tools that compile Python to C/machine code for performance. Brief.

##### Running Code in Code
Covers programmatic execution: `exec()` for running code strings, `eval()` for expressions, `import` as code execution, `importlib` functions, `runpy` module, and `compile()`. More detailed than most subsections (~4 pages) — includes security warnings about `exec`/`eval`.

##### Other Launch Options
Mentions: `py` Windows launcher, Unix `#!` shebang lines, `python -i` for post-mortem interactive mode, frozen binaries, and cloud/container deployments. Brief.

#### Which Option Should I Use?
Practical guidance: use a text editor + command line for learning, graduate to an IDE for larger projects. Recommends experimenting with multiple approaches.

---

## Part II. Objects and Operations

The core data types tour. Covers every built-in object type in Python with hands-on interactive examples. This is the largest foundational section of the book, building the vocabulary of Python's object model.

---

### Chapter 4. Introducing Python Objects

Preview/survey chapter. Gives a quick interactive tour of all major types to establish context before the deep dives in Chapters 5–9. Relatively shallow — breadth over depth.

#### The Python Conceptual Hierarchy
Introduces the hierarchy: programs are composed of modules, which contain statements, which contain expressions, which create and process objects. Frames objects as the fundamental building blocks.

#### Why Use Built-in Objects?
Argues for using built-in types over implementing your own: they're optimised in C, debugged, standardised, and part of the language. Notes the "batteries included" philosophy.

#### Python's Core Object Types
Table listing all core types: numbers, strings, lists, dictionaries, tuples, files, sets, booleans, None, and type. Sets up the chapter's tour.

#### Numbers
Quick demo of integer and float arithmetic at the `>>>` prompt. Shows basic operators, `math` module, and `random` module. Very brief — full treatment in Chapter 5.

#### Strings
First substantial type preview. Covers strings at an introductory level.

##### Sequence Operations
Demonstrates indexing (`S[0]`), slicing (`S[1:3]`), `len()`, and concatenation (`+`). Introduces the concept of sequences as ordered collections.

##### Immutability
Shows that strings cannot be changed in place. Demonstrates that operations create new string objects. First introduction of the mutable/immutable distinction.

##### Type-Specific Methods
Demonstrates `find()`, `replace()`, `split()`, `upper()`, `isalpha()`, `strip()`. Introduces method-call syntax (`object.method()`).

##### Getting Help
Shows `dir(str)` to list available methods and `help(str.replace)` to get documentation interactively.

##### Other Ways to Code Strings
Mentions raw strings, byte strings, triple-quoted strings, and escape sequences — previews without full detail.

##### Unicode Strings
Brief note that Python 3 `str` is Unicode, with `\u` and `\U` escapes. Notes `bytes` for raw binary. Previews Chapter 37.

#### Lists
Preview of lists — the mutable ordered sequence type.

##### Sequence Operations
Shows lists support the same indexing, slicing, and `len()` as strings.

##### Type-Specific Operations
Demonstrates `append()`, `pop()`, `sort()`, `reverse()`, and `insert()`.

##### Bounds Checking
Shows that out-of-range indexing raises `IndexError`. Python doesn't silently grow lists on assignment.

##### Nesting
Demonstrates lists of lists (matrixes). Shows nested indexing (`M[1][2]`).

##### Comprehensions
Introduces list comprehension syntax (`[x**2 for x in range(5)]`) with filtering. Shows it applied to matrix processing. Brief but includes nested comprehensions.

#### Dictionaries
Preview of dictionaries — the mutable mapping type.

##### Mapping Operations
Demonstrates creation, key-based access, assignment, `len()`. Shows dictionaries are unordered (conceptually) but insertion-ordered (implementation).

##### Nesting Revisited
Shows dictionaries containing lists and other dictionaries. Nested access patterns.

##### Missing Keys: if Tests
Shows `KeyError` on missing keys. Introduces `if key in dict` tests, `get()` with defaults, and `try/except` as alternatives. First glimpse of conditional logic.

##### Item Iteration: for Loops
Demonstrates `for key in dict` iteration. First use of a `for` loop — previews Chapter 13.

#### Tuples
Brief preview of tuples — immutable ordered sequences.

##### Why Tuples?
Explains tuples as "constant lists": they provide integrity guarantees (can't be changed) and can serve as dictionary keys (since they're hashable).

#### Files
Preview of file objects.

##### Unicode and Byte Files
Notes that `open()` in text mode handles Unicode encoding/decoding automatically; binary mode gives raw bytes. Brief preview of Chapter 37.

##### Other File-Like Tools
Mentions `os` module (directory listings, process tools), `socket`, `subprocess`, `urllib`, and `io.StringIO` as file-like interfaces. Brief.

#### Other Object Types
Catch-all for remaining built-in types.

##### Sets
Demonstrates `set()` creation, set operations (`&`, `|`, `-`), and set comprehensions. Brief.

##### Booleans and None
Notes `True`/`False` as integers (1/0) and `None` as the Python null/placeholder. Brief.

##### Types
Shows `type()` to inspect object types. Notes that types are themselves objects.

##### Type Hinting
Brief mention that Python supports optional type annotations (PEP 484). Notes they're not enforced at runtime. Previews later discussion.

##### User-Defined Objects
Notes that classes let you create new object types. Brief forward reference to Part VI.

##### And Everything Else
Mentions that everything in Python is an object: functions, modules, classes, compiled code, stack frames, etc.

---

### Chapter 5. Numbers and Expressions

Deep dive into all numeric types and expression operators. Comprehensive reference-style chapter with many interactive examples.

#### Numeric Object Basics
Overview of Python's numeric types and the tools available for working with them.

##### Numeric Literals
Catalogues all numeric literal forms: integers (decimal, hex `0x`, octal `0o`, binary `0b`), floats (`1.0`, `1e2`), complex (`3+4j`), and special forms. Includes a reference table.

##### Built-in Numeric Tools
Lists built-in functions (`int()`, `float()`, `complex()`, `abs()`, `round()`, `pow()`, `divmod()`, `bin()`, `hex()`, `oct()`) and modules (`math`, `random`, `decimal`, `fractions`).

#### Python Expression Operators
Reference section covering all expression operators.

##### Mixed Operators: Precedence
Full precedence table for Python operators (from lowest to highest). Explains how precedence determines evaluation order.

##### Parentheses Group Subexpressions
Demonstrates using parentheses to override default precedence. Notes this is standard but important for clarity.

##### Mixed Types Are Converted Up
Explains automatic numeric type coercion: `int` → `float` → `complex`. Shows examples of mixed-type expressions.

##### Preview: Operator Overloading and Polymorphism
Brief forward reference: classes can define `__add__`, `__mul__`, etc. to make custom objects work with `+`, `*`, etc. Previews Part VI.

#### Numbers in Action
Practical demonstrations of numeric operations at the interactive prompt.

##### Variables and Basic Expressions
Shows variable assignment and arithmetic. Notes Python variables don't need declarations — they're created on assignment.

##### Numeric Display Formats
Covers `repr()` vs. `str()` for numbers, format specifications (`format(x, '.2f')`), and how the interactive prompt uses `repr()`.

##### Comparison Operators
Demonstrates `<`, `>`, `<=`, `>=`, `==`, `!=`. Covers chained comparisons (`1 < x < 10`). Notes floating-point comparison pitfalls.

##### Division Operators
Full treatment of Python 3's three division modes: true division (`/` always returns float), floor division (`//` truncates), and modulus (`%`). Shows behaviour with negative numbers.

##### Integer Precision
Demonstrates Python's arbitrary-precision integers (no overflow). Shows very large integers. Notes this is automatic and unlimited.

##### Complex Numbers
Shows complex literal syntax (`3+4j`), `.real`/`.imag` attributes, `conjugate()`, and `cmath` module for complex math functions.

##### Hex, Octal, and Binary
Demonstrates literal prefixes (`0x`, `0o`, `0b`), conversion functions (`hex()`, `oct()`, `bin()`), and `int('ff', 16)` for parsing.

##### Bitwise Operations
Covers `&`, `|`, `^`, `~`, `<<`, `>>` with examples. Shows practical uses (flags, masks). Notes `bit_length()` and `bit_count()` methods.

##### Underscore Separators in Numbers
Demonstrates `1_000_000` and `0xFF_FF` for readability in numeric literals (Python 3.6+). Shows this works in all numeric literal forms.

##### Other Built-in Numeric Tools
Covers `math` module functions (`sqrt`, `floor`, `ceil`, `trunc`, `pi`, `e`), `random` module (`random()`, `randint()`, `choice()`, `shuffle()`), and rounding/truncation subtleties.

#### Other Numeric Objects
Covers specialised numeric types beyond `int`/`float`/`complex`.

##### Decimal Objects
`decimal.Decimal` for fixed-precision arithmetic. Covers creation, context management (`getcontext()`, precision, rounding modes), and use cases (financial calculations). Moderate detail.

##### Fraction Objects
`fractions.Fraction` for rational arithmetic. Covers creation from integers, floats, and strings. Shows arithmetic that maintains exact fractions. Conversion to/from floats.

##### Set Objects
Comprehensive set coverage (~6 pages). Creation via `set()` and `{}`; set operations (union `|`, intersection `&`, difference `-`, symmetric difference `^`); methods vs. operators; frozensets; set comprehensions; practical uses (removing duplicates, membership testing, graph algorithms). Covers supersets/subsets.

##### Boolean Objects
`True`/`False` as `int` subclass. Shows `True + True == 2`. Covers truth-value testing, `bool()` constructor, and how booleans interact with other types.

#### Numeric Extensions
Brief note on third-party numeric libraries: NumPy (arrays, vectorisation), SciPy, pandas, Matplotlib. Points to external resources — no detailed coverage.

---

### Chapter 6. The Dynamic Typing Interlude

Conceptual chapter explaining Python's type system. Focuses on mental models rather than large code examples. Essential for understanding Python's behaviour with assignments and object references.

#### The Case of the Missing Declaration Statements
Explains why Python has no type declarations and how its assignment model works.

##### Variables, Objects, and References
The core mental model: variables are names (references/pointers) that refer to objects in memory. Assignment creates a reference, not a container. Illustrated with diagrams.

##### Types Live with Objects, Not Variables
A variable can refer to any type of object at different times. Type information is attached to objects, not to variable names. Demonstrates reassigning a name from int to string.

##### Objects Are Garbage-Collected
Explains automatic memory management. Reference counting as the primary mechanism, with cyclic-reference detection via the `gc` module. Objects are freed when no references remain.

#### Shared References
Covers what happens when multiple variables refer to the same object — a critical topic for understanding Python's behaviour.

##### Shared References and In-Place Changes
Demonstrates the aliasing problem: when two names point to the same mutable object (e.g., list), changes through one name are visible through the other. Shows this does *not* happen with immutable objects (int, string).

##### Shared References and Equality
Explains `==` (value equality) vs. `is` (identity/same object). Demonstrates `id()` function. Notes CPython's small integer and short string caching (implementation detail, not to be relied upon).

#### Dynamic Typing Is Everywhere
Brief note that dynamic typing pervades all Python code: function arguments, return values, class attributes, etc. It's not an isolated feature.

#### Type Hinting: Optional, Unused, and Why?
Discusses PEP 484 type hints. Explains they're optional annotations, not enforced at runtime, used mainly by external tools (mypy, IDEs). Argues they have value for documentation and tooling but are not required by Python itself. Notes the philosophical debate in the community.

---

### Chapter 7. String Fundamentals

Thorough treatment of `str`. One of the longer chapters in Part II, with detailed coverage of all string operations and three formatting systems.

#### String Object Basics
Overview table of string literal forms and operations. Notes strings are immutable sequences of Unicode characters in Python 3.

#### String Literals
Covers all ways to write string literals.

##### Single and Double Quotes Are the Same
Demonstrates that `'hello'` and `"hello"` produce identical objects. Notes the convenience of nesting one inside the other.

##### Escape Sequences Are Special Characters
Full reference table of escape sequences (`\n`, `\t`, `\\`, `\'`, `\"`, `\0`, `\xNN`, `\uNNNN`, `\UNNNNNNNN`, `\ooo`). Shows practical use in print output.

##### Raw Strings Suppress Escapes
Demonstrates `r'...'` strings where backslashes are literal. Explains use cases: regex patterns, Windows file paths.

##### Triple Quotes and Multiline Strings
Shows `'''...'''` and `"""..."""` for multi-line string literals. Notes use in docstrings. Shows how embedded newlines are preserved.

#### Strings in Action
Practical string operations.

##### Basic Operations
Concatenation (`+`), repetition (`*`), `len()`, membership (`in`). Notes these are generic sequence operations shared with lists and tuples.

##### Indexing and Slicing
Detailed: positive/negative indexing, slice syntax (`S[i:j]`, `S[i:j:k]`), extended slicing with step, `S[::-1]` for reversal. Multiple examples.

##### String Conversion Tools
`int()`, `float()`, `str()`, `repr()`, `ord()`, `chr()`. Explains why `"42" + 1` is an error in Python (no implicit conversion). Shows explicit conversion patterns.

##### "Changing" Strings Part 1: Sequence Operations
Since strings are immutable, "changing" means creating new strings. Shows concatenation, slicing, and repetition as ways to build new strings from old.

#### String Methods
Comprehensive coverage of the `str` method set.

##### Method Call Syntax
Explains `object.method(args)` syntax. Notes methods are type-specific (unlike generic operations like `+`).

##### All String Methods (Today)
Reference listing of all string methods grouped by category. Not every method is demonstrated, but the full list is provided for reference.

##### "Changing" Strings, Part 2: String Methods
Demonstrates `replace()`, `translate()`, and string building with `join()` as alternatives to concatenation for "modifying" strings.

##### More String Methods: Parsing Text
Demonstrates `split()`, `partition()`, `strip()`, `lstrip()`, `rstrip()`, and their use for parsing structured text (CSV, columns, etc.).

##### Other Common String Methods
Brief demos of `startswith()`, `endswith()`, `count()`, `center()`, `ljust()`, `rjust()`, `zfill()`, `expandtabs()`.

#### String Formatting: The Triathlon
Major section comparing Python's three string-formatting systems in detail.

##### String-Formatting Options
Overview of the three options: `%` expressions, `.format()` method, and f-strings. Notes the historical progression.

##### The String-Formatting Expression
Full treatment of `%`-style formatting. Format codes (`%s`, `%d`, `%f`, `%e`, `%x`, etc.), width/precision specifiers, flags (`-`, `+`, `0`), dictionary-based formatting (`%(name)s`). Multiple examples. ~4 pages.

##### The String-Formatting Method
Full treatment of `str.format()`. Positional and keyword arguments, field names, attribute/index access in format strings, format specifications (fill, align, width, precision, type), nesting format specs. ~5 pages.

##### The F-String Formatting Literal
Full treatment of f-strings (`f'...'`). Inline expressions, format specifications, `=` for debug display (Python 3.8+), multiline f-strings, nesting, and comparison with `.format()`. ~5 pages.

##### And the Winner Is…
Compares the three systems on readability, features, and use cases. Notes f-strings are generally preferred for new code, but all three are used in practice and in existing codebases.

#### General Type Categories
Classifies Python objects into categories that share operations.

##### Types Share Operation Sets by Categories
Three categories: sequences (string, list, tuple — support indexing, slicing, concatenation), mappings (dict — support key access), and sets. Notes that category membership determines which operations are available.

##### Mutable Types Can Be Changed in Place
Distinguishes mutable (list, dict, set, bytearray) from immutable (int, float, str, tuple, frozenset, bytes). Explains the implications for aliasing and function argument passing.

---

### Chapter 8. Lists and Dictionaries

Deep dive into the two most-used mutable collection types. Heavily practical with many interactive examples.

#### Lists
Overview of list features: ordered, mutable, arbitrarily nestable, variable-length sequences of arbitrary objects. Lists literal syntax and key characteristics.

#### Lists in Action
Comprehensive practical demonstrations.

##### Basic List Operations
`len()`, concatenation (`+`), repetition (`*`), membership (`in`), iteration (`for`). Shows these are shared sequence operations.

##### Indexing and Slicing
Same patterns as strings but applied to lists: positive/negative indexing, slices, extended slices. Shows slice assignment (replacing a range of elements with a different-length sequence).

##### Changing Lists in Place
Index assignment (`L[i] = x`), slice assignment (`L[i:j] = [...]`), `del L[i]`, `del L[i:j]`. Shows how lists grow, shrink, and change via these operations.

##### More List Methods
`append()`, `extend()`, `insert()`, `pop()`, `remove()`, `sort()` (with `key=` and `reverse=`), `reverse()`, `copy()`, `clear()`, `count()`, `index()`. Includes notes on return values (many return `None`, modifying in place).

##### Iteration, Comprehensions, and Unpacking
List comprehensions reviewed; `for` iteration; unpacking assignment (`a, b, c = L`); starred unpacking (`first, *rest = L`). Shows combining these tools.

##### Other List Operations
`sorted()` (returns new list), `reversed()`, `list()` constructor, `enumerate()` usage with lists. Brief.

#### Dictionaries
Overview of dictionary features: mutable, unordered (but insertion-ordered since 3.7), key-value mappings with fast lookup. Literal syntax, key types (must be hashable).

#### Dictionaries in Action
Comprehensive practical demonstrations.

##### Basic Dictionary Operations
Creation, key access, `len()`, membership (`in` tests keys), `del`, iteration (over keys by default).

##### Changing Dictionaries in Place
Key assignment (adds or updates), `del`, `update()`. Shows building dictionaries incrementally.

##### More Dictionary Methods
`keys()`, `values()`, `items()` (return view objects), `get()`, `pop()`, `setdefault()`, `update()`, `copy()`, `clear()`, `popitem()`. Explains view objects and their set-like operations.

##### Other Dictionary Makers
Alternative creation methods: `dict(name=value)`, `dict(zip(keys, vals))`, `dict.fromkeys()`. Shows when each is convenient.

##### Dictionary Comprehensions
`{k: v for k, v in iterable}` syntax. Shows filtering and transformation. Compares to `dict(zip(...))`.

##### Key Insertion Ordering
Explains that since Python 3.7 dictionaries officially preserve insertion order. Notes this changed dict iteration, `repr()`, and equality semantics. Discusses whether to use `dict` or `collections.OrderedDict`.

##### Dictionary "Union" Operator
The `|` and `|=` merge operators (Python 3.9+). Shows merging dictionaries and the precedence of duplicate keys (right operand wins).

##### Intermission: Books Database
Worked example: building a small books database as nested dictionaries. Demonstrates record-like usage, nested access, and iteration over records.

##### Dictionary Usage Tips
Extended practical section (~7 pages). Covers: using dicts for sparse data structures, as case/switch replacements, for simulating flexible records, for building simple databases. Shows `if/in` tests, `get()` defaults, `defaultdict`, and `try/except` patterns for missing keys. Discusses dict vs. list for various tasks.

---

### Chapter 9. Tuples, Files, and Everything Else

Wraps up the built-in types tour with tuples, files, a comprehensive core-types review, and common gotchas.

#### Tuples
Covers tuples — immutable ordered sequences.

##### Tuples in Action
Creation (with and without parentheses), single-element tuples (`(1,)`), indexing, slicing, concatenation, repetition, methods (`count()`, `index()`), tuple unpacking, nesting.

##### Why Lists and Tuples?
Explains the rationale for having both: tuples provide integrity (cannot be changed accidentally) and can be used as dictionary keys and in sets (since they're hashable). Lists provide flexibility.

##### Records Revisited: Named Tuples
Introduces `collections.namedtuple` for creating lightweight classes with named fields. Shows creation, access by name and index, `_asdict()`, `_replace()`, and `_fields`. Notes `typing.NamedTuple` as a class-based alternative.

#### Files
Comprehensive treatment of file I/O.

##### Opening Files
The `open()` function: filename, mode (`'r'`, `'w'`, `'a'`, `'rb'`, `'wb'`, etc.), encoding parameter. Explains the full set of mode characters.

##### Using Files
Reading methods (`read()`, `readline()`, `readlines()`), writing methods (`write()`, `writelines()`), and their return values. Notes file iterators for line-by-line reading.

##### Files in Action
Interactive demonstrations: writing and reading text files, reading line by line, writing lists of lines.

##### Text and Binary Files: The Short Story
Explains that text mode decodes bytes to strings and encodes strings to bytes; binary mode gives raw bytes. Notes the encoding defaults.

##### Storing Objects with Conversions
Shows manual serialisation: converting Python objects to strings for storage and parsing them back. Demonstrates the awkwardness of this approach.

##### Storing Objects with pickle
Introduces `pickle` for automatic serialisation: `pickle.dump()` and `pickle.load()`. Shows pickling and unpickling various objects. Notes that pickle handles nested objects and cross-references.

##### Storing Objects with JSON
Introduces `json` module: `json.dump()`/`json.dumps()` and `json.load()`/`json.loads()`. Shows the JSON ↔ Python type mapping. Notes JSON's limitations (no tuples, no sets, keys must be strings).

##### Storing Objects with Other Tools
Briefly mentions `shelve` (persistent dictionary), `dbm`, `sqlite3`, `csv`, `xml`, `configparser`, and `struct` as other persistence/serialisation tools.

##### File Context Managers
Introduces the `with open(...) as f:` pattern for automatic file closing. Brief — full treatment in Chapter 34.

##### Other File Tools
Mentions `os` module (file operations, directory tools), `tempfile`, `io.StringIO`/`io.BytesIO`, `pathlib`, `fileinput`. Brief survey.

#### Core Types Review and Summary
Major review section bringing together concepts from all type chapters.

##### Object Flexibility
Notes that Python's objects can be freely nested: lists of dicts of lists, etc. Shows complex nested structures.

##### References Versus Copies
Detailed treatment of copying: assignment creates references (not copies), how to make true copies (`L[:]`, `dict.copy()`, `set.copy()`, `copy.copy()`, `copy.deepcopy()`). Shows the difference between shallow and deep copies with nested structures.

##### Comparisons, Equality, and Truth
Covers `==` vs. `is`, comparison of different types, comparison of nested objects (recursive equality), and how ordering works for sequences and dictionaries.

##### The Meaning of True and False in Python
Comprehensive truth-value rules: zero numbers are false, empty collections are false, `None` is false, everything else is true. Shows how this affects `if`, `while`, `and`, `or`. Explains short-circuit evaluation of `and`/`or`.

##### Python's Type Hierarchies
Shows the hierarchy: object → numbers, sequences, mappings, sets, callables, etc. Notes that types form a tree with `object` at the root.

##### Type Objects
Demonstrates `type()`, `isinstance()`, and `issubclass()`. Shows that types are objects you can pass around and test.

#### Other Types in Python
Brief mention of types not covered in detail: `bytearray`, `memoryview`, `range`, `enumerate`, `zip`, `map`, `filter`, `property`, `staticmethod`, `classmethod`, etc.

#### Built-in Type Gotchas
Common mistakes and surprising behaviours.

##### Assignment Creates References, Not Copies
Reiterates the aliasing issue with a concrete example of accidental shared mutation.

##### Repetition Adds One Level Deep
Shows that `[[]] * 3` creates three references to the *same* inner list, not three independent lists. A common gotcha.

##### Beware of Cyclic Data Structures
Notes that self-referencing structures (e.g., a list containing itself) can cause infinite loops in printing and comparison. Python handles printing with `[...]` but code must be careful.

##### Immutable Types Can't Be Changed in Place
Reiterates that trying to assign to an index of a string or tuple raises `TypeError`. Seems obvious but is a common beginner error.

---

## Part III. Statements and Syntax

Covers Python's procedural statement set: assignments, conditionals, loops, the iteration protocol, and documentation tools. Moves from expressions and objects to control flow.

---

### Chapter 10. Introducing Python Statements

Overview chapter introducing Python's statement set and its distinctive syntax.

#### The Python Conceptual Hierarchy Revisited
Updates the hierarchy from Chapter 4: programs → modules → statements → expressions → objects. Frames statements as the processing layer that connects expressions.

#### Python's Statements
Reference table of all Python statements with syntax and brief descriptions. Includes: assignment, `print`, `if`/`elif`/`else`, `for`, `while`, `pass`, `break`, `continue`, `def`, `return`, `yield`, `global`, `nonlocal`, `import`, `from`, `class`, `try`/`except`/`finally`, `raise`, `assert`, `with`, `del`, `match`.

#### A Tale of Two ifs
Compares Python's `if` statement to C/Java equivalents, illustrating Python's syntactic distinctiveness.

##### What Python Adds
Colons (`:`) at the end of header lines. Indentation to define blocks.

##### What Python Removes
No braces for blocks, no parentheses around test expressions (optional), no semicolons to end statements.

##### Why Indentation Syntax?
Extended discussion of Python's indentation-as-syntax design. Covers the rationale (forces readable code), common objections and responses, and edge cases. Notes that the standard is 4 spaces (not tabs).

##### A Few Special Cases
Covers: semicolons to separate statements on one line, backslash continuation for long lines, parentheses/brackets/braces for implicit continuation, triple-quoted strings spanning lines.

#### A Quick Example: Interactive Loops
Progressively builds a loop program to demonstrate statement syntax.

##### A Simple Interactive Loop
Basic `while True:` loop with `input()` and `print()`. Shows the pattern.

##### Doing Math on User Inputs
Adds `int()` conversion to process numeric input. Demonstrates type conversion.

##### Handling Errors by Testing Inputs
Adds `if` test to check for valid input before converting. Introduces conditional logic in context.

##### Handling Errors with try Statements
Replaces the `if` test with `try`/`except` to catch `ValueError`. Shows exception handling is often cleaner than testing.

##### Supporting Floating-Point Numbers
Switches from `int()` to `float()` conversion. Brief.

##### Nesting Code Three Levels Deep
Shows `while` containing `try` containing `if` — demonstrates Python's indentation-based nesting.

---

### Chapter 11. Assignments, Expressions, and Prints

Comprehensive treatment of assignment in all its forms, expression statements, and the `print()` function.

#### Assignments
Major section covering every assignment form in Python.

##### Assignment Syntax Forms
Reference table of all assignment forms: basic, tuple/list unpacking, extended unpacking, augmented, named expressions.

##### Basic Assignments
Standard `name = value`. Covers multiple assignment on one line (`a = b = 0`).

##### Sequence Assignments
Tuple and list unpacking: `a, b = 1, 2` and `[a, b] = [1, 2]`. Shows swapping values (`a, b = b, a`), unpacking in `for` loops, and nested sequence unpacking.

##### Extended-Unpacking Assignments
Starred unpacking (`first, *rest = sequence`, `*init, last = sequence`). Full treatment of all starred-target positions. Shows practical patterns including splitting iterables and multiple stars (illegal). ~5 pages.

##### Multiple-Target Assignments
`a = b = c = value`. Explains that all names reference the same object (shared reference, not copies).

##### Augmented Assignments
`+=`, `-=`, `*=`, etc. Full list. Explains they may mutate in place for mutable types (lists) but create new objects for immutable types (strings, ints). Notes the subtle difference from `a = a + b` for mutable types.

##### Named Assignment Expressions
The walrus operator `:=` (Python 3.8+). Full treatment: syntax, use cases (while loops, comprehension filters, conditional assignments), scope rules, and style guidance. Shows before/after comparisons. ~3 pages.

##### Variable Name Rules
Naming conventions: allowed characters, case sensitivity, reserved words (full list), soft keywords. Covers `_` conventions (`_private`, `__mangled`, `__dunder__`, `_` in interactive prompt). PEP 8 naming style.

#### Expression Statements
Explains that expressions can stand alone as statements (e.g., function calls, method calls).

##### Expression Statements and In-Place Changes
Warns about a common gotcha: `L.append(x)` returns `None` (modifies in place), so `L = L.append(x)` sets `L` to `None`.

#### Print Operations
Covers the `print()` function in detail.

##### The print Function
Full signature: `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`. Demonstrates each parameter with examples. Shows printing multiple objects, custom separators, custom line endings.

##### Print Stream Redirection
Demonstrates `print(file=f)` for writing to files. Shows `sys.stdout` reassignment for global redirection. Covers `io.StringIO` for capturing output to a string. Practical patterns for logging.

---

### Chapter 12. if and match Selections

Covers conditional branching with `if` and the newer `match` statement.

#### if Statements
Python's primary conditional construct.

##### General Format
Syntax: `if test: ... elif test: ... else: ...`. Notes `elif` can repeat, `else` is optional.

##### Basic Examples
Simple `if`, `if`/`else`, and `if`/`elif`/`else` demos.

##### Multiple-Choice Selections
Shows multi-way branching with chained `elif`. Demonstrates dictionary-based dispatch as an alternative to long `if`/`elif` chains.

#### match Statements
Python 3.10+ structural pattern matching.

##### Basic match Usage
Syntax: `match value: case pattern: ...`. Demonstrates matching against literal values, sequences, mappings, and captures. Shows the wildcard `_` pattern and `|` for alternatives.

##### Advanced match Usage
Guard clauses (`case x if x > 0`), class patterns (`case Point(x, y)`), nested patterns, starred patterns in sequences. Moderate depth — enough to understand and use the feature, not exhaustive coverage of all pattern forms.

#### Python Syntax Revisited
Formal summary of Python's syntax rules.

##### Block Delimiters: Indentation Rules
Reiterates indentation-as-syntax rules. Spaces vs. tabs (don't mix). Standard: 4 spaces. Notes `TabError` in Python 3.

##### Statement Delimiters: Lines and Continuations
Physical vs. logical lines. Backslash continuation, implicit continuation inside `()`, `[]`, `{}`. Semicolons for multiple statements on one line.

##### Special Syntax Cases in Action
Demonstrates multi-line conditions, long string literals, and chained assignments in practice.

#### Truth Values Revisited
Comprehensive review of what counts as true/false: `0`, `0.0`, `''`, `[]`, `{}`, `set()`, `None`, `False` are false; almost everything else is true. Short-circuit `and`/`or` — returns one of the operands, not necessarily `True`/`False`.

#### The if/else Ternary Expression
`result = X if condition else Y`. Shows use cases and nesting. Notes it's an expression (can appear inside other expressions), not a statement.

---

### Chapter 13. while and for Loops

Full treatment of both loop types and all loop control tools.

#### while Loops
Python's general-purpose loop.

##### General Format
`while test: body` with optional `else` clause.

##### Examples
Counting loops, interactive input loops, sentinel loops. Shows basic patterns.

#### break, continue, pass, and the Loop else
Loop control statements — each covered individually.

##### General Loop Format
Shows the full `while`/`for` syntax with all optional clauses: `break`, `continue`, and `else`.

##### pass
The no-operation statement. Used as a placeholder in empty blocks. Notes the `...` (Ellipsis) alternative.

##### continue
Jumps to the top of the enclosing loop for the next iteration. Shows filtering patterns (skip items meeting a condition).

##### break
Exits the enclosing loop immediately. Shows search/sentinel patterns.

##### Loop else
The `else` clause on `while` and `for` loops: runs only if the loop completes normally (no `break`). Shows the search-with-default pattern. Detailed explanation — this is a Python-specific feature unfamiliar to most programmers.

#### for Loops
Python's iteration loop — more commonly used than `while`.

##### General Format
`for target in iterable: body` with optional `else`. Explains that `for` works with any iterable object.

##### Examples
Iterating over: lists, strings, tuples, dictionary keys/values/items, ranges, files, and nested sequences (tuple unpacking in `for`). Multiple examples including practical patterns.

#### Loop Coding Techniques
Comprehensive section on iteration idioms and tools.

##### Counter Loops: range
`range(start, stop, step)` for generating integer sequences. Shows use as a loop counter and for index-based iteration.

##### Sequence Scans: while, range, and for
Compares three ways to scan a sequence: `while` with index, `for` with `range(len(L))`, and `for item in L`. Notes that direct `for` iteration is preferred.

##### Sequence Shufflers: range and len
Using `range(len(L))` to access items by offset for shuffling or reordering.

##### Skipping Items: range and Slices
Using `range(0, n, 2)` or slicing (`L[::2]`) to process every other item.

##### Changing Lists: range and Comprehensions
Patterns for modifying a list: `for i in range(len(L)): L[i] = ...` vs. list comprehension to build a new list. Notes comprehension is usually preferred.

##### Parallel Traversals: zip
`zip(L1, L2, ...)` to iterate over multiple sequences in parallel. Shows `zip` for building dictionaries, transposing matrixes, and the `zip_longest` alternative.

##### Offsets and Items: enumerate
`enumerate(iterable, start=0)` returns (index, item) pairs. Shows use for offset tracking during iteration.

---

### Chapter 14. Iterations and Comprehensions

Dives into the iteration protocol and comprehension syntax. Bridges the statement chapters with the advanced functional topics in Part IV.

#### Iterations
Covers the iteration protocol that underlies `for` loops and many built-in tools.

##### The Iteration Protocol
Explains `__iter__()` and `__next__()` (or `__getitem__()` as fallback). Shows manual iteration with `iter()` and `next()`. Demonstrates `StopIteration`. Explains the difference between iterables (have `__iter__`) and iterators (have `__next__`). Shows that file objects are their own iterators. ~5 pages.

##### Other Built-in Iterables
Demonstrates that `range`, `map`, `zip`, `filter`, `enumerate`, `open`, dictionary views (`.keys()`, `.values()`, `.items()`), and `os.popen` are all iterables/iterators. Shows that iterators are single-pass and exhaustible. Notes `list()` to materialise an iterator. ~5 pages.

#### Comprehensions
Systematic treatment of list comprehensions (building on earlier previews).

##### List Comprehension Basics
`[expression for item in iterable]`. Shows equivalence to a `for` loop with `append`. Notes comprehensions are often faster due to internal optimisation.

##### List Comprehensions and Files
Demonstrates `[line.rstrip() for line in open('file')]` and similar file-processing patterns.

##### Extended List Comprehension Syntax
Adding `if` filters: `[x for x in L if x > 0]`. Nested `for` clauses: `[x*y for x in A for y in B]`. Shows that nested `for` corresponds to nested loops.

##### Comprehensions Cliff-Hanger
Notes that set, dict, and generator comprehensions exist but will be covered in Chapter 20.

#### Iteration Tools
Brief survey of iteration-related built-in functions: `sum()`, `any()`, `all()`, `max()`, `min()`, `sorted()`, `zip()`, `map()`, `filter()`, and `functools.reduce()`. Notes they all accept iterables.

#### Other Iteration Topics
Forward references to generator functions/expressions (Chapter 20) and user-defined iterable classes (Chapter 30).

---

### Chapter 15. The Documentation Interlude

Covers all available Python documentation tools and common coding mistakes.

#### Python Documentation Sources
Survey of documentation methods.

##### # Comments
In-line and block comments. Notes the `#` comment convention and that comments are for programmers, not users.

##### The dir Function
Using `dir()` and `dir(object)` to list available attributes. Shows how to filter results (e.g., ignoring `__dunder__` names). Explains it works on modules, types, and instances.

##### Docstrings and \_\_doc\_\_
The triple-quoted string convention at the top of modules, functions, classes, and methods. Shows how to access via `object.__doc__`. Explains docstring conventions (first line as summary, blank line, detailed description).

##### Pydoc: The help Function
Using `help()` interactively. Shows `help(str)`, `help(str.replace)`, `help(module)`. Explains the output format.

##### Pydoc: HTML Reports
Generating HTML documentation: `python -m pydoc -b` for a browser-based documentation server, `python -m pydoc -w module` for writing HTML files. Shows the interface.

##### Beyond Docstrings: Sphinx
Brief mention of Sphinx for professional documentation projects. Notes reStructuredText format, autodoc extension, and ReadTheDocs hosting.

##### The Standard Manuals
Points to docs.python.org: Library Reference, Language Reference, Tutorial, and What's New. Explains when each is useful.

##### Web Resources
Mentions PyPI, Stack Overflow, Real Python, PEPs, and other community resources.

#### Common Coding Gotchas
Checklist of frequent beginner mistakes: forgetting colons, mixing tabs and spaces, misspelling names, using `=` instead of `==`, calling functions without parentheses, improper indentation, etc.

---

## Part IV. Functions and Generators

The functional programming core. Covers function definition, scope rules, argument passing, advanced function topics (recursion, lambdas, generators, comprehensions, async), and benchmarking.

---

### Chapter 16. Function Basics

Introduction to function definition and calling. Establishes fundamental concepts.

#### Why Use Functions?
Motivates functions: code reuse, procedural decomposition, consistency, reducing redundancy. Brief.

#### Function Coding Overview
Roadmap of function tools covered in this part.

##### Basic Function Tools
`def`, `return`, arguments. Notes these are the core mechanisms.

##### Advanced Function Tools
Lists generators, lambdas, decorators, annotations as advanced topics to come.

##### General Function Concepts
Functions are objects. `def` creates an object and assigns it to a name. Functions can be passed, stored, and called.

##### def Statements
Syntax: `def name(args): body`. Notes that `def` is an executable statement (creates the function object at runtime).

##### return Statements
`return value` sends a result back to the caller. Functions without `return` return `None`.

##### def Executes at Runtime
Emphasises that `def` is not a compile-time declaration — it runs when reached. Functions can be defined conditionally.

##### lambda Makes Anonymous Functions
Brief preview: `lambda args: expression` creates a small unnamed function. Full treatment in Chapter 19.

#### A First Example: Definitions and Calls
Walks through a simple function definition and calling.

##### Definition
Defines a function that computes the intersection of two sequences.

##### Calls
Calls the function with various arguments and shows results.

##### Polymorphism in Python
Shows that the intersection function works with lists, strings, tuples — any sequence type — without modification. First explicit discussion of Python's duck-typing polymorphism.

#### A Second Example: Intersecting Sequences
A more developed function example.

##### Definition
A function using nested `for` loops and `if`/`in` to build an intersection list.

##### Calls
Demonstrates calls with lists, strings, and mixed types.

##### Polymorphism Revisited
Reinforces that the function works with any iterable, not just lists. Explains why this is powerful.

##### Segue: Local Variables
Notes that variables assigned inside a function are local — they exist only during the function call. Previews scope rules (Chapter 17).

---

### Chapter 17. Scopes

Deep treatment of Python's name-resolution rules. One of the more conceptually important chapters.

#### Python Scopes Basics
Introduces the scope concept: where a name is visible and accessible.

##### Scopes Overview
Defines the four scope layers: Local (inside the current function), Enclosing (enclosing function for nested functions), Global (module level), Built-in (`builtins` module). Diagrams the layers.

##### Name Resolution: The LEGB Rule
Explains lookup order: Local → Enclosing → Global → Built-in. Shows that assignment creates a name in the local scope by default. ~3 pages with multiple examples.

##### Scopes Examples
Interactive demonstrations of LEGB lookup at various levels. Shows local hiding global, and accessing globals from functions.

##### The Built-in Scope
Explains that `builtins` is a module automatically available. Shows `import builtins; dir(builtins)`. Notes that you can override built-in names (and why you shouldn't).

#### The global Statement
Declaring names to be at module (global) scope.

##### Program Design: Minimize Global Variables
Argues against relying on globals for function communication. Functions should use arguments and return values. Globals create hidden dependencies.

##### Program Design: Minimize Cross-File Changes
Warns against modifying another module's globals directly (e.g., `mod.X = 5`). Recommends using setter functions instead. Explains the maintenance risks.

##### Other Ways to Access Globals
Shows `globals()` dictionary, and the `sys.modules` trick for accessing any module's namespace.

#### Nested Functions and Scopes
The "Enclosing" layer of LEGB — closures.

##### Nested Scopes Overview
Explains that an inner function can reference names from the enclosing function's scope, even after the enclosing function has returned.

##### Nested Scopes Examples
Demonstrates a nested function reading a variable from its enclosing scope. Shows the closure in action.

##### Closures and Factory Functions
Functions that return other functions, with enclosed state. Shows practical patterns: callback customisation, function factories. Multiple examples.

##### Arbitrary Scope Nesting
Notes that nesting can go to any depth. LEGB walks up through all enclosing functions.

#### The nonlocal Statement
Declaring names to be in an enclosing (not global) scope.

##### nonlocal Basics
Syntax: `nonlocal name`. Allows assignment to a name in an enclosing function's scope.

##### nonlocal in Action
Demonstrates counter functions and state-retention patterns using `nonlocal`. Compares with global approach.

##### nonlocal Boundary Cases
Rules: the name must already exist in an enclosing scope. `nonlocal` only applies to enclosing function scopes, not module scope. Shows error cases.

#### State-Retention Options
Comprehensive comparison of four techniques for retaining state between function calls.

##### Nonlocals: Changeable, Per-Call, LEGB
Shows closure-based state retention. Each call to the factory function creates independent state.

##### Globals: Changeable but Shared
Shows global-variable state retention. Simpler but state is shared across all callers.

##### Function Attributes: Changeable, Per-Call, Explicit
Shows `func.attr = value` for attaching state directly to function objects. Per-function-object, not per-call.

##### Classes: Changeable, Per-Call, OOP
Shows class-based state retention via `__init__` and instance attributes. The OOP approach.

##### And the Winner Is…
Notes that all four have valid uses. Closures for simple state; classes for complex state with methods; globals and function attributes for specialised cases.

#### Scopes and Argument Defaults
Explains that default argument values are evaluated once at `def` time, not at each call.

##### Loops Require Defaults, Not Scopes
Shows the classic closure-in-a-loop bug: all closures capture the same variable. Solution: use default arguments to capture the current value. Detailed example.

---

### Chapter 18. Arguments

Comprehensive treatment of how arguments are passed, matched, and ordered.

#### Argument-Passing Basics
How Python passes arguments to functions.

##### Arguments and Shared References
Arguments are passed by assigning objects to local names (shared references). The function gets a reference to the same object — not a copy. Demonstrates with immutable and mutable arguments.

##### Avoiding Mutable Argument Changes
Strategies to prevent unintended mutation of caller's data: pass copies (`L[:]`, `dict.copy()`), copy inside the function, or document the expected behaviour.

##### Simulating Output Parameters and Multiple Results
Returning tuples to simulate multiple return values. Tuple unpacking at the call site. Shows this is idiomatic Python.

#### Special Argument-Matching Modes
Covers all of Python's argument matching features.

##### Argument Matching Overview
Lists all modes: positional, keyword, default, `*args`, `**kwargs`, keyword-only, positional-only. Notes that Python has more argument-matching modes than most languages.

##### Argument Matching Syntax
Reference table of all syntax forms in both function definitions and calls.

##### Argument Passing Details
Step-by-step explanation of how Python matches arguments to parameters at call time. Covers the priority order.

##### Keyword and Default Examples
Demonstrates `def f(a, b=0, c=1)` and calls with mixed positional/keyword arguments. Shows how defaults work.

##### Arbitrary Arguments Examples
`*args` (collects extra positionals into a tuple) and `**kwargs` (collects extra keywords into a dict). Shows unpacking at call sites: `f(*L)` and `f(**D)`. Multiple examples.

##### Keyword-Only Arguments
Parameters after `*` or `*args` must be passed by keyword: `def f(a, *, key=val)`. Explains the rationale (forcing clarity at call sites). Python 3 only.

##### Positional-Only Arguments
Parameters before `/` must be passed positionally: `def f(a, b, /, c)`. Explains the rationale (allowing parameter name changes without breaking callers). Python 3.8+.

#### Argument Ordering: The Gritty Details
Full specification of argument-ordering rules.

##### Definition Ordering
Required order in `def`: positional → `*args` → keyword-only → `**kwargs`, with `/` for positional-only. Full examples of each combination.

##### Calls Ordering
Ordering rules at the call site: positionals, then keywords, then `*iterable`, then `**dict`. Shows how they interact.

#### Example: The min Wakeup Call
Worked example reimplementing the built-in `min()` function using various argument features.

##### Full Credit
Builds a `min()` using `*args` to accept arbitrary arguments.

##### Bonus Points
Enhances it with keyword-only arguments for a `key=` function parameter.

##### The Punch Line
Reveals that Python's built-in `min()` already does this — but the exercise teaches argument-matching features.

#### Example: Generalized Set Functions
Builds intersection and union functions that work with any number of sequences.

##### Testing the Code
Demonstrates the functions with various inputs.

#### Example: Rolling Your Own Print
Builds a custom `print`-like function to demonstrate keyword arguments.

##### Using Keyword-Only Arguments
Shows how keyword-only arguments (after `*`) are perfect for option flags like `sep=` and `end=`.

---

### Chapter 19. Function Odds and Ends

Remaining function topics: design, recursion, first-class functions, lambdas, and functional programming tools.

#### Function Design Concepts
Guidelines for function design: keep functions small, give them one clear purpose, use arguments and return values (not globals), avoid side effects where possible. Cohesion and coupling principles. ~2 pages.

#### Recursive Functions
Full treatment of recursion in Python.

##### Summation with Recursion
Classic recursive sum function. Shows base case and recursive case.

##### Coding Alternatives
Builds alternative solutions: `while` loop, `for` loop, `sum()`, showing recursion vs. iteration.

##### Loop Statements Versus Recursion
Discusses when recursion is appropriate (tree structures, divide-and-conquer) vs. when loops are better (simple iteration). Notes Python's recursion limit (`sys.setrecursionlimit()`).

##### Handling Arbitrary Structures
Recursive processing of nested/tree-like data (lists of lists, dictionaries). Shows `isinstance()` dispatch for handling mixed types. Practical examples of walking nested structures. ~4 pages.

#### Function Tools: Attributes, Annotations, Etc.
Advanced function features.

##### The First-Class Object Model
Explains that functions are objects: they can be assigned to variables, stored in lists/dicts, passed as arguments, returned from functions. Shows practical implications.

##### Function Introspection
Examining function objects: `func.__name__`, `func.__doc__`, `func.__defaults__`, `func.__code__`, `func.__module__`, `func.__dict__`, `func.__annotations__`. Brief demonstration of each.

##### Function Attributes
Attaching arbitrary attributes to functions: `func.count = 0`. Shows use for state retention. Notes functions are just objects with a `__dict__`.

##### Function Annotations and Decorations
Annotation syntax: `def f(x: int, y: str = '') -> bool:`. Stored in `func.__annotations__` as a dict. Not enforced at runtime — used by external tools (mypy, IDE hints). Brief mention of decorators (preview for Chapter 39).

#### Anonymous Functions: lambda
Full treatment of `lambda` expressions.

##### lambda Basics
Syntax: `lambda args: expression`. Returns a function object. Limited to a single expression (no statements). Shows basic usage.

##### Why Use lambda?
Use cases: short callbacks, `sort(key=lambda x: x[1])`, inline in function calls, jump tables (dicts of lambdas). Notes lambdas are most useful when a function is used once in a limited context.

##### How (Not) to Obfuscate Your Python Code
Warns against complex/nested lambdas. Shows unreadable lambda abuse vs. readable `def` equivalent. Argues for readability.

##### Scopes: lambdas Can Be Nested Too
Lambdas participate in LEGB scoping just like `def` functions. Shows closures created with lambdas.

#### Functional Programming Tools
Python's built-in functional tools.

##### Mapping Functions over Iterables: map
`map(func, iterable)` applies a function to every item. Shows `map(str.upper, words)` and `map(pow, [1,2,3], [4,5,6])`. Compares with comprehensions.

##### Selecting Items in Iterables: filter
`filter(func, iterable)` keeps items where `func` returns true. Shows equivalence to comprehension with `if`.

##### Combining Items in Iterables: reduce
`functools.reduce(func, iterable)` accumulates a result across items. Shows sum, product, max patterns. Notes that explicit loops are often clearer.

---

### Chapter 20. Comprehensions and Generations

Advanced iteration: completes comprehension coverage and introduces generators and async functions.

#### Comprehensions: The Final Act
Finalises comprehension syntax coverage.

##### List Comprehensions Review
Recap: `[expr for x in iter if cond]`. Shows equivalence to loop + append.

##### Formal Comprehension Syntax
Full syntax: set comprehensions (`{expr for ...}`), dictionary comprehensions (`{k: v for ...}`), generator expressions (`(expr for ...)`). Shows all four forms side by side.

##### Example: List Comprehensions and Matrixes
Builds matrix operations (row extraction, column extraction, transposition) using comprehensions. Shows nested comprehensions for 2D processing. ~3 pages.

#### Generator Functions and Expressions
Major section on lazy iteration.

##### Generator Functions: yield Versus return
Defines generator functions (using `yield`). Shows state suspension and resumption. Demonstrates that generators produce one item at a time, saving memory. Shows the iterator protocol (`__iter__`, `__next__`, `StopIteration`). Covers `send()` to push values into generators, `throw()` to inject exceptions, and `close()` to terminate. ~6 pages.

##### Generator Expressions: Iterables Meet Comprehensions
`(expr for x in iter if cond)` — parenthesized comprehension that returns a generator. Shows memory savings for large datasets. Demonstrates use in `sum()`, `max()`, `any()`, `all()`, and `''.join()`.

##### Generator Functions Versus Generator Expressions
Compares when to use each. Generator functions for complex logic; expressions for simple transformations. Notes that generator expressions can replace `map()` and `filter()`.

##### Generator Odds and Ends
`yield from` for delegating to sub-generators. Generator return values (`return value` in generator → `StopIteration.value`). Generator-based `__iter__` for classes. Recursive generators. `sys.getrefcount()` and generator lifecycle. ~4 pages.

#### Example: Shuffling Sequences
Worked example using generators and comprehensions.

##### Scrambling Sequences
Generator function that produces all rotations of a sequence. Shows both generator and list-based approaches.

##### Permutating Sequences
Recursive generator function for all permutations of a sequence. Demonstrates recursive `yield from`. ~3 pages.

#### Example: Emulating zip and map
Reimplements built-in tools to demonstrate generator patterns.

##### Coding Your Own map
Multiple versions of `map()`: list-based, generator-based, and multi-iterable.

##### Coding Your Own zip and 2.X map
Multiple versions of `zip()`: using `while`/indexing, using iterators, and generators. Also shows Python 2.X `map` padding behaviour reimplemented.

#### Asynchronous Functions: The Short Story
Introduction to async programming in Python.

##### Async Basics
`async def` to define coroutines, `await` to pause for results, `asyncio.run()` to start the event loop. Shows `asyncio.gather()` for concurrency. Demonstrates async generators (`async for`) and async comprehensions. Covers `asyncio.sleep()`, task creation, and basic event-loop mechanics. ~6 pages.

##### The Async Wrap-Up
Notes that full async programming is beyond the book's scope. Points to `asyncio` docs. Mentions `trio` and `anyio` as alternatives.

---

### Chapter 21. The Benchmarking Interlude

Practical chapter on measuring and comparing code performance, plus function gotchas.

#### Benchmarking with Homegrown Tools
Builds custom timing tools to benchmark different Python constructs.

##### Timer Module: Take 1
A simple function-based timer using `time.perf_counter()`. Shows basic timing of code snippets.

##### Timer Module: Take 2
A more robust version using a class with `__enter__`/`__exit__` (context manager). Shows timing with `with` blocks.

##### Timing Runner and Script
A script that compares multiple code techniques (for loops, list comprehensions, `map()`, generator expressions) across iterations. Shows the test harness.

##### Iteration Results
Presents and analyses timing results. Discusses relative performance of iteration tools: comprehensions and `map()` typically faster than `for` loops. Notes that results vary by Python version and task.

##### More Module Mods
Enhances the timer module with additional features: reporting format, best-of-N timing, callable timing vs. code-string timing.

#### Benchmarking with Python's timeit
Covers Python's standard `timeit` module.

##### Basic timeit Usage
Command-line usage: `python -m timeit "code"` with `-s` for setup. API usage: `timeit.timeit()`, `timeit.repeat()`. Shows how timeit manages timing loops and repetitions automatically.

##### Automating timeit Benchmarking
Building scripts that automate timeit runs across multiple techniques and report comparative results. Shows practical automation patterns.

#### Function Gotchas
Common function pitfalls.

##### Local Names Are Detected Statically
Python determines local vs. global at compile time, not runtime. Shows the `UnboundLocalError` that occurs when a name is assigned later in a function but referenced before assignment. Explains the fix (`global` or reordering).

##### Defaults and Mutable Objects
The classic mutable default argument bug: `def f(L=[])` shares one list across all calls. Shows the problem and the fix (`def f(L=None): if L is None: L = []`).

##### Functions Without returns
Functions without `return` return `None`. Shows the gotcha of assigning the result of such a function.

##### Miscellaneous Function Gotchas
Brief notes on: enclosing scope loop variables, lambda scoping, and mixing `*args` ordering.

---

## Part V. Modules and Packages

Covers Python's module and package system: importing, namespaces, the module search path, packages, and advanced module topics.

---

### Chapter 22. Modules: The Big Picture

Conceptual overview of the module system.

#### Module Essentials
Defines a module as a file containing Python code: the highest-level program organization unit (after packages). Modules provide namespaces, code reuse, and system organization.

#### Why Use Modules?
Code reuse (write once, import anywhere), system partitioning (manageable pieces), namespace management (avoiding name clashes). Brief.

#### Python Program Architecture
How programs are structured with modules.

##### How to Structure a Program
One top-level "script" file plus zero or more imported module files. Shows the common pattern.

##### Imports and Attributes
`import` creates a module object; attributes are accessed via `module.name`. Shows how imports connect files.

##### Standard-Library Modules
Notes that Python ships with a large standard library of pre-built modules. Points to docs.python.org library reference.

#### How Imports Work
The three-step import process.

##### Step 1: Find It
Python searches the module search path to locate the file. Covers the search order.

##### Step 2: Compile It (Maybe)
If the source is newer than the cached `.pyc` file (or no `.pyc` exists), Python compiles to bytecode and saves it in `__pycache__`. Explains `.pyc` file naming (includes Python version).

##### Step 3: Run It
The module's top-level code is executed. All assignments create module attributes. This happens only on the *first* import.

#### The Module Search Path
Detailed treatment of where Python looks for modules.

##### Search-Path Components
The home directory (script location or CWD), `PYTHONPATH` environment variable, `.pth` path files, standard library directories, and `site-packages`. Explains the order.

##### Configuring the Search Path
Setting `PYTHONPATH`, creating `.pth` files in site directories, modifying `sys.path` at runtime.

##### The sys.path List
`sys.path` is the runtime search path. Shows how to inspect and modify it. Notes it's initialised from the search-path components.

##### Module File Selection
Which file types Python imports: `.py` source, `.pyc` bytecode, C extensions (`.so`/`.pyd`), package directories, built-in modules, zip imports.

##### Path Outliers: Standalones and Packages
Notes that standalone executables (PyInstaller) and namespace packages have special search-path behaviour.

---

### Chapter 23. Module Coding Basics

Hands-on module creation and usage.

#### Creating Modules
How to make a module.

##### Module Filenames
Any `.py` file is a module. The filename (minus `.py`) becomes the module name. Notes that module names must be valid Python identifiers.

##### Other Kinds of Modules
C extensions, built-in modules (compiled into the interpreter), package directories, zip files.

#### Using Modules
All the ways to import and use modules.

##### The import Statement
`import module` creates a module object in the caller's namespace. Access via `module.name`. Shows basic usage.

##### The from Statement
`from module import name` copies specific names into the caller's namespace directly. Shows usage and notes it's an assignment.

##### The from \* Statement
`from module import *` copies all names (or those in `__all__`). Notes this is generally discouraged in code but convenient interactively.

##### Imports Happen Only Once
On first import, the module is found, compiled, and run. Subsequent imports reuse the already-loaded module object. Demonstrates this.

##### Imports Are Runtime Assignments
`import` is an executable statement, not a compile-time directive. Module objects and names are created at runtime.

##### import and from Equivalence
Shows that `from mod import x` is equivalent to `import mod; x = mod.x; del mod` (conceptually). Both run the module.

##### Potential Pitfalls of the from Statement
Warns: `from` creates copies of names, not links. Changing the name in the importing module doesn't affect the original. Also, `from *` can overwrite existing names silently.

#### Module Namespaces
How modules create and manage namespaces.

##### How Files Generate Namespaces
All top-level assignments in a module file create attributes of the module object. The module's namespace is its `__dict__`.

##### Namespace Dictionaries: \_\_dict\_\_
Shows `module.__dict__` or `vars(module)` to inspect all module attributes. Includes system attributes like `__name__`, `__file__`, `__doc__`.

##### Attribute Name Qualification
Explains `object.name` qualification syntax. Shows how it applies to modules, classes, and instances uniformly.

##### Imports Versus Scopes
Imports do not nest scopes — they just assign names. A module's code always has access to its own globals, not the importer's.

##### Namespace Nesting
Shows modules importing from other modules: chains of attribute access (`A.B.C`).

#### Reloading Modules
Re-running a module's code without restarting Python.

##### reload Basics
`importlib.reload(module)` re-runs the module's top-level code. Notes it modifies the existing module object in place — doesn't create a new one.

##### reload Example
Demonstrates reloading during interactive development: change file, reload, see new behaviour.

##### reload Odds and Ends
Caveats: `from` imports aren't updated by reload, `reload` is transitive (doesn't reload dependencies), and class instances retain old methods.

---

### Chapter 24. Module Packages

Full treatment of Python's package system for organizing modules in directories.

#### Using Packages
How to import from packages.

##### Package Imports
Dotted import paths: `import dir1.dir2.module`, `from dir1.dir2 import module`. Shows the syntax and semantics.

##### Packages and the Module Search Path
Only the top-level package directory needs to be on `sys.path`. Subdirectories are found via the package structure.

#### Creating Packages
How to set up a package directory structure.

##### Basic Package Structure
Directories with `__init__.py` files. Shows a typical layout and explains the role of each file.

##### Package \_\_init\_\_.py Files
Run automatically on first package import. Used for package initialisation, declaring `__all__`, and establishing the package namespace. Shows examples.

##### Package \_\_main\_\_.py Files
Makes a package runnable with `python -m package`. Contains the code that runs when the package is executed as a script.

#### Why Packages?
Motivation for using packages.

##### A Tale of Two Systems
Worked example showing how packages disambiguate same-named modules in different subsystems. Demonstrates the problem and the package-based solution.

#### The Roles of \_\_init\_\_.py Files
Detailed discussion of `__init__.py` purposes: package marker, initialisation code, `__all__` for `from pkg import *`, convenience imports (re-exporting submodule names at package level).

#### Package-Relative Imports
Imports relative to the current package.

##### Relative and Absolute Imports
`from .module import name` (relative), `from ..package import name` (parent), and plain `import module` (absolute). Shows the syntax.

##### Relative-Import Rationales and Trade-Offs
Explains why relative imports exist (avoiding name clashes with system modules, making packages self-contained). Notes the controversy and style preferences.

##### Package-Relative Imports in Action
Worked examples showing relative imports in a multi-level package. Demonstrates various relative import forms and their effects.

#### Namespace Packages
Packages without `__init__.py` (Python 3.3+).

##### Python Import Models
Explains the three import models: regular packages (with `__init__.py`), namespace packages (without), and module imports.

##### Namespace-Package Rationales
Use cases: splitting a package across multiple directories (e.g., plugins, separately installed components). Shows the motivation.

##### The Module Search Algorithm
Step-by-step: Python first looks for a regular package, then for a module, then for a namespace package (collecting all matching directories). Detailed explanation.

##### Namespace Packages in Action
Worked example demonstrating a namespace package split across two directories. Shows how imports resolve.

---

### Chapter 25. Module Odds and Ends

Remaining module topics: design, data hiding, introspection, string-based imports, and gotchas.

#### Module Design Concepts
Guidelines: minimise coupling between modules, maximise cohesion within modules, avoid modifying other modules' globals, use `__all__` and `_` prefixes for data hiding. Brief.

#### Data Hiding in Modules
Controlling what's exported from modules.

##### Minimizing from \* Damage: \_X and \_\_all\_\_
`_name` convention: names starting with underscore are not imported by `from mod import *`. `__all__` list: explicitly defines which names `from mod import *` exports. Shows both mechanisms.

##### Managing Attribute Access: \_\_getattr\_\_ and \_\_dir\_\_
Module-level `__getattr__(name)` (Python 3.7+) intercepts access to undefined module attributes. Module-level `__dir__()` customises `dir(module)` output. Shows use for deprecation warnings and lazy attribute loading.

#### Enabling Language Changes: \_\_future\_\_
`from __future__ import feature` enables features before they become default. Lists historically significant futures (annotations, division, print_function). Brief.

#### Dual-Usage Modes: \_\_name\_\_ and \_\_main\_\_
The `if __name__ == '__main__':` idiom for making files work both as importable modules and runnable scripts.

##### Example: Unit Tests with \_\_name\_\_
Shows placing test code under `if __name__ == '__main__':` so it runs only when the file is executed directly, not when imported.

#### The as Extension for import and from
`import module as alias` and `from module import name as alias`. Shows use for shortening long names and avoiding conflicts.

#### Module Introspection
Inspecting module attributes programmatically.

##### Example: Listing Modules with \_\_dict\_\_
Script that iterates over `module.__dict__` to list attributes with types and values. Shows `getattr()` and `dir()` usage.

#### Importing Modules by Name String
Dynamic imports when the module name is a string variable.

##### Running Code Strings
`exec('import ' + name)` — works but crude and has security risks.

##### Direct Calls: Two Options
`importlib.import_module(name)` (preferred) and `__import__(name)` (lower-level). Shows usage.

##### Example: Transitive Module Reloads
Extended worked example (~8 pages): a utility function that recursively reloads a module and all modules it imports. Demonstrates `importlib.reload()`, `sys.modules`, `__dict__` traversal, and cycle detection. Practical tool for development workflows.

#### Module Gotchas
Common module-related mistakes and surprises.

##### Module Name Clashes: Package and Package-Relative Imports
A file named `string.py` in your directory shadows the standard `string` module. Shows the problem and solutions (rename, use packages, relative imports).

##### Statement Order Matters in Top-Level Code
Module code runs top-to-bottom. Using a name before it's assigned at module level causes `NameError`. Shows the issue and fix.

##### from Copies Names but Doesn't Link
Reiterates: `from mod import X` creates a new local name `X`. Reassigning `X` locally doesn't affect `mod.X`.

##### from \* Can Obscure the Meaning of Variables
`from mod import *` silently introduces many names. Hard to tell where a name came from. Discourages this in production code.

##### reload May Not Impact from Imports
After `from mod import X`, reloading `mod` updates `mod.X` but not the local `X`. Must re-execute the `from` statement.

##### reload, from, and Interactive Testing
Combining `reload` with `from` in interactive sessions is error-prone. Recommends using `import mod` and `mod.name` during development.

##### Recursive from Imports May Not Work
If module A does `from B import X` and B does `from A import Y`, one of them may fail because the other isn't fully loaded yet. Explains the problem and workarounds (restructure, use `import`).

---

## Part VI. Classes and OOP

Object-oriented programming from basics through advanced topics. Builds from simple class syntax to multiple inheritance, operator overloading, decorators, metaclasses, and `super()`.

---

### Chapter 26. OOP: The Big Picture

Conceptual introduction to OOP in Python. No detailed code — establishes the mental model.

#### Why Use Classes?
Classes enable code reuse through inheritance, provide a way to organise state and behaviour, and create new object types. Explains OOP in practical terms.

#### OOP from 30,000 Feet
High-level tour of OOP concepts as they manifest in Python.

##### Attribute Inheritance Search
The core mechanism: when you access `object.name`, Python searches the instance, then its class, then all superclasses. Diagram-based explanation.

##### Classes and Instances
Classes are factories/templates; instances are the concrete objects created from them. Shows the relationship.

##### Method Calls
`instance.method()` → Python finds `method` in the class tree, then calls it with `instance` as the first argument (`self`).

##### Coding Class Trees
Shows how class definitions and inheritance create tree structures. `class` statements with parent classes in parentheses.

##### Operator Overloading
Classes can define `__add__`, `__str__`, `__getitem__`, etc. to make instances respond to built-in operations (`+`, `print`, `[]`, etc.). Brief preview.

##### OOP Is About Code Reuse
Frames the entire OOP system as a code-reuse mechanism: write general code in superclasses, specialise in subclasses.

---

### Chapter 27. Class Coding Basics

First hands-on class code. Three progressive examples plus exploration of classes under the hood.

#### Classes Generate Multiple Instance Objects
The class/instance creation model.

##### Class Objects Provide Default Behavior
`class` statements create class objects with shared attributes (data and methods) that serve as defaults for all instances.

##### Instance Objects Are Concrete Items
Calling a class creates an instance with its own namespace (`__dict__`). Instance attributes override class attributes.

##### A First Example
Simple class with two methods. Creates two instances, shows attribute assignment and access. Demonstrates that instances share the class's methods.

#### Classes Are Customized by Inheritance
How subclasses extend and specialise superclasses.

##### A Second Example
Defines a superclass and a subclass that overrides one method. Shows inheritance-based customisation.

##### Classes Are Attributes in Modules
Notes that class objects live in modules and can be imported just like any other module attribute.

#### Classes Can Intercept Python Operators
Operator overloading makes custom objects act like built-in types.

##### A Third Example
Class with `__init__`, `__add__`, `__mul__`, `__repr__`, and `__iter__`. Demonstrates a custom number-like object that supports arithmetic and display.

#### The World's Simplest Python Class
An empty `class` used as a record/namespace (just `class C: pass`; then `C.name = value`).

##### Classes: Under the Hood
Shows `instance.__dict__`, `instance.__class__`, `class.__bases__`. Demonstrates the attribute tree with code.

##### Records Revisited: Classes Versus Dictionaries
Compares using classes vs. dicts for record-like data. Shows trade-offs: classes give methods and inheritance; dicts give flexibility and JSON compatibility.

---

### Chapter 28. A More Realistic Example

The book's most extended worked example: building a `Person`/`Manager` class hierarchy in 7 progressive steps. ~30 pages.

#### Step 1: Making Instances
Building the basic class with constructors.

##### Coding Constructors
`__init__` method: receives `self` and initial attribute values. Shows attribute assignment via `self.name = name`.

##### Testing as You Go
Demonstrates testing each step interactively. Emphasises incremental development.

##### Using Code Two Ways
Shows the `if __name__ == '__main__':` pattern so the module can be both imported and run directly.

#### Step 2: Adding Behavior Methods
Adding methods that operate on instance data.

##### Coding Methods
Methods that access and modify `self.attr`. Shows a `giveRaise()` method that modifies salary.

#### Step 3: Operator Overloading
Making instances printable.

##### Providing Print Displays
`__repr__` method to customise how instances appear in `print()` and the interactive prompt.

#### Step 4: Customizing Behavior by Subclassing
Creating a `Manager` subclass of `Person`.

##### Coding Subclasses
`class Manager(Person):` inherits all of `Person`'s methods and attributes.

##### Augmenting Methods: The Bad Way
Directly copying and modifying superclass code in the subclass. Shows why this is bad (code duplication).

##### Augmenting Methods: The Good Way
Calling the superclass method and extending it: `Person.giveRaise(self, ...)` or `super().giveRaise(...)`.

##### Polymorphism in Action
Shows that code written for `Person` objects works unchanged with `Manager` objects. The same interface, different behaviour.

##### Inherit, Customize, and Extend
Summarises the pattern: inherit defaults, override/extend what differs.

##### OOP: The Big Idea
OOP lets you build specialised objects from general ones. Relates to real-world software maintenance.

#### Step 5: Customizing Constructors, Too
Overriding `__init__` in `Manager` to add manager-specific attributes.

##### OOP Is Simpler Than You May Think
Reassurance that the basic patterns are straightforward: classes, inheritance, overriding.

##### Other Ways to Combine Classes: Composites
Introduces composition ("has-a"): embedding one object inside another instead of inheriting. Shows a `Department` class that contains `Person`/`Manager` objects.

#### Step 6: Using Introspection Tools
Building tools that examine class hierarchies at runtime.

##### Special Class Attributes
`instance.__class__`, `class.__name__`, `class.__bases__`, `instance.__dict__`. Shows what they contain and how to use them.

##### A Generic Display Tool
Builds a mixin class that provides a `__repr__` showing all instance attributes. Uses `__dict__` iteration.

##### Instance Versus Class Attributes
Clarifies what lives in instance `__dict__` vs. class `__dict__`. Shows how to distinguish them.

##### Name Considerations in Tool Classes
Discusses naming attributes to avoid collisions in mix-in classes (underscore prefixes, etc.).

##### Our Classes' Final Form
Shows the complete `Person`/`Manager` code after all enhancements.

#### Step 7 (Final): Storing Objects in a Database
Persisting the class hierarchy using `pickle` and `shelve`.

##### Pickles and Shelves
Reviews `pickle` (serialise any Python object) and `shelve` (persistent dictionary backed by a database file).

##### Storing Objects on a shelve Database
Demonstrates creating a shelve, storing `Person` and `Manager` instances by key, and closing.

##### Exploring Shelves Interactively
Reopening the shelve and accessing stored objects. Shows that objects retain their class and methods.

##### Updating Objects on a Shelf
Modifying a stored object: retrieve, change, store back. Shows the fetch-modify-store pattern.

#### Future Directions
Notes that the example could be extended with GUIs, web interfaces, or more database tools. Points to the companion book *Programming Python* for application-level development.

---

### Chapter 29. Class Coding Details

Reference-style chapter covering class mechanics systematically.

#### The class Statement
Formal class syntax.

##### General Syntax and Usage
`class Name(Superclass1, ...): body`. The class body runs in a new namespace. Assignments create class attributes. Methods are functions assigned as class attributes.

##### Example: Class Attributes
Shows data attributes and method attributes defined in the class body. Demonstrates that class attributes are shared by all instances.

#### Methods
How methods work.

##### Method Example
Defines and calls methods. Shows that `self` is passed automatically and refers to the instance.

##### Other Method-Call Possibilities
Calling unbound methods via the class: `Class.method(instance, args)`. Calling methods on other objects. Shows that methods are just functions with a class residence.

#### Inheritance
Detailed coverage of inheritance mechanics.

##### Attribute Tree Construction
Explains how `class` and instance creation build the attribute tree. Shows the search order: instance → class → superclasses (left-to-right, depth-first or MRO).

##### Inheritance Fine Print
Notes: multiple inheritance order matters, `object` is the implicit root, new-style class behaviour.

##### Specializing Inherited Methods
Overriding: define a method with the same name. Extending: call the superclass version and add to it.

##### Class Interface Techniques
Using inheritance to define interfaces: mix of abstract and concrete methods. Shows a class where subclasses must provide certain methods.

##### Abstract Superclasses
Using the `abc` module: `@abstractmethod` decorator, `ABC` base class. Shows how to enforce that subclasses implement required methods. Attempts to instantiate an abstract class raise `TypeError`.

#### Namespaces: The Conclusion
The definitive treatment of namespaces bringing together all prior discussion.

##### Simple Names: Global Unless Assigned
Unqualified names follow LEGB rules. Assignment makes a name local.

##### Attribute Names: Object Namespaces
Qualified names (`obj.name`) use the object's namespace (instance → class → superclass tree, or module `__dict__`).

##### The "Zen" of Namespaces: Assignments Classify Names
Where you assign a name determines its scope/namespace: inside `def` → local, inside `class` → class attribute, at module top level → module global. The single most important rule in Python scoping.

##### Nested Classes: The LEGB Scopes Rule Revisited
Classes nested inside functions or other classes. Notes that class bodies do *not* create an enclosing scope for LEGB purposes — this surprises many people. Shows the workaround (pass via arguments or defaults).

##### Namespace Dictionaries: Review
Shows `__dict__` for instances, classes, and modules. Ties together the attribute lookup chain with `__dict__` access.

##### Namespace Links: A Tree Climber
A utility function that walks the inheritance tree, printing all attributes at each level. Shows the class hierarchy structure concretely.

#### Documentation Strings Revisited
Docstrings in class and method definitions. Accessing via `Class.__doc__`, `instance.method.__doc__`. Notes conventions.

#### Classes Versus Modules
Comparison: modules are single files, classes can have multiple instances; modules are imported, classes are called; modules have module-level state, classes have per-instance and per-class state.

---

### Chapter 30. Operator Overloading

Comprehensive reference to Python's operator overloading methods. ~40 pages of detailed coverage.

#### The Basics
Overview of operator overloading in Python.

##### Constructors and Expressions: \_\_init\_\_ and \_\_sub\_\_
Shows `__init__` (called on instance creation) and `__sub__` (called for `-` operator). Establishes the pattern: define a dunder method → instances support the corresponding operation.

##### Common Operator-Overloading Methods
Reference table of commonly used dunder methods and the operations they intercept.

#### Indexing and Slicing: \_\_getitem\_\_ and \_\_setitem\_\_
Making instances support `[]` access.

##### Intercepting Slices
Shows that `__getitem__` receives a `slice` object when called with slice syntax. How to handle both integer and slice arguments.

##### Intercepting Item Assignments
`__setitem__` for `obj[key] = value`. Shows assignment to indices and slices.

##### But \_\_index\_\_ Means As-Integer
Clarifies that `__index__` is unrelated to indexing — it converts an object to an integer for use as an actual index in other sequences. Shows usage with `hex()`, `oct()`, `bin()`.

#### Index Iteration: \_\_getitem\_\_
If a class defines `__getitem__` but not `__iter__`, Python falls back to calling `__getitem__` with successive integer indices (0, 1, 2, ...) until `IndexError`. Shows this legacy iteration protocol.

#### Iterable Objects: \_\_iter\_\_ and \_\_next\_\_
The modern iteration protocol.

##### User-Defined Iterables
Class that defines `__iter__` (returns the iterator object) and `__next__` (returns the next value or raises `StopIteration`). Full example of a custom range-like iterable.

##### Multiple Iterators on One Object
Implementing `__iter__` to return a separate iterator object (not `self`) so multiple `for` loops can iterate independently over the same object. Shows the pattern with a helper iterator class.

##### Coding Alternative: \_\_iter\_\_ Plus yield
Using `yield` inside `__iter__` to make a generator-based iterator. Simpler than a separate iterator class. Shows the pattern and compares.

#### Membership: \_\_contains\_\_, \_\_iter\_\_, and \_\_getitem\_\_
The `in` operator calls `__contains__` first; falls back to `__iter__`; then to `__getitem__`. Shows all three and the priority order.

#### Attribute Access: \_\_getattr\_\_ and \_\_setattr\_\_
Intercepting attribute access.

##### Attribute Reference
`__getattr__(self, name)` called only for *undefined* attributes (after normal lookup fails). Shows computed/virtual attributes.

##### Attribute Assignment and Deletion
`__setattr__(self, name, value)` called for *all* attribute assignments. Must use `self.__dict__[name] = value` internally to avoid infinite recursion. `__delattr__` for `del`.

##### Other Attribute-Management Tools
Mentions properties and descriptors as alternatives (covered in Chapter 38).

##### Emulating Privacy for Instance Attributes: Part 1
Using `__setattr__` to reject assignments to certain attribute names. Simple privacy emulation.

#### String Representation: \_\_repr\_\_ and \_\_str\_\_
Making instances printable.

##### Why Two Display Methods?
`__repr__`: developer-oriented, used by interactive prompt and `repr()`. `__str__`: user-oriented, used by `print()` and `str()`. `__repr__` is the fallback if `__str__` is not defined.

##### Display Usage Notes
Guidance on when to define each. Notes that `__repr__` is always safe to define; `__str__` is optional for user-friendly display.

#### Right-Side and In-Place Ops: \_\_radd\_\_ and \_\_iadd\_\_
Handling operations where the custom object is on the right side or where in-place modification is desired.

##### Right-Side Addition
`__radd__` is called when the left operand doesn't know how to add. Shows the dispatch logic: Python tries `left.__add__(right)`, then `right.__radd__(left)`.

##### In-Place Addition
`__iadd__` for `+=`. Can modify in place (return `self`) for mutables, or create a new object for immutables. Falls back to `__add__` if not defined.

#### Call Expressions: \_\_call\_\_
Making instances callable like functions.

##### Function Interfaces and Callback-Based Code
`__call__` with practical use: callback objects that carry state, function-like objects with persistent state between calls. Shows use in event-driven programming.

#### Comparisons: \_\_lt\_\_, \_\_gt\_\_, and Others
`__lt__`, `__le__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`. Notes that Python does not automatically derive reciprocals (`__lt__` doesn't imply `__gt__`). Mentions `functools.total_ordering` decorator as a shortcut.

#### Boolean Tests: \_\_bool\_\_ and \_\_len\_\_
`__bool__` for truth testing (in `if`, `while`, `and`, `or`). Falls back to `__len__` (nonzero length = true). If neither is defined, object is always true.

#### Object Destruction: \_\_del\_\_
Called when an object is garbage-collected.

##### Destructor Usage Notes
Warns: don't rely on `__del__` for cleanup — use `with`/context managers instead. Notes that `__del__` may not be called (circular references, interpreter shutdown). Covers exception suppression in `__del__`.

---

### Chapter 31. Designing with Classes

OOP design patterns, principles, and advanced mechanisms.

#### Python and OOP
Frames Python's approach to OOP: no enforced encapsulation, duck typing instead of interfaces, conventions instead of access modifiers.

##### Polymorphism Means Interfaces, Not Call Signatures
Python's polymorphism is based on what operations an object supports, not on declared types or interface signatures.

#### OOP and Inheritance: "Is-a" Relationships
When to use inheritance: the subclass *is a* specialised kind of the superclass. Shows a classic `Employee → Manager` hierarchy.

#### OOP and Composition: "Has-a" Relationships
When to use composition: the container *has a* component. Objects embedded as attributes.

##### Stream Processors Revisited
Worked example: a stream-processor class that delegates to embedded reader and writer objects. Shows how composition enables pluggable components.

#### OOP and Delegation: "Like-a" Relationships
Wrapper/proxy objects that forward attribute access to an embedded object using `__getattr__`. Shows the delegation pattern.

#### Pseudoprivate Class Attributes
Python's name-mangling mechanism for attributes.

##### Name Mangling Overview
Names with `__name` (two leading underscores, at most one trailing) are mangled to `_ClassName__name`. Explains the mechanism.

##### Why Use Pseudoprivate Attributes?
Prevents accidental overriding in subclasses of shared attribute names. Not for true security — just name-collision avoidance.

#### Method Objects: Bound or Not
The nature of method objects in Python.

##### Bound Methods in Action
`instance.method` creates a bound method (carries the instance). Can be stored and called later. Shows `unbound = Class.method; unbound(instance)` equivalent. Practical uses in callbacks and event handlers.

#### Classes Are Objects: Generic Object Factories
Using class objects as first-class values.

##### Why Factories?
Factory functions that receive a class object and create instances. Shows `def factory(cls, *args): return cls(*args)`. Useful for frameworks and generic code.

#### Multiple Inheritance and the MRO
Detailed treatment of multiple inheritance.

##### How Multiple Inheritance Works
`class C(A, B):` inherits from both A and B. Shows diamond inheritance scenarios.

##### How the MRO Works
C3 linearization algorithm. Shows `Class.__mro__` and `Class.mro()`. Explains the ordering: local class first, then parents in order, with shared parents deferred to last. ~3 pages.

##### Attribute Conflict Resolution
When two parents define the same attribute, MRO determines which wins. Shows how to explicitly choose.

##### Example: "Mix-in" Attribute Listers
Extended worked example (~10 pages): builds three mixin classes for listing attributes. `ListInstance` (instance `__dict__`), `ListInherited` (all inherited attributes via `dir()`), `ListTree` (full tree with per-class breakdown). Demonstrates mix-in composition.

##### Example: Mapping Attributes to Inheritance Sources
Builds a tool that traces which class each attribute comes from. Walks the MRO and reports. ~4 pages.

#### Other Design-Related Topics
Brief mentions: design patterns (observer, strategy, singleton), SOLID principles, refactoring. Points to external resources.

---

### Chapter 32. Class Odds and Ends

Advanced class topics: extending built-ins, the object model, slots, properties, static/class methods, decorators preview, `super()`, and gotchas.

#### Extending Built-in Object Types
Two techniques for adding behaviour to built-in types.

##### Extending Types by Embedding
Wrapping a built-in object inside a class and delegating. Shows a set-like class that embeds a list.

##### Extending Types by Subclassing
Subclassing `list`, `dict`, `str`, etc. directly. Shows a custom list with additional methods. Notes some limitations.

#### The Python Object Model
How types and classes relate in Python 3.

##### Classes Are Types Are Classes
In Python 3, classes and types are the same thing. `type(instance)` returns the class; `type(class)` returns `type`.

##### Some Instances Are More Equal Than Others
Notes special-casing of built-in type instances vs. user-class instances in some internal operations.

##### The Inheritance Bifurcation
Explains that instance attribute lookup and class attribute lookup follow different rules (MRO for classes, descriptor protocol for attributes).

##### The Metaclass/Class Dichotomy
Brief note that `type` is the metaclass of regular classes, and this can be customised. Previews Chapter 40.

##### And One "object" to Rule Them All
`object` is the root of all classes. Provides default `__repr__`, `__hash__`, `__eq__`, etc. Explains why every class implicitly inherits from `object`.

#### Advanced Attribute Tools
Advanced mechanisms for controlling attribute access.

##### Slots: Attribute Declarations
`__slots__` class attribute: restricts instances to named attributes only (no `__dict__`). Covers memory savings, inheritance interaction, `__dict__` suppression, gotchas with single inheritance, multiple inheritance of slots, and when to use them. Thorough — ~8 pages.

##### Properties: Attribute Accessors
`@property` decorator for managed attributes (getter, setter, deleter). Shows computed attributes. Brief here — full treatment in Chapter 38.

##### \_\_getattribute\_\_ and Descriptors: Attribute Implementations
Brief introduction: `__getattribute__` is called for *every* attribute access (not just undefined). Descriptor protocol (`__get__`, `__set__`, `__delete__`) is how properties and methods work internally. Previews Chapter 38.

#### Static and Class Methods
Alternative method types that don't require an instance.

##### Why the Special Methods?
Explains the need: sometimes you want a method in a class that doesn't operate on an instance (utility functions, alternative constructors).

##### Plain-Function Methods
In Python 3, calling `Class.method(args)` works if the method doesn't use `self`. But this is fragile — better to use decorators.

##### Static Method Alternatives
Various ways to achieve "no self" methods: module-level functions, nested functions, staticmethod.

##### Using Static and Class Methods
`@staticmethod`: no `self` or `cls`. `@classmethod`: receives the class as first argument (`cls`). Shows syntax and usage.

##### Counting Instances with Static Methods
Worked example: a class variable tracking instance count, with a static method to report it.

##### Counting Instances with Class Methods
Same example reimplemented with `@classmethod`. Shows `cls` parameter. Demonstrates that `classmethod` knows which class it's called on (important for inheritance).

#### Decorators and Metaclasses
Preview of advanced topics covered in Chapters 39–40.

##### Function Decorator Basics
Explains `@decorator` syntax for functions. Shows that `@deco def f(): ...` is equivalent to `f = deco(f)`.

##### A First Look at User-Defined Function Decorators
Simple tracing decorator example. Shows a decorator that wraps a function to add pre/post processing.

##### A First Look at Class Decorators and Metaclasses
`@decorator` for classes: `@deco class C: ...` is `C = deco(C)`. Metaclasses: `class C(metaclass=M):` uses M to create C. Brief overview of when each is useful.

##### For More Details
Points to Chapters 39 and 40 for full treatment.

#### The super Function
Detailed treatment of `super()`.

##### The super Basics
`super().method()` calls the next class's method in the MRO. No arguments needed in Python 3 (uses implicit `__class__`). Shows basic usage for constructor chaining.

##### The super Details
How `super()` interacts with the MRO. Shows cooperative multiple inheritance: all classes in a diamond call `super()`, and the MRO ensures each class is called exactly once. Covers `super(Class, instance)` explicit form. Discusses the benefits (cooperative MI, adaptability) and pitfalls (all classes must cooperate, signature compatibility). ~7 pages.

##### The super Wrap-Up
Summary of when to use `super()` (cooperative MI) vs. explicit `Class.method(self)` calls (simple, direct). Notes the debate in the Python community.

#### Class Gotchas
Common class-related mistakes.

##### Changing Class Attributes Can Have Side Effects
Assigning to a class attribute affects all instances that haven't overridden it. Shows the surprise when `Class.attr = new_value` changes behaviour for all instances.

##### Changing Mutable Class Attributes Can Have Side Effects, Too
A mutable class attribute (e.g., list) is shared by all instances. Modifying it (not reassigning) via one instance affects all. Shows the gotcha and fix.

##### Multiple Inheritance: Order Matters
`class C(A, B)` vs. `class C(B, A)` can produce different behaviour. The MRO depends on the order.

##### Scopes in Methods and Classes
Reiterates: class bodies don't create enclosing scopes for methods. Can't access a class attribute in a method without `self.attr` or `ClassName.attr`.

##### Miscellaneous Class Gotchas
Brief notes on: forgetting `self`, calling superclass `__init__`, mutable default arguments in methods.

##### "Overwrapping-itis"
Warning against excessive wrapping and abstraction. Python's "we're all adults here" philosophy means not everything needs getters/setters and interfaces.

---

## Part VII. Exceptions

Covers Python's exception-handling model: `try`/`except`/`else`/`finally`, `raise`, `assert`, `with`, exception classes, and design patterns.

---

### Chapter 33. Exception Basics

Introduction to exceptions. Sets the stage for detailed chapters to follow.

#### Why Use Exceptions?
Motivates exception handling in Python.

##### Exception Roles
Five roles: error handling, event notification, special-case handling, termination actions, and unusual control flow (e.g., breaking out of nested loops).

#### Exceptions: The Short Story
Quick tour of all exception mechanisms.

##### Default Exception Handler
What happens when no handler is present: Python prints a traceback and terminates the program. Shows a simple error example.

##### Catching Exceptions
`try`/`except` to intercept errors. Shows basic syntax and a simple example.

##### Raising Exceptions
`raise ExceptionType(args)` to trigger exceptions manually. Shows raising built-in and custom exceptions.

##### User-Defined Exceptions
`class MyError(Exception): pass`. Shows creating custom exception classes. Brief.

##### Termination Actions
`try`/`finally` for guaranteed cleanup regardless of exceptions. Shows basic usage.

---

### Chapter 34. Exception Coding Details

Full syntax reference for all exception-related statements.

#### The try Statement
Detailed treatment of all `try` clause forms.

##### try Statement Clauses
Lists all clause combinations: `try`/`except`, `try`/`finally`, `try`/`except`/`else`, `try`/`except`/`finally`, and the full form. Shows the ordering rules.

##### The except and else Clauses
Multiple `except` clauses for different exception types. `except Type as variable` for accessing exception objects. Bare `except` (catches everything — discouraged). `else` clause: runs only if no exception occurred. Multiple examples. ~6 pages.

##### The finally Clause
Guaranteed cleanup code. Runs whether an exception occurred or not, whether it was caught or not. Shows interaction with `return`, `break`, `continue` in `try` blocks.

##### Combined try Clauses
Using `except`, `else`, and `finally` together. Shows the full form and explains execution order in various scenarios (no exception, caught exception, uncaught exception).

#### The raise Statement
Triggering exceptions programmatically.

##### Raising Exceptions
`raise instance`, `raise Class(args)`, re-raising in `except` with bare `raise`.

##### The except as hook
`except Type as var:` binds the exception instance to `var`. Shows accessing `.args`, custom attributes.

##### Scopes and except as
The `as` variable is deleted after the `except` block exits (Python 3 scoping rule). Shows the behaviour and workarounds.

##### Propagating Exceptions with raise
Bare `raise` re-raises the current exception. Used in `except` blocks after partial handling.

##### Exception Chaining: raise from
`raise NewException() from original` sets `__cause__` for explicit chaining. Implicit chaining via `__context__`. `raise X from None` to suppress chaining. Shows all forms.

#### The assert Statement
Debugging tool for invariant checking.

##### Example: Trapping Constraints (but Not Errors!)
`assert condition, message`. Shows it raises `AssertionError`. Notes: use for development-time checks, not for production error handling. Can be disabled with `python -O`.

#### The with Statement and Context Managers
Resource management with guaranteed cleanup.

##### Basic with Usage
`with expression as variable: body`. Shows file handling (`with open(...) as f:`) as the canonical example.

##### The Context-Management Protocol
`__enter__` and `__exit__` methods. Shows how to write a custom context manager class. Explains `__exit__` return value for suppressing exceptions.

##### Multiple Context Managers
`with A() as a, B() as b:` — multiple managers in one `with` statement.

##### The Termination-Handlers Shoot-Out
Compares `try/finally`, `with`, `__del__`, and `atexit` for cleanup. Shows trade-offs of each approach.

---

### Chapter 35. Exception Objects

Designing exception classes and the built-in exception hierarchy.

#### Exception Classes
Using classes for exceptions.

##### Coding Exceptions Classes
`class MyError(Exception):` with optional `__init__` and `__str__`. Shows adding custom attributes and display.

##### Why Exception Hierarchies?
Superclass exceptions catch subclass exceptions too. Build category hierarchies so handlers can catch broad categories. Worked example: `AppError` → `InputError`, `ProcessError`, etc.

#### Built-in Exception Classes
Python's built-in exception tree.

##### Built-in Exception Categories
Hierarchy: `BaseException` → `Exception` (most errors), `KeyboardInterrupt`, `SystemExit`, `GeneratorExit`. Under `Exception`: `ArithmeticError`, `LookupError`, `OSError`, etc.

##### Default Printing and State
Built-in exceptions store constructor args in `.args` tuple. Default `__str__` prints args.

#### Custom Print Displays
Overriding `__str__` in custom exception classes for user-friendly messages. Brief example.

#### Custom State and Behavior
Adding data and methods to exception classes.

##### Providing Exception Details
Storing extra info (filename, line number, context) in exception attributes via `__init__`.

##### Providing Exception Methods
Adding methods to exception classes (e.g., `log()`, `format_message()`). Shows that exception objects are just objects — they can have any methods.

#### Exception Groups: Yet Another Star!
Python 3.11+ `ExceptionGroup` and `except*`.

Shows `ExceptionGroup("msg", [exc1, exc2])` for bundling multiple exceptions (common in async/concurrent code). `except* Type:` catches matching exceptions from the group while letting others propagate. Moderate introduction — enough to understand and use the feature.

---

### Chapter 36. Exception Odds and Ends

Remaining exception topics: nesting, idioms, design, and the core-language wrap-up.

#### Nesting Exception Handlers
How nested `try` statements interact.

##### Example: Control-Flow Nesting
Exceptions propagate outward through dynamically nested `try` statements (across function calls). Shows the propagation chain.

##### Example: Syntactic Nesting
`try` blocks physically nested inside each other. Shows how Python tries inner handlers first, then outer.

#### Exception Idioms
Practical exception usage patterns.

##### Breaking Out of Multiple Nested Loops: "go to"
Using `raise` to break out of deeply nested loops to an outer `try`/`except`. Shows the pattern as a structured `goto` alternative.

##### Exceptions Aren't Always Errors
Exceptions as normal control flow: `StopIteration`, `SystemExit`, `KeyboardInterrupt`. Shows intentional use of exceptions for signalling.

##### Functions Can Signal Conditions with raise
Using `raise` to signal special conditions from functions (alternative to sentinel return values). Shows the pattern.

##### Closing Files and Server Connections
Using `try`/`finally` and `with` to ensure resources are released. Brief practical examples.

##### Debugging with Outer try Statements
Wrapping a top-level `try`/`except` around a program to catch unhandled exceptions and add debugging info.

##### Running In-Process Tests
Using exceptions to run test suites where individual test failures don't crash the whole suite.

##### More on sys.exc\_info
`sys.exc_info()` returns `(type, value, traceback)` for the current exception. Shows use for logging, re-raising with modified state.

##### Displaying Errors and Tracebacks
Using `traceback` module to format and display exception tracebacks programmatically. `traceback.print_exc()`, `traceback.format_exc()`.

#### Exception Design Tips and Gotchas
Best practices and common mistakes.

##### What Should Be Wrapped
Guidance on what to put in `try` blocks: wrap operations that *can* fail, not everything. Keep `try` blocks narrow.

##### Catching Too Much: Avoid Empty except and Exception
Bare `except:` catches everything including `SystemExit` and `KeyboardInterrupt` — almost always wrong. `except Exception:` is better but still broad. Argues for specific exception types.

##### Catching Too Little: Use Class-Based Categories
If you only catch specific exceptions, you miss related ones. Solution: catch a superclass category. Build hierarchies.

#### Core Language Wrap-Up
Final summary of the core language, pointing beyond to application development.

##### The Python Toolset
Survey of Python's broader toolset beyond the core language: standard library, PyPI, debugging tools, testing frameworks, profilers, IDEs.

##### Development Tools for Larger Projects
Brief coverage of tools for scaling up: `unittest`, `pytest`, `doctest` for testing; `pdb` for debugging; `profile`/`cProfile` for profiling; `pyflakes`/`pylint`/`mypy` for static analysis; `pip`/`setuptools` for packaging; `venv` for virtual environments. ~3 pages.

---

## Part VIII. Advanced Topics

Expert-level chapters covering Unicode, managed attributes, decorators, and metaclasses.

---

### Chapter 37. Unicode and Byte Strings

Deep dive into Unicode handling in Python. ~40 pages.

#### Unicode Foundations
Background on character encoding.

##### Character Representations
What Unicode code points are, the difference between characters and bytes, code point notation (U+XXXX). Historical context (ASCII → Latin-1 → Unicode).

##### Character Encodings
Explains UTF-8, UTF-16, UTF-32, Latin-1, ASCII as encoding schemes. How they map code points to bytes. Variable-width vs. fixed-width encodings.

#### Introducing Python String Tools
Python's string and bytes types.

##### The str Object
Python 3 `str` holds Unicode text. Immutable sequence of Unicode code points.

##### The bytes Object
`bytes` holds raw byte data. Immutable sequence of integers 0–255. Created with `b'...'` literals.

##### The bytearray Object
Mutable version of `bytes`. Supports in-place changes.

##### Text and Binary Files
`open()` in text mode returns `str` (encodes/decodes automatically). Binary mode returns `bytes` (raw data). Explains the duality.

#### Using Text Strings
Working with Unicode `str` objects in detail.

##### Literals and Basic Properties
`str` literals, methods, operations. All the basics reviewed in the Unicode context.

##### String Type Conversions
`str.encode(encoding)` → `bytes`. `bytes.decode(encoding)` → `str`. Shows common encodings. Error handling options (`'strict'`, `'ignore'`, `'replace'`, `'xmlcharrefreplace'`).

##### Coding Unicode Strings in Python
`\xNN` (hex byte), `\uNNNN` (16-bit code point), `\UNNNNNNNN` (32-bit code point), `\N{name}` (Unicode name). Shows encoding/decoding of non-ASCII characters. Demonstrates with Chinese, Arabic, emoji. ~5 pages.

##### Source-File Encoding Declarations
`# -*- coding: utf-8 -*-` or `# coding: utf-8` at the top of source files. Explains when needed and the default (UTF-8 since Python 3).

#### Using Byte Strings
Working with `bytes` and `bytearray`.

##### Methods
`bytes` supports most `str` methods that make sense for byte data. Notes which methods are missing.

##### Sequence Operations
Indexing returns an integer (0–255), not a character. Slicing returns `bytes`. Shows the difference from `str`.

##### Formatting
`bytes` supports `%` formatting but not `.format()` or f-strings. Brief.

##### Other Ways to Make Bytes
`bytes()` constructor, `bytes.fromhex()`, `struct.pack()`, `int.to_bytes()`. Brief.

##### Mixing String Types
Cannot concatenate `str` and `bytes` directly — must encode/decode explicitly. Shows the error and fix.

##### The bytearray Object
`bytearray` creation, in-place modification (index assignment, `extend()`, etc.), use cases (protocol buffers, binary data editing).

#### Using Text and Binary Files
How file modes affect encoding.

##### Text-File Basics
Text mode adds encoding/decoding layer. Default encoding is platform-dependent (`locale.getpreferredencoding()`). Shows explicit encoding specification.

##### Text and Binary Modes
Demonstrates the same file read in text vs. binary mode. Shows newline translation in text mode (`\r\n` → `\n` on Windows).

##### Unicode-Text Files
Reading/writing files with specific encodings: `open('f', encoding='utf-8')`, `open('f', encoding='latin-1')`. Shows handling of BOM (byte-order mark). Practical examples.

#### Unicode, Bytes, and Other String Tools
How Unicode interacts with other Python tools.

##### The re Pattern-Matching Module
`re` works with both `str` and `bytes`. Shows pattern matching on Unicode strings. Notes `re.UNICODE` flag.

##### The struct Binary-Data Module
`struct.pack()`/`struct.unpack()` for C-compatible binary data. Shows format strings. Returns/accepts `bytes`.

##### The pickle and json Serialization Modules
How `pickle` (binary protocol) and `json` (text/Unicode) handle strings and bytes. Notes `json` works with `str` only.

##### Filenames in open and Other Filename Tools
Filenames can be `str` or `bytes`. OS-level issues with non-UTF-8 filenames. `os.fsencode()`/`os.fsdecode()`. Surrogate escapes for undecodable bytes. ~3 pages.

#### The Unicode Twilight Zone
Edge cases and advanced Unicode issues.

##### Dropping the BOM in Python
BOM (byte-order mark) handling: `utf-8-sig`, `utf-16` (auto-BOM), explicit BOM detection. Shows reading/writing BOM-prefixed files. ~4 pages.

##### Unicode Normalization: Whither Standard?
NFC, NFD, NFKC, NFKD normalisation forms via `unicodedata.normalize()`. Explains why the same character can have multiple representations (composed vs. decomposed) and how to normalise for comparison and storage. ~2 pages.

---

### Chapter 38. Managed Attributes

Four techniques for intercepting attribute access, compared side-by-side. ~40 pages.

#### Why Manage Attributes?
Motivation: inserting logic (validation, logging, computed values) when attributes are accessed or changed.

##### Inserting Code to Run on Attribute Access
Overview of the four mechanisms: properties, descriptors, `__getattr__`, `__getattribute__`.

#### Properties
The `property` built-in.

##### The Basics
`property(fget, fset, fdel, doc)` creates a managed attribute. Shows placement in a class body.

##### A First Example
Demonstrates a class with a property that validates on assignment.

##### Computed Attributes
Property that computes its value on access (no stored data). Shows a calculated attribute.

##### Coding Properties with Decorators
`@property`, `@name.setter`, `@name.deleter` decorator syntax. Shows the preferred modern style.

#### Descriptors
The descriptor protocol underlying properties and methods.

##### The Basics
A descriptor is any object with `__get__`, `__set__`, or `__delete__`. Data descriptors (have `__set__` or `__delete__`) vs. non-data descriptors (only `__get__`). Explains the lookup priority: data descriptor → instance `__dict__` → non-data descriptor.

##### A First Example
Builds a descriptor class for managed attributes. Shows it working in a client class.

##### Computed Attributes
Descriptor that computes values on access. Shows the pattern.

##### Using State Information in Descriptors
Where to store state: in the descriptor instance (shared across all client instances), in the client instance (per-instance), or using `__set_name__` (Python 3.6+) for automatic naming. Shows trade-offs.

##### How Properties and Descriptors Relate
Properties are implemented as descriptors internally. Shows the equivalence.

#### \_\_getattr\_\_ and \_\_getattribute\_\_
Operator overloading methods for attribute interception.

##### The Basics
`__getattr__`: called only for undefined attributes. `__getattribute__`: called for *all* attribute accesses. The latter requires care to avoid infinite recursion.

##### A First Example
Demonstrates both methods intercepting attribute access.

##### Computed Attributes
Using `__getattr__` for on-demand computation. Shows the pattern.

##### \_\_getattr\_\_ and \_\_getattribute\_\_ Compared
Side-by-side comparison: when each is called, recursion risks, performance implications, use cases.

##### Management Techniques Compared
All four techniques compared in a table: properties (simple, per-attribute), descriptors (reusable, per-attribute), `__getattr__` (catch-all, undefined only), `__getattribute__` (catch-all, all access).

##### Intercepting Built-in Operation Attributes
A critical limitation: Python's built-in operations (e.g., `+`, `len()`, `[]`) skip `__getattr__`/`__getattribute__` for dunder methods. They look directly in the class `__dict__`. Shows the problem and workarounds.

#### Example: Attribute Validations
The same validation problem solved four ways.

##### Using Properties to Validate
Validates a `name` attribute using `@property` with a setter that checks constraints.

##### Using Descriptors to Validate
Same validation implemented as a reusable descriptor class. Shows it applied to multiple attributes.

##### Using \_\_getattr\_\_ to Validate
Same validation using `__getattr__` for read and `__setattr__` for write.

##### Using \_\_getattribute\_\_ to Validate
Same validation using `__getattribute__`. Shows the recursion-avoidance pattern (`object.__getattribute__(self, name)`).

---

### Chapter 39. Decorators

Comprehensive decorator treatment. ~60 pages.

#### What's a Decorator?
Conceptual overview.

##### Managing Calls and Instances
Decorators can intercept function calls or class instance creation, adding pre/post processing.

##### Managing Functions and Classes
Decorators can also process the function/class object itself at definition time (adding attributes, registering, wrapping).

##### Using and Defining Decorators
Shows `@decorator` syntax. Distinguishes using existing decorators from writing your own.

##### Why Decorators?
Benefits: explicit, maintainable, less error-prone than manual wrapping, enforce consistent augmentation, separate concerns.

#### The Basics
Formal decorator mechanics.

##### Function Decorator Basics
`@deco def f(): ...` ≡ `f = deco(f)`. Shows the wrapper pattern: `deco` returns a new callable that replaces `f`. Multiple examples. ~4 pages.

##### Class Decorator Basics
`@deco class C: ...` ≡ `C = deco(C)`. Shows decorators that return a wrapper class or modify the original class.

##### Decorator Nesting
`@A @B @C def f():` ≡ `f = A(B(C(f)))`. Shows the application order (inner to outer).

##### Decorator Arguments
`@deco(args)` is a call that returns a decorator: `deco(args)` returns the actual decorator function. Shows the three-level nesting pattern.

##### Decorators Manage Functions and Classes, Too
Decorators that modify the function/class itself (add attributes, register in a dict) rather than wrapping it.

#### Coding Function Decorators
Detailed patterns for building function decorators.

##### Tracing Function Calls
Builds a decorator that prints function calls and arguments. Shows the basic wrapper class/function pattern.

##### Decorator State Retention Options
Three approaches to retaining state: class instances (via `__init__`/`__call__`), enclosing scope (closure), function attributes. Compares pros and cons.

##### Class Pitfall: Decorating Methods
When a class-based decorator wraps a method, `self` gets confused (the decorator's `self` shadows the instance's). Shows the problem and solutions: use closures instead of classes, or use descriptors. ~5 pages.

##### Timing Function Calls
Builds a performance-timing decorator. Shows measuring total/average call time.

##### Adding Decorator Arguments
Building parameterised decorators with the three-level nesting pattern (factory → decorator → wrapper). Shows a configurable tracing decorator.

#### Coding Class Decorators
Decorators applied to classes.

##### Singleton Classes
Decorator that ensures only one instance of a class exists. Shows the pattern using a closure.

##### Tracing Object Interfaces
Decorator that wraps a class to trace all attribute access on its instances. Uses `__getattr__` delegation. Shows the proxy pattern. ~3 pages.

##### Class Pitfall: Retaining Multiple Instances
When using a class-based decorator on classes, each decoration creates one wrapper instance. Shows the problem and fix (use dictionaries or closures to track per-instance state).

#### Example: "Private" and "Public" Attributes
Extended worked example building access-control decorators. ~12 pages.

##### Implementing Private Attributes
Decorator that intercepts attribute access and blocks access to "private" names (defined by the programmer). Uses `__getattr__`/`__setattr__` delegation.

##### Implementation Details I
Handling edge cases: `__repr__`, `__str__`, built-in operation access, inheritance.

##### Generalizing for Public Declarations
Extends the decorator to support both "private" (blocked) and "public" (allowed) attribute declarations.

##### Implementation Details II
Further edge cases and refinements.

##### Delegating Built-In Operations
The challenge of proxying dunder methods: Python bypasses `__getattr__` for built-in operations. Shows `__add__`, `__iter__`, etc. must be explicitly defined in the proxy class. Discusses automated delegation techniques.

#### Example: Validating Function Arguments
Extended worked example building argument-validation decorators. ~12 pages.

##### The Goal
A decorator that checks function arguments against declared ranges at each call.

##### A Basic Range-Testing Decorator for Positional Arguments
First version: validates positional arguments against min/max ranges.

##### Generalizing for Keywords and Defaults
Extends to handle keyword arguments and default values. Shows the complexity of matching arguments to parameters.

##### Implementation Details
Uses `inspect` module for argument introspection. Shows `inspect.signature()` usage.

##### Open Issues
Discusses limitations: performance cost, error messages, composability with other decorators.

##### Decorator Arguments Versus Function Annotations
Compares storing validation info in decorator arguments vs. function annotations. Shows both approaches.

---

### Chapter 40. Metaclasses and Inheritance

The most advanced chapter. ~35 pages on metaclasses and the full inheritance algorithm.

#### To Metaclass or Not to Metaclass
When metaclasses are (and aren't) warranted.

##### The Downside of "Helper" Functions
Shows a pattern where every class must call a helper function after definition. Metaclasses automate this.

##### Metaclasses Versus Class Decorators: Round 1
Both can process classes at creation time. Compares: decorators are simpler; metaclasses are inherited and can provide methods to classes.

#### The Metaclass Model
How metaclasses work internally.

##### Classes Are Instances of type
In Python 3, `type(MyClass)` is `type`. Classes are instances of `type`, just as instances are instances of classes.

##### Metaclasses Are Subclasses of type
A metaclass is a class that inherits from `type` and customises class creation.

##### Class Statements Call a type
`class C(B): body` internally does: execute `body` to collect a namespace, then call `type('C', (B,), namespace)` to create the class object.

##### Class Statements Can Choose a type
`class C(metaclass=M):` uses `M` instead of `type` to create `C`.

##### Metaclass Method Protocol
Shows `__new__`, `__init__`, `__call__` in a metaclass and when each is invoked.

#### Coding Metaclasses
Building metaclasses.

##### A Basic Metaclass
Minimal metaclass that intercepts class creation. Shows `class Meta(type): def __new__(cls, name, bases, dict):`.

##### Customizing Construction and Initialization
Using `__new__` to modify the class before creation and `__init__` to process it after. Shows adding attributes, validating, and transforming the class.

##### Other Metaclass Coding Techniques
`__init_subclass__` (Python 3.6+): a simpler alternative for many metaclass use cases — a hook in the parent class that's called when subclasses are created. `__prepare__` for returning a custom namespace dict. Factory functions as metaclasses.

##### Managing Classes with Metaclasses and Decorators
Combining metaclasses with class decorators. Shows when to use each and how they can complement each other. Practical examples of class registration, validation, and augmentation.

#### Inheritance: The Finale
The complete Python inheritance algorithm — the most technically dense section.

##### Metaclass Versus Superclass
Metaclass attributes are accessible on the class but not on instances. Superclass attributes are accessible on both. Shows the distinction.

##### Metaclass Inheritance
If no `metaclass=` is specified, the metaclass is inherited from the parent class. Shows how metaclass propagates through a hierarchy.

##### Python Inheritance Algorithm: The Simple Version
Simplified lookup: for `instance.name`: check instance `__dict__`, then walk the MRO checking each class `__dict__`.

##### Python Inheritance Algorithm: The Less Simple Version
Full algorithm including descriptors: data descriptors in classes override instance `__dict__`; non-data descriptors are overridden by instance `__dict__`. Shows the priority: data descriptor → instance → non-data descriptor → class. ~3 pages.

##### The Inheritance Wrap-Up
Summary diagram of the complete attribute lookup algorithm.

#### Metaclass Methods
Methods defined in metaclasses.

##### Metaclass Methods Versus Class Methods
Metaclass methods are accessible via the class (not instances). Class methods are accessible via both. Shows the difference.

##### Operator Overloading in Metaclass Methods
Metaclass can define `__str__`, `__add__`, etc. to customize how the *class object* itself responds to operations.

##### Metaclass Methods Versus Instance Methods
Metaclass methods process the class; instance methods process instances. They live in different namespaces and don't conflict.

---

### Chapter 41. All Good Things

Closing chapter. Entirely expository — no new technical content.

#### The Python Tsunami
Reflects on Python's explosive growth and the ever-expanding ecosystem.

#### The Python Sandbox
Encourages readers to experiment, build projects, and learn by doing.

#### The Python Upside
Reiterates Python's strengths: readability, productivity, breadth of application.

#### Closing Thoughts
Final reflections on learning programming and the value of deep understanding.

#### Where to Go from Here
Recommends next steps: application-level books (*Programming Python*), domain-specific libraries, open-source projects, community engagement.

#### Encore: Print Your Own Completion Certificate!
A Python script that generates a personalised completion certificate. A fun capstone.

---

## Part IX. Appendixes

### Appendix A. Platform Usage Tips

#### Using Python on Windows
Installation via python.org installer, Microsoft Store, and `winget`. The `py` launcher, PATH configuration, registry settings, Windows-specific libraries (`winreg`, `winsound`, `msvcrt`), PowerShell and CMD considerations. ~6 pages.

#### Using Python on macOS
System Python vs. Homebrew vs. python.org. PATH considerations, framework builds, `tkinter` dependencies. ~5 pages.

#### Using Python on Linux
Package manager installation (apt, dnf, etc.), building from source, `deadsnakes` PPA, managing multiple versions. ~2 pages.

#### Using Python on Android
Termux (full Linux environment), QPython, Pydroid 3, BeeWare's Briefcase for Android apps. ~3 pages.

#### Using Python on iOS
Pythonista, Pyto, BeeWare's Briefcase for iOS apps. Limitations. ~1 page.

#### Standalone Apps and Executables
PyInstaller, cx_Freeze, Nuitka, py2exe (Windows), py2app (macOS), Briefcase (cross-platform), Kivy+Buildozer (mobile). Covers trade-offs, bundled size, and cross-compilation. ~3 pages.

#### Etcetera
Other platforms and deployment options: Raspberry Pi, WebAssembly (Pyodide), Docker, cloud platforms.

### Appendix B. Solutions to End-of-Part Exercises

Full solutions and discussion for all end-of-part programming exercises.

#### Part I, Getting Started
Solutions for basic setup and interpreter exercises.

#### Part II, Objects and Operations
Solutions for exercises on built-in types, operations, and data manipulation.

#### Part III, Statements and Syntax
Solutions for statement, loop, and iteration exercises.

#### Part IV, Functions and Generators
Solutions for function definition, scope, argument, generator, and timing exercises.

#### Part V, Modules and Packages
Solutions for module creation, import, package, and reload exercises.

#### Part VI, Classes and OOP
Solutions for class design, inheritance, operator overloading, and OOP exercises.

#### Part VII, Exceptions
Solutions for exception handling, custom exceptions, and design exercises.

---

## Overall Characterisation

This book is a **comprehensive core-language tutorial and reference** covering Python's syntax, semantics, object model, and execution model from absolute basics through expert-level topics (metaclasses, descriptors, decorators, the full inheritance algorithm, Unicode internals). It does *not* cover application domains (web frameworks, data science, GUIs, etc.). Depth varies by topic: foundational topics (types, statements, functions, classes) receive extensive treatment with many examples; advanced topics (decorators, metaclasses, managed attributes) are covered at a level suitable for someone who has mastered the basics and wants to understand the machinery. Each chapter ends with quizzes; each part ends with programming exercises (solutions in Appendix B).
