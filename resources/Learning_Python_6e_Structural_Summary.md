# Learning Python (6th Edition) — Structural Summary (More Detailed)

This version adds more *specific* coverage signals than the earlier summary by:
- including page spans (a proxy for depth),
- listing all subheadings under each heading, and
- for leaf subsections, extracting coverage cues (syntax/forms, REPL examples, exception cases, comparisons, best practices) plus key terms seen in the text.

# Copyright
- **Span:** PDF pp. 4–6 (3 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** reilly, rights, media, oreilly, editor, author, sales, information, corporate, nsight, designer, cover
- **Key terms/APIs that appear:** oreilly.com, all, errata.csp, any, open, property

# Table of Contents
- **Span:** PDF pp. 7–32 (26 pages; deep dive)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception)
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** knowledge, packages, package, files, module, summary, answers, contents, namespace, imports, relative, interactive
- **Key terms/APIs that appear:** import, __init__.py, __main__.py, open, type, time

# Preface
- **Span:** PDF pp. 33–38 (6 pages; moderate detail)
- **Breakdown:**
  - Python
  - This Book
  - This Edition
  - Media Choices
  - Updates and Examples
  - Conventions and Reuse
  - Acknowledgments
- **Granularity:** 7 immediate subheadings; 7 leaf subsections underneath

## Python
- **Span:** PDF pp. 33–33 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** programming, languages, world, computers, language, edition, preface, nearly, relative, newcomers, applies, based
- **Key terms/APIs that appear:** re, try, all, list, open

## This Book
- **Span:** PDF pp. 34–34 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** tools, decades, goals, domains, languages, training, learners, simply, today, first, edition, promoting
- **Key terms/APIs that appear:** all, time, re, any, math

## This Edition
- **Span:** PDF pp. 35–35 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** edition, changes, world, coverage, version, decades, worth, newer, prior, decade, later, content
- **Key terms/APIs that appear:** all, type, async, __main__.py, except, time

## Media Choices
- **Span:** PDF pp. 36–36 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** media, online, print, chapters, unless, forms, ebook, reduced, learn, three, reference, publisher
- **Key terms/APIs that appear:** print, all, i.e, e.g, a.k, f.k, re, any

## Updates and Examples
- **Span:** PDF pp. 37–37 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** files, errata, list, constant, width, commands, updates, change, edition, online, usual, website
- **Key terms/APIs that appear:** all, list, a.k, time, zip, any

## Conventions and Reuse
- **Span:** PDF pp. 37–37 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** files, errata, list, constant, width, commands, updates, change, edition, online, usual, website
- **Key terms/APIs that appear:** all, list, a.k, time, zip, any

## Acknowledgments
- **Span:** PDF pp. 38–38 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** notes, sidebars, topics, begin, messages, space, please, though, earlier, acknowledgments, element, indicates
- **Key terms/APIs that appear:** time

# Part I. Getting Started
- **Span:** PDF pp. 39–88 (50 pages; extended treatment)
- **Breakdown:**
  - Chapter 1. A Python Q&A Session
  - Chapter 2. How Python Runs Programs
  - Chapter 3. How You Run Programs
- **Granularity:** 3 immediate subheadings; 56 leaf subsections underneath

## Chapter 1. A Python Q&A Session
- **Span:** PDF pp. 41–54 (14 pages; detailed)
- **Breakdown:**
  - Why Do People Use Python?
  - Is Python a “Scripting Language”?
  - OK, but What’s the Downside?
  - Who Uses Python Today?
  - What Can I Do with Python?
  - What Are Python’s Technical Strengths?
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 9 immediate subheadings; 23 leaf subsections underneath

### Why Do People Use Python?
- **Span:** PDF pp. 41–42 (2 pages; brief)
- **Breakdown:**
  - Software Quality
  - Developer Productivity
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Software Quality
- **Span:** PDF pp. 42–42 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** programming, program, programs, coding, portable, interfaces, application, software, generally, moreover, offers, multiple
- **Key terms/APIs that appear:** all, set, math

#### Developer Productivity
- **Span:** PDF pp. 43–43 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** scripting, language, tools, oriented, programmers, software, people, programs, object, programming, script, beyond
- **Key terms/APIs that appear:** time, re, all

### Is Python a “Scripting Language”?
- **Span:** PDF pp. 43–43 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** scripting, language, tools, oriented, programmers, software, people, programs, object, programming, script, beyond
- **Key terms/APIs that appear:** time, re, all

### OK, but What’s the Downside?
- **Span:** PDF pp. 44–44 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** language, programs, tasks, development, compiled, languages, control, scripting, components, though, simple, today
- **Key terms/APIs that appear:** i.e, e.g, any, set, all

### Who Uses Python Today?
- **Span:** PDF pp. 45–45 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** speed, today, compiled, computer, software, program, execution, numeric, programming, regularly, speeds, numpy
- **Key terms/APIs that appear:** any, open, range, all, list, try

### What Can I Do with Python?
- **Span:** PDF pp. 46–47 (2 pages; brief)
- **Breakdown:**
  - Systems Programming
  - GUIs and UIs
  - Internet and Web Scripting
  - Component Integration
  - Database Access
  - Rapid Prototyping
  - Numeric and Scientific Programming
  - And More: AI, Games, Images, QA, Excel, Apps…
- **Granularity:** 8 immediate subheadings; 8 leaf subsections underneath

#### Systems Programming
- **Span:** PDF pp. 46–46 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** tools, portable, system, programs, standard, interfaces, command, files, comes, tkinter, parse, tasks
- **Key terms/APIs that appear:** all, any, json, os, zip, csv

#### GUIs and UIs
- **Span:** PDF pp. 46–46 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** tools, portable, system, programs, standard, interfaces, command, files, comes, tkinter, parse, tasks
- **Key terms/APIs that appear:** all, any, json, os, zip, csv

#### Internet and Web Scripting
- **Span:** PDF pp. 46–46 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** tools, portable, system, programs, standard, interfaces, command, files, comes, tkinter, parse, tasks
- **Key terms/APIs that appear:** all, any, json, os, zip, csv

#### Component Integration
- **Span:** PDF pp. 47–47 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** database, components, tools, object, relational, provide, systems, compiled, support, component, coded, language
- **Key terms/APIs that appear:** all, json, boost.python, pickle, type

#### Database Access
- **Span:** PDF pp. 47–47 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** database, components, tools, object, relational, provide, systems, compiled, support, component, coded, language
- **Key terms/APIs that appear:** all, json, boost.python, pickle, type

#### Rapid Prototyping
- **Span:** PDF pp. 47–47 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** database, components, tools, object, relational, provide, systems, compiled, support, component, coded, language
- **Key terms/APIs that appear:** all, json, boost.python, pickle, type

#### Numeric and Scientific Programming
- **Span:** PDF pp. 48–48 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** numeric, programming, tools, numpy, libraries, language, excel, scientific, scripting, languages, extension, earlier
- **Key terms/APIs that appear:** math, time, try, all

#### And More: AI, Games, Images, QA, Excel, Apps…
- **Span:** PDF pp. 48–48 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** numeric, programming, tools, numpy, libraries, language, excel, scientific, scripting, languages, extension, earlier
- **Key terms/APIs that appear:** math, time, try, all

### What Are Python’s Technical Strengths?
- **Span:** PDF pp. 48–51 (4 pages; moderate detail)
- **Breakdown:**
  - It’s Object-Oriented and Functional
  - It’s Free and Open
  - It’s Portable
  - It’s Powerful
  - It’s Mixable
  - It’s Relatively Easy to Use
  - It’s Relatively Easy to Learn
- **Granularity:** 7 immediate subheadings; 7 leaf subsections underneath

#### It’s Object-Oriented and Functional
- **Span:** PDF pp. 49–49 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** object, portable, oriented, language, source, platform, class, supports, programming, tools, based, software
- **Key terms/APIs that appear:** any, open, list, all, set, re, time

#### It’s Free and Open
- **Span:** PDF pp. 49–49 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** object, portable, oriented, language, source, platform, class, supports, programming, tools, based, software
- **Key terms/APIs that appear:** any, open, list, all, set, re, time

#### It’s Portable
- **Span:** PDF pp. 49–49 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** object, portable, oriented, language, source, platform, class, supports, programming, tools, based, software
- **Key terms/APIs that appear:** any, open, list, all, set, re, time

#### It’s Powerful
- **Span:** PDF pp. 50–50 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** tools, objects, languages, built, systems, development, language, large, types, memory, programming, support
- **Key terms/APIs that appear:** all, type, e.g, range, collections, open

#### It’s Mixable
- **Span:** PDF pp. 51–51 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** programming, programs, languages, systems, language, tools, simple, rapid, program, learn, despite, syntax
- **Key terms/APIs that appear:** type, all, time, re, any

#### It’s Relatively Easy to Use
- **Span:** PDF pp. 51–51 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** programming, programs, languages, systems, language, tools, simple, rapid, program, learn, despite, syntax
- **Key terms/APIs that appear:** type, all, time, re, any

#### It’s Relatively Easy to Learn
- **Span:** PDF pp. 51–51 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** programming, programs, languages, systems, language, tools, simple, rapid, program, learn, despite, syntax
- **Key terms/APIs that appear:** type, all, time, re, any

### Chapter Summary
- **Span:** PDF pp. 52–52 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **Key concepts (from text):** answers, software, reasons, people, language, details, questions, coding, summary, programming, notable, today
- **Key terms/APIs that appear:** re, all, open, any

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 52–52 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** answers, software, reasons, people, language, details, questions, coding, summary, programming, notable, today
- **Key terms/APIs that appear:** re, all, open, any

### Test Your Knowledge: Answers
- **Span:** PDF pp. 52–54 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** answers, development, software, reasons, people, programming, today, though, language, details, knowledge, questions
- **Key terms/APIs that appear:** re, all, open, any

## Chapter 2. How Python Runs Programs
- **Span:** PDF pp. 55–64 (10 pages; detailed)
- **Breakdown:**
  - Introducing the Python Interpreter
  - Program Execution
  - Execution-Model Variations
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 6 immediate subheadings; 9 leaf subsections underneath

### Introducing the Python Interpreter
- **Span:** PDF pp. 55–55 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** interpreter, program, programs, details, executes, point, running, platform, chapters, language, write, computer
- **Key terms/APIs that appear:** set, re

### Program Execution
- **Span:** PDF pp. 56–58 (3 pages; brief)
- **Breakdown:**
  - The Programmer’s View
  - Python’s View
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### The Programmer’s View
- **Span:** PDF pp. 56–56 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** program, py, print, files, statements, script, script0, hello, world, window, command, execution
- **Key terms/APIs that appear:** print, all, script0.py, re, any, raise, type

#### Python’s View
- **Span:** PDF pp. 56–58 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** bytecode, files, program, source, py, statements, execution, programs, machine, print, compiled, common
- **Key terms/APIs that appear:** all, print, re, time, script0.py, e.g, any, import, script0.cpython, raise, type

### Execution-Model Variations
- **Span:** PDF pp. 59–62 (4 pages; moderate detail)
- **Breakdown:**
  - Python Implementation Alternatives
  - Standalone Executables
  - Future Possibilities
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Python Implementation Alternatives
- **Span:** PDF pp. 60–61 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** cpython, language, compiler, programs, jython, machine, standard, system, options, numba, implementation, ironpython
- **Key terms/APIs that appear:** all, type, time, e.g, sys, re, list, open, async, math, yield

#### Standalone Executables
- **Span:** PDF pp. 62–62 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** cpython, programs, standalone, executables, frozen, compiler, binaries, files, bundle, bytecode, micropython, system
- **Key terms/APIs that appear:** e.g, all, re, list, any

#### Future Possibilities
- **Span:** PDF pp. 63–63 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** model, bytecode, future, execution, compiler, machine, cpython, programs, really, source, standard, coding
- **Key terms/APIs that appear:** type, time, re, all

### Chapter Summary
- **Span:** PDF pp. 63–63 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** model, bytecode, future, execution, compiler, machine, cpython, programs, really, source, standard, coding
- **Key terms/APIs that appear:** type, time, re, all

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 63–63 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** model, bytecode, future, execution, compiler, machine, cpython, programs, really, source, standard, coding
- **Key terms/APIs that appear:** type, time, re, all

### Test Your Knowledge: Answers
- **Span:** PDF pp. 64–64 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** program, machine, programs, bytecode, compilers, answers, interpreter, write, instructions, files, extension, level
- **Key terms/APIs that appear:** re, all, type

## Chapter 3. How You Run Programs
- **Span:** PDF pp. 65–88 (24 pages; deep dive)
- **Breakdown:**
  - Installing Python
  - Interactive Code
  - Program Files
  - Other Ways to Run Files
  - Which Option Should I Use?
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
  - Test Your Knowledge: Part I Exercises
- **Granularity:** 9 immediate subheadings; 24 leaf subsections underneath

### Installing Python
- **Span:** PDF pp. 65–65 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** start, users, techniques, install, programs, programming, program, module, imports, installing, windows, linux
- **Key terms/APIs that appear:** all, time, re, type, set

### Interactive Code
- **Span:** PDF pp. 66–71 (6 pages; moderate detail)
- **Breakdown:**
  - Starting an Interactive REPL
  - Where to Run: Code Folders
  - What Not to Type: Prompts and Comments
  - Other Python REPLs
  - Running Code Interactively
  - Why the Interactive Prompt?
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Starting an Interactive REPL
- **Span:** PDF pp. 66–66 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** interactive, command, py, python3, windows, start, coding, install, appendix, platform, copyright, credits
- **Key terms/APIs that appear:** type, re, print, any

#### Where to Run: Code Folders
- **Span:** PDF pp. 67–67 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** folder, prompt, dedicated, interactive, system, session, windows, linux, android, platform, command, start
- **Key terms/APIs that appear:** all, re, type, e.g, a.k, set, i.e, input, except, any, sorted

#### What Not to Type: Prompts and Comments
- **Span:** PDF pp. 68–68 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** prompts, folder, repls, system, files, later, create, start, commands, lines, prompt, listings
- **Key terms/APIs that appear:** type, os, re, os.getcwd, os.chdir, set, import, except, all

#### Other Python REPLs
- **Span:** PDF pp. 68–68 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** prompts, folder, repls, system, files, later, create, start, commands, lines, prompt, listings
- **Key terms/APIs that appear:** type, os, re, os.getcwd, os.chdir, set, import, except, all

#### Running Code Interactively
- **Span:** PDF pp. 69–69 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** interactive, print, future, system, prompts, session, interactively, input, results, cpython, though, console
- **Key terms/APIs that appear:** print, type, re, input, all, sys.ps1, sys, set, time

#### Why the Interactive Prompt?
- **Span:** PDF pp. 70–71 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., NameError)
- **Key concepts (from text):** prompt, interactive, language, error, later, files, print, first, lines, system, using, import
- **Key terms/APIs that appear:** sys, type, print, re, try, import, all, sys.ps1, e.g, time

### Program Files
- **Span:** PDF pp. 72–74 (3 pages; brief)
- **Breakdown:**
  - A First Script
  - Running Files with Command Lines
  - Command-Line Usage Variations
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### A First Script
- **Span:** PDF pp. 72–72 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** files, module, program, interactive, programs, prompt, command, statements, testing, later, paste, system
- **Key terms/APIs that appear:** type, os, os.getcwd, import, any, script1.py, re, try, all, time, open, set

#### Running Files with Command Lines
- **Span:** PDF pp. 73–73 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** files, print, py, first, script, import, module, comments, script1, platform, string, named
- **Key terms/APIs that appear:** print, import, sys, re, script1.py, sys.platform, all, i.e, raise, type

#### Command-Line Usage Variations
- **Span:** PDF pp. 74–74 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** command, windows, shell, py, system, script, output, though, syntax, python3, prompt, appendix
- **Key terms/APIs that appear:** all, type, script1.py, e.g, saveit.txt, try, print, input

### Other Ways to Run Files
- **Span:** PDF pp. 75–83 (9 pages; detailed)
- **Breakdown:**
  - Clicking and Tapping File Icons
  - The IDLE Graphical User Interface
  - Other IDEs for Python
  - Smartphone Apps
  - WebAssembly for Browsers
  - Jupyter Notebooks for Science
  - Ahead-of-Time Compilers for Speed
  - Running Code in Code
  - Other Launch Options
- **Granularity:** 9 immediate subheadings; 9 leaf subsections underneath

#### Clicking and Tapping File Icons
- **Span:** PDF pp. 75–75 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** py, files, command, script, explorer, clicks, window, users, script1, output, directory, working
- **Key terms/APIs that appear:** script1.py, open, re, set, saveit.py, input, type, all

#### The IDLE Graphical User Interface
- **Span:** PDF pp. 76–76 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** windows, appendix, command, macos, linux, program, output, interactive, system, lines, clicks, standard
- **Key terms/APIs that appear:** all, script1.py, input, re

#### Other IDEs for Python
- **Span:** PDF pp. 77–77 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** command, window, shell, module, search, standard, windows, usual, files, script, platform, system
- **Key terms/APIs that appear:** any, all, open, idlelib.idle, idle.py, e.g, import, type, set, re

#### Smartphone Apps
- **Span:** PDF pp. 77–77 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** command, window, shell, module, search, standard, windows, usual, files, script, platform, system
- **Key terms/APIs that appear:** any, all, open, idlelib.idle, idle.py, e.g, import, type, set, re

#### WebAssembly for Browsers
- **Span:** PDF pp. 78–78 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** browsers, tools, webassembly, jupyter, compiler, programs, browser, pyodide, speed, cpython, development, using
- **Key terms/APIs that appear:** all, set, a.k, open, time, any

#### Jupyter Notebooks for Science
- **Span:** PDF pp. 78–78 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** browsers, tools, webassembly, jupyter, compiler, programs, browser, pyodide, speed, cpython, development, using
- **Key terms/APIs that appear:** all, set, a.k, open, time, any

#### Ahead-of-Time Compilers for Speed
- **Span:** PDF pp. 78–78 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** browsers, tools, webassembly, jupyter, compiler, programs, browser, pyodide, speed, cpython, development, using
- **Key terms/APIs that appear:** all, set, a.k, open, time, any

#### Running Code in Code
- **Span:** PDF pp. 79–82 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** module, import, files, imports, reload, modules, py, names, script1, title, attributes, myfile
- **Key terms/APIs that appear:** import, script1.py, all, open, myfile.title, threenames.py, any, re, print, time, myfile.py, i.e

#### Other Launch Options
- **Span:** PDF pp. 83–83 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** command, namespace, module, tools, system, launch, programs, options, launching, script1, py, output
- **Key terms/APIs that appear:** os, all, re, script1.py, import, os.system, subprocess.run, open, any

### Which Option Should I Use?
- **Span:** PDF pp. 84–84 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
  - calls out caveats and edge cases
- **Key concepts (from text):** command, script, lines, programs, system, start, smartphone, icons, general, environment, choice, launch
- **Key terms/APIs that appear:** all, try, set, type

### Chapter Summary
- **Span:** PDF pp. 84–84 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - flags idioms and recommended usage patterns
  - calls out caveats and edge cases
- **Key concepts (from text):** command, script, lines, programs, system, start, smartphone, icons, general, environment, choice, launch
- **Key terms/APIs that appear:** all, try, set, type

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 84–84 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - flags idioms and recommended usage patterns
  - calls out caveats and edge cases
- **Key concepts (from text):** command, script, lines, programs, system, start, smartphone, icons, general, environment, choice, launch
- **Key terms/APIs that appear:** all, try, set, type

### Test Your Knowledge: Answers
- **Span:** PDF pp. 85–85 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** module, window, command, system, interactive, output, prompt, shell, windows, macos, launch, systems
- **Key terms/APIs that appear:** type, input, open, import, i.e, os, print, time

### Test Your Knowledge: Part I Exercises
- **Span:** PDF pp. 86–88 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** error, command, debugging, py, print, start, module, errors, variable, running, directory, learn
- **Key terms/APIs that appear:** print, re, e.g, type, all, import, try, module1.py, any, set, script1.py, time

# Part II. Objects and Operations
- **Span:** PDF pp. 89–280 (192 pages; extended treatment)
- **Breakdown:**
  - Chapter 4. Introducing Python Objects
  - Chapter 5. Numbers and Expressions
  - Chapter 6. The Dynamic Typing Interlude
  - Chapter 7. String Fundamentals
  - Chapter 8. Lists and Dictionaries
  - Chapter 9. Tuples, Files, and Everything Else
- **Granularity:** 6 immediate subheadings; 137 leaf subsections underneath

## Chapter 4. Introducing Python Objects
- **Span:** PDF pp. 91–120 (30 pages; deep dive)
- **Breakdown:**
  - The Python Conceptual Hierarchy
  - Why Use Built-in Objects?
  - Python’s Core Object Types
  - Numbers
  - Strings
  - Lists
  - Dictionaries
  - Tuples
  - Files
  - Other Object Types
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 13 immediate subheadings; 31 leaf subsections underneath

### The Python Conceptual Hierarchy
- **Span:** PDF pp. 91–91 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** objects, modules, statements, expressions, things, stuff, operations, programs, built, object, hierarchy, language
- **Key terms/APIs that appear:** e.g, time

### Why Use Built-in Objects?
- **Span:** PDF pp. 92–92 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** built, objects, object, types, tools, language, level, languages, structures, usually, provide, implemented
- **Key terms/APIs that appear:** all, e.g, re, list

### Python’s Core Object Types
- **Span:** PDF pp. 93–93 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** objects, object, types, built, modules, created, program, instance, though, lists, dictionaries, functions
- **Key terms/APIs that appear:** re, collections, open, set, docs.txt, data.bin, any, type, list, range, dict, tuple

### Numbers
- **Span:** PDF pp. 94–94 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** object, types, objects, numbers, operations, instance, string, list, set, integer, expression, language
- **Key terms/APIs that appear:** list, set, type, all, time, any, try

### Strings
- **Span:** PDF pp. 95–102 (8 pages; detailed)
- **Breakdown:**
  - Sequence Operations
  - Immutability
  - Type-Specific Methods
  - Getting Help
  - Other Ways to Code Strings
  - Unicode Strings
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Sequence Operations
- **Span:** PDF pp. 96–96 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** string, indexing, operations, single, assign, second, index, variable, value, character, length, first
- **Key terms/APIs that appear:** len, time, any, a.k, type, yield

#### Immutability
- **Span:** PDF pp. 97–97 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** string, operation, strings, objects, offsets, everything, learn, later, different, characters, slice, bound
- **Key terms/APIs that appear:** all, len, property, any

#### Type-Specific Methods
- **Span:** PDF pp. 98–99 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** strings, string, methods, objects, object, using, version, immutable, place, list, bytearray, method
- **Key terms/APIs that appear:** all, list, bytearray, bytes, line.rstrip, b.extend, b.decode, e.g, s.find, s.replace, line.split, s.upper

#### Getting Help
- **Span:** PDF pp. 100–100 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** methods, method, string, function, operations, objects, names, object, list, attributes, replace, strings
- **Key terms/APIs that appear:** list, all, dir, e.g, str, astring.upper, s.replace, str.replace, builtins.str, len, type, any

#### Other Ways to Code Strings
- **Span:** PDF pp. 101–101 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** string, strings, object, characters, escape, unless, single, quotes, display, windows, pydoc, documentation
- **Key terms/APIs that appear:** type, all, len, e.g, any, str, dir, try, re, json

#### Unicode Strings
- **Span:** PDF pp. 102–102 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** bytes, unicode, strings, characters, encoded, ascii, points, encode, string, files, character, encodings
- **Key terms/APIs that appear:** bytes, len, str, print, any, all, a.k, bytearray, map

### Lists
- **Span:** PDF pp. 103–106 (4 pages; moderate detail)
- **Breakdown:**
  - Sequence Operations
  - Type-Specific Operations
  - Bounds Checking
  - Nesting
  - Comprehensions
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Sequence Operations
- **Span:** PDF pp. 103–103 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** list, lists, strings, files, objects, operations, later, string, sequence, fixed, three, return
- **Key terms/APIs that appear:** list, type, re, collections, bytes, json, csv, all, len

#### Type-Specific Operations
- **Span:** PDF pp. 103–103 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** list, lists, strings, files, objects, operations, later, string, sequence, fixed, three, return
- **Key terms/APIs that appear:** list, type, re, collections, bytes, json, csv, all, len

#### Bounds Checking
- **Span:** PDF pp. 104–104 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., IndexError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** list, py, methods, error, append, object, method, given, insert, arbitrary, remove, items
- **Key terms/APIs that appear:** list, range, l.append, l.pop, m.sort, m.reverse, try, await, any

#### Nesting
- **Span:** PDF pp. 104–104 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., IndexError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** list, py, methods, error, append, object, method, given, insert, arbitrary, remove, items
- **Key terms/APIs that appear:** list, range, l.append, l.pop, m.sort, m.reverse, try, await, any

#### Comprehensions
- **Span:** PDF pp. 105–106 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** list, matrix, comprehensions, lists, nested, comprehension, column, range, structure, second, expression, items
- **Key terms/APIs that appear:** list, range, sum, filter, print, open, time, any, yield, all

### Dictionaries
- **Span:** PDF pp. 107–111 (5 pages; moderate detail)
- **Breakdown:**
  - Mapping Operations
  - Nesting Revisited
  - Missing Keys: if Tests
  - Item Iteration: for Loops
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Mapping Operations
- **Span:** PDF pp. 107–107 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** dictionaries, dictionary, value, lists, objects, record, set, unlike, sequences, instead, mappings, collections
- **Key terms/APIs that appear:** all, sum, set, collections, range, time, re

#### Nesting Revisited
- **Span:** PDF pp. 108–108 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** dictionary, nested, first, order, list, smith, dict, prior, multiple, later, dictionaries, zipping
- **Key terms/APIs that appear:** list, dict, zip, e.g, type, all, time

#### Missing Keys: if Tests
- **Span:** PDF pp. 109–110 (2 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., KeyError)
- **Key concepts (from text):** statement, dictionary, missing, expression, later, objects, object, structure, dictionaries, result, memory, languages
- **Key terms/APIs that appear:** all, time, print, d.get, list, type, re, a.k, pickle, json, filter, try

#### Item Iteration: for Loops
- **Span:** PDF pp. 111–111 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** iteration, object, items, list, protocol, methods, values, results, iterable, dictionaries, iterator, variable
- **Key terms/APIs that appear:** time, d.keys, list, all, e.g, range, d.values, d.items, dict, collections, print

### Tuples
- **Span:** PDF pp. 112–112 (1 page; very brief)
- **Breakdown:**
  - Why Tuples?
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Why Tuples?
- **Span:** PDF pp. 113–113 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError)
- **Key concepts (from text):** tuples, tuple, object, files, write, lists, items, access, content, output, string, dictionaries
- **Key terms/APIs that appear:** tuple, open, f.write, input, list, type, t.append, data.txt, f.close, re

### Files
- **Span:** PDF pp. 113–114 (2 pages; brief)
- **Breakdown:**
  - Unicode and Byte Files
  - Other File-Like Tools
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Unicode and Byte Files
- **Span:** PDF pp. 114–114 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** files, content, binary, unicode, bytes, string, hello, print, reads, encoding, strings, world
- **Key terms/APIs that appear:** open, bytes, print, data.txt, data.bin, time, any, f.read, text.split, line.rstrip, bf.write, bf.close

#### Other File-Like Tools
- **Span:** PDF pp. 115–115 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** encoding, object, files, unicode, unidata, x84ck, types, set, content, encodings, encoded, encode
- **Key terms/APIs that appear:** open, unidata.txt, set, tf.write, tf.close, any, bytes, collections

### Other Object Types
- **Span:** PDF pp. 115–118 (4 pages; moderate detail)
- **Breakdown:**
  - Sets
  - Booleans and None
  - Types
  - Type Hinting
  - User-Defined Objects
  - And Everything Else
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Sets
- **Span:** PDF pp. 115–115 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** encoding, object, files, unicode, unidata, x84ck, types, set, content, encodings, encoded, encode
- **Key terms/APIs that appear:** open, unidata.txt, set, tf.write, tf.close, any, bytes, collections

#### Booleans and None
- **Span:** PDF pp. 116–116 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** none, set, object, list, true, objects, false, booleans, difference, duplicates, order, neutral
- **Key terms/APIs that appear:** set, type, list, filter, bool, all, print

#### Types
- **Span:** PDF pp. 116–116 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** none, set, object, list, true, objects, false, booleans, difference, duplicates, order, neutral
- **Key terms/APIs that appear:** set, type, list, filter, bool, all, print

#### Type Hinting
- **Span:** PDF pp. 117–117 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** object, types, hinting, objects, true, using, specific, polymorphism, declarations, testing, list, required
- **Key terms/APIs that appear:** type, list, all, isinstance, range, any, int

#### User-Defined Objects
- **Span:** PDF pp. 118–118 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** objects, object, class, classes, though, process, everything, defined, oriented, types, workers, worker
- **Key terms/APIs that appear:** type, all, sue.lastname, bob.lastname, sue.giveraise, sue.pay, set, re

#### And Everything Else
- **Span:** PDF pp. 118–118 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** objects, object, class, classes, though, process, everything, defined, oriented, types, workers, worker
- **Key terms/APIs that appear:** type, all, sue.lastname, bob.lastname, sue.giveraise, sue.pay, set, re

### Chapter Summary
- **Span:** PDF pp. 119–119 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, types, objects, strings, operations, available, string, knowledge, considered, sequence, specific, instance
- **Key terms/APIs that appear:** type, list, any, all, set, open

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 119–119 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, types, objects, strings, operations, available, string, knowledge, considered, sequence, specific, instance
- **Key terms/APIs that appear:** type, list, any, all, set, open

### Test Your Knowledge: Answers
- **Span:** PDF pp. 119–120 (2 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, types, objects, strings, operations, sequence, specific, method, immutable, mapping, available, calls
- **Key terms/APIs that appear:** type, all, e.g, list, any, set, open, range

## Chapter 5. Numbers and Expressions
- **Span:** PDF pp. 121–152 (32 pages; extended treatment)
- **Breakdown:**
  - Numeric Object Basics
  - Python Expression Operators
  - Numbers in Action
  - Other Numeric Objects
  - Numeric Extensions
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 8 immediate subheadings; 24 leaf subsections underneath

### Numeric Object Basics
- **Span:** PDF pp. 121–122 (2 pages; brief)
- **Breakdown:**
  - Numeric Literals
  - Built-in Numeric Tools
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Numeric Literals
- **Span:** PDF pp. 122–122 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** literals, point, numbers, floating, integers, digits, decimal, types, numeric, octal, number, object
- **Key terms/APIs that appear:** type, list, print, math, set, bool, time

#### Built-in Numeric Tools
- **Span:** PDF pp. 123–123 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** numbers, number, integer, built, complex, literals, numeric, expression, operators, expressions, string, objects
- **Key terms/APIs that appear:** all, e.g, int, math, type, str, set, random

### Python Expression Operators
- **Span:** PDF pp. 123–126 (4 pages; moderate detail)
- **Breakdown:**
  - Mixed Operators: Precedence
  - Parentheses Group Subexpressions
  - Mixed Types Are Converted Up
  - Preview: Operator Overloading and Polymorphism
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Mixed Operators: Precedence
- **Span:** PDF pp. 125–125 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** operators, operator, precedence, right, expressions, expression, parts, first, lower, higher, action, instance
- **Key terms/APIs that appear:** yield, e.g, all, collections, lambda, await, type, sum, except

#### Parentheses Group Subexpressions
- **Span:** PDF pp. 126–126 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** expressions, integer, floating, point, parentheses, first, expression, converted, result, complex, float, results
- **Key terms/APIs that appear:** type, float, math, any, re, all, int

#### Mixed Types Are Converted Up
- **Span:** PDF pp. 126–126 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** expressions, integer, floating, point, parentheses, first, expression, converted, result, complex, float, results
- **Key terms/APIs that appear:** type, float, math, any, re, all, int

#### Preview: Operator Overloading and Polymorphism
- **Span:** PDF pp. 127–127 (1 page; very brief)
- **Focus:** preview of later material
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** objects, variables, expressions, numbers, numeric, operators, integer, automatically, classes, applied, action, first
- **Key terms/APIs that appear:** all, type, e.g, any, time, i.e, float, re, property, try, math

### Numbers in Action
- **Span:** PDF pp. 127–140 (14 pages; detailed)
- **Breakdown:**
  - Variables and Basic Expressions
  - Numeric Display Formats
  - Comparison Operators
  - Division Operators
  - Integer Precision
  - Complex Numbers
  - Hex, Octal, and Binary
  - Bitwise Operations
  - Underscore Separators in Numbers
  - Other Built-in Numeric Tools
- **Granularity:** 10 immediate subheadings; 10 leaf subsections underneath

#### Variables and Basic Expressions
- **Span:** PDF pp. 127–128 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., NameError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** objects, expressions, variables, expression, numbers, first, values, automatically, assigned, integer, results, result
- **Key terms/APIs that appear:** type, re, all, any, e.g, i.e, time, float, property, try, math, list

#### Numeric Display Formats
- **Span:** PDF pp. 129–129 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** floating, point, digits, results, display, numbers, string, formatting, strings, decimal, result, values
- **Key terms/APIs that appear:** time, print, map

#### Comparison Operators
- **Span:** PDF pp. 130–131 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** false, true, comparisons, str, tests, numbers, objects, string, numeric, expressions, chained, print
- **Key terms/APIs that appear:** str, print, type, range, e.g, math, bytes.decode, bytes, all, float, import

#### Division Operators
- **Span:** PDF pp. 132–133 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** floor, division, result, true, truncation, int, remainder, trunc, import, types, round, operators
- **Key terms/APIs that appear:** math, int, import, type, math.trunc, float, math.floor, math.isclose, tuple

#### Integer Precision
- **Span:** PDF pp. 134–134 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., ValueError)
  - includes performance/efficiency notes
- **Key concepts (from text):** numbers, complex, precision, integer, standard, integers, imaginary, parts, programming, support, unlimited, built
- **Key terms/APIs that appear:** math, sys.set_int_max_str_digits, sys, type, all

#### Complex Numbers
- **Span:** PDF pp. 134–134 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., ValueError)
  - includes performance/efficiency notes
- **Key concepts (from text):** numbers, complex, precision, integer, standard, integers, imaginary, parts, programming, support, unlimited, built
- **Key terms/APIs that appear:** math, sys.set_int_max_str_digits, sys, type, all

#### Hex, Octal, and Binary
- **Span:** PDF pp. 134–135 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., ValueError)
  - includes performance/efficiency notes
- **Key concepts (from text):** numbers, complex, strings, value, integer, digits, binary, decimal, int, integers, string, octal
- **Key terms/APIs that appear:** int, math, all, sys.set_int_max_str_digits, sys, type, bytes, try, map, any

#### Bitwise Operations
- **Span:** PDF pp. 136–136 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** binary, bitwise, operations, numbers, format, digits, formatting, octal, tools, probably, generally, converters
- **Key terms/APIs that appear:** re, dict, math

#### Underscore Separators in Numbers
- **Span:** PDF pp. 137–138 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., NameError, SyntaxError)
  - includes performance/efficiency notes
- **Key concepts (from text):** number, string, true, underscores, numbers, literals, digits, binary, decimal, digit, separators, values
- **Key terms/APIs that appear:** len, float, int, re, tuple, x.bit_length, all, bytes, any, except

#### Other Built-in Numeric Tools
- **Span:** PDF pp. 139–140 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** random, built, module, round, numbers, tools, functions, library, modules, import, statistics, underscores
- **Key terms/APIs that appear:** math, random, import, math.sqrt, int, math.pi, math.floor, math.trunc, random.random, random.randint, sum, min

### Other Numeric Objects
- **Span:** PDF pp. 141–150 (10 pages; detailed)
- **Breakdown:**
  - Decimal Objects
  - Fraction Objects
  - Set Objects
  - Boolean Objects
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Decimal Objects
- **Span:** PDF pp. 141–141 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** decimal, floating, point, random, numeric, suits, decimals, tikka, lasagna, hearts, clubs, diamonds
- **Key terms/APIs that appear:** random, random.choice, random.shuffle, math, e.g, a.k, yield, print, import

#### Fraction Objects
- **Span:** PDF pp. 142–143 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** decimal, fraction, floating, point, precision, number, object, decimals, digits, objects, module, fractions
- **Key terms/APIs that appear:** decimal.decimal, math, import, type, all, decimal.from_float, decimal.getcontext, str, yield, set, input, property

#### Set Objects
- **Span:** PDF pp. 144–149 (6 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
  - includes performance/efficiency notes
- **Key concepts (from text):** set, decimal, objects, fraction, list, order, results, items, comprehensions, engineers, operations, literal
- **Key terms/APIs that appear:** set, list, all, type, sorted, s.add, collections, any, import, re, decimal.decimal, filter

#### Boolean Objects
- **Span:** PDF pp. 150–150 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** true, false, engineers, managers, bool, boolean, objects, though, set, object, values, integers
- **Key terms/APIs that appear:** type, bool, all, set, print, int, time, except, str, yield, isinstance

### Numeric Extensions
- **Span:** PDF pp. 151–151 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** numeric, expression, extensions, tools, domain, object, value, objects, address, coding, though, types
- **Key terms/APIs that appear:** type, time, any, open, re

### Chapter Summary
- **Span:** PDF pp. 151–151 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** numeric, expression, extensions, tools, domain, object, value, objects, address, coding, though, types
- **Key terms/APIs that appear:** type, time, any, open, re

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 151–151 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** numeric, expression, extensions, tools, domain, object, value, objects, address, coding, though, types
- **Key terms/APIs that appear:** type, time, any, open, re

### Test Your Knowledge: Answers
- **Span:** PDF pp. 152–152 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** floating, point, result, expression, integer, string, number, binary, function, octal, hexadecimal, square
- **Key terms/APIs that appear:** math, type, int, i.e, math.sqrt, e.g, math.trunc, math.floor, import, float, all

## Chapter 6. The Dynamic Typing Interlude
- **Span:** PDF pp. 153–166 (14 pages; detailed)
- **Breakdown:**
  - The Case of the Missing Declaration Statements
  - Shared References
  - Dynamic Typing Is Everywhere
  - Type Hinting: Optional, Unused, and Why?
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 7 immediate subheadings; 10 leaf subsections underneath

### The Case of the Missing Declaration Statements
- **Span:** PDF pp. 153–157 (5 pages; moderate detail)
- **Breakdown:**
  - Variables, Objects, and References
  - Types Live with Objects, Not Variables
  - Objects Are Garbage-Collected
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Variables, Objects, and References
- **Span:** PDF pp. 154–155 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, objects, variables, variable, references, value, memory, names, never, links, pointers, model
- **Key terms/APIs that appear:** type, all, i.e, any, time, e.g, a.k, sum, list

#### Types Live with Objects, Not Variables
- **Span:** PDF pp. 156–156 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** object, objects, types, variable, integer, string, variables, happens, reference, different, point, simply
- **Key terms/APIs that appear:** type, all, time, int, str, float, any

#### Objects Are Garbage-Collected
- **Span:** PDF pp. 156–157 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** object, objects, reference, garbage, types, space, references, collection, variable, integer, string, different
- **Key terms/APIs that appear:** type, time, all, re, e.g, l.append, a.k, int, str, float, any, set

### Shared References
- **Span:** PDF pp. 158–161 (4 pages; moderate detail)
- **Breakdown:**
  - Shared References and In-Place Changes
  - Shared References and Equality
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Shared References and In-Place Changes
- **Span:** PDF pp. 159–160 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, objects, list, place, change, references, different, changes, assignment, changed, variable, reference
- **Key terms/APIs that appear:** list, all, l1.copy, x.copy, type, re, collections, time, set

#### Shared References and Equality
- **Span:** PDF pp. 161–161 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** objects, object, shared, references, different, true, lists, equality, reference, names, nested, values
- **Key terms/APIs that appear:** any, type, copy.copy, copy.deepcopy, dict, set, import, all, open, time, except

### Dynamic Typing Is Everywhere
- **Span:** PDF pp. 162–162 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, dynamic, typing, cached, reference, different, true, though, getrefcount, model, immutable, objects
- **Key terms/APIs that appear:** sys, sys.getrefcount, import, all, re

### Type Hinting: Optional, Unused, and Why?
- **Span:** PDF pp. 163–163 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., NameError)
- **Key concepts (from text):** hints, list, optional, unused, int, hinting, float, types, tools, strings, function, variable
- **Key terms/APIs that appear:** type, list, int, float, any, e.g, collections, str

### Chapter Summary
- **Span:** PDF pp. 164–164 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** dynamic, typing, language, hinting, typed, value, model, statements, references, notion, dynamically, learners
- **Key terms/APIs that appear:** type, any, all

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 164–164 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** dynamic, typing, language, hinting, typed, value, model, statements, references, notion, dynamically, learners
- **Key terms/APIs that appear:** type, any, all

### Test Your Knowledge: Answers
- **Span:** PDF pp. 165–166 (2 pages; brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** object, references, reference, string, changed, prints, assigned, point, statement, place, really, list
- **Key terms/APIs that appear:** all, list, i.e, tuple, time

## Chapter 7. String Fundamentals
- **Span:** PDF pp. 167–210 (44 pages; extended treatment)
- **Breakdown:**
  - String Object Basics
  - String Literals
  - Strings in Action
  - String Methods
  - String Formatting: The Triathlon
  - General Type Categories
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 9 immediate subheadings; 24 leaf subsections underneath

### String Object Basics
- **Span:** PDF pp. 167–168 (2 pages; brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** strings, string, unicode, bytes, files, tools, processing, operations, object, characters, ascii, basics
- **Key terms/APIs that appear:** bytes, type, set, e.g, data.txt, s.find, s.rstrip, s.replace, s.split, s.isdigit, s.lower, s.endswith

### String Literals
- **Span:** PDF pp. 169–175 (7 pages; moderate detail)
- **Breakdown:**
  - Single and Double Quotes Are the Same
  - Escape Sequences Are Special Characters
  - Raw Strings Suppress Escapes
  - Triple Quotes and Multiline Strings
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Single and Double Quotes Are the Same
- **Span:** PDF pp. 169–169 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** string, quotes, tools, double, literals, single, forms, strings, library, advanced, though, quote
- **Key terms/APIs that appear:** re, all, s.lower, re.match, test.bin, print, map, set, json, bytes, type

#### Escape Sequences Are Special Characters
- **Span:** PDF pp. 170–173 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** string, characters, character, escape, escapes, strings, point, bytes, value, unicode, single, values
- **Key terms/APIs that appear:** bytes, all, len, any, print, re, str, e.g, a.k, except, tuple, map

#### Raw Strings Suppress Escapes
- **Span:** PDF pp. 174–174 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** strings, backslashes, windows, string, escapes, escape, characters, myfile, directory, usually, works, backslash
- **Key terms/APIs that appear:** text.dat, open, print, any, len, ext.dat, e.g, re, time

#### Triple Quotes and Multiline Strings
- **Span:** PDF pp. 175–175 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** string, strings, single, quotes, triple, literal, double, three, quoted, backslash, quote, character
- **Key terms/APIs that appear:** all, any, type, print, re

### Strings in Action
- **Span:** PDF pp. 176–183 (8 pages; detailed)
- **Breakdown:**
  - Basic Operations
  - Indexing and Slicing
  - String Conversion Tools
  - “Changing” Strings Part 1: Sequence Operations
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Basic Operations
- **Span:** PDF pp. 176–177 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** string, strings, py, print, triple, using, comments, quoted, operator, myjob, added, characters
- **Key terms/APIs that appear:** print, open, os, len, e.g, os.getcwd, str.find, json, import, any, re, str

#### Indexing and Slicing
- **Span:** PDF pp. 178–180 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., IndexError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** items, slicing, offset, offsets, slice, string, fetches, bounds, object, indexing, length, first
- **Key terms/APIs that appear:** all, re, a.k, collections, type, map, try, len, range, reversed

#### String Conversion Tools
- **Span:** PDF pp. 181–182 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** string, character, number, str, convert, int, function, slices, built, expression, tools, strings
- **Key terms/APIs that appear:** str, int, all, sys, echo.py, list, sys.argv, print, re, float, math, line.rstrip

#### “Changing” Strings Part 1: Sequence Operations
- **Span:** PDF pp. 183–183 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** string, strings, character, true, sequence, concatenation, change, using, int, ordinals, comparisons, compares
- **Key terms/APIs that appear:** int, collections, all, str

### String Methods
- **Span:** PDF pp. 184–188 (5 pages; moderate detail)
- **Breakdown:**
  - Method Call Syntax
  - All String Methods (Today)
  - “Changing” Strings, Part 2: String Methods
  - More String Methods: Parsing Text
  - Other Common String Methods
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Method Call Syntax
- **Span:** PDF pp. 184–184 (1 page; very brief)
- **Focus:** syntax forms and call/usage rules
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** string, methods, objects, operations, object, strings, attribute, value, bytearray, functions, method, function
- **Key terms/APIs that appear:** bytearray, type, s.replace, e.g, object.attribute, except, re, print, str, all, set, range

#### All String Methods (Today)
- **Span:** PDF pp. 185–185 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** method, object, string, methods, start, arguments, result, optional, width, expression, mapping, built
- **Key terms/APIs that appear:** s.find, all, any, object.method, s.capitalize, s.ljust, s.casefold, s.lower, s.center, s.lstrip, s.count, s.maketrans

#### “Changing” Strings, Part 2: String Methods
- **Span:** PDF pp. 186–187 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** string, replace, strings, method, list, substring, py, methods, sequence, object, iterable, operations
- **Key terms/APIs that appear:** list, any, s.replace, all, e.g, time, s.isidentifier, s.startswith, s.islower, s.strip, s.isnumeric, s.swapcase

#### More String Methods: Parsing Text
- **Span:** PDF pp. 188–188 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** string, substrings, split, parsing, list, delimiter, py, earlier, simple, methods, common, fixed
- **Key terms/APIs that appear:** line.split, list, csv, all, bytearray

#### Other Common String Methods
- **Span:** PDF pp. 189–189 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** string, methods, awesome, true, method, strings, formatting, python's, endswith, operations, whitespace, perform
- **Key terms/APIs that appear:** line.endswith, re, line.rstrip, line.upper, line.isalpha, line.startswith, line.find, s.method, str.method, len, any, str

### String Formatting: The Triathlon
- **Span:** PDF pp. 189–205 (17 pages; deep dive)
- **Breakdown:**
  - String-Formatting Options
  - The String-Formatting Expression
  - The String-Formatting Method
  - The F-String Formatting Literal
  - And the Winner Is…
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### String-Formatting Options
- **Span:** PDF pp. 190–190 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** formatting, string, tools, value, three, options, method, format, expression, history, today, functionality
- **Key terms/APIs that appear:** all, re, string.template, time, try, set

#### The String-Formatting Expression
- **Span:** PDF pp. 191–194 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** string, formatting, format, expression, values, point, right, floating, conversion, targets, dictionary, strings
- **Key terms/APIs that appear:** type, all, any, str, tuple, vars, e.g, list, set, print, re, time

#### The String-Formatting Method
- **Span:** PDF pp. 195–199 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** format, method, formatting, string, template, first, arguments, fstring, expression, expressions, object, argument
- **Key terms/APIs that appear:** type, sys, e.g, all, any, template.format, dict, tuple, list, int, re, map

#### The F-String Formatting Literal
- **Span:** PDF pp. 200–204 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** string, format, strings, expression, method, formatting, values, expressions, f'learning, width, formatted, though
- **Key terms/APIs that appear:** any, str, what.upper, re, print, all, str.format, e.g, a.k, list, time, bytes

#### And the Winner Is…
- **Span:** PDF pp. 205–205 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** formatting, scripting, strings, string, expression, f'use, values, loaded, files, method, edition, expressions
- **Key terms/APIs that appear:** any, e.g, time, re, all

### General Type Categories
- **Span:** PDF pp. 206–207 (2 pages; brief)
- **Breakdown:**
  - Types Share Operation Sets by Categories
  - Mutable Types Can Be Changed in Place
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Types Share Operation Sets by Categories
- **Span:** PDF pp. 206–206 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** string, formatter, formatters, types, three, categories, template, tools, strings, built, module, templating
- **Key terms/APIs that appear:** all, type, string.template, t.substitute, dict, import, collections

#### Mutable Types Can Be Changed in Place
- **Span:** PDF pp. 207–207 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, types, strings, sequence, support, lists, objects, place, tuples, immutable, numbers, sequences
- **Key terms/APIs that appear:** type, any, map, list, all, try, bytearray

### Chapter Summary
- **Span:** PDF pp. 208–208 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** string, method, expression, strings, types, character, object, list, integer, methods, sequence, expressions
- **Key terms/APIs that appear:** type, list, set, collections, all, len, any

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 208–208 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** string, method, expression, strings, types, character, object, list, integer, methods, sequence, expressions
- **Key terms/APIs that appear:** type, list, set, collections, all, len, any

### Test Your Knowledge: Answers
- **Span:** PDF pp. 208–210 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** string, method, strings, expression, character, types, characters, object, unicode, list, slice, ascii
- **Key terms/APIs that appear:** type, list, set, all, len, s.split, collections, any, range, try, print

## Chapter 8. Lists and Dictionaries
- **Span:** PDF pp. 211–244 (34 pages; extended treatment)
- **Breakdown:**
  - Lists
  - Lists in Action
  - Dictionaries
  - Dictionaries in Action
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 7 immediate subheadings; 20 leaf subsections underneath

### Lists
- **Span:** PDF pp. 211–212 (2 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** lists, list, object, strings, objects, operations, contain, place, index, mutable, items, sequence
- **Key terms/APIs that appear:** list, any, type, collections, all, i.e, l.append, l.extend, l.insert, l.index, l.count, re

### Lists in Action
- **Span:** PDF pp. 213–221 (9 pages; detailed)
- **Breakdown:**
  - Basic List Operations
  - Indexing and Slicing
  - Changing Lists in Place
  - More List Methods
  - Iteration, Comprehensions, and Unpacking
  - Other List Operations
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Basic List Operations
- **Span:** PDF pp. 213–213 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** list, lists, operations, py, assignment, square, strings, concatenation, written, runtime, literal, operation
- **Key terms/APIs that appear:** list, l.sort, l.reverse, l.copy, l.clear, l.pop, l.remove, range, map, type, all, except

#### Indexing and Slicing
- **Span:** PDF pp. 214–214 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** lists, list, string, nested, slicing, matrix, true, indexing, strings, instance, convert, str
- **Key terms/APIs that appear:** list, type, str, all

#### Changing Lists in Place
- **Span:** PDF pp. 215–217 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** list, slice, object, place, append, insert, items, assignment, lists, extend, write, replaces
- **Key terms/APIs that appear:** list, all, l.append, l.sort, len, l.extend, l.insert, str.lower, type, str, time

#### More List Methods
- **Span:** PDF pp. 218–219 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** list, sorted, sorting, lists, built, methods, offset, py, value, function, default, mixed
- **Key terms/APIs that appear:** list, sorted, str, l.append, l.pop, type, reversed, l.sort, all, str.lower, list.sort, x.lower

#### Iteration, Comprehensions, and Unpacking
- **Span:** PDF pp. 220–221 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** list, unpacking, sequence, range, loops, lists, items, iterable, comprehensions, iteration, expression, results
- **Key terms/APIs that appear:** list, range, any, map, print, all, tuple, res.append, m.extend, filter, re

#### Other List Operations
- **Span:** PDF pp. 222–222 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** dictionaries, list, lists, delete, place, py, empty, operations, slice, object, languages, mutable
- **Key terms/APIs that appear:** list, all, type, collections, l.copy, time, try, property, set, any

### Dictionaries
- **Span:** PDF pp. 222–223 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** dictionaries, list, lists, dictionary, operations, object, place, objects, tables, empty, mutable, delete
- **Key terms/APIs that appear:** list, type, any, collections, dict, all, set, l.copy, e.g, time, try, property

### Dictionaries in Action
- **Span:** PDF pp. 224–240 (17 pages; deep dive)
- **Breakdown:**
  - Basic Dictionary Operations
  - Changing Dictionaries in Place
  - More Dictionary Methods
  - Other Dictionary Makers
  - Dictionary Comprehensions
  - Key Insertion Ordering
  - Dictionary “Union” Operator
  - Intermission: Books Database
  - Dictionary Usage Tips
- **Granularity:** 9 immediate subheadings; 9 leaf subsections underneath

#### Basic Dictionary Operations
- **Span:** PDF pp. 225–225 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** dictionaries, dictionary, list, py, value, works, create, insertion, index, lists, notice, order
- **Key terms/APIs that appear:** list, all, len, d.keys, sorted

#### Changing Dictionaries in Place
- **Span:** PDF pp. 225–225 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** dictionaries, dictionary, list, py, value, works, create, insertion, index, lists, notice, order
- **Key terms/APIs that appear:** list, all, len, d.keys, sorted

#### More Dictionary Methods
- **Span:** PDF pp. 226–226 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** list, dictionary, py, program, value, values, entry, years, lists, methods, script, present
- **Key terms/APIs that appear:** list, all, d.get, d.pop, d.keys, d.values, d.items, type, time, print

#### Other Dictionary Makers
- **Span:** PDF pp. 227–228 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** dict, dictionary, values, dictionaries, value, method, list, literal, literals, update, keyword, similar
- **Key terms/APIs that appear:** dict, all, list, time, any, d.pop, l.pop, type, zip, d.update, dict.fromkeys, dir

#### Dictionary Comprehensions
- **Span:** PDF pp. 229–229 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** dictionary, values, comprehensions, iterable, dictionaries, list, value, comprehension, effect, result, dict, basic
- **Key terms/APIs that appear:** zip, list, dict, set, map, any, tuple, re, range

#### Key Insertion Ordering
- **Span:** PDF pp. 230–230 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** none, order, dictionary, comprehensions, dictionaries, dict, insertion, py, fromkeys, list, lists, method
- **Key terms/APIs that appear:** dict, list, dict.fromkeys, set, c.lower, e.g, d.pop, filter, all, random, any

#### Dictionary “Union” Operator
- **Span:** PDF pp. 231–231 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** dictionary, update, union, dictionaries, dict, popitem, really, though, place, insertion, order, ordering
- **Key terms/APIs that appear:** dict, d.popitem, c.update, set, i.e, d.copy, list, tuple, all

#### Intermission: Books Database
- **Span:** PDF pp. 232–233 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** value, dictionary, edition, values, items, dictionaries, list, titles, title, given, simple, method
- **Key terms/APIs that appear:** list, all, map, dict, print, d.keys, mapattrs.py, set, tuple, zip

#### Dictionary Usage Tips
- **Span:** PDF pp. 234–240 (7 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError, IndexError, KeyError, TypeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** list, dictionary, items, dictionaries, values, dict, lists, sorted, matrix, objects, views, set
- **Key terms/APIs that appear:** list, dict, sorted, d.keys, set, d.items, print, d1.items, d2.items, time, any, all

### Chapter Summary
- **Span:** PDF pp. 241–241 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **Key concepts (from text):** list, dictionary, place, value, dictionaries, change, lists, operations, slice, append, assignment, object
- **Key terms/APIs that appear:** list, type, dict, l.append, dict.fromkeys, d.pop, collections, time, range, all, any

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 241–241 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** list, dictionary, place, value, dictionaries, change, lists, operations, slice, append, assignment, object
- **Key terms/APIs that appear:** list, type, dict, l.append, dict.fromkeys, d.pop, collections, time, range, all, any

### Test Your Knowledge: Answers
- **Span:** PDF pp. 241–244 (4 pages; moderate detail)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** list, dictionary, dictionaries, lists, record, place, value, collections, dict, types, objects, change
- **Key terms/APIs that appear:** list, collections, dict, all, type, set, l.append, dict.fromkeys, d.pop, s.add, time, range

## Chapter 9. Tuples, Files, and Everything Else
- **Span:** PDF pp. 245–280 (36 pages; extended treatment)
- **Breakdown:**
  - Tuples
  - Files
  - Core Types Review and Summary
  - Other Types in Python
  - Built-in Type Gotchas
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
  - Test Your Knowledge: Part II Exercises
- **Granularity:** 9 immediate subheadings; 28 leaf subsections underneath

### Tuples
- **Span:** PDF pp. 245–250 (6 pages; moderate detail)
- **Breakdown:**
  - Tuples in Action
  - Why Lists and Tuples?
  - Records Revisited: Named Tuples
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Tuples in Action
- **Span:** PDF pp. 247–248 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** tuples, parentheses, tuple, list, lists, sequence, object, operations, really, syntax, true, comma
- **Key terms/APIs that appear:** tuple, list, sorted, any, e.g, tmp.sort, all, print, lambda

#### Why Lists and Tuples?
- **Span:** PDF pp. 249–249 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** tuple, tuples, lists, objects, index, list, though, offset, immutability, change, comprehension, generator
- **Key terms/APIs that appear:** tuple, list, t.index, t.count, e.g, any, time, collections

#### Records Revisited: Named Tuples
- **Span:** PDF pp. 250–250 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** dictionary, tuples, record, access, tuple, named, types, list, built, extension, fields, position
- **Key terms/APIs that appear:** tuple, list, type, import, collections, pat.values, pat.items, pat.name, pat.jobs, pat._asdict, set, dict

### Files
- **Span:** PDF pp. 251–261 (11 pages; detailed)
- **Breakdown:**
  - Opening Files
  - Using Files
  - Files in Action
  - Text and Binary Files: The Short Story
  - Storing Objects with Conversions
  - Storing Objects with pickle
  - Storing Objects with JSON
  - Storing Objects with Other Tools
  - File Context Managers
  - Other File Tools
- **Granularity:** 10 immediate subheadings; 10 leaf subsections underneath

#### Opening Files
- **Span:** PDF pp. 252–252 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** filename, files, processing, strings, external, arguments, argument, string, output, content, write, first
- **Key terms/APIs that appear:** open, e.g, all, file.txt, os, input, afile.method, os.getcwd, time, import

#### Using Files
- **Span:** PDF pp. 252–253 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** files, strings, object, close, filename, string, output, content, write, objects, external, processing
- **Key terms/APIs that appear:** open, e.g, all, time, file.txt, os, input, any, print, afile.method, os.getcwd, import

#### Files in Action
- **Span:** PDF pp. 254–254 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** myfile, string, empty, write, lines, newline, readline, hello, goodbye, output, strings, input
- **Key terms/APIs that appear:** open, myfile.txt, myfile.readline, input, print, myfile.write, all, myfile.close, time

#### Text and Binary Files: The Short Story
- **Span:** PDF pp. 255–255 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** files, myfile, users, windows, write, str, string, escapes, slashes, print, myfile2, directory
- **Key terms/APIs that appear:** open, str, os, myfile2.txt, myfile.txt, print, myfile.write, newdata.txt, float, myfile.close, os.getcwd, os.listdir

#### Storing Objects with Conversions
- **Span:** PDF pp. 256–257 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** files, string, binary, strings, write, unicode, bytes, objects, numbers, content, convert, ascii
- **Key terms/APIs that appear:** open, bytes, all, datafile.txt, f.write, str, int, myfile3.bin, f.readline, line.rstrip, any, re

#### Storing Objects with pickle
- **Span:** PDF pp. 258–258 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** pickle, object, list, objects, dictionary, string, parts, expression, convert, converting, strings, using
- **Key terms/APIs that appear:** pickle, list, any, all, open, datafile.pkl, int, f.readline, line.split, pickle.dump, f.close, pickle.load

#### Storing Objects with JSON
- **Span:** PDF pp. 259–259 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** json, objects, pickle, format, module, files, first, smith, shelve, string, options, binary
- **Key terms/APIs that appear:** json, pickle, json.dumps, import, re, dict, datafile.pkl, json.loads, bytes, open, sys, range

#### Storing Objects with Other Tools
- **Span:** PDF pp. 260–260 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** json, files, struct, csv, testjson, module, strings, unicode, binary, close, print, readable
- **Key terms/APIs that appear:** json, open, csv, testjson.txt, file.close, data.bin, print, import, map, json.dump, json.load, struct.pack

#### File Context Managers
- **Span:** PDF pp. 261–261 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** files, myfile, close, details, additional, tools, context, though, processing, output, statement, objects
- **Key terms/APIs that appear:** open, try, data.txt, sys, myfile.close, sys.stdout, all, dir, print

#### Other File Tools
- **Span:** PDF pp. 261–261 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** files, myfile, close, details, additional, tools, context, though, processing, output, statement, objects
- **Key terms/APIs that appear:** open, try, data.txt, sys, myfile.close, sys.stdout, all, dir, print

### Core Types Review and Summary
- **Span:** PDF pp. 262–271 (10 pages; detailed)
- **Breakdown:**
  - Object Flexibility
  - References Versus Copies
  - Comparisons, Equality, and Truth
  - The Meaning of True and False in Python
  - Python’s Type Hierarchies
  - Type Objects
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Object Flexibility
- **Span:** PDF pp. 263–263 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** object, sequence, lists, dictionaries, called, types, tuples, choose, index, mutable, mapping, extension
- **Key terms/APIs that appear:** type, set, any, e.g, bytearray, collections

#### References Versus Copies
- **Span:** PDF pp. 264–265 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** list, references, object, copies, objects, reference, dictionary, nested, assigned, changing, three, shared
- **Key terms/APIs that appear:** list, set, dict, x.copy, l.copy, d.copy, any, all

#### Comparisons, Equality, and Truth
- **Span:** PDF pp. 266–268 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** objects, nested, comparisons, magnitude, true, object, equality, structures, tests, comparison, value, lists
- **Key terms/APIs that appear:** all, type, sorted, e.g, str, int, list, time, dict, copy.deepcopy, i.e, any

#### The Meaning of True and False in Python
- **Span:** PDF pp. 269–270 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., IndexError)
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** false, true, none, object, list, items, words, sorted, values, objects, value, boolean
- **Key terms/APIs that appear:** list, type, sorted, d1.items, any, bool, d2.items, print, re, all, time, range

#### Python’s Type Hierarchies
- **Span:** PDF pp. 271–271 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, types, built, objects, functions, names, bool, though, statements, function, isinstance, true
- **Key terms/APIs that appear:** type, e.g, bool, isinstance, all, list, types.functiontype, dict, str, tuple, int, float

#### Type Objects
- **Span:** PDF pp. 271–271 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, types, built, objects, functions, names, bool, though, statements, function, isinstance, true
- **Key terms/APIs that appear:** type, e.g, bool, isinstance, all, list, types.functiontype, dict, str, tuple, int, float

### Other Types in Python
- **Span:** PDF pp. 272–272 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** types, objects, object, classes, major, built, organized, categories, besides, studied, program, tions
- **Key terms/APIs that appear:** tuple

### Built-in Type Gotchas
- **Span:** PDF pp. 273–274 (2 pages; brief)
- **Breakdown:**
  - Assignment Creates References, Not Copies
  - Repetition Adds One Level Deep
  - Beware of Cyclic Data Structures
  - Immutable Types Can’t Be Changed in Place
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Assignment Creates References, Not Copies
- **Span:** PDF pp. 273–273 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - calls out caveats and edge cases
- **Key concepts (from text):** built, objects, references, tools, range, sequence, list, object, level, changes, types, language
- **Key terms/APIs that appear:** range, type, list, e.g, import, re, all, re.compile, open, lambda, time

#### Repetition Adds One Level Deep
- **Span:** PDF pp. 274–274 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** list, sequence, level, object, repetition, times, assigned, references, shared, remember, slice, mutable
- **Key terms/APIs that appear:** list, open, all, range, re

#### Beware of Cyclic Data Structures
- **Span:** PDF pp. 275–275 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, cycle, cyclic, immutable, place, reference, programs, objects, structures, exercise, getting, stuff
- **Key terms/APIs that appear:** re, open, tuple, l.append, reloadall.py, list, set, all, any, type

#### Immutable Types Can’t Be Changed in Place
- **Span:** PDF pp. 275–275 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, cycle, cyclic, immutable, place, reference, programs, objects, structures, exercise, getting, stuff
- **Key terms/APIs that appear:** re, open, tuple, l.append, reloadall.py, list, set, all, any, type

### Chapter Summary
- **Span:** PDF pp. 275–275 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, cycle, cyclic, immutable, place, reference, programs, objects, structures, exercise, getting, stuff
- **Key terms/APIs that appear:** re, open, tuple, l.append, reloadall.py, list, set, all, any, type

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 276–276 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, objects, tuple, tuples, strings, types, files, json, list, processing, default, module
- **Key terms/APIs that appear:** tuple, all, type, json, list, pickle, open, input, e.g, len, any, set

### Test Your Knowledge: Answers
- **Span:** PDF pp. 276–276 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, objects, tuple, tuples, strings, types, files, json, list, processing, default, module
- **Key terms/APIs that appear:** tuple, all, type, json, list, pickle, open, input, e.g, len, any, set

### Test Your Knowledge: Part II Exercises
- **Span:** PDF pp. 277–280 (4 pages; moderate detail)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** list, string, object, indexing, strings, happens, slice, following, slicing, bounds, lists, characters
- **Key terms/APIs that appear:** list, e.g, try, type, tuple, time, any, myfile.txt, all, re, copy.deepcopy, adict.copy

# Part III. Statements and Syntax
- **Span:** PDF pp. 281–414 (134 pages; extended treatment)
- **Breakdown:**
  - Chapter 10. Introducing Python Statements
  - Chapter 11. Assignments, Expressions, and Prints
  - Chapter 12. if and match Selections
  - Chapter 13. while and for Loops
  - Chapter 14. Iterations and Comprehensions
  - Chapter 15. The Documentation Interlude
- **Granularity:** 6 immediate subheadings; 85 leaf subsections underneath

## Chapter 10. Introducing Python Statements
- **Span:** PDF pp. 283–298 (16 pages; deep dive)
- **Breakdown:**
  - The Python Conceptual Hierarchy Revisited
  - Python’s Statements
  - A Tale of Two ifs
  - A Quick Example: Interactive Loops
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 7 immediate subheadings; 15 leaf subsections underneath

### The Python Conceptual Hierarchy Revisited
- **Span:** PDF pp. 283–283 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** statements, objects, expressions, programs, statement, program, hierarchy, modules, process, built, chapters, things
- **Key terms/APIs that appear:** e.g, re

### Python’s Statements
- **Span:** PDF pp. 284–285 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** statements, print, statement, await, reserved, syntax, functions, continue, expressions, yield, words, though
- **Key terms/APIs that appear:** print, await, type, yield, async, import, set, sys, try, except, raise, list

### A Tale of Two ifs
- **Span:** PDF pp. 286–291 (6 pages; moderate detail)
- **Breakdown:**
  - What Python Adds
  - What Python Removes
  - Why Indentation Syntax?
  - A Few Special Cases
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### What Python Adds
- **Span:** PDF pp. 286–286 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., SyntaxError)
- **Key concepts (from text):** statement, colon, statements, language, syntax, programmers, typing, character, nested, header, equivalent, thing
- **Key terms/APIs that appear:** any, type, all

#### What Python Removes
- **Span:** PDF pp. 286–287 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., SyntaxError)
- **Key concepts (from text):** statement, statements, language, syntax, colon, parentheses, languages, nested, block, semicolons, programmers, required
- **Key terms/APIs that appear:** type, re, any, all, set

#### Why Indentation Syntax?
- **Span:** PDF pp. 288–289 (2 pages; brief)
- **Focus:** syntax forms and call/usage rules
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., IndentationError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** indentation, language, block, nested, indent, statements, syntax, indented, right, spaces, consistent, outer
- **Key terms/APIs that appear:** any, all

#### A Few Special Cases
- **Span:** PDF pp. 290–291 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** statements, statement, lines, nested, block, special, language, spaces, indentation, syntax, braces, print
- **Key terms/APIs that appear:** any, print, set, all, sum, re, list

### A Quick Example: Interactive Loops
- **Span:** PDF pp. 292–296 (5 pages; moderate detail)
- **Breakdown:**
  - A Simple Interactive Loop
  - Doing Math on User Inputs
  - Handling Errors by Testing Inputs
  - Handling Errors with try Statements
  - Supporting Floating-Point Numbers
  - Nesting Code Three Levels Deep
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### A Simple Interactive Loop
- **Span:** PDF pp. 292–292 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** statements, statement, compound, true, single, simple, write, print, lines, syntax, interactive, reply
- **Key terms/APIs that appear:** print, any, re, interact.py, reply.upper, time, all, input

#### Doing Math on User Inputs
- **Span:** PDF pp. 293–293 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** input, reply, statement, enter, expression, string, nested, header, indented, effect, returns, appears
- **Key terms/APIs that appear:** input, print, all, math, e.g, reply.upper, open, try, type, str, int

#### Handling Errors by Testing Inputs
- **Span:** PDF pp. 294–294 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., ValueError)
- **Key concepts (from text):** reply, print, enter, int, script, input, string, isdigit, statement, true, convert, object
- **Key terms/APIs that appear:** print, int, input, math, time, i.e, s.isdigit, t.isdigit, reply.isdigit, all, raise, type

#### Handling Errors with try Statements
- **Span:** PDF pp. 295–295 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** statement, block, enter, print, except, exception, associated, words, using, errors, error, reply
- **Key terms/APIs that appear:** try, all, print, except, i.e, input, int

#### Supporting Floating-Point Numbers
- **Span:** PDF pp. 296–296 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** enter, print, reply, statement, error, break, floating, point, numbers, input, statements, indented
- **Key terms/APIs that appear:** try, print, input, except, float, any, re, int, all

#### Nesting Code Three Levels Deep
- **Span:** PDF pp. 297–297 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** statement, enter, print, input, reply, prior, string, nested, chapters, strings, float, int
- **Key terms/APIs that appear:** print, input, float, int, reply.isdigit, re, open, any, import, set, all

### Chapter Summary
- **Span:** PDF pp. 297–297 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** statement, enter, print, input, reply, prior, string, nested, chapters, strings, float, int
- **Key terms/APIs that appear:** print, input, float, int, reply.isdigit, re, open, any, import, set, all

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 298–298 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** statement, statements, single, lines, nested, block, compound, tests, script, knowledge, normally, common
- **Key terms/APIs that appear:** all, type, try, any, re

### Test Your Knowledge: Answers
- **Span:** PDF pp. 298–298 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** statement, statements, single, lines, nested, block, compound, tests, script, knowledge, normally, common
- **Key terms/APIs that appear:** all, type, try, any, re

## Chapter 11. Assignments, Expressions, and Prints
- **Span:** PDF pp. 299–328 (30 pages; deep dive)
- **Breakdown:**
  - Assignments
  - Expression Statements
  - Print Operations
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 6 immediate subheadings; 14 leaf subsections underneath

### Assignments
- **Span:** PDF pp. 299–317 (19 pages; deep dive)
- **Breakdown:**
  - Assignment Syntax Forms
  - Basic Assignments
  - Sequence Assignments
  - Extended-Unpacking Assignments
  - Multiple-Target Assignments
  - Augmented Assignments
  - Named Assignment Expressions
  - Variable Name Rules
- **Granularity:** 8 immediate subheadings; 8 leaf subsections underneath

#### Assignment Syntax Forms
- **Span:** PDF pp. 300–300 (1 page; very brief)
- **Focus:** syntax forms and call/usage rules
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** assignment, assignments, py, tuple, expression, forms, list, sequence, object, right, targets, assigned
- **Key terms/APIs that appear:** tuple, list, all, any, i.e, re, time

#### Basic Assignments
- **Span:** PDF pp. 301–301 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** assignment, target, object, expression, augmented, targets, value, allows, string, assigned, assigns, names
- **Key terms/APIs that appear:** any, i.e, object.attr, all, except

#### Sequence Assignments
- **Span:** PDF pp. 302–303 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., ValueError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** string, sequence, tuple, assignment, first, second, right, values, list, variables, items, target
- **Key terms/APIs that appear:** tuple, list, type, any, e.g, time, all, a.k, re, collections, range

#### Extended-Unpacking Assignments
- **Span:** PDF pp. 304–308 (5 pages; moderate detail)
- **Focus:** advanced variants and extensions
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., SyntaxError, ValueError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** sequence, assignment, starred, target, list, unpacking, assignments, extended, tuple, first, front, loops
- **Key terms/APIs that appear:** list, tuple, all, range, any, print, c.attr, type, l.pop, set

#### Multiple-Target Assignments
- **Span:** PDF pp. 309–309 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** object, multiple, unpack, assignment, starred, expressions, appear, target, assignments, three, variables, function
- **Key terms/APIs that appear:** all, any, set, try, collections, list, tuple, map, dict, except

#### Augmented Assignments
- **Span:** PDF pp. 310–311 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** augmented, place, object, assignment, list, assignments, objects, expression, concatenation, slower, append, instead
- **Key terms/APIs that appear:** list, b.append, all, type, e.g, i.e, l.append, l.extend, time, tuple, any, map

#### Named Assignment Expressions
- **Span:** PDF pp. 312–314 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., SyntaxError, TypeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** assignment, expression, statement, readline, list, value, parentheses, print, py, named, expressions, result
- **Key terms/APIs that appear:** file.readline, list, print, all, tuple, any, l.extend, e.g, len, str, type, try

#### Variable Name Rules
- **Span:** PDF pp. 315–317 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** names, reserved, words, variable, though, rules, underscores, instance, module, objects, variables, statement
- **Key terms/APIs that appear:** type, all, import, any, e.g, time, raise, try, except, list, and.py, code.py

### Expression Statements
- **Span:** PDF pp. 318–319 (2 pages; brief)
- **Breakdown:**
  - Expression Statements and In-Place Changes
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Expression Statements and In-Place Changes
- **Span:** PDF pp. 319–319 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** statements, expression, print, change, place, list, statement, return, none, append, though, expressions
- **Key terms/APIs that appear:** print, list, l.append, all, e.g, yield, await, any

### Print Operations
- **Span:** PDF pp. 320–325 (6 pages; moderate detail)
- **Breakdown:**
  - The print Function
  - Print Stream Redirection
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### The print Function
- **Span:** PDF pp. 320–322 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** print, output, string, stream, object, standard, objects, function, keyword, prints, strings, printed
- **Key terms/APIs that appear:** print, any, str, sys, sys.stdout, re, all, open, data.txt, type, int, e.g

#### Print Stream Redirection
- **Span:** PDF pp. 323–325 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** print, stdout, write, stream, output, object, hello, world, program, original, printed, printing
- **Key terms/APIs that appear:** print, sys, sys.stdout, log.txt, open, import, str, sys.stderr, all, log2.txt, sys.__stdout__, log.close

### Chapter Summary
- **Span:** PDF pp. 326–326 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** print, three, assignments, operations, statements, statement, multiple, knowledge, place, temp1, temp2, str
- **Key terms/APIs that appear:** print, open, str, l.sort, e.g, a.append, bytes, all

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 326–326 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** print, three, assignments, operations, statements, statement, multiple, knowledge, place, temp1, temp2, str
- **Key terms/APIs that appear:** print, open, str, l.sort, e.g, a.append, bytes, all

### Test Your Knowledge: Answers
- **Span:** PDF pp. 326–328 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** print, stdout, write, method, three, object, syntax, operation, place, list, printed, redirect
- **Key terms/APIs that appear:** print, sys, sys.stdout, list, open, input, e.g, script.py, str, all, sorted, any

## Chapter 12. if and match Selections
- **Span:** PDF pp. 329–348 (20 pages; deep dive)
- **Breakdown:**
  - if Statements
  - match Statements
  - Python Syntax Revisited
  - Truth Values Revisited
  - The if/else Ternary Expression
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 8 immediate subheadings; 13 leaf subsections underneath

### if Statements
- **Span:** PDF pp. 329–332 (4 pages; moderate detail)
- **Breakdown:**
  - General Format
  - Basic Examples
  - Multiple-Choice Selections
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### General Format
- **Span:** PDF pp. 329–329 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** statements, statement, tests, general, block, selection, first, match, selections, actions, logic, compound
- **Key terms/APIs that appear:** all

#### Basic Examples
- **Span:** PDF pp. 330–330 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** true, print, associated, block, optional, statement, parts, false, prompts, mobile, statements, omitted
- **Key terms/APIs that appear:** print, all, os, except, input, re

#### Multiple-Choice Selections
- **Span:** PDF pp. 331–332 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., KeyError)
- **Key concepts (from text):** choice, print, statement, dictionary, branch, windows, linux, multiple, default, macos, switch, action
- **Key terms/APIs that appear:** print, os, try, branch.get, dict, lambda, time, set, all, except

### match Statements
- **Span:** PDF pp. 333–336 (4 pages; moderate detail)
- **Breakdown:**
  - Basic match Usage
  - Advanced match Usage
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Basic match Usage
- **Span:** PDF pp. 333–334 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** match, print, statement, choice, multiple, state, statements, dictionary, basic, logic, first, assigned
- **Key terms/APIs that appear:** print, all, any, e.g, branch.get, colors.get, dict, set, try

#### Advanced match Usage
- **Span:** PDF pp. 335–336 (2 pages; brief)
- **Focus:** advanced variants and extensions
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** match, patterns, print, sequence, matches, logic, pattern, mapping, multiple, choice, literal, state
- **Key terms/APIs that appear:** print, dict, list, pat.name, try, any, all, tuple, e.g, matchdemo.py, self.name, re

### Python Syntax Revisited
- **Span:** PDF pp. 337–341 (5 pages; moderate detail)
- **Breakdown:**
  - Block Delimiters: Indentation Rules
  - Statement Delimiters: Lines and Continuations
  - Special Syntax Cases in Action
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Block Delimiters: Indentation Rules
- **Span:** PDF pp. 338–339 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** indentation, block, statements, indented, print, spaces, ignored, blocks, nested, syntax, start, level
- **Key terms/APIs that appear:** print, all, any, re, x.endswith, except

#### Statement Delimiters: Lines and Continuations
- **Span:** PDF pp. 340–340 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** lines, statement, spaces, multiple, statements, indentation, rules, block, error, though, parentheses, string
- **Key terms/APIs that appear:** re, open, any, type, list

#### Special Syntax Cases in Action
- **Span:** PDF pp. 341–341 (1 page; very brief)
- **Focus:** syntax forms and call/usage rules
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** lines, pairs, parentheses, statement, program, literals, backslashes, print, usually, string, special, syntax
- **Key terms/APIs that appear:** open, print, any, re, i.e, list, set

### Truth Values Revisited
- **Span:** PDF pp. 342–343 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** true, false, object, return, operand, returns, boolean, operators, result, right, truth, values
- **Key terms/APIs that appear:** all, any, print, e.g, i.e, try

### The if/else Ternary Expression
- **Span:** PDF pp. 344–344 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** expression, ternary, statement, effect, object, common, prior, boolean, statements, equivalent, formal, value
- **Key terms/APIs that appear:** all

### Chapter Summary
- **Span:** PDF pp. 345–345 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** expression, true, false, statement, bool, boolean, first, returns, ternary, truth, words, exactly
- **Key terms/APIs that appear:** bool, i.e, time, any, list, re, yield

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 345–345 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** expression, true, false, statement, bool, boolean, first, returns, ternary, truth, words, exactly
- **Key terms/APIs that appear:** bool, i.e, time, any, list, re, yield

### Test Your Knowledge: Answers
- **Span:** PDF pp. 346–348 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** true, statement, false, expression, boolean, object, returns, values, short, select, nonempty, multiple
- **Key terms/APIs that appear:** all, any, set, filter, list, bool, lambda, open, re

## Chapter 13. while and for Loops
- **Span:** PDF pp. 349–372 (24 pages; deep dive)
- **Breakdown:**
  - while Loops
  - break, continue, pass, and the Loop else
  - for Loops
  - Loop Coding Techniques
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 7 immediate subheadings; 19 leaf subsections underneath

### while Loops
- **Span:** PDF pp. 349–350 (2 pages; brief)
- **Breakdown:**
  - General Format
  - Examples
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### General Format
- **Span:** PDF pp. 349–349 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** statements, statement, loops, looping, iteration, general, control, false, language, additional, explore, tools
- **Key terms/APIs that appear:** all, any, re, range, zip, enumerate, list, map, filter

#### Examples
- **Span:** PDF pp. 350–350 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** print, true, break, loops, keeps, statements, value, first, character, string, statement, executing
- **Key terms/APIs that appear:** print, type, all, input, range

### break, continue, pass, and the Loop else
- **Span:** PDF pp. 351–355 (5 pages; moderate detail)
- **Breakdown:**
  - General Loop Format
  - pass
  - continue
  - break
  - Loop else
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### General Loop Format
- **Span:** PDF pp. 351–351 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** break, statements, statement, continue, simple, empty, nothing, loops, placeholder, works, action, nested
- **Key terms/APIs that appear:** time, i.e, re, all, type

#### pass
- **Span:** PDF pp. 351–351 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** break, statements, statement, continue, simple, empty, nothing, loops, placeholder, works, action, nested
- **Key terms/APIs that appear:** time, i.e, re, all, type

#### continue
- **Span:** PDF pp. 352–352 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** alternative, later, func1, ellipsis, statement, continue, nothing, appear, expression, none, numbers, empty
- **Key terms/APIs that appear:** any, type, print, try, time, all

#### break
- **Span:** PDF pp. 353–353 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** break, continue, print, nested, favorite, language, statement, what's, reached, alternative, learn, loops
- **Key terms/APIs that appear:** print, input, try, all, re

#### Loop else
- **Span:** PDF pp. 354–355 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** found, break, print, clause, search, prime, input, factor, favorite, language, following, whether
- **Key terms/APIs that appear:** print, input, e.g, try, all, list, set

### for Loops
- **Span:** PDF pp. 356–360 (5 pages; moderate detail)
- **Breakdown:**
  - General Format
  - Examples
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### General Format
- **Span:** PDF pp. 356–356 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** object, target, sequence, statement, items, statements, break, loops, assignment, assign, iterable, works
- **Key terms/APIs that appear:** all, any, list, print, i.e, set, type

#### Examples
- **Span:** PDF pp. 356–360 (5 pages; moderate detail)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** assignment, items, print, loops, target, list, sequence, tuple, object, sequences, nested, statement
- **Key terms/APIs that appear:** print, list, tuple, all, any, sum, time, i.e, d.items, set, type, re

### Loop Coding Techniques
- **Span:** PDF pp. 361–369 (9 pages; detailed)
- **Breakdown:**
  - Counter Loops: range
  - Sequence Scans: while, range, and for
  - Sequence Shufflers: range and len
  - Skipping Items: range and Slices
  - Changing Lists: range and Comprehensions
  - Parallel Traversals: zip
  - Offsets and Items: enumerate
- **Granularity:** 7 immediate subheadings; 7 leaf subsections underneath

#### Counter Loops: range
- **Span:** PDF pp. 362–362 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** range, list, loops, built, function, series, generates, integers, results, sequence, argument, tuples
- **Key terms/APIs that appear:** range, list, all, type, zip, enumerate, print

#### Sequence Scans: while, range, and for
- **Span:** PDF pp. 363–363 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** range, print, pythons, iteration, manual, offsets, list, sequence, though, results, automatically, iterate
- **Key terms/APIs that appear:** range, len, print, list, all, time

#### Sequence Shufflers: range and len
- **Span:** PDF pp. 364–364 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - includes performance/efficiency notes
- **Key concepts (from text):** range, sequence, print, though, different, sequences, useful, better, simple, iteration, loops, coding
- **Key terms/APIs that appear:** range, len, print, type, re, any, except, time, list

#### Skipping Items: range and Slices
- **Span:** PDF pp. 365–365 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** range, list, items, visit, integer, combination, technique, abcdefghijk, print, second, string, third
- **Key terms/APIs that appear:** range, list, len, print, re, try, time

#### Changing Lists: range and Comprehensions
- **Span:** PDF pp. 365–365 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** range, list, items, visit, integer, combination, technique, abcdefghijk, print, second, string, third
- **Key terms/APIs that appear:** range, list, len, print, re, try, time

#### Parallel Traversals: zip
- **Span:** PDF pp. 366–368 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** list, script, program, range, parallel, tuples, items, result, arguments, lists, dictionary, dict
- **Key terms/APIs that appear:** zip, list, range, dict, len, any, time, tuple, type, all, print, a.k

#### Offsets and Items: enumerate
- **Span:** PDF pp. 369–369 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** offset, appears, enumerate, function, iteration, offsets, items, print, range, counter, built, object
- **Key terms/APIs that appear:** enumerate, print, range, zip, tuple, data.txt, line.rstrip, time, all, list, open

### Chapter Summary
- **Span:** PDF pp. 370–370 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** loops, break, range, statement, continue, iteration, statements, knowledge, counter, exits, concepts, enumerate
- **Key terms/APIs that appear:** range, enumerate, list, zip, i.e, all

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 370–370 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** loops, break, range, statement, continue, iteration, statements, knowledge, counter, exits, concepts, enumerate
- **Key terms/APIs that appear:** range, enumerate, list, zip, i.e, all

### Test Your Knowledge: Answers
- **Span:** PDF pp. 370–372 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** loops, print, range, list, though, break, statement, items, files, lines, rstrip, iteration
- **Key terms/APIs that appear:** data.txt, open, print, range, all, line.rstrip, list, file.read, os.popen, enumerate, zip, reversed

## Chapter 14. Iterations and Comprehensions
- **Span:** PDF pp. 373–394 (22 pages; deep dive)
- **Breakdown:**
  - Iterations
  - Comprehensions
  - Iteration Tools
  - Other Iteration Topics
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 7 immediate subheadings; 11 leaf subsections underneath

### Iterations
- **Span:** PDF pp. 374–384 (11 pages; detailed)
- **Breakdown:**
  - The Iteration Protocol
  - Other Built-in Iterables
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### The Iteration Protocol
- **Span:** PDF pp. 375–379 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** iteration, object, iterator, protocol, files, testing, method, stopiteration, built, objects, readline, calling
- **Key terms/APIs that appear:** open, data.txt, print, all, f.__next__, time, f.readline, any, line.upper, i.__next__, try, l.__iter__

#### Other Built-in Iterables
- **Span:** PDF pp. 380–384 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** list, range, results, enumerate, iteration, iterables, iterable, built, filter, tools, multiple, objects
- **Key terms/APIs that appear:** list, range, enumerate, zip, map, filter, all, print, lambda, time, bool, open

### Comprehensions
- **Span:** PDF pp. 385–388 (4 pages; moderate detail)
- **Breakdown:**
  - List Comprehension Basics
  - List Comprehensions and Files
  - Extended List Comprehension Syntax
  - Comprehensions Cliff-Hanger
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### List Comprehension Basics
- **Span:** PDF pp. 385–385 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** list, set, iteration, protocol, comprehensions, comprehension, expression, results, tools, iterable, ultimately, works
- **Key terms/APIs that appear:** list, set, os, range, os.popen, a.k, os.walk, yield, all, len

#### List Comprehensions and Files
- **Span:** PDF pp. 386–386 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** list, lines, comprehensions, expression, result, rstrip, iteration, inside, results, comprehension, earlier, method
- **Key terms/APIs that appear:** list, all, open, time, res.append, data.txt, f.readlines, line.rstrip, re

#### Extended List Comprehension Syntax
- **Span:** PDF pp. 387–388 (2 pages; brief)
- **Focus:** syntax forms and call/usage rules; advanced variants and extensions
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** lines, list, rstrip, expression, comprehensions, testing, comprehension, statement, string, close, filter, equivalent
- **Key terms/APIs that appear:** open, list, data.txt, line.rstrip, filter, all, line.split, re, any, len, line.upper, line.replace

#### Comprehensions Cliff-Hanger
- **Span:** PDF pp. 389–389 (1 page; very brief)
- **Focus:** preview of later material
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** list, comprehensions, tools, comprehension, iteration, prior, instead, though, probably, understand, programming, better
- **Key terms/APIs that appear:** list, all, set, any, res.append, filter, time, open, type

### Iteration Tools
- **Span:** PDF pp. 389–392 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** list, testing, iterable, iteration, built, comprehensions, protocol, tools, comprehension, items, function, true
- **Key terms/APIs that appear:** open, data.txt, list, all, any, map, set, enumerate, sorted, filter, zip, line.upper

### Other Iteration Topics
- **Span:** PDF pp. 393–393 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** iteration, list, iterable, tools, functions, defined, iterables, probably, comprehensions, classes, objects, syntax
- **Key terms/APIs that appear:** zip, list, any, data.txt, print, open, yield, all, set

### Chapter Summary
- **Span:** PDF pp. 393–393 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** iteration, list, iterable, tools, functions, defined, iterables, probably, comprehensions, classes, objects, syntax
- **Key terms/APIs that appear:** zip, list, any, data.txt, print, open, yield, all, set

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 394–394 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** iteration, list, iterable, comprehensions, tools, object, built, objects, protocol, iterator, expression, knowledge
- **Key terms/APIs that appear:** list, all, any, time, map, sorted, sum, tuple, open

### Test Your Knowledge: Answers
- **Span:** PDF pp. 394–394 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** iteration, list, iterable, comprehensions, tools, object, built, objects, protocol, iterator, expression, knowledge
- **Key terms/APIs that appear:** list, all, any, time, map, sorted, sum, tuple, open

## Chapter 15. The Documentation Interlude
- **Span:** PDF pp. 395–414 (20 pages; deep dive)
- **Breakdown:**
  - Python Documentation Sources
  - Common Coding Gotchas
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
  - Test Your Knowledge: Part III Exercises
- **Granularity:** 6 immediate subheadings; 13 leaf subsections underneath

### Python Documentation Sources
- **Span:** PDF pp. 395–409 (15 pages; detailed)
- **Breakdown:**
  - # Comments
  - The dir Function
  - Docstrings and __doc__
  - Pydoc: The help Function
  - Pydoc: HTML Reports
  - Beyond Docstrings: Sphinx
  - The Standard Manuals
  - Web Resources
- **Granularity:** 8 immediate subheadings; 8 leaf subsections underneath

#### # Comments
- **Span:** PDF pp. 396–396 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** documentation, comments, function, objects, attributes, available, docstrings, list, names, pydoc, module, larger
- **Key terms/APIs that appear:** dir, sys, list, all, e.g, any, import, len, i.e, x.startswith, type

#### The dir Function
- **Span:** PDF pp. 396–397 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** attributes, list, documentation, names, function, objects, comments, startswith, available, docstrings, built, object
- **Key terms/APIs that appear:** dir, list, type, sys, len, all, x.startswith, any, str, e.g, a.startswith, import

#### Docstrings and __doc__
- **Span:** PDF pp. 398–400 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** docstrings, documentation, class, module, function, square, print, strings, import, comments, objects, string
- **Key terms/APIs that appear:** print, import, any, re, docstrings.py, sys, except, square.__doc__, partvi.__doc__, docstrings.__doc__, docstrings.square, docstrings.partvi

#### Pydoc: The help Function
- **Span:** PDF pp. 401–403 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** docstrings, function, module, built, object, omitted, class, pydoc, documentation, tools, string, dict
- **Key terms/APIs that appear:** sys, type, dict, e.g, import, str, all, builtins.object, map, sys.getrefcount, map.__doc__, docs.python

#### Pydoc: HTML Reports
- **Span:** PDF pp. 404–407 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** pydoc, module, browser, documentation, server, script, command, py, search, level, index, import
- **Key terms/APIs that appear:** import, all, any, time, e.g, _pydoc.css, open, input, docstrings.py, pydoc.__file__, pydoc.py, __init__.py

#### Beyond Docstrings: Sphinx
- **Span:** PDF pp. 408–408 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** manuals, standard, language, reference, sphinx, documentation, projects, tools, probably, details, documents, docstrings
- **Key terms/APIs that appear:** re, yield, random, set

#### The Standard Manuals
- **Span:** PDF pp. 408–408 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** manuals, standard, language, reference, sphinx, documentation, projects, tools, probably, details, documents, docstrings
- **Key terms/APIs that appear:** re, yield, random, set

#### Web Resources
- **Span:** PDF pp. 409–409 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** resources, standard, manuals, today, available, elsewhere, finally, besides, website, hosts, additional, cover
- **Key terms/APIs that appear:** re

### Common Coding Gotchas
- **Span:** PDF pp. 410–410 (1 page; very brief)
- **Focus:** common pitfalls and edge cases
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** statement, avoid, prompt, statements, interactive, blank, lines, coding, unnested, nested, spaces, block
- **Key terms/APIs that appear:** re, all, e.g, type, any, range, list, a.k, list.append, list.sort, mylist.append, time

### Chapter Summary
- **Span:** PDF pp. 411–411 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** function, documentation, list, close, import, reference, parentheses, extensions, modules, takes, learn, functions
- **Key terms/APIs that appear:** list, import, e.g, file.close, any, type, set, mod.py, all

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 411–411 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** function, documentation, list, close, import, reference, parentheses, extensions, modules, takes, learn, functions
- **Key terms/APIs that appear:** list, import, e.g, file.close, any, type, set, mod.py, all

### Test Your Knowledge: Answers
- **Span:** PDF pp. 412–412 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** documentation, pydoc, ascii, statements, character, docstrings, modules, points, browser, function, list, exercises
- **Key terms/APIs that appear:** all, list, dir, a.startswith, any, filter, import, range, sum, map

### Test Your Knowledge: Part III Exercises
- **Span:** PDF pp. 412–414 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** list, index, documentation, found, pydoc, ascii, statements, function, coding, characters, write, exercises
- **Key terms/APIs that appear:** list, all, range, print, map, type, power.py, dir, sorted, lambda, a.startswith, l.index

# Part IV. Functions and Generators
- **Span:** PDF pp. 415–594 (180 pages; extended treatment)
- **Breakdown:**
  - Chapter 16. Function Basics
  - Chapter 17. Scopes
  - Chapter 18. Arguments
  - Chapter 19. Function Odds and Ends
  - Chapter 20. Comprehensions and Generations
  - Chapter 21. The Benchmarking Interlude
- **Granularity:** 6 immediate subheadings; 111 leaf subsections underneath

## Chapter 16. Function Basics
- **Span:** PDF pp. 417–430 (14 pages; detailed)
- **Breakdown:**
  - Why Use Functions?
  - Function Coding Overview
  - A First Example: Definitions and Calls
  - A Second Example: Intersecting Sequences
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 7 immediate subheadings; 18 leaf subsections underneath

### Why Use Functions?
- **Span:** PDF pp. 418–418 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** functions, lambda, tools, pizza, function, global, changer, nonlocal, yield, range, async, await
- **Key terms/APIs that appear:** lambda, yield, range, async, await, all, time, re

### Function Coding Overview
- **Span:** PDF pp. 419–422 (4 pages; moderate detail)
- **Breakdown:**
  - Basic Function Tools
  - Advanced Function Tools
  - General Function Concepts
  - def Statements
  - return Statements
  - def Executes at Runtime
  - lambda Makes Anonymous Functions
- **Granularity:** 7 immediate subheadings; 7 leaf subsections underneath

#### Basic Function Tools
- **Span:** PDF pp. 419–419 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, functions, object, caller, lambda, return, statements, statement, result, called, built, tools
- **Key terms/APIs that appear:** lambda, open, len, zip, range, map, all, list

#### Advanced Function Tools
- **Span:** PDF pp. 420–420 (1 page; very brief)
- **Focus:** advanced variants and extensions
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, functions, arguments, names, object, global, variables, enclosing, statement, caller, passed, objects
- **Key terms/APIs that appear:** any, all, yield, time, type, list, await, async

#### General Function Concepts
- **Span:** PDF pp. 420–420 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, functions, arguments, names, object, global, variables, enclosing, statement, caller, passed, objects
- **Key terms/APIs that appear:** any, all, yield, time, type, list, await, async

#### def Statements
- **Span:** PDF pp. 421–421 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** function, return, statement, object, statements, expression, header, result, arguments, later, assigned, value
- **Key terms/APIs that appear:** type, all, time, list

#### return Statements
- **Span:** PDF pp. 421–421 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** function, return, statement, object, statements, expression, header, result, arguments, later, assigned, value
- **Key terms/APIs that appear:** type, all, time, list

#### def Executes at Runtime
- **Span:** PDF pp. 422–422 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, functions, object, statement, runtime, objects, statements, lambda, execution, assigns, legal, inside
- **Key terms/APIs that appear:** time, lambda, func.attr, yield, await, async, all

#### lambda Makes Anonymous Functions
- **Span:** PDF pp. 422–422 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, functions, object, statement, runtime, objects, statements, lambda, execution, assigns, legal, inside
- **Key terms/APIs that appear:** time, lambda, func.attr, yield, await, async, all

### A First Example: Definitions and Calls
- **Span:** PDF pp. 423–424 (2 pages; brief)
- **Breakdown:**
  - Definition
  - Calls
  - Polymorphism in Python
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Definition
- **Span:** PDF pp. 423–423 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** lambda, function, expression, object, called, first, calls, times, return, assign, result, definition
- **Key terms/APIs that appear:** lambda, re, list, any, all, time, try

#### Calls
- **Span:** PDF pp. 424–424 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, times, objects, object, arguments, passed, expression, parentheses, assigned, means, numbers, depends
- **Key terms/APIs that appear:** i.e, lambda, time, a.k, type

#### Polymorphism in Python
- **Span:** PDF pp. 424–424 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, times, objects, object, arguments, passed, expression, parentheses, assigned, means, numbers, depends
- **Key terms/APIs that appear:** i.e, lambda, time, a.k, type

### A Second Example: Intersecting Sequences
- **Span:** PDF pp. 425–427 (3 pages; brief)
- **Breakdown:**
  - Definition
  - Calls
  - Polymorphism Revisited
  - Segue: Local Variables
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Definition
- **Span:** PDF pp. 425–425 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** function, objects, types, support, expected, times, coded, detect, second, sequences, passed, expression
- **Key terms/APIs that appear:** any, type, raise, int, str, time, except, set

#### Calls
- **Span:** PDF pp. 426–426 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, intersect, result, intersection, works, module, simple, objects, logic, change, coding, means
- **Key terms/APIs that appear:** any, import, list, inter1.py, res.append, all, set, lambda

#### Polymorphism Revisited
- **Span:** PDF pp. 427–427 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** intersect, objects, types, function, support, files, object, operator, though, iteration, argument, local
- **Key terms/APIs that appear:** all, any, type, e.g, open, lambda, time, file.readlines, file.seek, input, range, list

#### Segue: Local Variables
- **Span:** PDF pp. 427–427 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** intersect, objects, types, function, support, files, object, operator, though, iteration, argument, local
- **Key terms/APIs that appear:** all, any, type, e.g, open, lambda, time, file.readlines, file.seek, input, range, list

### Chapter Summary
- **Span:** PDF pp. 428–428 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, functions, return, object, local, lambda, variable, passed, variables, though, assignment, called
- **Key terms/APIs that appear:** lambda, all, time, re

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 428–428 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, functions, return, object, local, lambda, variable, passed, variables, though, assignment, called
- **Key terms/APIs that appear:** lambda, all, time, re

### Test Your Knowledge: Answers
- **Span:** PDF pp. 428–430 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, functions, object, return, lambda, statement, expression, local, passed, variables, called, though
- **Key terms/APIs that appear:** lambda, time, any, all, re, import, set

## Chapter 17. Scopes
- **Span:** PDF pp. 431–460 (30 pages; deep dive)
- **Breakdown:**
  - Python Scopes Basics
  - The global Statement
  - Nested Functions and Scopes
  - The nonlocal Statement
  - State-Retention Options
  - Scopes and Argument Defaults
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 9 immediate subheadings; 23 leaf subsections underneath

### Python Scopes Basics
- **Span:** PDF pp. 431–438 (8 pages; detailed)
- **Breakdown:**
  - Scopes Overview
  - Name Resolution: The LEGB Rule
  - Scopes Examples
  - The Built-in Scope
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Scopes Overview
- **Span:** PDF pp. 432–433 (2 pages; brief)
- **Focus:** introduces core ideas and syntax
- **Key concepts (from text):** function, names, global, module, scope, assigned, local, scopes, inside, variable, variables, enclosing
- **Key terms/APIs that appear:** lambda, all, any, import, time, list, i.e, l.append, open, zip, type

#### Name Resolution: The LEGB Rule
- **Span:** PDF pp. 434–435 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception)
- **Key concepts (from text):** names, scopes, scope, local, enclosing, statement, variables, lookup, global, statements, function, functions
- **Key terms/APIs that appear:** all, e.g, any, except, try, lambda, set, i.e, object.name, map, list

#### Scopes Examples
- **Span:** PDF pp. 436–436 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** names, class, scope, local, assigned, lambda, function, level, object, module, scopes101, global
- **Key terms/APIs that appear:** lambda, scopes101.py, all, import, scopes101.func, any

#### The Built-in Scope
- **Span:** PDF pp. 437–438 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., ArithmeticError, AssertionError, AttributeError, BlockingIOError, BrokenPipeError)
- **Key concepts (from text):** built, function, names, scope, builtins, module, global, local, variable, variables, instance, called
- **Key terms/APIs that appear:** open, zip, import, dir, list, all, builtins.zip, any, type, len, data.txt, x.startswith

### The global Statement
- **Span:** PDF pp. 439–443 (5 pages; moderate detail)
- **Breakdown:**
  - Program Design: Minimize Global Variables
  - Program Design: Minimize Cross-File Changes
  - Other Ways to Access Globals
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Program Design: Minimize Global Variables
- **Span:** PDF pp. 440–441 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** global, functions, module, function, names, globals, variables, scope, outside, assigned, later, statement
- **Key terms/APIs that appear:** all, time, try, e.g, lambda, print, map, raise, property, async

#### Program Design: Minimize Cross-File Changes
- **Span:** PDF pp. 442–442 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** module, first, second, variable, global, variables, py, import, changes, files, cross, change
- **Key terms/APIs that appear:** import, second.py, first.x, all, first.py, print, first.setx, re

#### Other Ways to Access Globals
- **Span:** PDF pp. 443–443 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** global, change, thismod, module, local, import, first, modules, person, function, attributes, loaded
- **Key terms/APIs that appear:** import, thismod.var, sys, sys.modules, print, thismod.py, thismod.test, all

### Nested Functions and Scopes
- **Span:** PDF pp. 444–446 (3 pages; brief)
- **Breakdown:**
  - Nested Scopes Overview
  - Nested Scopes Examples
  - Closures and Factory Functions
  - Arbitrary Scope Nesting
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Nested Scopes Overview
- **Span:** PDF pp. 444–444 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **Key concepts (from text):** scope, function, enclosing, scopes, global, nested, module, nonlocal, local, functions, first, names
- **Key terms/APIs that appear:** all, any, e.g, re, time, list, type

#### Nested Scopes Examples
- **Span:** PDF pp. 444–444 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **Key concepts (from text):** scope, function, enclosing, scopes, global, nested, module, nonlocal, local, functions, first, names
- **Key terms/APIs that appear:** all, any, e.g, re, time, list, type

#### Closures and Factory Functions
- **Span:** PDF pp. 445–446 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, action, enclosing, nested, functions, maker, scope, remembers, state, return, local, returns
- **Key terms/APIs that appear:** any, a.k, print, all, lambda, i.e, re, time, set, tuple

#### Arbitrary Scope Nesting
- **Span:** PDF pp. 447–447 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** scope, enclosing, nonlocal, functions, nested, function, global, lambda, state, py, closures, names
- **Key terms/APIs that appear:** lambda, all, open, print, except, min

### The nonlocal Statement
- **Span:** PDF pp. 447–449 (3 pages; brief)
- **Breakdown:**
  - nonlocal Basics
  - nonlocal in Action
  - nonlocal Boundary Cases
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### nonlocal Basics
- **Span:** PDF pp. 448–448 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** scope, nonlocal, names, enclosing, state, scopes, global, lookup, inner, function, statement, outer
- **Key terms/APIs that appear:** lambda, list, print

#### nonlocal in Action
- **Span:** PDF pp. 448–448 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** scope, nonlocal, names, enclosing, state, scopes, global, lookup, inner, function, statement, outer
- **Key terms/APIs that appear:** lambda, list, print

#### nonlocal Boundary Cases
- **Span:** PDF pp. 449–449 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., UnboundLocalError)
- **Key concepts (from text):** state, function, outer, inner, enclosing, nonlocal, label, scope, nonlocals, nested, print, return
- **Key terms/APIs that appear:** print, time

### State-Retention Options
- **Span:** PDF pp. 450–453 (4 pages; moderate detail)
- **Breakdown:**
  - Nonlocals: Changeable, Per-Call, LEGB
  - Globals: Changeable but Shared
  - Function Attributes: Changeable, Per-Call, Explicit
  - Classes: Changeable, Per-Call, OOP
  - And the Winner Is…
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Nonlocals: Changeable, Per-Call, LEGB
- **Span:** PDF pp. 451–451 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError)
- **Key concepts (from text):** state, nonlocal, enclosing, scope, global, outer, start, inner, label, function, changeable, saved
- **Key terms/APIs that appear:** print, f.state, any

#### Globals: Changeable but Shared
- **Span:** PDF pp. 451–451 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError)
- **Key concepts (from text):** state, nonlocal, enclosing, scope, global, outer, start, inner, label, function, changeable, saved
- **Key terms/APIs that appear:** print, f.state, any

#### Function Attributes: Changeable, Per-Call, Explicit
- **Span:** PDF pp. 452–453 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** state, function, inner, attributes, scope, nonlocal, outer, nested, object, functions, global, names
- **Key terms/APIs that appear:** inner.state, f.state, print, re, g.state, l.append, list

#### Classes: Changeable, Per-Call, OOP
- **Span:** PDF pp. 454–454 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** state, classes, attributes, functions, changeable, function, instance, class, scopes, information, support, retention
- **Key terms/APIs that appear:** all, time, lp6e.year, lp6e.python, lp5e.year, lp5e.python, e.g, any

#### And the Winner Is…
- **Span:** PDF pp. 454–454 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** state, classes, attributes, functions, changeable, function, instance, class, scopes, information, support, retention
- **Key terms/APIs that appear:** all, time, lp6e.year, lp6e.python, lp5e.year, lp5e.python, e.g, any

### Scopes and Argument Defaults
- **Span:** PDF pp. 454–456 (3 pages; brief)
- **Breakdown:**
  - Loops Require Defaults, Not Scopes
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Loops Require Defaults, Not Scopes
- **Span:** PDF pp. 456–456 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** functions, scope, nested, enclosing, lambda, value, variable, function, defaults, list, remember, scopes
- **Key terms/APIs that appear:** all, lambda, list, range, acts.append, except, try

### Chapter Summary
- **Span:** PDF pp. 457–457 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** function, defaults, scope, state, enclosing, scopes, retain, variable, default, makeactions, range, lambda
- **Key terms/APIs that appear:** range, lambda, acts.append, e.g, any, time, re

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 458–458 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** print, output, py, function, passed, nested, attributes, finally, looked, general, design, ideas
- **Key terms/APIs that appear:** print, re

### Test Your Knowledge: Answers
- **Span:** PDF pp. 459–460 (2 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, scope, nested, global, custom, variable, state, enclosing, original, makeopen, py, print
- **Key terms/APIs that appear:** open, print, data.txt, f.read, import, builtins.open, makeopen.py, time, any

## Chapter 18. Arguments
- **Span:** PDF pp. 461–492 (32 pages; extended treatment)
- **Breakdown:**
  - Argument-Passing Basics
  - Special Argument-Matching Modes
  - Argument Ordering: The Gritty Details
  - Example: The min Wakeup Call
  - Example: Generalized Set Functions
  - Example: Rolling Your Own Print
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 9 immediate subheadings; 20 leaf subsections underneath

### Argument-Passing Basics
- **Span:** PDF pp. 461–465 (5 pages; moderate detail)
- **Breakdown:**
  - Arguments and Shared References
  - Avoiding Mutable Argument Changes
  - Simulating Output Parameters and Multiple Results
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Arguments and Shared References
- **Span:** PDF pp. 462–463 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, object, argument, objects, assignment, mutable, caller, arguments, passed, references, change, place
- **Key terms/APIs that appear:** input, list, e.g

#### Avoiding Mutable Argument Changes
- **Span:** PDF pp. 464–464 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** arguments, object, place, mutable, objects, function, change, list, argument, changes, impact, passed
- **Key terms/APIs that appear:** list, input, list.copy, b.copy

#### Simulating Output Parameters and Multiple Results
- **Span:** PDF pp. 465–465 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** tuple, function, change, multiple, changes, objects, tuples, return, object, passed, argument, results
- **Key terms/APIs that appear:** tuple, any, list, type, e.g, a.k, raise, all, property

### Special Argument-Matching Modes
- **Span:** PDF pp. 466–477 (12 pages; detailed)
- **Breakdown:**
  - Argument Matching Overview
  - Argument Matching Syntax
  - Argument Passing Details
  - Keyword and Default Examples
  - Arbitrary Arguments Examples
  - Keyword-Only Arguments
  - Positional-Only Arguments
- **Granularity:** 7 immediate subheadings; 7 leaf subsections underneath

#### Argument Matching Overview
- **Span:** PDF pp. 466–466 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** arguments, argument, definition, function, matching, passed, specify, values, names, arbitrarily, tools, matched
- **Key terms/APIs that appear:** all, lambda, re, list, collections

#### Argument Matching Syntax
- **Span:** PDF pp. 467–467 (1 page; very brief)
- **Focus:** syntax forms and call/usage rules
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** arguments, function, keyword, argument, passed, value, position, positional, calls, matching, caller, matched
- **Key terms/APIs that appear:** any, all, dict, tuple, list, print

#### Argument Passing Details
- **Span:** PDF pp. 468–468 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** arguments, function, keyword, defaults, argument, optional, matching, modes, definition, unpackings, positional, default
- **Key terms/APIs that appear:** any, all, dict, re, tuple

#### Keyword and Default Examples
- **Span:** PDF pp. 469–470 (2 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** defaults, function, argument, arguments, keywords, default, values, keyword, position, definition, value, first
- **Key terms/APIs that appear:** all, print, type, any, time

#### Arbitrary Arguments Examples
- **Span:** PDF pp. 471–474 (4 pages; moderate detail)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., SyntaxError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** arguments, function, argument, syntax, dict, unpacking, keyword, tuple, functions, definition, print, dictionary
- **Key terms/APIs that appear:** dict, any, tuple, print, all, list, tracer0.py, time, e.g, lambda, range, open

#### Keyword-Only Arguments
- **Span:** PDF pp. 475–476 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., SyntaxError, TypeError)
- **Key concepts (from text):** kwonly, keyword, arguments, argument, passed, typeerror, function, positional, optional, required, appear, print
- **Key terms/APIs that appear:** print, list, any, all, i.e, set

#### Positional-Only Arguments
- **Span:** PDF pp. 477–477 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** arguments, keyword, mostlypos, passed, positional, argument, print, function, typeerror, list, allpos, lambda
- **Key terms/APIs that appear:** print, list, lambda, i.e, re, all

### Argument Ordering: The Gritty Details
- **Span:** PDF pp. 478–480 (3 pages; brief)
- **Breakdown:**
  - Definition Ordering
  - Calls Ordering
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Definition Ordering
- **Span:** PDF pp. 478–479 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., SyntaxError, TypeError)
- **Key concepts (from text):** arguments, keyword, positional, argument, ordering, default, function, combo, follows, collector, parameter, passed
- **Key terms/APIs that appear:** all, any, list, lambda, e.g, print, type

#### Calls Ordering
- **Span:** PDF pp. 480–480 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., SyntaxError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** arguments, positional, keyword, unpackings, calls, expression, function, iterable, argument, ordering, similar, combination
- **Key terms/APIs that appear:** all, any, map, re, type, print, dict, try

### Example: The min Wakeup Call
- **Span:** PDF pp. 481–483 (3 pages; brief)
- **Breakdown:**
  - Full Credit
  - Bonus Points
  - The Punch Line
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Full Credit
- **Span:** PDF pp. 481–482 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., SyntaxError)
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** first, argument, arguments, function, list, print, keyword, value, objects, lists, tuple, sorted
- **Key terms/APIs that appear:** list, time, print, all, tuple, sorted, mins.py, min, set, type, list.sort, timings.txt

#### Bonus Points
- **Span:** PDF pp. 483–483 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** function, arguments, return, value, minmax, exception, error, functions, errors, maximum, minimum, py
- **Key terms/APIs that appear:** raise, try, print, mins.py, e.g, minmax.py, import, type, all, list, any, max

#### The Punch Line
- **Span:** PDF pp. 484–484 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** functions, arguments, function, items, union, minmax, py, passed, change, single, coding, really
- **Key terms/APIs that appear:** all, max, any, minmax.py, inter2.py, res.append, min, re, set, tuple

### Example: Generalized Set Functions
- **Span:** PDF pp. 484–485 (2 pages; brief)
- **Breakdown:**
  - Testing the Code
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Testing the Code
- **Span:** PDF pp. 485–485 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** items, intersect, trace, union, hackk, tester, functions, module, arguments, tools, inter2, imports
- **Key terms/APIs that appear:** print, res.append, inter2.py, re, any, import, range, len, sorted, set

### Example: Rolling Your Own Print
- **Span:** PDF pp. 486–488 (3 pages; brief)
- **Breakdown:**
  - Using Keyword-Only Arguments
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Using Keyword-Only Arguments
- **Span:** PDF pp. 487–488 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** print3, arguments, py, keyword, import, keywords, kargs, output, first, print, extra, version
- **Key terms/APIs that appear:** import, sys, print, kargs.pop, raise, print3.py, log.txt, sys.stdout, file.write, open, all, any

### Chapter Summary
- **Span:** PDF pp. 489–489 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** print, arguments, function, tools, keyword, studied, functions, objects, argument, output, built, version
- **Key terms/APIs that appear:** print, open, builtins.print, e.g, lambda, map, filter, try

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 489–489 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** print, arguments, function, tools, keyword, studied, functions, objects, argument, output, built, version
- **Key terms/APIs that appear:** print, open, builtins.print, e.g, lambda, map, filter, try

### Test Your Knowledge: Answers
- **Span:** PDF pp. 490–492 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** arguments, keyword, passed, defaults, options, output, position, positional, knowledge, order, dictionary, function
- **Key terms/APIs that appear:** time, sorted, e.g, print, tuple, any, str.format, re, set, import, list, all

## Chapter 19. Function Odds and Ends
- **Span:** PDF pp. 493–520 (28 pages; deep dive)
- **Breakdown:**
  - Function Design Concepts
  - Recursive Functions
  - Function Tools: Attributes, Annotations, Etc.
  - Anonymous Functions: lambda
  - Functional Programming Tools
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 8 immediate subheadings; 19 leaf subsections underneath

### Function Design Concepts
- **Span:** PDF pp. 493–494 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** function, functions, coupling, variables, design, global, arguments, change, related, functional, tools, module
- **Key terms/APIs that appear:** e.g, lambda, re, any, i.e, self.edition, map, filter, all, list, open, time

### Recursive Functions
- **Span:** PDF pp. 495–501 (7 pages; moderate detail)
- **Breakdown:**
  - Summation with Recursion
  - Coding Alternatives
  - Loop Statements Versus Recursion
  - Handling Arbitrary Structures
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Summation with Recursion
- **Span:** PDF pp. 495–495 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** functions, function, recursion, mysum, list, recursive, level, import, calls, though, understand, scope
- **Key terms/APIs that appear:** list, sum, import, re, mysum.py, all, any, open, try, print

#### Coding Alternatives
- **Span:** PDF pp. 496–496 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** mysum, return, recursive, first, unpacking, three, strings, level, alternatives, ternary, expression, assume
- **Key terms/APIs that appear:** any, type, e.g, all, mysum_alts.py, print, list, sum, input, len

#### Loop Statements Versus Recursion
- **Span:** PDF pp. 497–497 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** mysum, recursion, function, calls, though, recursive, return, first, third, variant, works, input
- **Key terms/APIs that appear:** open, input, sum, all, time

#### Handling Arbitrary Structures
- **Span:** PDF pp. 498–501 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., RecursionError)
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** sumtree, recursive, tester, front, list, trace, items, import, stack, summer, first, visited
- **Key terms/APIs that appear:** list, import, print, all, isinstance, sum, re, items.pop, items.extend, visited.add, sumtree.py, sumtree_tester.py

### Function Tools: Attributes, Annotations, Etc.
- **Span:** PDF pp. 502–507 (6 pages; moderate detail)
- **Breakdown:**
  - The First-Class Object Model
  - Function Introspection
  - Function Attributes
  - Function Annotations and Decorations
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### The First-Class Object Model
- **Span:** PDF pp. 503–503 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, object, functions, exclaim, objects, passed, arguments, model, special, generic, adding, argument
- **Key terms/APIs that appear:** any, list, print, time

#### Function Introspection
- **Span:** PDF pp. 504–504 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, functions, object, class, introspection, objects, tools, implore, exclaim, return, flexible, instance
- **Key terms/APIs that appear:** func.__code__, dir, func.__name__, print, type, set

#### Function Attributes
- **Span:** PDF pp. 505–505 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, attributes, count, handles, names, objects, functions, defined, attach, arbitrary, button, press
- **Key terms/APIs that appear:** dir, func.count, func.handles, f.book, all, len, lambda, x.startswith, re

#### Function Annotations and Decorations
- **Span:** PDF pp. 506–507 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, annotations, return, arguments, following, float, int, class, object, argument, decorator, tools
- **Key terms/APIs that appear:** func.__annotations__, float, int, all, any, type, list, print, re

### Anonymous Functions: lambda
- **Span:** PDF pp. 508–512 (5 pages; moderate detail)
- **Breakdown:**
  - lambda Basics
  - Why Use lambda?
  - How (Not) to Obfuscate Your Python Code
  - Scopes: lambdas Can Be Nested Too
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### lambda Basics
- **Span:** PDF pp. 509–509 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** lambda, expression, arguments, functions, function, assigned, statement, scope, general, followed, parentheses, allowed
- **Key terms/APIs that appear:** lambda, re, list, type

#### Why Use lambda?
- **Span:** PDF pp. 510–510 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** lambda, function, return, list, title, expression, inline, functions, print, prints, editions, labeler
- **Key terms/APIs that appear:** lambda, list, print

#### How (Not) to Obfuscate Your Python Code
- **Span:** PDF pp. 511–512 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., NameError)
- **Key concepts (from text):** lambda, function, print, functions, lower, expressions, statements, showall, dictionary, logic, expression, upper
- **Key terms/APIs that appear:** lambda, print, map, list, s.upper, s.lower, e.g, sys.stdout, a.upper, b.lower, type, re

#### Scopes: lambdas Can Be Nested Too
- **Span:** PDF pp. 513–513 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** lambda, function, nested, action, enclosing, scope, programming, better, scopes, lambdas, access, functional
- **Key terms/APIs that appear:** lambda, a.k, yield, any

### Functional Programming Tools
- **Span:** PDF pp. 513–516 (4 pages; moderate detail)
- **Breakdown:**
  - Mapping Functions over Iterables: map
  - Selecting Items in Iterables: filter
  - Combining Items in Iterables: reduce
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Mapping Functions over Iterables: map
- **Span:** PDF pp. 514–514 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, list, counters, functions, iterable, results, built, apply, items, updated, return, lambda
- **Key terms/APIs that appear:** map, list, all, lambda, updated.append, res.append, filter

#### Selecting Items in Iterables: filter
- **Span:** PDF pp. 515–515 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** list, function, items, filter, sequence, built, iterable, arguments, sequences, comprehension, functional, range
- **Key terms/APIs that appear:** map, list, filter, range, all, lambda

#### Combining Items in Iterables: reduce
- **Span:** PDF pp. 516–516 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** reduce, function, sequence, lambda, items, built, tally, list, iterable, myreduce, range, equivalent
- **Key terms/APIs that appear:** lambda, list, range, filter, functools, sum, res.append, map, import

### Chapter Summary
- **Span:** PDF pp. 517–517 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, lambda, functions, reduce, functional, programming, though, operator, expressions, functools, filter, related
- **Key terms/APIs that appear:** lambda, functools, map, filter, functools.reduce, operator.add, import

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 517–517 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, lambda, functions, reduce, functional, programming, though, operator, expressions, functools, filter, related
- **Key terms/APIs that appear:** lambda, functools, map, filter, functools.reduce, operator.add, import

### Test Your Knowledge: Answers
- **Span:** PDF pp. 517–520 (4 pages; moderate detail)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** function, lambda, functions, button, reduce, though, statements, results, functional, tools, filter, annotations
- **Key terms/APIs that appear:** lambda, map, filter, functools, all, print, functools.reduce, import, except, operator.add, i.e, x.pack

## Chapter 20. Comprehensions and Generations
- **Span:** PDF pp. 521–566 (46 pages; extended treatment)
- **Breakdown:**
  - Comprehensions: The Final Act
  - Generator Functions and Expressions
  - Example: Shuffling Sequences
  - Example: Emulating zip and map
  - Asynchronous Functions: The Short Story
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 8 immediate subheadings; 16 leaf subsections underneath

### Comprehensions: The Final Act
- **Span:** PDF pp. 521–527 (7 pages; moderate detail)
- **Breakdown:**
  - List Comprehensions Review
  - Formal Comprehension Syntax
  - Example: List Comprehensions and Matrixes
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### List Comprehensions Review
- **Span:** PDF pp. 522–522 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** list, expression, comprehensions, function, results, iterable, apply, lists, though, similar, arbitrary, applying
- **Key terms/APIs that appear:** list, map, all, range, lambda, res.append, re, filter

#### Formal Comprehension Syntax
- **Span:** PDF pp. 523–524 (2 pages; brief)
- **Focus:** syntax forms and call/usage rules
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** list, comprehension, filter, range, comprehensions, clause, expression, equivalent, numbers, though, clauses, nested
- **Key terms/APIs that appear:** list, filter, range, lambda, map, res.append, any, time, all, set, re

#### Example: List Comprehensions and Matrixes
- **Span:** PDF pp. 525–527 (3 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** list, comprehensions, range, nested, column, append, matrixes, matrix, statement, following, lists, index
- **Key terms/APIs that appear:** list, range, zip, len, res.append, map, tmp.append, time, a.k, filter, all, any

### Generator Functions and Expressions
- **Span:** PDF pp. 528–543 (16 pages; deep dive)
- **Breakdown:**
  - Generator Functions: yield Versus return
  - Generator Expressions: Iterables Meet Comprehensions
  - Generator Functions Versus Generator Expressions
  - Generator Odds and Ends
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Generator Functions: yield Versus return
- **Span:** PDF pp. 528–533 (6 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** generator, yield, functions, iteration, generators, return, protocol, function, method, result, value, list
- **Key terms/APIs that appear:** yield, all, list, range, map, time, any, lambda, print, g.send, line.rstrip, x.__next__

#### Generator Expressions: Iterables Meet Comprehensions
- **Span:** PDF pp. 534–537 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** generator, list, expressions, comprehensions, results, expression, split, range, filter, functions, iteration, parentheses
- **Key terms/APIs that appear:** list, map, range, line.split, filter, all, x.upper, lambda, len, time, sorted, any

#### Generator Functions Versus Generator Expressions
- **Span:** PDF pp. 538–538 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** generator, expression, function, results, statement, automatically, method, returns, produce, yield, functions, expressions
- **Key terms/APIs that appear:** yield, list, all, time, lambda

#### Generator Odds and Ends
- **Span:** PDF pp. 539–543 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., NameError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** generator, comprehension, generators, range, iterators, results, iteration, list, expression, comprehensions, expressions, support
- **Key terms/APIs that appear:** range, all, list, os, set, len, yield, os.walk, any, type, lambda, x.upper

### Example: Shuffling Sequences
- **Span:** PDF pp. 544–550 (7 pages; moderate detail)
- **Breakdown:**
  - Scrambling Sequences
  - Permutating Sequences
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Scrambling Sequences
- **Span:** PDF pp. 544–546 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** generator, list, range, coding, scramble, results, function, print, generators, functions, values, yield
- **Key terms/APIs that appear:** list, range, len, print, yield, lambda, all, any, time, type, re, res.append

#### Permutating Sequences
- **Span:** PDF pp. 547–550 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** list, permute2, sequence, generator, permute1, results, generators, range, import, scramble1, shuffle, produce
- **Key terms/APIs that appear:** list, range, import, len, all, any, print, yield, math, random, math.factorial, set

### Example: Emulating zip and map
- **Span:** PDF pp. 551–554 (4 pages; moderate detail)
- **Breakdown:**
  - Coding Your Own map
  - Coding Your Own zip and 2.X map
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Coding Your Own map
- **Span:** PDF pp. 552–552 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** mymap, arguments, list, results, built, multiple, preceding, lists, py, result, return, function
- **Key terms/APIs that appear:** zip, map, list, re, print, lists.py, res.append, list.py, generate.py, all, yield

#### Coding Your Own zip and 2.X map
- **Span:** PDF pp. 553–554 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** list, return, generators, results, none, mymappad, myzip, tuple, print, result, built, padding
- **Key terms/APIs that appear:** list, zip, map, any, all, tuple, print, s.pop, yield, len, list.py, res.append

### Asynchronous Functions: The Short Story
- **Span:** PDF pp. 555–562 (8 pages; detailed)
- **Breakdown:**
  - Async Basics
  - The Async Wrap-Up
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Async Basics
- **Span:** PDF pp. 556–561 (6 pages; moderate detail)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** async, producer, await, print, asyncio, result, tasks, sleep, start, label, functions, coroutine
- **Key terms/APIs that appear:** async, await, all, print, time, asyncio.run, asyncio.sleep, asyncio.create_task, yield, range, list, all_async_demos.py

#### The Async Wrap-Up
- **Span:** PDF pp. 562–562 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** async, anext, await, coded, iterable, normal, value, print, result, function, yield, asynchronous
- **Key terms/APIs that appear:** async, all, await, print, yield, asyncio.sleep, asyncio.run, range, time, type

### Chapter Summary
- **Span:** PDF pp. 563–563 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** generator, tools, list, comprehensions, iteration, async, functions, expressions, though, generators, knowledge, result
- **Key terms/APIs that appear:** list, all, async, yield, re, map, await, time

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 563–563 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** generator, tools, list, comprehensions, iteration, async, functions, expressions, though, generators, knowledge, result
- **Key terms/APIs that appear:** list, all, async, yield, re, map, await, time

### Test Your Knowledge: Answers
- **Span:** PDF pp. 563–566 (4 pages; moderate detail)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., RunTimeError, RuntimeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** generator, list, function, stopiteration, iters, comprehensions, yield, return, async, iteration, functions, statement
- **Key terms/APIs that appear:** list, map, yield, async, all, time, await, any, tuple, except, re, try

## Chapter 21. The Benchmarking Interlude
- **Span:** PDF pp. 567–594 (28 pages; deep dive)
- **Breakdown:**
  - Benchmarking with Homegrown Tools
  - Benchmarking with Python’s timeit
  - Function Gotchas
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
  - Test Your Knowledge: Part IV Exercises
- **Granularity:** 7 immediate subheadings; 15 leaf subsections underneath

### Benchmarking with Homegrown Tools
- **Span:** PDF pp. 567–577 (11 pages; detailed)
- **Breakdown:**
  - Timer Module: Take 1
  - Timer Module: Take 2
  - Timing Runner and Script
  - Iteration Results
  - More Module Mods
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Timer Module: Take 1
- **Span:** PDF pp. 568–568 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** function, timer, calls, module, total, arguments, start, perf_counter, range, tested, short, verify
- **Key terms/APIs that appear:** time, time.perf_counter, range, import, timer0.py, time.process_time, time.clock, str.upper, any, str

#### Timer Module: Take 2
- **Span:** PDF pp. 569–570 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** total, result, timer, function, arguments, return, calls, functions, times, pargs, kargs, module
- **Key terms/APIs that appear:** time, import, range, min, any, timer.once, str.upper, timer.total, collections, all, filter, str

#### Timing Runner and Script
- **Span:** PDF pp. 571–572 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** results, total, timer, result, list, function, times, runner, bestoftotal, script, functions, repslist
- **Key terms/APIs that appear:** time, list, sys, all, str.upper, timer.bestoftotal, str, range, any, print, timer.bestof, min

#### Iteration Results
- **Span:** PDF pp. 573–575 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** list, repslist, return, results, forloop, listcomp, mapcall, genexpr, genfunc, cpython, slower, py
- **Key terms/APIs that appear:** list, map, all, range, timer_tests.py, timer_tests2.py, res.append, import, lambda, yield, time, timeseqs.py

#### More Module Mods
- **Span:** PDF pp. 576–577 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** timer2, bestoftotal, kargs, total, py, pargs, reps1, timer, arguments, return, function, functions
- **Key terms/APIs that appear:** timer2.bestoftotal, time, str.upper, map, str, timer.py, timer2.total, all, range, import, min, timer_tests3.py

### Benchmarking with Python’s timeit
- **Span:** PDF pp. 578–586 (9 pages; detailed)
- **Breakdown:**
  - Basic timeit Usage
  - Automating timeit Benchmarking
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Basic timeit Usage
- **Span:** PDF pp. 578–581 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
- **Key concepts (from text):** timeit, repeat, command, string, timing, module, list, range, loops, setup, number, python3
- **Key terms/APIs that appear:** time, list, range, min, import, timeit.repeat, re, timer2.bestoftotal, len, random, open, math

#### Automating timeit Benchmarking
- **Span:** PDF pp. 582–586 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** range, timeit, pythons, command, py, list, script, lines, set, module, stmts, repeat
- **Key terms/APIs that appear:** range, time, all, list, set, sys, pybench_tests.py, print, import, os, os.popen, sys.argv

### Function Gotchas
- **Span:** PDF pp. 587–590 (4 pages; moderate detail)
- **Breakdown:**
  - Local Names Are Detected Statically
  - Defaults and Mutable Objects
  - Functions Without returns
  - Miscellaneous Function Gotchas
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Local Names Are Detected Statically
- **Span:** PDF pp. 587–587 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., UnboundLocalError)
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** function, local, assigned, results, selector, assignment, names, locals, module, print, everywhere, platform
- **Key terms/APIs that appear:** all, re, print, import, any

#### Defaults and Mutable Objects
- **Span:** PDF pp. 588–589 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** function, saver, default, global, list, local, print, object, value, mutable, version, called
- **Key terms/APIs that appear:** list, time, print, saver.x, import, __main__.x, x.append, e.g, set, raise, all

#### Functions Without returns
- **Span:** PDF pp. 590–590 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, return, list, functions, none, enclosing, append, scopes, statements, value, print, result
- **Key terms/APIs that appear:** list, print, all, list.append, a.k, yield, re, try, raise, any

#### Miscellaneous Function Gotchas
- **Span:** PDF pp. 590–590 (1 page; very brief)
- **Focus:** common pitfalls and edge cases
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** function, return, list, functions, none, enclosing, append, scopes, statements, value, print, result
- **Key terms/APIs that appear:** list, print, all, list.append, a.k, yield, re, try, raise, any

### Chapter Summary
- **Span:** PDF pp. 591–591 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** built, functions, iteration, tools, knowledge, relative, list, comprehensions, assignment, reassign, names, scope
- **Key terms/APIs that appear:** list, time, map, all, re, type, any

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 591–591 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** built, functions, iteration, tools, knowledge, relative, list, comprehensions, assignment, reassign, names, scope
- **Key terms/APIs that appear:** list, time, map, all, re, type, any

### Test Your Knowledge: Answers
- **Span:** PDF pp. 591–591 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** built, functions, iteration, tools, knowledge, relative, list, comprehensions, assignment, reassign, names, scope
- **Key terms/APIs that appear:** list, time, map, all, re, type, any

### Test Your Knowledge: Part IV Exercises
- **Span:** PDF pp. 592–594 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** function, arguments, dictionary, print, results, functions, adder, three, module, write, argument, py
- **Key terms/APIs that appear:** print, type, time, list, sum, math, try, dict, any, re, all, i.e

# Part V. Modules and Packages
- **Span:** PDF pp. 595–684 (90 pages; extended treatment)
- **Breakdown:**
  - Chapter 22. Modules: The Big Picture
  - Chapter 23. Module Coding Basics
  - Chapter 24. Module Packages
  - Chapter 25. Module Odds and Ends
- **Granularity:** 4 immediate subheadings; 74 leaf subsections underneath

## Chapter 22. Modules: The Big Picture
- **Span:** PDF pp. 597–612 (16 pages; deep dive)
- **Breakdown:**
  - Module Essentials
  - Why Use Modules?
  - Python Program Architecture
  - How Imports Work
  - The Module Search Path
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 8 immediate subheadings; 16 leaf subsections underneath

### Module Essentials
- **Span:** PDF pp. 597–597 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** modules, module, provides, imports, import, files, program, packages, namespaces, programs, package, namespace
- **Key terms/APIs that appear:** import, __main__.py, importlib.reload, all

### Why Use Modules?
- **Span:** PDF pp. 598–598 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** modules, module, programs, names, imported, global, program, functions, system, packages, imports, files
- **Key terms/APIs that appear:** all, type, any, import

### Python Program Architecture
- **Span:** PDF pp. 598–600 (3 pages; brief)
- **Breakdown:**
  - How to Structure a Program
  - Imports and Attributes
  - Standard-Library Modules
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### How to Structure a Program
- **Span:** PDF pp. 599–599 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** files, modules, program, py, tools, level, attributes, module, architecture, structure, imports, statements
- **Key terms/APIs that appear:** b.py, c.py, a.k, a.py, import

#### Imports and Attributes
- **Span:** PDF pp. 599–600 (2 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** py, files, module, import, modules, program, level, attributes, statements, tools, function, defined
- **Key terms/APIs that appear:** import, a.py, b.py, c.py, a.k, b.job, e.g, object.attribute, print, re, all, time

#### Standard-Library Modules
- **Span:** PDF pp. 601–601 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** modules, library, import, standard, tools, module, imports, py, programs, instance, available, function
- **Key terms/APIs that appear:** import, any, all, sys, b.py, sys.stdlib_module_names, time, a.py, c.py, b.job, os, list

### How Imports Work
- **Span:** PDF pp. 601–604 (4 pages; moderate detail)
- **Breakdown:**
  - Step 1: Find It
  - Step 2: Compile It (Maybe)
  - Step 3: Run It
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Step 1: Find It
- **Span:** PDF pp. 602–602 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** module, import, modules, bytecode, imports, first, three, steps, program, statement, operation, compile
- **Key terms/APIs that appear:** import, sys, sys.modules, all, os, time, b.py, sorted, dir

#### Step 2: Compile It (Maybe)
- **Span:** PDF pp. 602–604 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** bytecode, module, files, import, modules, source, imported, imports, py, created, program, codefile
- **Key terms/APIs that appear:** import, all, sys, sys.modules, time, os, re, codefile.py, codefile.cpython, dir, b.py, codefile.pypy310

#### Step 3: Run It
- **Span:** PDF pp. 605–605 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** module, import, search, statements, modules, later, imported, files, process, first, components, bytecode
- **Key terms/APIs that appear:** import, sys, all, any, sys.builtin_module_names, time, sys.modules, importlib.reload, print, set, os, re

### The Module Search Path
- **Span:** PDF pp. 605–610 (6 pages; moderate detail)
- **Breakdown:**
  - Search-Path Components
  - Configuring the Search Path
  - The sys.path List
  - Module File Selection
  - Path Outliers: Standalones and Packages
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Search-Path Components
- **Span:** PDF pp. 605–607 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** module, directory, search, files, directories, import, modules, first, library, pythonpath, standard, packages
- **Key terms/APIs that appear:** import, all, any, sys, set, re, sys.path, list, sys.builtin_module_names, time, os, sys.modules

#### Configuring the Search Path
- **Span:** PDF pp. 608–608 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** users, search, list, pythonpath, pycode, module, pybench, permute, files, set, environment, macos
- **Key terms/APIs that appear:** list, set, e.g, sys.path, sys, all, pybench.py, permute.py, permute.permute1, pybench.runner, mypath.pth, import

#### The sys.path List
- **Span:** PDF pp. 608–608 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** users, search, list, pythonpath, pycode, module, pybench, permute, files, set, environment, macos
- **Key terms/APIs that appear:** list, set, e.g, sys.path, sys, all, pybench.py, permute.py, permute.permute1, pybench.runner, mypath.pth, import

#### Module File Selection
- **Span:** PDF pp. 609–609 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** search, users, list, module, program, import, library, settings, frameworks, framework, versions, scripts
- **Key terms/APIs that appear:** sys, sys.path, list, import, set, all, mypath.pth, python312.zip, e.g, zip, any, dir

#### Path Outliers: Standalones and Packages
- **Span:** PDF pp. 610–610 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, bytecode, source, files, import, named, directory, coded, search, py, imports, linked
- **Key terms/APIs that appear:** import, type, b.py, zip, any, all, b.cpython, b.pyc, e.g, b.so, b.pyd, b.attr

### Chapter Summary
- **Span:** PDF pp. 611–611 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** module, import, directory, search, imports, statements, directories, standard, pythonpath, package, set, syntax
- **Key terms/APIs that appear:** import, all, set, any, time

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 611–611 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** module, import, directory, search, imports, statements, directories, standard, pythonpath, package, set, syntax
- **Key terms/APIs that appear:** import, all, set, any, time

### Test Your Knowledge: Answers
- **Span:** PDF pp. 611–612 (2 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** module, import, directory, imports, search, statements, directories, files, namespace, standard, package, modules
- **Key terms/APIs that appear:** import, all, set, i.e, any, time, zip

## Chapter 23. Module Coding Basics
- **Span:** PDF pp. 613–630 (18 pages; deep dive)
- **Breakdown:**
  - Creating Modules
  - Using Modules
  - Module Namespaces
  - Reloading Modules
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 7 immediate subheadings; 20 leaf subsections underneath

### Creating Modules
- **Span:** PDF pp. 613–613 (1 page; very brief)
- **Breakdown:**
  - Module Filenames
  - Other Kinds of Modules
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Module Filenames
- **Span:** PDF pp. 613–613 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, modules, py, object, import, names, attribute, filenames, create, editor, simply, automatically
- **Key terms/APIs that appear:** import, module1.py, all, type, any, re, print

#### Other Kinds of Modules
- **Span:** PDF pp. 614–614 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, import, names, modules, py, files, external, variable, extension, module1, imported, specific
- **Key terms/APIs that appear:** import, all, i.e, if.py, m.extension, e.g, module1.py, module1.printer, any, try, re

### Using Modules
- **Span:** PDF pp. 614–619 (6 pages; moderate detail)
- **Breakdown:**
  - The import Statement
  - The from Statement
  - The from * Statement
  - Imports Happen Only Once
  - Imports Are Runtime Assignments
  - import and from Equivalence
  - Potential Pitfalls of the from Statement
- **Granularity:** 7 immediate subheadings; 7 leaf subsections underneath

#### The import Statement
- **Span:** PDF pp. 614–614 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, import, names, modules, py, files, external, variable, extension, module1, imported, specific
- **Key terms/APIs that appear:** import, all, i.e, if.py, m.extension, e.g, module1.py, module1.printer, any, try, re

#### The from Statement
- **Span:** PDF pp. 615–615 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** names, module, import, printer, statement, modules, module1, copies, copied, hello, world, really
- **Key terms/APIs that appear:** import, all, e.g, list, module1.printer, re, set

#### The from * Statement
- **Span:** PDF pp. 615–615 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** names, module, import, printer, statement, modules, module1, copies, copied, hello, world, really
- **Key terms/APIs that appear:** import, all, e.g, list, module1.printer, re, set

#### Imports Happen Only Once
- **Span:** PDF pp. 616–616 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, import, function, imports, first, modules, later, loaded, variable, attribute, rerun, level
- **Key terms/APIs that appear:** import, init.flag, init.py, print, time, all, re

#### Imports Are Runtime Assignments
- **Span:** PDF pp. 617–617 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** module, import, names, share, modules, object, copied, shared, mutable, statements, imported, changing
- **Key terms/APIs that appear:** import, share.py, share.x, share.y, time, try, list

#### import and from Equivalence
- **Span:** PDF pp. 618–618 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** module, names, import, statement, modules, changes, share, function, imported, assignment, copied, object
- **Key terms/APIs that appear:** import, all, share.x, module.name1, module.name2, e.g, module.name, except, re

#### Potential Pitfalls of the from Statement
- **Span:** PDF pp. 618–619 (2 pages; brief)
- **Focus:** common pitfalls and edge cases
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, import, names, statement, modules, variables, imported, assignment, scope, changes, share, though
- **Key terms/APIs that appear:** import, all, time, any, share.x, module.name1, module.name2, e.g, module.name, module.attr, m.py, n.py

### Module Namespaces
- **Span:** PDF pp. 620–624 (5 pages; moderate detail)
- **Breakdown:**
  - How Files Generate Namespaces
  - Namespace Dictionaries: __dict__
  - Attribute Name Qualification
  - Imports Versus Scopes
  - Namespace Nesting
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### How Files Generate Namespaces
- **Span:** PDF pp. 620–620 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** module, names, import, modules, namespaces, level, py, statements, simple, files, object, assigned
- **Key terms/APIs that appear:** import, o.py, i.e, m.py, dir, m.func, n.func, m.x, e.g, re, all, time

#### Namespace Dictionaries: __dict__
- **Span:** PDF pp. 621–621 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** module, import, spaces, attribute, namespace, klass, statements, scope, dictionary, function, print, scopes
- **Key terms/APIs that appear:** import, sys, print, spaces.py, spaces.klass, time, all, spaces.sys, spaces.var, spaces.func, any, type

#### Attribute Name Qualification
- **Span:** PDF pp. 622–622 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** spaces, dict, names, attribute, qualification, object, module, built, list, fetch, assigned, value
- **Key terms/APIs that appear:** spaces.__dict__, sys, dir, list, vars, sorted, spaces.var, spaces.__name__, spaces.__file__, spaces.py, name.startswith, a.k

#### Imports Versus Scopes
- **Span:** PDF pp. 623–623 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** module, global, names, scopes, object, py, means, qualification, attributes, import, modules, imports
- **Key terms/APIs that appear:** x.y, lex2.py, lex1.f, import, lex1.py, lex1.x, all, print

#### Namespace Nesting
- **Span:** PDF pp. 624–624 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** nest2, nest3, imported, imports, py, never, names, module, scopes, print, files, access
- **Key terms/APIs that appear:** print, import, nest3.py, nest2.py, nest1.py, nest2.nest3, all, nest3.x, nest2.x, time

### Reloading Modules
- **Span:** PDF pp. 625–627 (3 pages; brief)
- **Breakdown:**
  - reload Basics
  - reload Example
  - reload Odds and Ends
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### reload Basics
- **Span:** PDF pp. 626–626 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** module, reload, import, object, reloads, function, attributes, clients, statements, change, namespace, fetch
- **Key terms/APIs that appear:** import, module.attributes, re, changer.py, any, all

#### reload Example
- **Span:** PDF pp. 626–627 (2 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** module, reload, import, changer, function, object, modules, message, reloads, version, printer, attributes
- **Key terms/APIs that appear:** import, sys, changer.py, changer.printer, sys.modules, print, module.attributes, re, i.e, sys.mod, any, all

#### reload Odds and Ends
- **Span:** PDF pp. 628–628 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** reload, module, import, statement, function, imports, names, related, tools, instead, modules, though
- **Key terms/APIs that appear:** import, e.g

### Chapter Summary
- **Span:** PDF pp. 628–628 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **Key concepts (from text):** reload, module, import, statement, function, imports, names, related, tools, instead, modules, though
- **Key terms/APIs that appear:** import, e.g

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 628–628 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** reload, module, import, statement, function, imports, names, related, tools, instead, modules, though
- **Key terms/APIs that appear:** import, e.g

### Test Your Knowledge: Answers
- **Span:** PDF pp. 629–630 (2 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** module, names, import, imported, modules, scope, statement, knowledge, answers, source, objects, extension
- **Key terms/APIs that appear:** import, module.name

## Chapter 24. Module Packages
- **Span:** PDF pp. 631–654 (24 pages; deep dive)
- **Breakdown:**
  - Using Packages
  - Creating Packages
  - Why Packages?
  - The Roles of __init__.py Files
  - Package-Relative Imports
  - Namespace Packages
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 9 immediate subheadings; 17 leaf subsections underneath

### Using Packages
- **Span:** PDF pp. 631–632 (2 pages; brief)
- **Breakdown:**
  - Package Imports
  - Packages and the Module Search Path
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Package Imports
- **Span:** PDF pp. 632–632 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** import, module, directory, search, package, statements, py, paths, packages, syntax, platform, imports
- **Key terms/APIs that appear:** import, dir1.dir2, mod.py, list, any, mod.pyc, mod.so, sys.path, all, sys

#### Packages and the Module Search Path
- **Span:** PDF pp. 632–632 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** import, module, directory, search, package, statements, py, paths, packages, syntax, platform, imports
- **Key terms/APIs that appear:** import, dir1.dir2, mod.py, list, any, mod.pyc, mod.so, sys.path, all, sys

### Creating Packages
- **Span:** PDF pp. 633–637 (5 pages; moderate detail)
- **Breakdown:**
  - Basic Package Structure
  - Package __init__.py Files
  - Package __main__.py Files
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Basic Package Structure
- **Span:** PDF pp. 633–634 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError)
- **Key concepts (from text):** import, module, package, folder, nested, search, py, packages, directory, folders, loading, names
- **Key terms/APIs that appear:** import, dir1.dir2, dir1.mod, mod.py, mod.var, all, print, list, sys.path, __init__.py, __main__.py, sys

#### Package __init__.py Files
- **Span:** PDF pp. 635–636 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., ModuleNotFoundError)
- **Key concepts (from text):** py, package, import, module, paths, files, folder, packages, running, reload, loading, first
- **Key terms/APIs that appear:** dir1.dir2, __init__.py, import, mod.var, time, mod.py, dir1.__init__, print, dir1.mod, all, mod__.py, dir1.var

#### Package __main__.py Files
- **Span:** PDF pp. 637–637 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** py, package, files, executing, python3, running, search, folder, program, script, automatically, whenever
- **Key terms/APIs that appear:** __main__.py, dir1.dir2, __init__.py, mod.py, dir1.__main__, dir1.__init__, print, mod__.py, time, re, import, any

### Why Packages?
- **Span:** PDF pp. 638–640 (3 pages; brief)
- **Breakdown:**
  - A Tale of Two Systems
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### A Tale of Two Systems
- **Span:** PDF pp. 638–640 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** py, import, utilities, files, package, packages, common, directory, search, module, program, imports
- **Key terms/APIs that appear:** import, all, utilities.py, main.py, __main__.py, other.py, re, sys, sys.path, system1.utilities, system2.utilities, zip

### The Roles of __init__.py Files
- **Span:** PDF pp. 641–641 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** package, py, files, directory, module, names, initialization, automatically, namespace, search, import, nested
- **Key terms/APIs that appear:** __init__.py, import, time, list, all, __main__.py, dir1.dir2, open, set, any

### Package-Relative Imports
- **Span:** PDF pp. 642–646 (5 pages; moderate detail)
- **Breakdown:**
  - Relative and Absolute Imports
  - Relative-Import Rationales and Trade-Offs
  - Package-Relative Imports in Action
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Relative and Absolute Imports
- **Span:** PDF pp. 642–642 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** package, import, imports, module, files, relative, folder, syntax, names, parent, though, means
- **Key terms/APIs that appear:** import, sys.path, sys, __init__.py

#### Relative-Import Rationales and Trade-Offs
- **Span:** PDF pp. 643–643 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** package, imports, relative, module, import, folder, absolute, search, files, filename, paths, today
- **Key terms/APIs that appear:** import, sys.path, sys, re, __main__.py, package.module, all, e.g, list, any, print

#### Package-Relative Imports in Action
- **Span:** PDF pp. 643–646 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., ImportError, ModuleNotFoundError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** package, py, import, imports, relative, module, executing, absolute, folder, python3, print, files
- **Key terms/APIs that appear:** import, dir1.__main__, __main__.py, dir1.mod, print, sys.path, dir1.__init__, sys, re, mod.var, all, any

### Namespace Packages
- **Span:** PDF pp. 647–650 (4 pages; moderate detail)
- **Breakdown:**
  - Python Import Models
  - Namespace-Package Rationales
  - The Module Search Algorithm
  - Namespace Packages in Action
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Python Import Models
- **Span:** PDF pp. 647–647 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** packages, import, package, module, namespace, model, relative, search, imports, original, folder, modules
- **Key terms/APIs that appear:** import, __init__.py, sys.path, sys, all, folder.folder, folder.module, anyfolder.anyfolder, any

#### Namespace-Package Rationales
- **Span:** PDF pp. 648–648 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** package, packages, namespace, search, import, py, module, directory, regular, multiple, directories, imports
- **Key terms/APIs that appear:** import, __init__.py, set, sys.path, sys, time, type, any, all

#### The Module Search Algorithm
- **Span:** PDF pp. 648–648 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** package, packages, namespace, search, import, py, module, directory, regular, multiple, directories, imports
- **Key terms/APIs that appear:** import, __init__.py, set, sys.path, sys, time, type, any, all

#### Namespace Packages in Action
- **Span:** PDF pp. 649–650 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** package, namespace, search, py, directory, packages, folder, part1, part2, module, import, regular
- **Key terms/APIs that appear:** import, __init__.py, set, mod1.py, mod2.py, sub.mod2, print, sys.path, sys, any, sub.mod1, time

### Chapter Summary
- **Span:** PDF pp. 651–651 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** import, packages, part1, module, chapter24, package, part2, py, directory, loading, relative, namespace
- **Key terms/APIs that appear:** import, sub.mod2, sub.mod1, mod1.py, mod2.py, sub.__path__, __init__.py, print, dir, except, re, map

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 652–652 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** import, package, packages, module, search, statement, files, optional, relative, imports, instead, namespace
- **Key terms/APIs that appear:** import, __init__.py, time, sys.path, any, sys

### Test Your Knowledge: Answers
- **Span:** PDF pp. 652–654 (3 pages; brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** package, import, module, packages, search, namespace, directories, files, statement, optional, py, relative
- **Key terms/APIs that appear:** import, __init__.py, time, all, sys.path, any, sys

## Chapter 25. Module Odds and Ends
- **Span:** PDF pp. 655–684 (30 pages; deep dive)
- **Breakdown:**
  - Module Design Concepts
  - Data Hiding in Modules
  - Enabling Language Changes: __future__
  - Dual-Usage Modes: __name__ and __main__
  - The as Extension for import and from
  - Module Introspection
  - Importing Modules by Name String
  - Module Gotchas
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
  - Test Your Knowledge: Part V Exercises
- **Granularity:** 12 immediate subheadings; 21 leaf subsections underneath

### Module Design Concepts
- **Span:** PDF pp. 655–655 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, functions, modules, tools, design, related, topics, briefly, concepts, classes, general, prompt
- **Key terms/APIs that appear:** re, all, a.k, set, except

### Data Hiding in Modules
- **Span:** PDF pp. 656–659 (4 pages; moderate detail)
- **Breakdown:**
  - Minimizing from * Damage: _X and __all__
  - Managing Attribute Access: __getattr__ and __dir__
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Minimizing from * Damage: _X and __all__
- **Span:** PDF pp. 657–657 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., NameError)
- **Key concepts (from text):** names, import, unders, copied, module, copies, underscores, hiding, list, single, underscore, imports
- **Key terms/APIs that appear:** import, list, all, e.g, unders.py, unders._d, alls.py, any

#### Managing Attribute Access: __getattr__ and __dir__
- **Span:** PDF pp. 658–659 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError, NameError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, getattr, gamod, attribute, virtual, import, modules, classes, names, defined, access, though
- **Key terms/APIs that appear:** import, gamod.hack, list, all, dir, print, raise, alls.a, alls.b, alls._c, alls._d, __init__.py

### Enabling Language Changes: __future__
- **Span:** PDF pp. 660–660 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** future, module, import, statement, changes, script, feature, language, version, though, appear, default
- **Key terms/APIs that appear:** import, set, dualmode.py, print, yield, list

### Dual-Usage Modes: __name__ and __main__
- **Span:** PDF pp. 660–662 (3 pages; brief)
- **Breakdown:**
  - Example: Unit Tests with __name__
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Example: Unit Tests with __name__
- **Span:** PDF pp. 661–662 (2 pages; brief)
- **Focus:** worked examples and usage patterns; review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** minmax, module, script, print, return, py, lessthan, dualmode, import, python3, bottom, usage
- **Key terms/APIs that appear:** print, import, set, dualmode.py, minmax.py, re, dualmode.title, __main__.py, minmax.minmax, minmax.lessthan, all, time

### The as Extension for import and from
- **Span:** PDF pp. 663–663 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** import, modulename, module, extension, attrname, works, original, script, statements, following, importer, scope
- **Key terms/APIs that appear:** import, formats.py, set

### Module Introspection
- **Span:** PDF pp. 664–666 (3 pages; brief)
- **Breakdown:**
  - Example: Listing Modules with __dict__
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Example: Listing Modules with __dict__
- **Span:** PDF pp. 665–666 (2 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** module, listing, mydir, built, py, print, minmax, lessthan, dict, modules, tkinter, import
- **Key terms/APIs that appear:** print, mydir.py, import, sys, re, sys.modules, module.__name__, module.__dict__, __init__.py, getattr, sorted, list

### Importing Modules by Name String
- **Span:** PDF pp. 667–675 (9 pages; detailed)
- **Breakdown:**
  - Running Code Strings
  - Direct Calls: Two Options
  - Example: Transitive Module Reloads
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Running Code Strings
- **Span:** PDF pp. 667–667 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., ModuleNotFoundError, SyntaxError)
- **Key concepts (from text):** string, module, import, variable, importing, tools, namespace, statement, runtime, mydir, program, programs
- **Key terms/APIs that appear:** import, mydir.listing, x.py, string.py, getattr, time, try

#### Direct Calls: Two Options
- **Span:** PDF pp. 668–668 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** import, string, module, importlib, email, py, imports, package, modname, python3, message, reload
- **Key terms/APIs that appear:** import, importlib.import_module, email.message, string.py, __init__.py, message.py, a.py, time

#### Example: Transitive Module Reloads
- **Span:** PDF pp. 668–675 (8 pages; detailed)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
  - calls out caveats and edge cases
- **Key concepts (from text):** module, reloading, import, py, reload, string, modules, tkinter, python3, reloadall, reloads, reload_all
- **Key terms/APIs that appear:** import, all, collections, dir1.dir2, reloadall.py, ra.rb, reloadall3.py, collections.abc, os, os.popen, type, set

### Module Gotchas
- **Span:** PDF pp. 676–680 (5 pages; moderate detail)
- **Breakdown:**
  - Module Name Clashes: Package and Package-Relative Imports
  - Statement Order Matters in Top-Level Code
  - from Copies Names but Doesn’t Link
  - from * Can Obscure the Meaning of Variables
  - reload May Not Impact from Imports
  - reload, from, and Interactive Testing
  - Recursive from Imports May Not Work
- **Granularity:** 7 immediate subheadings; 7 leaf subsections underneath

#### Module Name Clashes: Package and Package-Relative Imports
- **Span:** PDF pp. 676–676 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, directory, package, import, names, modules, function, imports, files, version, level, first
- **Key terms/APIs that appear:** import, all, any, sys.path, set, sys

#### Statement Order Matters in Top-Level Code
- **Span:** PDF pp. 676–676 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, directory, package, import, names, modules, function, imports, files, version, level, first
- **Key terms/APIs that appear:** import, all, any, sys.path, set, sys

#### from Copies Names but Doesn’t Link
- **Span:** PDF pp. 677–677 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** func1, func2, module, names, assigned, level, bottom, statement, importer, nested, py, printer
- **Key terms/APIs that appear:** import, nested.py, print, time, nested1.py, all, re

#### from * Can Obscure the Meaning of Variables
- **Span:** PDF pp. 678–678 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** module, names, import, changes, nested, impact, objects, modules, using, reload, variables, list
- **Key terms/APIs that appear:** import, any, list, all, nested.x, nested.printer, re

#### reload May Not Impact from Imports
- **Span:** PDF pp. 678–678 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** module, names, import, changes, nested, impact, objects, modules, using, reload, variables, list
- **Key terms/APIs that appear:** import, any, list, all, nested.x, nested.printer, re

#### reload, from, and Interactive Testing
- **Span:** PDF pp. 679–679 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, reload, import, function, importlib, reloads, names, doesn, launch, refer, remember, place
- **Key terms/APIs that appear:** import, module.function, re, module.x, try, all

#### Recursive from Imports May Not Work
- **Span:** PDF pp. 680–680 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., ImportError)
- **Key concepts (from text):** import, recur1, imports, module, recur2, recursive, modules, names, fetch, assigned, statements, doesn
- **Key terms/APIs that appear:** import, recur1.py, recur2.py, all, time

### Chapter Summary
- **Span:** PDF pp. 681–681 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **Key concepts (from text):** module, import, names, attribute, level, instead, future, knowledge, variable, string, using, exercises
- **Key terms/APIs that appear:** import, all, set, list, getattr

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 681–681 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** module, import, names, attribute, level, instead, future, knowledge, variable, string, using, exercises
- **Key terms/APIs that appear:** import, all, set, list, getattr

### Test Your Knowledge: Answers
- **Span:** PDF pp. 681–681 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** module, import, names, attribute, level, instead, future, knowledge, variable, string, using, exercises
- **Key terms/APIs that appear:** import, all, set, list, getattr

### Test Your Knowledge: Part V Exercises
- **Span:** PDF pp. 682–684 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, import, mymod, py, functions, function, string, interactively, imports, package, input, directory
- **Key terms/APIs that appear:** import, mymod.py, input, try, re, all, importlib.import_module, file.readlines, file.read, sys.argv, reloadall.py, file.seek

# Part VI. Classes and OOP
- **Span:** PDF pp. 685–910 (226 pages; extended treatment)
- **Breakdown:**
  - Chapter 26. OOP: The Big Picture
  - Chapter 27. Class Coding Basics
  - Chapter 28. A More Realistic Example
  - Chapter 29. Class Coding Details
  - Chapter 30. Operator Overloading
  - Chapter 31. Designing with Classes
  - Chapter 32. Class Odds and Ends
- **Granularity:** 7 immediate subheadings; 142 leaf subsections underneath

## Chapter 26. OOP: The Big Picture
- **Span:** PDF pp. 687–698 (12 pages; detailed)
- **Breakdown:**
  - Why Use Classes?
  - OOP from 30,000 Feet
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 5 immediate subheadings; 10 leaf subsections underneath

### Why Use Classes?
- **Span:** PDF pp. 687–688 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** classes, objects, inheritance, class, object, functions, robots, built, programming, types, define, pizza
- **Key terms/APIs that appear:** time, all, collections, any, re, set, sys, type

### OOP from 30,000 Feet
- **Span:** PDF pp. 689–696 (8 pages; detailed)
- **Breakdown:**
  - Attribute Inheritance Search
  - Classes and Instances
  - Method Calls
  - Coding Class Trees
  - Operator Overloading
  - OOP Is About Code Reuse
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Attribute Inheritance Search
- **Span:** PDF pp. 689–690 (2 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** object, attribute, search, attributes, objects, classes, terms, expression, class, inheritance, instances, superclasses
- **Key terms/APIs that appear:** all, object.attribute, e.g, i2.w, c3.w, i1.x, i2.x, i1.y, i2.y, i1.z, i2.z, i2.name

#### Classes and Instances
- **Span:** PDF pp. 691–691 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** classes, instances, class, employee, instance, attribute, object, model, attached, method, function, implied
- **Key terms/APIs that appear:** i2.w, c3.w, e.g, pat.giveraise, employee.giveraise, list, type, try, map, raise

#### Method Calls
- **Span:** PDF pp. 691–691 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** classes, instances, class, employee, instance, attribute, object, model, attached, method, function, implied
- **Key terms/APIs that appear:** i2.w, c3.w, e.g, pat.giveraise, employee.giveraise, list, type, try, map, raise

#### Coding Class Trees
- **Span:** PDF pp. 692–693 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, instances, classes, attributes, objects, though, instance, function, statements, method, called, object
- **Key terms/APIs that appear:** all, time, i1.name, employee.giveraise, classtree1.py, e.g, c3.z, classtree2.py, c1.setname, self.name, i1.setname, i2.setname

#### Operator Overloading
- **Span:** PDF pp. 694–694 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, method, operator, objects, set, setname, instance, called, instances, calls, named, trees
- **Key terms/APIs that appear:** set, i1.name, i1.setname, any, time, c1.setname, classtree3.py, self.name, i2.name, all, print, re

#### OOP Is About Code Reuse
- **Span:** PDF pp. 694–696 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, classes, employee, methods, instance, method, objects, behavior, instances, default, object, inheritance
- **Key terms/APIs that appear:** all, set, any, i1.name, time, i1.setname, print, re, type, c1.setname, classtree3.py, self.name

### Chapter Summary
- **Span:** PDF pp. 697–697 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** classes, class, object, instance, superclasses, frameworks, programming, higher, design, argument, search, objects
- **Key terms/APIs that appear:** collections, time, all

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 697–697 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** classes, class, object, instance, superclasses, frameworks, programming, higher, design, argument, search, objects
- **Key terms/APIs that appear:** collections, time, all

### Test Your Knowledge: Answers
- **Span:** PDF pp. 697–698 (2 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, instance, method, classes, object, search, objects, inheritance, function, superclasses, argument, first
- **Key terms/APIs that appear:** any, time, i.e, collections, all

## Chapter 27. Class Coding Basics
- **Span:** PDF pp. 699–716 (18 pages; deep dive)
- **Breakdown:**
  - Classes Generate Multiple Instance Objects
  - Classes Are Customized by Inheritance
  - Classes Can Intercept Python Operators
  - The World’s Simplest Python Class
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 7 immediate subheadings; 11 leaf subsections underneath

### Classes Generate Multiple Instance Objects
- **Span:** PDF pp. 699–701 (3 pages; brief)
- **Breakdown:**
  - Class Objects Provide Default Behavior
  - Instance Objects Are Concrete Items
  - A First Example
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Class Objects Provide Default Behavior
- **Span:** PDF pp. 700–700 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, object, attributes, instance, statement, instances, methods, classes, objects, behavior, first, assignments
- **Key terms/APIs that appear:** class.name, re, all, time, any

#### Instance Objects Are Concrete Items
- **Span:** PDF pp. 700–700 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, object, attributes, instance, statement, instances, methods, classes, objects, behavior, first, assignments
- **Key terms/APIs that appear:** class.name, re, all, time, any

#### A First Example
- **Span:** PDF pp. 700–701 (2 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, object, instance, attributes, statement, instances, objects, firstclass, methods, classes, setdata, statements
- **Key terms/APIs that appear:** self.data, re, all, firstclass.setdata, time, any, class.name, firstclass.display, x.setdata, y.setdata, print, yield

### Classes Are Customized by Inheritance
- **Span:** PDF pp. 702–704 (3 pages; brief)
- **Breakdown:**
  - A Second Example
  - Classes Are Attributes in Modules
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### A Second Example
- **Span:** PDF pp. 703–703 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, classes, attribute, inheritance, inherit, superclasses, attributes, instances, names, search, secondclass, display
- **Key terms/APIs that appear:** all, print, object.attribute, e.g, x.attr, self.attr, self.data, list, re, any

#### Classes Are Attributes in Modules
- **Span:** PDF pp. 704–704 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** firstclass, secondclass, display, class, setdata, instance, subclasses, finds, method, object, inheritance, instances
- **Key terms/APIs that appear:** any, import, z.setdata, z.display, x.display, i.e, time, re

### Classes Can Intercept Python Operators
- **Span:** PDF pp. 705–708 (4 pages; moderate detail)
- **Breakdown:**
  - A Third Example
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### A Third Example
- **Span:** PDF pp. 707–708 (2 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** thirdclass, method, object, instance, str, class, print, value, operator, display, overloading, place
- **Key terms/APIs that appear:** print, self.data, time, all, str, any, __init__.py, a.display, b.display, a.mul, set, re

### The World’s Simplest Python Class
- **Span:** PDF pp. 709–712 (4 pages; moderate detail)
- **Breakdown:**
  - Classes: Under the Hood
  - Records Revisited: Classes Versus Dictionaries
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Classes: Under the Hood
- **Span:** PDF pp. 709–710 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., KeyError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, attributes, attribute, object, objects, dict, namespace, inheritance, classes, instances, instance, statement
- **Key terms/APIs that appear:** x.name, x.__dict__, rec.name, list, y.name, all, dir, dict, rec.age, rec.__dict__, key.startswith, y.__dict__

#### Records Revisited: Classes Versus Dictionaries
- **Span:** PDF pp. 711–712 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, method, attributes, methods, simple, instance, classes, records, record, argument, though, attribute
- **Key terms/APIs that appear:** any, print, rec.method, rec.name, pers1.name, pers2.name, self.name, self.jobs, tuple, time, obj.name, x.method

### Chapter Summary
- **Span:** PDF pp. 713–713 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, classes, instances, attributes, logic, methods, dictionaries, named, tuples, construction, basics, simple
- **Key terms/APIs that appear:** e.g, time, tuple, set, all, map, dict

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 713–713 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, classes, instances, attributes, logic, methods, dictionaries, named, tuples, construction, basics, simple
- **Key terms/APIs that appear:** e.g, time, tuple, set, all, map, dict

### Test Your Knowledge: Answers
- **Span:** PDF pp. 714–716 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, attributes, method, instance, object, operator, overloading, created, classes, though, statement, argument
- **Key terms/APIs that appear:** all, type, e.g, i.e, set

## Chapter 28. A More Realistic Example
- **Span:** PDF pp. 717–750 (34 pages; extended treatment)
- **Breakdown:**
  - Step 1: Making Instances
  - Step 2: Adding Behavior Methods
  - Step 3: Operator Overloading
  - Step 4: Customizing Behavior by Subclassing
  - Step 5: Customizing Constructors, Too
  - Step 6: Using Introspection Tools
  - Step 7 (Final): Storing Objects in a Database
  - Future Directions
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 11 immediate subheadings; 26 leaf subsections underneath

### Step 1: Making Instances
- **Span:** PDF pp. 717–720 (4 pages; moderate detail)
- **Breakdown:**
  - Coding Constructors
  - Testing as You Go
  - Using Code Two Ways
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Coding Constructors
- **Span:** PDF pp. 718–718 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** instance, class, person, object, arguments, later, py, first, attributes, created, method, module
- **Key terms/APIs that appear:** self.job, person.py, person_1.py, person_2.py, self.name, self.pay, re, any, time

#### Testing as You Go
- **Span:** PDF pp. 719–719 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, default, none, person, defaults, testing, function, features, probably, making, attributes, write
- **Key terms/APIs that appear:** all, self.name, self.job, self.pay, print, person_3.py, person_4.py, bob.name, bob.pay, sue.name, sue.pay, any

#### Using Code Two Ways
- **Span:** PDF pp. 720–720 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, tests, arguments, functions, bottom, person, module, information, classes, imported, notice, object
- **Key terms/APIs that appear:** import, person_4.py, person_5.py, self.name, self.job, self.pay, any, type, all, set, print, time

### Step 2: Adding Behavior Methods
- **Span:** PDF pp. 721–723 (3 pages; brief)
- **Breakdown:**
  - Coding Methods
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Coding Methods
- **Span:** PDF pp. 722–723 (2 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** methods, print, operations, class, person, smith, change, jones, lastname, method, raise, int
- **Key terms/APIs that appear:** print, sue.pay, self.pay, raise, re, int, self.name, bob.name, person_6.py, self.job, bob.pay, sue.name

### Step 3: Operator Overloading
- **Span:** PDF pp. 724–725 (2 pages; brief)
- **Breakdown:**
  - Providing Print Displays
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Providing Print Displays
- **Span:** PDF pp. 724–725 (2 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** print, method, class, object, instance, giveraise, percent, displays, lastname, instances, operator, overloading
- **Key terms/APIs that appear:** print, self.pay, time, self.name, raise, bob.lastname, sue.lastname, e.g, re, any, int, all

### Step 4: Customizing Behavior by Subclassing
- **Span:** PDF pp. 726–730 (5 pages; moderate detail)
- **Breakdown:**
  - Coding Subclasses
  - Augmenting Methods: The Bad Way
  - Augmenting Methods: The Good Way
  - Polymorphism in Action
  - Inherit, Customize, and Extend
  - OOP: The Big Idea
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Coding Subclasses
- **Span:** PDF pp. 726–726 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** person, manager, class, behavior, jones, instances, software, inheritance, define, subclass, giveraise, managers
- **Key terms/APIs that appear:** any, all, re, raise, print, time

#### Augmenting Methods: The Bad Way
- **Span:** PDF pp. 727–727 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** instance, giveraise, class, method, manager, person, bonus, percent, version, original, paste, directly
- **Key terms/APIs that appear:** self.pay, person.giveraise, instance.method, class.method, self.giveraise, int, re

#### Augmenting Methods: The Good Way
- **Span:** PDF pp. 727–728 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** person, giveraise, manager, method, class, instance, percent, bonus, version, jones, print, lastname
- **Key terms/APIs that appear:** self.pay, print, self.name, person.giveraise, self.giveraise, int, instance.method, class.method, person_9.py, self.job, bob.lastname, sue.lastname

#### Polymorphism in Action
- **Span:** PDF pp. 729–729 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** super, class, giveraise, inheritance, explicit, multiple, methods, superclass, single, method, inherited, person
- **Key terms/APIs that appear:** super, all, re, person.giveraise, print, person_9_plus.py, obj.giveraise, any, try, list

#### Inherit, Customize, and Extend
- **Span:** PDF pp. 730–730 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** person, giveraise, manager, method, object, version, classes, extend, somethingelse, three, objects, inherit
- **Key terms/APIs that appear:** all, type, pat.lastname, pat.giveraise, pat.somethingelse, any, re, print

#### OOP: The Big Idea
- **Span:** PDF pp. 731–731 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** manager, person, class, giveraise, customizing, classes, simply, changed, future, provide, constructor, rather
- **Key terms/APIs that appear:** time, person_10.py, self.name, self.job, self.pay, yield, all

### Step 5: Customizing Constructors, Too
- **Span:** PDF pp. 731–735 (5 pages; moderate detail)
- **Breakdown:**
  - OOP Is Simpler Than You May Think
  - Other Ways to Combine Classes: Composites
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### OOP Is Simpler Than You May Think
- **Span:** PDF pp. 733–733 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** classes, methods, attributes, getattr, concepts, instance, behavior, logic, class, operator, overloading, customizing
- **Key terms/APIs that appear:** all, getattr, x.y, re, yield

#### Other Ways to Combine Classes: Composites
- **Span:** PDF pp. 733–735 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** person, manager, objects, embedded, methods, object, classes, class, giveraise, inheritance, jones, department
- **Key terms/APIs that appear:** all, self.person, self.members, getattr, print, composite.py, department.py, import, list, x.y, pat.giveraise, manager.giveraise

### Step 6: Using Introspection Tools
- **Span:** PDF pp. 736–741 (6 pages; moderate detail)
- **Breakdown:**
  - Special Class Attributes
  - A Generic Display Tool
  - Instance Versus Class Attributes
  - Name Considerations in Tool Classes
  - Our Classes’ Final Form
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Special Class Attributes
- **Span:** PDF pp. 737–737 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** person, class, tools, attributes, dict, print, classes, instance, attribute, names, provides, modules
- **Key terms/APIs that appear:** print, pat.__dict__, pat.__class__, any, list, instance.__class__, object.__dict__, person.py, person.person, set, time, all

#### A Generic Display Tool
- **Span:** PDF pp. 738–738 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, instance, dict, attributes, slots, display, attrs, getattr, classes, instances, inheritance, prior
- **Key terms/APIs that appear:** any, getattr, classtools.py, pat.__dict__, obj.attr, self.__dict__, attrs.append, self.__class__, self.gatherattrs, print, hasattr, dir

#### Instance Versus Class Attributes
- **Span:** PDF pp. 739–739 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, toptest, attributes, instance, count, methods, inherited, instances, attribute, str, attr1, attr2
- **Key terms/APIs that appear:** toptest.count, all, print, sorted, dir, self.attr1, self.attr2, classtools.py, any, str, re, filter

#### Name Considerations in Tool Classes
- **Span:** PDF pp. 740–740 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, gatherattrs, classes, attrdisplay, person, method, methods, display, inheritance, subclass, toptest, import
- **Key terms/APIs that appear:** import, dir, pat.__dict__, a.startswith, classtree.py, lister.py, self.gatherattrs, list, all

#### Our Classes’ Final Form
- **Span:** PDF pp. 740–741 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, person, classes, attrdisplay, gatherattrs, giveraise, methods, print, lastname, final, percent, display
- **Key terms/APIs that appear:** print, self.pay, import, self.name, dir, all, pat.__dict__, a.startswith, classtree.py, lister.py, self.gatherattrs, person.py

### Step 7 (Final): Storing Objects in a Database
- **Span:** PDF pp. 742–746 (5 pages; moderate detail)
- **Breakdown:**
  - Pickles and Shelves
  - Storing Objects on a shelve Database
  - Exploring Shelves Interactively
  - Updating Objects on a Shelf
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Pickles and Shelves
- **Span:** PDF pp. 742–742 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** objects, jones, person, display, classes, module, object, pickle, manager, class, general, future
- **Key terms/APIs that appear:** pickle, bytes, person_14.py, any, all, re

#### Storing Objects on a shelve Database
- **Span:** PDF pp. 743–743 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** objects, shelve, module, pickle, store, person, object, class, shelves, pickled, shelf, instances
- **Key terms/APIs that appear:** pickle, import, all, re, dict.keys, person.person, person.py, len, dict, map, open, sqlite3

#### Exploring Shelves Interactively
- **Span:** PDF pp. 744–745 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** objects, shelf, jones, class, module, person, shelve, stored, files, import, persondb, database
- **Key terms/APIs that appear:** import, open, all, re, print, shelve.open, persondb.db, makedb.py, any, list, obj.name, db.close

#### Updating Objects on a Shelf
- **Span:** PDF pp. 746–746 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** jones, person, objects, database, shelve, smith, shelf, script, updatedb, py, python3, prints
- **Key terms/APIs that appear:** updatedb.py, time, shelve.open, all, import, open, sue.giveraise, db.close, rec.lastname, rec.pay, raise, re

### Future Directions
- **Span:** PDF pp. 747–747 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** classes, database, object, basics, tools, future, objects, class, persistence, larger, shelve, details
- **Key terms/APIs that appear:** all, open, pickle, raise, sqlite3, json, any, set

### Chapter Summary
- **Span:** PDF pp. 747–747 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** classes, database, object, basics, tools, future, objects, class, persistence, larger, shelve, details
- **Key terms/APIs that appear:** all, open, pickle, raise, sqlite3, json, any, set

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 748–748 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, better, instance, object, module, methods, future, manager, method, instead, copying, knowledge
- **Key terms/APIs that appear:** all, print, type, list, pickle, any, time

### Test Your Knowledge: Answers
- **Span:** PDF pp. 748–750 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, method, classes, methods, better, objects, inheritance, instance, future, generic, manager, object
- **Key terms/APIs that appear:** print, all, list, time, type, pickle, any, super

## Chapter 29. Class Coding Details
- **Span:** PDF pp. 751–776 (26 pages; deep dive)
- **Breakdown:**
  - The class Statement
  - Methods
  - Inheritance
  - Namespaces: The Conclusion
  - Documentation Strings Revisited
  - Classes Versus Modules
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 9 immediate subheadings; 20 leaf subsections underneath

### The class Statement
- **Span:** PDF pp. 751–753 (3 pages; brief)
- **Breakdown:**
  - General Syntax and Usage
  - Example: Class Attributes
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### General Syntax and Usage
- **Span:** PDF pp. 751–751 (1 page; very brief)
- **Focus:** syntax forms and call/usage rules
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, statement, study, header, coding, details, quite, first, concepts, introduced, mechanics, inheritance
- **Key terms/APIs that appear:** all, re

#### Example: Class Attributes
- **Span:** PDF pp. 752–753 (2 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, instance, attributes, statement, instances, object, names, method, attribute, shareddata, assign, shared
- **Key terms/APIs that appear:** all, self.data, x.attr, shareddata.attr, y.attr, mixednames.data, any, a.k, time, print, self.attr, x.method

### Methods
- **Span:** PDF pp. 754–755 (2 pages; brief)
- **Breakdown:**
  - Method Example
  - Other Method-Call Possibilities
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Method Example
- **Span:** PDF pp. 754–754 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** method, class, instance, methods, object, attribute, argument, classes, objects, first, names, define
- **Key terms/APIs that appear:** self.message, instance.method, class.method, list, print

#### Other Method-Call Possibilities
- **Span:** PDF pp. 755–755 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** instance, class, methods, printer, method, argument, called, object, nextclass, automatically, assigned, instances
- **Key terms/APIs that appear:** nextclass.printer, x.message, any, all, x.printer, class.attribute, set, try

### Inheritance
- **Span:** PDF pp. 756–761 (6 pages; moderate detail)
- **Breakdown:**
  - Attribute Tree Construction
  - Inheritance Fine Print
  - Specializing Inherited Methods
  - Class Interface Techniques
  - Abstract Superclasses
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Attribute Tree Construction
- **Span:** PDF pp. 756–756 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, attribute, object, inheritance, instance, attributes, namespace, superclasses, created, statement, happens, namespaces
- **Key terms/APIs that appear:** time, object.attr, all

#### Inheritance Fine Print
- **Span:** PDF pp. 757–757 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** method, super, inheritance, class, attributes, print, instance, default, classes, behavior, superclass, names
- **Key terms/APIs that appear:** super, super.method, sub.method, print, x.method, all

#### Specializing Inherited Methods
- **Span:** PDF pp. 757–758 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** method, super, class, superclass, inheritance, print, attributes, default, calls, classes, instance, behavior
- **Key terms/APIs that appear:** super, super.method, sub.method, print, all, x.method, super.__init__, time, re

#### Class Interface Techniques
- **Span:** PDF pp. 759–759 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** method, super, print, class, action, extender, delegate, replacer, provider, inheritor, klass, interface
- **Key terms/APIs that appear:** super, print, specialize.py, super.method, extender.method, self.action, replacer.method, provider.action, klass.__name__, x.delegate, any

#### Abstract Superclasses
- **Span:** PDF pp. 760–761 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AssertionError, NotImplementedError)
- **Key concepts (from text):** method, action, class, delegate, super, provider, classes, defined, abstract, inheritance, subclass, exception
- **Key terms/APIs that appear:** super, x.delegate, self.action, raise, super.method, extender.method, specialize.py, replacer.method, provider.action, super.delegate, a.k, tuple

### Namespaces: The Conclusion
- **Span:** PDF pp. 762–771 (10 pages; detailed)
- **Breakdown:**
  - Simple Names: Global Unless Assigned
  - Attribute Names: Object Namespaces
  - The “Zen” of Namespaces: Assignments Classify Names
  - Nested Classes: The LEGB Scopes Rule Revisited
  - Namespace Dictionaries: Review
  - Namespace Links: A Tree Climber
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Simple Names: Global Unless Assigned
- **Span:** PDF pp. 763–763 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, names, attribute, global, functions, assignment, local, scope, classes, enclosing, outer, object
- **Key terms/APIs that appear:** e.g, c.gvar, c.nvar, object.x, any, all, try, print, map

#### Attribute Names: Object Namespaces
- **Span:** PDF pp. 763–763 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, names, attribute, global, functions, assignment, local, scope, classes, enclosing, outer, object
- **Key terms/APIs that appear:** e.g, c.gvar, c.nvar, object.x, any, all, try, print, map

#### The “Zen” of Namespaces: Assignments Classify Names
- **Span:** PDF pp. 764–765 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** manynames, print, attribute, class, instance, module, local, function, method, names, object, inheritance
- **Key terms/APIs that appear:** print, all, i.x, manynames.py, manynames.x, c.x, self.x, i.m, import, a.k, manynames.f, manynames.c

#### Nested Classes: The LEGB Scopes Rule Revisited
- **Span:** PDF pp. 766–767 (2 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** enclosing, local, global, class, print, nested, scope, function, scopes, functions, nester, names
- **Key terms/APIs that appear:** print, i.method1, i.method2, any, funcscope.py, a.k, classscope1.py, classscope2.py, all, except

#### Namespace Dictionaries: Review
- **Span:** PDF pp. 768–769 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, instance, dict, namespace, dictionaries, print, attributes, local, attribute, dictionary, data1, enclosing
- **Key terms/APIs that appear:** print, x.__dict__, super, self.x, e.g, list, classscope3.py, c.x, i.x, i.method1, i.method2, self.data1

#### Namespace Links: A Tree Climber
- **Span:** PDF pp. 770–771 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, attributes, object, classtree, instance, tools, function, display, dict, attribute, inheritance, namespace
- **Key terms/APIs that appear:** dir, x.__dict__, classtree.py, print, __main__.selftest, list, import, x.data3, x.hello, cls.__name__, cls.__bases__, inst.__class__

### Documentation Strings Revisited
- **Span:** PDF pp. 772–772 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** docstr, klass, method, documentation, strings, module, docstrings, class, classes, print, docstring, string
- **Key terms/APIs that appear:** docstr.klass, docstr.__doc__, self.__doc__, self.method, docstr.func, klass.__doc__, klass.method, print, docstr.py, all, a.k, method.__doc__

### Classes Versus Modules
- **Span:** PDF pp. 773–773 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** klass, documentation, classes, modules, object, docstr, method, program, builtins, class, defined, comments
- **Key terms/APIs that appear:** builtins.object, klass.__doc__, docstr.klass, self.__doc__, klass.method, self.method, docstr.func, docstr.py, list, any, re

### Chapter Summary
- **Span:** PDF pp. 774–774 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, classes, superclass, method, statement, inheritance, methods, abstract, manually, modules, operator, overloading
- **Key terms/APIs that appear:** all, class.x, superclass.__init__, super

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 774–774 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, classes, superclass, method, statement, inheritance, methods, abstract, manually, modules, operator, overloading
- **Key terms/APIs that appear:** all, class.x, superclass.__init__, super

### Test Your Knowledge: Answers
- **Span:** PDF pp. 774–776 (3 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, superclass, method, classes, statement, manually, local, scope, subclass, modules, instance, inheritance
- **Key terms/APIs that appear:** all, super, class.x, superclass.__init__, superclass.method

## Chapter 30. Operator Overloading
- **Span:** PDF pp. 777–816 (40 pages; extended treatment)
- **Breakdown:**
  - The Basics
  - Indexing and Slicing: __getitem__ and __setitem__
  - Index Iteration: __getitem__
  - Iterable Objects: __iter__ and __next__
  - Membership: __contains__, __iter__, and __getitem__
  - Attribute Access: __getattr__ and __setattr__
  - String Representation: __repr__ and __str__
  - Right-Side and In-Place Ops: __radd__ and __iadd__
  - Call Expressions: __call__
  - Comparisons: __lt__, __gt__, and Others
  - Boolean Tests: __bool__ and __len__
  - Object Destruction: __del__
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 15 immediate subheadings; 25 leaf subsections underneath

### The Basics
- **Span:** PDF pp. 777–779 (3 pages; brief)
- **Breakdown:**
  - Constructors and Expressions: __init__ and __sub__
  - Common Operator-Overloading Methods
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Constructors and Expressions: __init__ and __sub__
- **Span:** PDF pp. 778–778 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** number, method, instance, class, overloading, operator, methods, built, start, classes, common, expressions
- **Key terms/APIs that appear:** self.data, ber.py, number.py, number.__init__, number.__sub__, y.data, e.g, any, import, all, list

#### Common Operator-Overloading Methods
- **Span:** PDF pp. 778–779 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** method, number, class, operator, overloading, instance, methods, object, built, creation, expressions, start
- **Key terms/APIs that appear:** any, x.any, x.attr, all, self.data, ber.py, number.py, number.__init__, number.__sub__, y.data, e.g, x.undefined

### Indexing and Slicing: __getitem__ and __setitem__
- **Span:** PDF pp. 780–782 (3 pages; brief)
- **Breakdown:**
  - Intercepting Slices
  - Intercepting Item Assignments
  - But __index__ Means As-Integer
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Intercepting Slices
- **Span:** PDF pp. 781–781 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** slice, getitem, slicing, indexing, index, object, called, none, list, passed, method, class
- **Key terms/APIs that appear:** list, self.data, math, print

#### Intercepting Item Assignments
- **Span:** PDF pp. 782–782 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** slice, index, none, getitem, setitem, slicing, object, print, assignment, start, class, indexer
- **Key terms/APIs that appear:** print, self.data, type, index.start, index.stop, index.step, x.data, any, isinstance, int

#### But __index__ Means As-Integer
- **Span:** PDF pp. 783–783 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., IndexError)
- **Key concepts (from text):** index, getitem, iteration, indexing, method, integer, class, lp255e, object, stepperindex, contexts, slicing
- **Key terms/APIs that appear:** self.data, range, time, any

### Index Iteration: __getitem__
- **Span:** PDF pp. 783–783 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., IndexError)
- **Key concepts (from text):** index, getitem, iteration, indexing, method, integer, class, lp255e, object, stepperindex, contexts, slicing
- **Key terms/APIs that appear:** self.data, range, time, any

### Iterable Objects: __iter__ and __next__
- **Span:** PDF pp. 784–793 (10 pages; detailed)
- **Breakdown:**
  - User-Defined Iterables
  - Multiple Iterators on One Object
  - Coding Alternative: __iter__ Plus yield
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### User-Defined Iterables
- **Span:** PDF pp. 785–786 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., IndexError, TypeError)
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** squares, iteration, object, class, iterable, state, getitem, calls, instance, defined, built, iterables
- **Key terms/APIs that appear:** all, self.value, list, map, self.stop, raise, squares.py, import, print, try, range, random

#### Multiple Iterators on One Object
- **Span:** PDF pp. 787–789 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** iterator, object, multiple, class, objects, active, wrapped, classes, iterable, state, print, built
- **Key terms/APIs that appear:** print, time, self.wrapped, tuple, list, self.offset, range, all, skipper.py, map, re, yield

#### Coding Alternative: __iter__ Plus yield
- **Span:** PDF pp. 790–793 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** generator, yield, squares, class, start, state, object, method, function, local, iteration, value
- **Key terms/APIs that appear:** yield, self.stop, import, self.start, print, self.value, self.wrapped, range, squares_yield.py, squares_yield.squares, g.__iter__, squares.__iter__

### Membership: __contains__, __iter__, and __getitem__
- **Span:** PDF pp. 794–796 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., IndexError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** contains, iteration, trace, getitem, membership, iters, method, methods, tests, slice, manual, print
- **Key terms/APIs that appear:** map, self.data, print, contains.py, self.ix, yield, list, all, len, time, import, test.ljust

### Attribute Access: __getattr__ and __setattr__
- **Span:** PDF pp. 797–799 (3 pages; brief)
- **Breakdown:**
  - Attribute Reference
  - Attribute Assignment and Deletion
  - Other Attribute-Management Tools
  - Emulating Privacy for Instance Attributes: Part 1
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Attribute Reference
- **Span:** PDF pp. 797–797 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError)
- **Key concepts (from text):** attribute, getattr, class, access, object, method, undefined, error, attrname, instance, attributes, value
- **Key terms/APIs that appear:** x.age, x.name, raise, a.k, object.attribute, self.undefined, x.__getattr__, try

#### Attribute Assignment and Deletion
- **Span:** PDF pp. 798–798 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError)
- **Key concepts (from text):** setattr, attribute, class, value, dict, assignments, loops, assignment, method, though, assigning, exception
- **Key terms/APIs that appear:** all, any, setattr, self.__dict__, self.name, x.age, super, self.attr, self.__setattr__, x.__setattr__, x.name, self.age

#### Other Attribute-Management Tools
- **Span:** PDF pp. 799–799 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., NameError)
- **Key concepts (from text):** attribute, class, tools, attributes, dict, setattr, instance, access, slots, getattr, methods, py
- **Key terms/APIs that appear:** self.__dict__, private0.py, all, property, list, raise, object.__setattr__, composite.py, self.attr, self.privates, dir, getattr

#### Emulating Privacy for Instance Attributes: Part 1
- **Span:** PDF pp. 799–799 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., NameError)
- **Key concepts (from text):** attribute, class, tools, attributes, dict, setattr, instance, access, slots, getattr, methods, py
- **Key terms/APIs that appear:** self.__dict__, private0.py, all, property, list, raise, object.__setattr__, composite.py, self.attr, self.privates, dir, getattr

### String Representation: __repr__ and __str__
- **Span:** PDF pp. 800–802 (3 pages; brief)
- **Breakdown:**
  - Why Two Display Methods?
  - Display Usage Notes
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Why Two Display Methods?
- **Span:** PDF pp. 801–801 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** str, display, print, string, displays, methods, addrepr, adder, object, representation, alternative, return
- **Key terms/APIs that appear:** print, str, __main__.adder, self.data, all, re, except

#### Display Usage Notes
- **Span:** PDF pp. 802–802 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** str, value, display, addboth, string, addstr, print, contexts, class, return, object, friendly
- **Key terms/APIs that appear:** print, str, self.data, all, __main__.addstr, e.g, try, raise

### Right-Side and In-Place Ops: __radd__ and __iadd__
- **Span:** PDF pp. 803–807 (5 pages; moderate detail)
- **Breakdown:**
  - Right-Side Addition
  - In-Place Addition
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Right-Side Addition
- **Span:** PDF pp. 804–807 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., NotImplementedError, TypeError)
- **Key concepts (from text):** commuter5, class, return, commuter, instance, right, object, print, commuter6, commuter1, py, classes
- **Key terms/APIs that appear:** self.val, type, print, commuter.py, isinstance, all, re, self.data, import, commuter.commuter1, i.e, self.__add__

#### In-Place Addition
- **Span:** PDF pp. 808–808 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - includes performance/efficiency notes
- **Key concepts (from text):** place, method, number, class, methods, though, return, overloading, addition, support, allows, changes
- **Key terms/APIs that appear:** self.val, x.val, y.val, e.g, type, all

### Call Expressions: __call__
- **Span:** PDF pp. 808–810 (3 pages; brief)
- **Breakdown:**
  - Function Interfaces and Callback-Based Code
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Function Interfaces and Callback-Based Code
- **Span:** PDF pp. 810–810 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** state, function, event, functions, class, color, information, callback, register, handlers, button, arguments
- **Key terms/APIs that appear:** self.color, x.comp, i.e, a.k, e.g, print

### Comparisons: __lt__, __gt__, and Others
- **Span:** PDF pp. 811–812 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., NotImplementedError)
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, methods, function, vetter, color, method, callback, class, return, instance, comparison, x10898f650
- **Key terms/APIs that appear:** __main__.vetter, self.data, print, lambda, self.color, cb1.changecolor, cb2.changecolor, e.g, other.data, all, list, sorted

### Boolean Tests: __bool__ and __len__
- **Span:** PDF pp. 813–813 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** truth, bool, object, true, false, length, boolean, class, return, means, methods, method
- **Key terms/APIs that appear:** print, bool, set, any

### Object Destruction: __del__
- **Span:** PDF pp. 814–814 (1 page; very brief)
- **Breakdown:**
  - Destructor Usage Notes
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Destructor Usage Notes
- **Span:** PDF pp. 814–814 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** instance, destructor, objects, reclaimed, print, destructors, close, method, automatically, space, object, class
- **Key terms/APIs that appear:** print, self.name, time, i.e, pat.live, sys.stderr, all, sys

### Chapter Summary
- **Span:** PDF pp. 815–815 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** methods, overloading, class, objects, operator, addition, statement, context, garbage, details, coverage, termination
- **Key terms/APIs that appear:** a.k, e.g, try, all, type, set

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 815–815 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** methods, overloading, class, objects, operator, addition, statement, context, garbage, details, coverage, termination
- **Key terms/APIs that appear:** a.k, e.g, try, all, type, set

### Test Your Knowledge: Answers
- **Span:** PDF pp. 816–816 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** str, method, object, called, print, iteration, getitem, methods, built, naturally, tries, first
- **Key terms/APIs that appear:** print, str, all, yield, except, type, map

## Chapter 31. Designing with Classes
- **Span:** PDF pp. 817–854 (38 pages; extended treatment)
- **Breakdown:**
  - Python and OOP
  - OOP and Inheritance: “Is-a” Relationships
  - OOP and Composition: “Has-a” Relationships
  - OOP and Delegation: “Like-a” Relationships
  - Pseudoprivate Class Attributes
  - Method Objects: Bound or Not
  - Classes Are Objects: Generic Object Factories
  - Multiple Inheritance and the MRO
  - Other Design-Related Topics
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 12 immediate subheadings; 17 leaf subsections underneath

### Python and OOP
- **Span:** PDF pp. 817–817 (1 page; very brief)
- **Breakdown:**
  - Polymorphism Means Interfaces, Not Call Signatures
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Polymorphism Means Interfaces, Not Call Signatures
- **Span:** PDF pp. 818–818 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** object, class, classes, types, inheritance, polymorphism, based, argument, method, useful, interface, interfaces
- **Key terms/APIs that appear:** type, set, x.operation, i.e, re, try, list, len, int, isinstance, any, super

### OOP and Inheritance: “Is-a” Relationships
- **Span:** PDF pp. 818–819 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, employee, object, salary, print, classes, robot, specific, inheritance, pizza, types, method
- **Key terms/APIs that appear:** print, type, self.name, self.salary, employees.py, employee.__init__, set, x.operation, i.e, self.__class__, chef.__init__, pat.work

### OOP and Composition: “Has-a” Relationships
- **Span:** PDF pp. 820–823 (4 pages; moderate detail)
- **Breakdown:**
  - Stream Processors Revisited
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Stream Processors Revisited
- **Span:** PDF pp. 822–823 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, uppercase, converter, writer, processor, reader, process, converters, objects, classes, stream, composition
- **Key terms/APIs that appear:** trihack.txt, import, open, converters.py, e.g, streams.py, self.reader, self.writer, trihackup.txt, re, sys, reader.read

### OOP and Delegation: “Like-a” Relationships
- **Span:** PDF pp. 824–825 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** object, class, wrapper, method, wrapped, classes, getattr, trace, delegation, composition, interface, attribute
- **Key terms/APIs that appear:** all, pickle, import, getattr, list, shop.chef, shopfile.pkl, trace.py, self.wrapped, x.n, open, print

### Pseudoprivate Class Attributes
- **Span:** PDF pp. 826–828 (3 pages; brief)
- **Breakdown:**
  - Name Mangling Overview
  - Why Use Pseudoprivate Attributes?
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Name Mangling Overview
- **Span:** PDF pp. 827–827 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **Key concepts (from text):** class, instance, attribute, names, attributes, mangling, classes, method, enclosing, named, single, pseudoprivate
- **Key terms/APIs that appear:** self.x, all, print, self.__x, self._hack__x, e.g, self.attr, i.x, any, set

#### Why Use Pseudoprivate Attributes?
- **Span:** PDF pp. 827–828 (2 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, names, instance, method, classes, attributes, attribute, pseudoprivate, mangling, expanded, print, underscores
- **Key terms/APIs that appear:** self.x, self.__x, print, pseudoprivate.py, any, super, e.g, all, set, self._hack__x, self.attr, i.x

### Method Objects: Bound or Not
- **Span:** PDF pp. 829–832 (4 pages; moderate detail)
- **Breakdown:**
  - Bound Methods in Action
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Bound Methods in Action
- **Span:** PDF pp. 830–832 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** method, instance, bound, function, class, methods, object, though, functions, handler, argument, simple
- **Key terms/APIs that appear:** hack.doit, print, inst.doit, self.base, all, lambda, __main__.hack, hack3.doit3, x.double, self.handler, time, list

### Classes Are Objects: Generic Object Factories
- **Span:** PDF pp. 833–833 (1 page; very brief)
- **Breakdown:**
  - Why Factories?
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Why Factories?
- **Span:** PDF pp. 834–834 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, objects, classes, factory, classarg, aclass, though, instance, reader, streams, stream, dynamic
- **Key terms/APIs that appear:** time, getattr, obj.attr, all, import

### Multiple Inheritance and the MRO
- **Span:** PDF pp. 834–852 (19 pages; deep dive)
- **Breakdown:**
  - How Multiple Inheritance Works
  - How the MRO Works
  - Attribute Conflict Resolution
  - Example: “Mix-in” Attribute Listers
  - Example: Mapping Attributes to Inheritance Sources
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### How Multiple Inheritance Works
- **Span:** PDF pp. 835–836 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, inheritance, multiple, attr2, classes, attr1, order, superclass, right, attributes, attribute, search
- **Key terms/APIs that appear:** all, i.attr1, i.attr2, set, re, type

#### How the MRO Works
- **Span:** PDF pp. 837–838 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, object, classes, mro_diamond, inheritance, order, built, print, search, list, first, diamonds
- **Key terms/APIs that appear:** all, c.__name__, print, list, a.__mro__, mro_diamond.b, mro_diamond.c, x.attr, c.__mro__, mro_diamond.a, mro_diamond.d, import

#### Attribute Conflict Resolution
- **Span:** PDF pp. 839–839 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, inheritance, default, method, attribute, branch, search, conflict, multiple, right, attributes, choice
- **Key terms/APIs that appear:** e.g, any, self.attr, superclass.attr, b.attr, c.attr, self.method, b.method, c.method, super

#### Example: “Mix-in” Attribute Listers
- **Span:** PDF pp. 840–848 (9 pages; detailed)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, instance, classes, attributes, inheritance, str, object, listtree, methods, display, module, dict
- **Key terms/APIs that appear:** all, print, dir, import, super, getattr, self.__dict__, testmixin.tester, testmixin.py, set, re, str

#### Example: Mapping Attributes to Inheritance Sources
- **Span:** PDF pp. 849–852 (4 pages; moderate detail)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, instance, attributes, dict, inheritance, mapattrs, tester, testmixin, object, locals, classes, attribute
- **Key terms/APIs that appear:** testmixin.tester, __main__.a, dir, all, dict, print, __main__.d, import, super, mapattrs.py, pprint.pformat, instance.__class__

### Other Design-Related Topics
- **Span:** PDF pp. 853–853 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** design, classes, related, topics, patterns, though, chapters, methods, attributes, inheritance, studied, combine
- **Key terms/APIs that appear:** type, any

### Chapter Summary
- **Span:** PDF pp. 853–853 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **Key concepts (from text):** design, classes, related, topics, patterns, though, chapters, methods, attributes, inheritance, studied, combine
- **Key terms/APIs that appear:** type, any

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 853–853 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** design, classes, related, topics, patterns, though, chapters, methods, attributes, inheritance, studied, combine
- **Key terms/APIs that appear:** type, any

### Test Your Knowledge: Answers
- **Span:** PDF pp. 854–854 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** class, object, instance, multiple, inheritance, common, classes, attributes, order, methods, names, statement
- **Key terms/APIs that appear:** all, e.g, super

## Chapter 32. Class Odds and Ends
- **Span:** PDF pp. 855–910 (56 pages; extended treatment)
- **Breakdown:**
  - Extending Built-in Object Types
  - The Python Object Model
  - Advanced Attribute Tools
  - Static and Class Methods
  - Decorators and Metaclasses
  - The super Function
  - Class Gotchas
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
  - Test Your Knowledge: Part VI Exercises
- **Granularity:** 11 immediate subheadings; 33 leaf subsections underneath

### Extending Built-in Object Types
- **Span:** PDF pp. 855–858 (4 pages; moderate detail)
- **Breakdown:**
  - Extending Types by Embedding
  - Extending Types by Subclassing
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Extending Types by Embedding
- **Span:** PDF pp. 856–856 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** set, return, class, value, functions, list, setwrapper, append, union, inheritance, types, py
- **Key terms/APIs that appear:** set, self.data, list, setwrapper.py, res.append, any, len, self.concat, self.intersect, self.union, x.union, type

#### Extending Types by Subclassing
- **Span:** PDF pp. 857–858 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** list, set, built, print, class, indexing, return, types, behavior, subclass, py, mylist
- **Key terms/APIs that appear:** list, set, print, type, setsubclass.py, typesubclass.py, x.reverse, map, all, any, e.g, list.__getitem__

### The Python Object Model
- **Span:** PDF pp. 859–863 (5 pages; moderate detail)
- **Breakdown:**
  - Classes Are Types Are Classes
  - Some Instances Are More Equal Than Others
  - The Inheritance Bifurcation
  - The Metaclass/Class Dichotomy
  - And One “object” to Rule Them All
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Classes Are Types Are Classes
- **Span:** PDF pp. 859–859 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, classes, object, built, instances, types, defined, set, str, list, operations, model
- **Key terms/APIs that appear:** type, set, str, list, all, isinstance, a.k, __main__.hack, i.__class__, hack.__class__, str.__class__, re

#### Some Instances Are More Equal Than Others
- **Span:** PDF pp. 860–860 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, classes, instances, built, defined, metaclass, created, types, object, instance, different, true
- **Key terms/APIs that appear:** type, str, isinstance

#### The Inheritance Bifurcation
- **Span:** PDF pp. 861–861 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, inheritance, classes, nonclass, instances, bases, instance, object, searches, though, search, different
- **Key terms/APIs that appear:** type, __main__.c, isinstance, i.__class__, c.__class__, all, a.k, c.__bases__

#### The Metaclass/Class Dichotomy
- **Span:** PDF pp. 862–862 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, dict, object, classes, bases, inheritance, instances, metaclass, trees, inherited, instance, searched
- **Key terms/APIs that appear:** type, __main__.c, c.__class__, x.__dict__, i.__class__, c.__mro__, i.__dict__, i.e, c.__dict__, c.__bases__, i.__bases__, a.k

#### And One “object” to Rule Them All
- **Span:** PDF pp. 863–863 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** object, class, true, bases, classes, inherits, though, isinstance, method, roles, later, topic
- **Key terms/APIs that appear:** type, isinstance, all, dir, i.e, c.__bases__, d.__bases__, type.__bases__, object.__bases__, x.__repr__, object.__setattr__, await

### Advanced Attribute Tools
- **Span:** PDF pp. 864–874 (11 pages; detailed)
- **Breakdown:**
  - Slots: Attribute Declarations
  - Properties: Attribute Accessors
  - __getattribute__ and Descriptors: Attribute Implementations
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Slots: Attribute Declarations
- **Span:** PDF pp. 864–871 (8 pages; detailed)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError, TypeError, ValueError)
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** slots, class, instance, attributes, attribute, dict, tools, names, getattr, instances, print, listtree
- **Key terms/APIs that appear:** getattr, all, print, i.a, i.b, any, dir, list, i.__dict__, i.c, i.age, setattr

#### Properties: Attribute Accessors
- **Span:** PDF pp. 872–873 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** attribute, properties, class, property, slots, attributes, getage, getattr, method, set, methods, object
- **Key terms/APIs that appear:** property, set, x.age, e.g, x.name, x.job, type, print, test.py, obj.name, self._age, x._age

#### __getattribute__ and Descriptors: Attribute Implementations
- **Span:** PDF pp. 874–874 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** getattr, setattr, value, attribute, class, properties, set, coder, generic, references, withoperators, undefined
- **Key terms/APIs that appear:** set, self.__dict__, x.age, x.job, instance.age, print, all, object.__setattr__, x._age, e.g, age.setter, raise

### Static and Class Methods
- **Span:** PDF pp. 875–882 (8 pages; detailed)
- **Breakdown:**
  - Why the Special Methods?
  - Plain-Function Methods
  - Static Method Alternatives
  - Using Static and Class Methods
  - Counting Instances with Static Methods
  - Counting Instances with Class Methods
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Why the Special Methods?
- **Span:** PDF pp. 875–875 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, methods, instance, instances, descriptors, agedesc, properties, special, static, called, method, attribute
- **Key terms/APIs that appear:** x.age, re, type, staticmethod, instance._age, agedesc.__get__, agedesc.__set__, x._age, e.g, classmethod, list, all

#### Plain-Function Methods
- **Span:** PDF pp. 876–876 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, instance, methods, instances, called, access, plain, method, functions, argument, counter, stored
- **Key terms/APIs that appear:** all, hack1.py, hack.numinstances, any, re, time, print

#### Static Method Alternatives
- **Span:** PDF pp. 877–877 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** class, methods, instance, printnuminstances, instances, functions, function, method, static, numinstances, number, created
- **Key terms/APIs that appear:** hack.hack, hack.printnuminstances, hack.numinstances, import, a.printnuminstances, hack2.py, re, print, any

#### Using Static and Class Methods
- **Span:** PDF pp. 878–878 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** instance, class, methods, method, object, static, passed, smeth, cmeth, simply, requiring, allmethods
- **Key terms/APIs that appear:** staticmethod, classmethod, print, allmethods.py, any, a.k, obj.imeth, allmethods.methods, try, all, import

#### Counting Instances with Static Methods
- **Span:** PDF pp. 879–879 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, methods, instance, method, static, printnuminstances, called, staticmethod, passed, cmeth, instances, allmethods
- **Key terms/APIs that appear:** staticmethod, allmethods.methods, hack.numinstances, methods.imeth, methods.smeth, obj.smeth, methods.cmeth, obj.cmeth, hack_static.py, hack.printnuminstances, a.printnuminstances, type

#### Counting Instances with Class Methods
- **Span:** PDF pp. 880–882 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, printnuminstances, method, instance, numinstances, instances, methods, number, static, hack_class2, subclass, count
- **Key terms/APIs that appear:** hack.printnuminstances, classmethod, print, hack.numinstances, cls.numinstances, hack_class2.hack, import, a.printnuminstances, sub.printnuminstances, hack_class2.sub, all, c.printnuminstances

### Decorators and Metaclasses
- **Span:** PDF pp. 883–888 (6 pages; moderate detail)
- **Breakdown:**
  - Function Decorator Basics
  - A First Look at User-Defined Function Decorators
  - A First Look at Class Decorators and Metaclasses
  - For More Details
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Function Decorator Basics
- **Span:** PDF pp. 883–884 (2 pages; brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, decorators, class, decorator, classes, functions, later, method, staticmethod, calls, syntax, logic
- **Key terms/APIs that appear:** staticmethod, classmethod, print, hack.numinstances, property, any, hack_static_deco.py, hack.printnuminstances, a.printnuminstances, alldecorators.py, time, list

#### A First Look at User-Defined Function Decorators
- **Span:** PDF pp. 885–885 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, calls, function, methods, decorators, print, return, tracer, alldecorators, object, functions, defined
- **Key terms/APIs that appear:** print, self.calls, self.func, alldecorators.methods, property, self.__class__, obj.imeth, obj.smeth, obj.cmeth, obj.name, tracer1.py, import

#### A First Look at Class Decorators and Metaclasses
- **Span:** PDF pp. 886–887 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, decorator, function, return, decorators, later, count, calls, tracer, instance, oncall, aclass
- **Key terms/APIs that appear:** any, oncall.calls, print, x.hack, hack.numinstances, self.wrapped, tracer1.py, tracer2.py, func.__name__, aclass.numinstances, x.attr, set

#### For More Details
- **Span:** PDF pp. 888–888 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, metaclass, metaclasses, decorators, creation, object, decorator, advanced, classname, defined, instance, earlier
- **Key terms/APIs that appear:** type, time, all

### The super Function
- **Span:** PDF pp. 889–897 (9 pages; detailed)
- **Breakdown:**
  - The super Basics
  - The super Details
  - The super Wrap-Up
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### The super Basics
- **Span:** PDF pp. 889–889 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** super, class, superclass, method, function, explicitly, multiple, inheritance, alternative, reference, attributes, implicitly
- **Key terms/APIs that appear:** super, print, c.act, i.act, class.method, all

#### The super Details
- **Span:** PDF pp. 890–896 (7 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError, RuntimeError, TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, super, method, superclass, explicit, instance, object, calls, print, proxy, methods, though
- **Key terms/APIs that appear:** super, print, all, list, i.act, __class__.__bases__, __main__.c, c.attr2, any, prx.act, e.__mro__, __main__.e

#### The super Wrap-Up
- **Span:** PDF pp. 897–897 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** super, method, inheritance, trees, index, built, class, multiple, dispatch, especially, superclass, single
- **Key terms/APIs that appear:** super, all, yield

### Class Gotchas
- **Span:** PDF pp. 898–902 (5 pages; moderate detail)
- **Breakdown:**
  - Changing Class Attributes Can Have Side Effects
  - Changing Mutable Class Attributes Can Have Side Effects, Too
  - Multiple Inheritance: Order Matters
  - Scopes in Methods and Classes
  - Miscellaneous Class Gotchas
  - “Overwrapping-itis”
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Changing Class Attributes Can Have Side Effects
- **Span:** PDF pp. 898–898 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, instances, change, attribute, attributes, object, changes, changing, especially, general, references, program
- **Key terms/APIs that appear:** all, x.a, any, i.a, j.a, super, set

#### Changing Mutable Class Attributes Can Have Side Effects, Too
- **Span:** PDF pp. 899–899 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - calls out caveats and edge cases
- **Key concepts (from text):** class, shared, attributes, instances, object, mutable, perobj, changing, attribute, instance, variables, classes
- **Key terms/APIs that appear:** all, x.a, x.b, x.c, y.a, x.i, y.shared, y.perobj, x.shared, x.perobj, any, x.name

#### Multiple Inheritance: Order Matters
- **Span:** PDF pp. 900–900 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, super, listtree, str, inheritance, shared, attributes, order, header, searches, first, instance
- **Key terms/APIs that appear:** super, x.shared, list, tkinter.button, super.other, all, time

#### Scopes in Methods and Classes
- **Span:** PDF pp. 901–901 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, method, classes, local, listtree, nested, function, scope, scopes, generate, enclosing, count
- **Key terms/APIs that appear:** super, sub.other, listtree.__str__, hack.count, super.other, listtree.other, self.count, any, print, all

#### Miscellaneous Class Gotchas
- **Span:** PDF pp. 902–902 (1 page; very brief)
- **Focus:** common pitfalls and edge cases
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, method, instance, scope, methods, constructor, generate, count, enclosing, superclass, module, classes
- **Key terms/APIs that appear:** all, hack.count, print, super, i.method, e.g

#### “Overwrapping-itis”
- **Span:** PDF pp. 903–903 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** classes, class, understand, decorators, though, abstraction, point, making, deeply, system, multiple, related
- **Key terms/APIs that appear:** super, time, all, type

### Chapter Summary
- **Span:** PDF pp. 903–903 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** classes, class, understand, decorators, though, abstraction, point, making, deeply, system, multiple, related
- **Key terms/APIs that appear:** super, time, all, type

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 903–903 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** classes, class, understand, decorators, though, abstraction, point, making, deeply, system, multiple, related
- **Key terms/APIs that appear:** super, time, all, type

### Test Your Knowledge: Answers
- **Span:** PDF pp. 904–904 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, method, function, static, methods, instance, called, built, classes, functions, tools, inheritance
- **Key terms/APIs that appear:** type, any, time, super, set, list

### Test Your Knowledge: Part VI Exercises
- **Span:** PDF pp. 904–910 (7 pages; moderate detail)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, method, instance, methods, list, classes, called, employee, customer, object, mylist, calls
- **Key terms/APIs that appear:** list, e.g, type, print, all, self.data, i.e, any, set, try, x.add, x.data

# Part VII. Exceptions
- **Span:** PDF pp. 911–984 (74 pages; extended treatment)
- **Breakdown:**
  - Chapter 33. Exception Basics
  - Chapter 34. Exception Coding Details
  - Chapter 35. Exception Objects
  - Chapter 36. Exception Odds and Ends
- **Granularity:** 4 immediate subheadings; 56 leaf subsections underneath

## Chapter 33. Exception Basics
- **Span:** PDF pp. 913–922 (10 pages; detailed)
- **Breakdown:**
  - Why Use Exceptions?
  - Exceptions: The Short Story
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 5 immediate subheadings; 9 leaf subsections underneath

### Why Use Exceptions?
- **Span:** PDF pp. 913–914 (2 pages; brief)
- **Breakdown:**
  - Exception Roles
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Exception Roles
- **Span:** PDF pp. 914–914 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** exception, exceptions, statement, program, handler, marker, error, handling, programs, respond, raised, instance
- **Key terms/APIs that appear:** try, all, any, raise, time

### Exceptions: The Short Story
- **Span:** PDF pp. 915–919 (5 pages; moderate detail)
- **Breakdown:**
  - Default Exception Handler
  - Catching Exceptions
  - Raising Exceptions
  - User-Defined Exceptions
  - Termination Actions
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Default Exception Handler
- **Span:** PDF pp. 915–915 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception, IndexError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** exception, index, backtracking, exceptions, function, simply, fetcher, default, handler, console, stdin, standard
- **Key terms/APIs that appear:** try, any, open, raise, range, list, all, re, input

#### Catching Exceptions
- **Span:** PDF pp. 916–916 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception, IndexError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** exception, program, error, fetcher, exceptions, handler, message, catch, except, block, pyshell, default
- **Key terms/APIs that appear:** try, except, print, range, time

#### Raising Exceptions
- **Span:** PDF pp. 917–917 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., IndexError)
- **Key concepts (from text):** exception, exceptions, caught, except, indexerror, raise, point, global, trigger, triggered, short, statement
- **Key terms/APIs that appear:** try, except, raise, any, print, time, l.append, all, re, type

#### User-Defined Exceptions
- **Span:** PDF pp. 918–918 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AssertionError, Exception, IndexError)
- **Key concepts (from text):** exception, raise, exceptions, combust, class, defined, indexerror, traceback, recent, stdin, module, built
- **Key terms/APIs that appear:** raise, re, except, try, print

#### Termination Actions
- **Span:** PDF pp. 919–919 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., IndexError)
  - calls out caveats and edge cases
- **Key concepts (from text):** finally, exception, print, fetch, fetcher, block, termination, actions, program, function, stdin, blocks
- **Key terms/APIs that appear:** try, print, except, range

### Chapter Summary
- **Span:** PDF pp. 920–920 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception)
- **Key concepts (from text):** exceptions, finally, exception, except, clauses, termination, actions, regardless, statement, statements, occur, raised
- **Key terms/APIs that appear:** try, except, any, pizzarobot.txt, file.write, import, open, raise

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 921–921 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
- **Key concepts (from text):** exception, processing, actions, error, program, knowledge, termination, block, special, script, recover, trigger
- **Key terms/APIs that appear:** try, raise, time, all, filter, any, except

### Test Your Knowledge: Answers
- **Span:** PDF pp. 921–922 (2 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
  - includes performance/efficiency notes
- **Key concepts (from text):** exception, error, program, exceptions, errors, processing, actions, return, dostuff, knowledge, termination, operation
- **Key terms/APIs that appear:** all, try, except, raise, time, filter, any

## Chapter 34. Exception Coding Details
- **Span:** PDF pp. 923–948 (26 pages; deep dive)
- **Breakdown:**
  - The try Statement
  - The raise Statement
  - The assert Statement
  - The with Statement and Context Managers
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 7 immediate subheadings; 17 leaf subsections underneath

### The try Statement
- **Span:** PDF pp. 923–935 (13 pages; detailed)
- **Breakdown:**
  - try Statement Clauses
  - The except and else Clauses
  - The finally Clause
  - Combined try Clauses
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### try Statement Clauses
- **Span:** PDF pp. 923–923 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception)
- **Key concepts (from text):** clauses, statement, except, exception, statements, exceptions, details, syntax, first, handlers, finally, separate
- **Key terms/APIs that appear:** try, except, all, re, raise

#### The except and else Clauses
- **Span:** PDF pp. 924–929 (6 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError, Exception, IndexError, NameError, SyntaxError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** exception, except, exceptions, block, statements, statement, catch, raised, clauses, clause, program, crashware
- **Key terms/APIs that appear:** try, except, all, crashware.py, any, tuple, print, i.e, kaboom.py, raise, re, list

#### The finally Clause
- **Span:** PDF pp. 930–931 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception, MyError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** exception, finally, block, statement, except, clause, py, actions, function, program, raises, closer
- **Key terms/APIs that appear:** try, except, closer.py, raise, open, kaboom.py, i.e, a.k, file.write, temp.txt, file.close, e.g

#### Combined try Clauses
- **Span:** PDF pp. 932–935 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception, IndexError, ZeroDivisionError)
- **Key concepts (from text):** finally, except, exception, print, statement, block, raised, statements, exceptions, combined, action, regardless
- **Key terms/APIs that appear:** except, try, print, all, trycombos.py, any, raise, type, time

### The raise Statement
- **Span:** PDF pp. 936–939 (4 pages; moderate detail)
- **Breakdown:**
  - Raising Exceptions
  - The except as hook
  - Scopes and except as
  - Propagating Exceptions with raise
  - Exception Chaining: raise from
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Raising Exceptions
- **Span:** PDF pp. 936–936 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception, IndexError, TypeError)
- **Key concepts (from text):** raise, instance, class, exceptions, raised, exception, indexerror, statement, classes, created, create, except
- **Key terms/APIs that appear:** raise, try, except, time, any

#### The except as hook
- **Span:** PDF pp. 936–936 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception, IndexError, TypeError)
- **Key concepts (from text):** raise, instance, class, exceptions, raised, exception, indexerror, statement, classes, created, create, except
- **Key terms/APIs that appear:** raise, try, except, time, any

#### Scopes and except as
- **Span:** PDF pp. 937–937 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception, NameError)
- **Key concepts (from text):** except, exception, instance, class, variable, handler, though, block, available, myexc, raise, print
- **Key terms/APIs that appear:** except, try, raise, print, any, x.args, time, re

#### Propagating Exceptions with raise
- **Span:** PDF pp. 938–938 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception, IndexError, NameError, TypeError, ZeroDivisionError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** exception, raise, exceptions, except, statement, propagating, handler, indexerror, error, nameerror, defined, reference
- **Key terms/APIs that appear:** raise, try, except, print, list

#### Exception Chaining: raise from
- **Span:** PDF pp. 938–939 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception, IndexError, NameError, SyntaxError, TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** exception, raise, exceptions, recent, traceback, stdin, module, except, error, indexerror, statement, division
- **Key terms/APIs that appear:** raise, try, except, print, list, all

### The assert Statement
- **Span:** PDF pp. 940–941 (2 pages; brief)
- **Breakdown:**
  - Example: Trapping Constraints (but Not Errors!)
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Example: Trapping Constraints (but Not Errors!)
- **Span:** PDF pp. 941–941 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AssertionError)
- **Key concepts (from text):** assert, asserter, errors, py, module, function, error, negative, running, trapping, constraints, message
- **Key terms/APIs that appear:** asserter.py, asserter.f, import, file.py, type

### The with Statement and Context Managers
- **Span:** PDF pp. 942–946 (5 pages; moderate detail)
- **Breakdown:**
  - Basic with Usage
  - The Context-Management Protocol
  - Multiple Context Managers
  - The Termination-Handlers Shoot-Out
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Basic with Usage
- **Span:** PDF pp. 942–942 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** statement, block, context, protocol, tools, exception, objects, managers, automatically, expression, variable, object
- **Key terms/APIs that appear:** try, somefile.txt, time, async, await, open, print

#### The Context-Management Protocol
- **Span:** PDF pp. 943–944 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception, TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** context, statement, block, exception, print, decimal, myfile, managers, manager, management, automatically, value
- **Key terms/APIs that appear:** print, open, try, decimal.decimal, withas.py, action.message, type, raise, any, somefile.txt, myfile.close, threading.lock

#### Multiple Context Managers
- **Span:** PDF pp. 945–945 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** context, statement, block, managers, manager, method, exception, return, effect, coding, module, entry
- **Key terms/APIs that appear:** withas.py, open, input, lines.txt, matches.txt, output.write, raise, try, time, any

#### The Termination-Handlers Shoot-Out
- **Span:** PDF pp. 946–946 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** files, close, exception, file1, file2, print, context, following, lines, lines1, lines2, line1
- **Key terms/APIs that appear:** open, print, lines1.txt, lines2.txt, zip, all, enumerate, line1.lower, line2.lower, input, any, filter

### Chapter Summary
- **Span:** PDF pp. 947–947 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** output, input, close, exceptions, uppers, files, exception, lines1, write, upper, finally, statements
- **Key terms/APIs that appear:** open, input, uppers.txt, try, lines1.txt, output.write, line.upper, raise, input.close, output.close, print, all

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 948–948 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., AssertionError, Exception)
- **Key concepts (from text):** statement, exceptions, finally, exception, raise, except, designed, block, raised, actions, raises, knowledge
- **Key terms/APIs that appear:** try, raise, except

### Test Your Knowledge: Answers
- **Span:** PDF pp. 948–948 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., AssertionError, Exception)
- **Key concepts (from text):** statement, exceptions, finally, exception, raise, except, designed, block, raised, actions, raises, knowledge
- **Key terms/APIs that appear:** try, raise, except

## Chapter 35. Exception Objects
- **Span:** PDF pp. 949–964 (16 pages; deep dive)
- **Breakdown:**
  - Exception Classes
  - Built-in Exception Classes
  - Custom Print Displays
  - Custom State and Behavior
  - Exception Groups: Yet Another Star!
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 8 immediate subheadings; 11 leaf subsections underneath

### Exception Classes
- **Span:** PDF pp. 950–953 (4 pages; moderate detail)
- **Breakdown:**
  - Coding Exceptions Classes
  - Why Exception Hierarchies?
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Coding Exceptions Classes
- **Span:** PDF pp. 950–951 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
- **Key concepts (from text):** exception, class, general, raise, exceptions, instance, classes, superclass, except, category, subclasses, specific1
- **Key terms/APIs that appear:** raise, except, try, all, any, sys, categoric.py, sys.exc_info, type, __main__.general, __main__.specific1, __main__.specific2

#### Why Exception Hierarchies?
- **Span:** PDF pp. 952–953 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
  - calls out caveats and edge cases
- **Key concepts (from text):** exception, library, exceptions, class, except, mathlib, catch, tuple, py, divzero, instance, hierarchies
- **Key terms/APIs that appear:** except, try, all, tuple, raise, sys.exc_info, client.py, mathlib.func, sys, any, time, mathlib.py

### Built-in Exception Classes
- **Span:** PDF pp. 954–956 (3 pages; brief)
- **Breakdown:**
  - Built-in Exception Categories
  - Default Printing and State
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Built-in Exception Categories
- **Span:** PDF pp. 955–955 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., ArithmeticError, Exception, FileNotFoundError, FloatingPointError, IndexError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** exception, exceptions, built, errors, superclass, class, except, specific, subclass, system, classes, numeric
- **Key terms/APIs that appear:** all, except, try, e.g, time, tuple, set, any, type

#### Default Printing and State
- **Span:** PDF pp. 956–956 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception, IndexError)
- **Key concepts (from text):** stuff, indexerror, built, arguments, exception, print, classes, constructor, instance, printed, raise, traceback
- **Key terms/APIs that appear:** print, raise, tuple, i.args, any, time, str

### Custom Print Displays
- **Span:** PDF pp. 957–957 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception)
- **Key concepts (from text):** display, exception, print, mybad, raise, stuff, str, class, sorry, mistake, constructor, displays
- **Key terms/APIs that appear:** print, try, raise, except, x.args, tuple, str

### Custom State and Behavior
- **Span:** PDF pp. 958–960 (3 pages; brief)
- **Breakdown:**
  - Providing Exception Details
  - Providing Exception Methods
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Providing Exception Details
- **Span:** PDF pp. 959–959 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception, FormatError)
- **Key concepts (from text):** exception, state, instance, formaterror, extra, error, custom, py, raised, statement, access, class
- **Key terms/APIs that appear:** try, code.py, except, raise, x.args, print, sys.exc_info, self.line, self.file, x.file, x.line, parsely.py

#### Providing Exception Methods
- **Span:** PDF pp. 959–960 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., CustomFormatError, Exception, FormatError)
- **Key concepts (from text):** exception, formaterror, py, state, error, class, instance, parser, except, raised, extra, custom
- **Key terms/APIs that appear:** try, code.py, except, raise, parsely.py, self.line, self.file, print, sys.exc_info, x.args, errors.txt, exc.logerror

### Exception Groups: Yet Another Star!
- **Span:** PDF pp. 961–962 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception, IndexError, LookupError, SyntaxError, TypeError)
- **Key concepts (from text):** except, indexerror, exception, exceptions, group, typeerror, print, clause, syntaxerror, raise, clauses, exceptiongroup
- **Key terms/APIs that appear:** except, try, print, raise, e.exceptions, all, any, sys.exc_info, sys, tuple, type

### Chapter Summary
- **Span:** PDF pp. 963–963 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception, IndexError, SyntaxError)
- **Key concepts (from text):** exceptions, exception, except, indexerror, class, group, print, groups, catch, raise, syntaxerror, process
- **Key terms/APIs that appear:** except, try, print, e.exceptions, raise, type, all, set

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 964–964 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception)
- **Key concepts (from text):** exception, exceptions, except, class, raised, built, superclasses, objects, handlers, instance, categories, knowledge
- **Key terms/APIs that appear:** except, try, any, tuple, list, print, str

### Test Your Knowledge: Answers
- **Span:** PDF pp. 964–964 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception)
- **Key concepts (from text):** exception, exceptions, except, class, raised, built, superclasses, objects, handlers, instance, categories, knowledge
- **Key terms/APIs that appear:** except, try, any, tuple, list, print, str

## Chapter 36. Exception Odds and Ends
- **Span:** PDF pp. 965–984 (20 pages; deep dive)
- **Breakdown:**
  - Nesting Exception Handlers
  - Exception Idioms
  - Exception Design Tips and Gotchas
  - Core Language Wrap-Up
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
  - Test Your Knowledge: Part VII Exercises
- **Granularity:** 8 immediate subheadings; 19 leaf subsections underneath

### Nesting Exception Handlers
- **Span:** PDF pp. 965–968 (4 pages; moderate detail)
- **Breakdown:**
  - Example: Control-Flow Nesting
  - Example: Syntactic Nesting
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Example: Control-Flow Nesting
- **Span:** PDF pp. 966–967 (2 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception, IndexError, SyntaxError, TypeError)
- **Key concepts (from text):** exception, action2, except, action1, typeerror, action3, finally, control, matching, handler, clauses, print
- **Key terms/APIs that appear:** try, except, print, raise, nested_exc_normal.py, all, i.e, nested_exc_group.py, time

#### Example: Syntactic Nesting
- **Span:** PDF pp. 968–968 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception, SyntaxError, TypeError)
- **Key concepts (from text):** exception, nested, print, inner, outer, exceptions, handler, recent, runtime, handlers, syntactically, nesting
- **Key terms/APIs that appear:** try, print, except, nested_exc_group.py, import, raise, all, type, int, list

### Exception Idioms
- **Span:** PDF pp. 969–975 (7 pages; moderate detail)
- **Breakdown:**
  - Breaking Out of Multiple Nested Loops: “go to”
  - Exceptions Aren’t Always Errors
  - Functions Can Signal Conditions with raise
  - Closing Files and Server Connections
  - Debugging with Outer try Statements
  - Running In-Process Tests
  - More on sys.exc_info
  - Displaying Errors and Tracebacks
- **Granularity:** 8 immediate subheadings; 8 leaf subsections underneath

#### Breaking Out of Multiple Nested Loops: “go to”
- **Span:** PDF pp. 969–969 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception, IndexError, SyntaxError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** finally, except, exception, indexerror, print, nested, syntactic, nesting, raise1, noraise, raise2, roles
- **Key terms/APIs that appear:** except, print, try, finally.py, raise, func.__name__, time, set

#### Exceptions Aren’t Always Errors
- **Span:** PDF pp. 970–970 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., EOFError, Exception)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** raise, print, break, loop3, exception, exceptions, except, exits, level, exitloop, variable, errors
- **Key terms/APIs that appear:** raise, print, try, except, breaker.py, all, input, sys.stdin, range, type, any, sys

#### Functions Can Signal Conditions with raise
- **Span:** PDF pp. 971–971 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., EOFError, Exception)
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** return, exception, signal, exceptions, raise, found, failure, value, searcher, success, function, empty
- **Key terms/APIs that appear:** raise, try, input, except, any, sys.exit, sys, set, all

#### Closing Files and Server Connections
- **Span:** PDF pp. 972–972 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** exception, myfile, program, files, exc_info, except, close, termination, uncaught, exceptions, connections, processing
- **Key terms/APIs that appear:** try, sys, sys.exc_info, except, open, any, myfile.close, input, tuple, all, import, print

#### Debugging with Outer try Statements
- **Span:** PDF pp. 972–972 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** exception, myfile, program, files, exc_info, except, close, termination, uncaught, exceptions, connections, processing
- **Key terms/APIs that appear:** try, sys, sys.exc_info, except, open, any, myfile.close, input, tuple, all, import, print

#### Running In-Process Tests
- **Span:** PDF pp. 973–973 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** exception, exc_info, testing, tests, except, programs, program, allows, driver, testname, testdriver, tools
- **Key terms/APIs that appear:** sys, sys.exc_info, except, try, import, print, any, os, i.e, os.system, os.popen, open

#### More on sys.exc_info
- **Span:** PDF pp. 973–974 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., Exception)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** exception, exc_info, instance, except, class, print, testing, tests, uncaught, empty, traceback, programs
- **Key terms/APIs that appear:** sys, sys.exc_info, except, type, try, print, sys.exception, __main__.e, i.e, import, any, os

#### Displaying Errors and Tracebacks
- **Span:** PDF pp. 975–975 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception, ZeroDivisionError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** traceback, exception, badly, module, py, inverse, instance, exc_info, standard, class, available, object
- **Key terms/APIs that appear:** sys, badly.py, sys.exception, sys.exc_info, badly.txt, type, traceback.print_exc, re, import, try, except, open

### Exception Design Tips and Gotchas
- **Span:** PDF pp. 976–978 (3 pages; brief)
- **Breakdown:**
  - What Should Be Wrapped
  - Catching Too Much: Avoid Empty except and Exception
  - Catching Too Little: Use Class-Based Categories
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### What Should Be Wrapped
- **Span:** PDF pp. 976–976 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception, IndexError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** exception, design, exceptions, except, statements, gotchas, wrapped, generally, failures, instead, error, function
- **Key terms/APIs that appear:** try, except, all, sum, any

#### Catching Too Much: Avoid Empty except and Exception
- **Span:** PDF pp. 976–977 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception, IndexError, KeyError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** exception, except, exceptions, catch, design, error, empty, gotchas, statements, system, program, built
- **Key terms/APIs that appear:** try, except, all, sys, sys.exit, exiter.py, print, sum, any, raise, re, import

#### Catching Too Little: Use Class-Based Categories
- **Span:** PDF pp. 978–978 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception, KeyError, NameError)
  - flags idioms and recommended usage patterns
  - calls out caveats and edge cases
- **Key concepts (from text):** exception, except, error, general, handler, handlers, exceptions, program, catching, specific, myexcept3, dictionary
- **Key terms/APIs that appear:** except, try, sys, list, sys.excepthook, os._exit, sys.exit, os, any, raise

### Core Language Wrap-Up
- **Span:** PDF pp. 979–981 (3 pages; brief)
- **Breakdown:**
  - The Python Toolset
  - Development Tools for Larger Projects
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### The Python Toolset
- **Span:** PDF pp. 979–979 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** language, tools, built, extensions, programming, larger, modules, advanced, complete, types, program, functions
- **Key terms/APIs that appear:** all, any, set, open, time

#### Development Tools for Larger Projects
- **Span:** PDF pp. 979–981 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception)
  - includes performance/efficiency notes
- **Key concepts (from text):** tools, language, modules, program, library, source, testing, programs, standard, provides, system, debugging
- **Key terms/APIs that appear:** time, all, any, open, print, e.g, set, try, re, zip, except

### Chapter Summary
- **Span:** PDF pp. 982–982 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** larger, module, tools, chapters, virtual, packages, environment, language, topics, exceptions, final, reading
- **Key terms/APIs that appear:** time, all, re, set

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 983–983 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception, IndexError, KeyError, MyError)
- **Key concepts (from text):** function, exception, called, error, knowledge, exercises, print, objects, exceptions, write, indexerror, catch
- **Key terms/APIs that appear:** print, try, any, except, raise, exctools.py, time, re, all, sys

### Test Your Knowledge: Answers
- **Span:** PDF pp. 983–983 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception, IndexError, KeyError, MyError)
- **Key concepts (from text):** function, exception, called, error, knowledge, exercises, print, objects, exceptions, write, indexerror, catch
- **Key terms/APIs that appear:** print, try, any, except, raise, exctools.py, time, re, all, sys

### Test Your Knowledge: Part VII Exercises
- **Span:** PDF pp. 983–984 (2 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., Exception, IndexError, KeyError, MyError)
- **Key concepts (from text):** function, exception, exercises, called, error, knowledge, exceptions, appendix, print, objects, write, indexerror
- **Key terms/APIs that appear:** print, try, any, except, raise, exctools.py, time, re, all, sys, set

# Part VIII. Advanced Topics
- **Span:** PDF pp. 985–1170 (186 pages; extended treatment)
- **Breakdown:**
  - Chapter 37. Unicode and Byte Strings
  - Chapter 38. Managed Attributes
  - Chapter 39. Decorators
  - Chapter 40. Metaclasses and Inheritance
  - Chapter 41. All Good Things
- **Granularity:** 5 immediate subheadings; 109 leaf subsections underneath

## Chapter 37. Unicode and Byte Strings
- **Span:** PDF pp. 987–1028 (42 pages; extended treatment)
- **Breakdown:**
  - Unicode Foundations
  - Introducing Python String Tools
  - Using Text Strings
  - Using Byte Strings
  - Using Text and Binary Files
  - Unicode, Bytes, and Other String Tools
  - The Unicode Twilight Zone
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 10 immediate subheadings; 28 leaf subsections underneath

### Unicode Foundations
- **Span:** PDF pp. 988–991 (4 pages; moderate detail)
- **Breakdown:**
  - Character Representations
  - Character Encodings
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Character Representations
- **Span:** PDF pp. 988–988 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** character, characters, ascii, value, latin, codes, unicode, integer, programmers, strings, stored, range
- **Key terms/APIs that appear:** range, all, a.k, bytes

#### Character Encodings
- **Span:** PDF pp. 989–991 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., UnicodeEncodeError)
  - includes performance/efficiency notes
- **Key concepts (from text):** bytes, ascii, character, unicode, encodings, characters, encode, latin, codes, encoding, string, points
- **Key terms/APIs that appear:** bytes, all, len, set, map, any, yield, a.k, range, time, type, list

### Introducing Python String Tools
- **Span:** PDF pp. 992–993 (2 pages; brief)
- **Breakdown:**
  - The str Object
  - The bytes Object
  - The bytearray Object
  - Text and Binary Files
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### The str Object
- **Span:** PDF pp. 992–992 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** bytes, unicode, encoded, str, content, decoded, string, binary, points, types, characters, sequence
- **Key terms/APIs that appear:** bytes, str, type, all, e.g, bytearray, yield, print, any, re

#### The bytes Object
- **Span:** PDF pp. 992–992 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** bytes, unicode, encoded, str, content, decoded, string, binary, points, types, characters, sequence
- **Key terms/APIs that appear:** bytes, str, type, all, e.g, bytearray, yield, print, any, re

#### The bytearray Object
- **Span:** PDF pp. 993–993 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** bytes, files, binary, str, content, object, bytearray, returns, string, operations, ascii, character
- **Key terms/APIs that appear:** bytes, str, bytearray, open, e.g, range, list, type, all, a.k, int, any

#### Text and Binary Files
- **Span:** PDF pp. 993–993 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** bytes, files, binary, str, content, object, bytearray, returns, string, operations, ascii, character
- **Key terms/APIs that appear:** bytes, str, bytearray, open, e.g, range, list, type, all, a.k, int, any

### Using Text Strings
- **Span:** PDF pp. 994–1003 (10 pages; detailed)
- **Breakdown:**
  - Literals and Basic Properties
  - String Type Conversions
  - Coding Unicode Strings in Python
  - Source-File Encoding Declarations
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Literals and Basic Properties
- **Span:** PDF pp. 994–994 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** bytes, string, str, object, unicode, literal, content, objects, argument, adding, binary, represent
- **Key terms/APIs that appear:** bytes, str, type, open, re, bytearray, all

#### String Type Conversions
- **Span:** PDF pp. 995–996 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** str, bytes, encoding, string, encode, decode, b'code, object, ascii, typeerror, strings, argument
- **Key terms/APIs that appear:** str, bytes, s.encode, b.decode, all, type, list, open, print, len, e.g, int

#### Coding Unicode Strings in Python
- **Span:** PDF pp. 997–1001 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., SyntaxError, UnicodeDecodeError, UnicodeEncodeError)
- **Key concepts (from text):** bytes, encode, unicode, ascii, characters, escapes, latin, encoding, str, character, decode, encoded
- **Key terms/APIs that appear:** bytes, s.encode, str, len, open, b.decode, sys, print, all, sys.platform, sys.getdefaultencoding, locale.getpreferredencoding

#### Source-File Encoding Declarations
- **Span:** PDF pp. 1002–1003 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** encoding, source, default, latin, ascii, unicode, coding, py, mystr1, strings, saved, latin1
- **Key terms/APIs that appear:** sys, print, latin1.py, open, astr.encode, utf8.py, len, e.g, all, sys.platform, sys.getdefaultencoding, locale.getpreferredencoding

### Using Byte Strings
- **Span:** PDF pp. 1004–1009 (6 pages; moderate detail)
- **Breakdown:**
  - Methods
  - Sequence Operations
  - Formatting
  - Other Ways to Make Bytes
  - Mixing String Types
  - The bytearray Object
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### Methods
- **Span:** PDF pp. 1004–1004 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** bytes, str, set, variable, attributes, strings, files, objects, binary, methods, unique, unicode
- **Key terms/APIs that appear:** bytes, str, set, dir, all, type, sorted, e.g, bytearray, re

#### Sequence Operations
- **Span:** PDF pp. 1005–1005 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** bytes, str, sequence, ascii, b'code, indexing, methods, operations, returns, integer, value, range
- **Key terms/APIs that appear:** bytes, str, range, b.find, b.replace, all, print, list, len

#### Formatting
- **Span:** PDF pp. 1006–1006 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError, SyntaxError, UnicodeEncodeError)
- **Key concepts (from text):** string, bytes, encoding, formatting, format, ascii, str, operations, strings, encode, method, today
- **Key terms/APIs that appear:** bytes, str, all, print, any, time, re

#### Other Ways to Make Bytes
- **Span:** PDF pp. 1006–1006 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError, SyntaxError, UnicodeEncodeError)
- **Key concepts (from text):** string, bytes, encoding, formatting, format, ascii, str, operations, strings, encode, method, today
- **Key terms/APIs that appear:** bytes, str, all, print, any, time, re

#### Mixing String Types
- **Span:** PDF pp. 1007–1007 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** bytes, str, replace, ascii, string, types, typeerror, b'abc, encode, b'code, decode, earlier
- **Key terms/APIs that appear:** bytes, str, b.replace, b.decode, type, try

#### The bytearray Object
- **Span:** PDF pp. 1008–1009 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError, ValueError)
- **Key concepts (from text):** bytearray, bytes, str, sequence, integer, object, string, mutable, operations, set, place, strings
- **Key terms/APIs that appear:** bytearray, bytes, str, set, dir, c.append, range, c.replace, type, list, sorted, int

### Using Text and Binary Files
- **Span:** PDF pp. 1010–1014 (5 pages; moderate detail)
- **Breakdown:**
  - Text-File Basics
  - Text and Binary Modes
  - Unicode-Text Files
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Text-File Basics
- **Span:** PDF pp. 1011–1011 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** write, binary, files, close, default, input, str, directory, folder, flush, platform, encoding
- **Key terms/APIs that appear:** open, temp.txt, input, str, bytes, e.g, re, a.k, file.write, file.close, file.read

#### Text and Binary Modes
- **Span:** PDF pp. 1011–1012 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** bytes, binary, write, str, files, input, default, close, b'abc, platform, encoding, unicode
- **Key terms/APIs that appear:** bytes, open, str, temp.bin, temp.txt, input, bytearray, re, e.g, a.k, file.write, file.close

#### Unicode-Text Files
- **Span:** PDF pp. 1013–1014 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError, UnicodeDecodeError, UnicodeEncodeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** encoding, files, bytes, ascii, str, default, binary, unicode, decode, write, object, encode
- **Key terms/APIs that appear:** open, bytes, str, uni.txt, uni2.txt, all, file.write, file.close, temp.bin, ascii.txt, e.g, lp5e.html

### Unicode, Bytes, and Other String Tools
- **Span:** PDF pp. 1015–1020 (6 pages; moderate detail)
- **Breakdown:**
  - The re Pattern-Matching Module
  - The struct Binary-Data Module
  - The pickle and json Serialization Modules
  - Filenames in open and Other Filename Tools
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### The re Pattern-Matching Module
- **Span:** PDF pp. 1015–1015 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** bytes, tools, str, library, string, encoding, image, codecs, module, fastest, b'python, pizza
- **Key terms/APIs that appear:** bytes, open, re, any, str, re.match, import, bytearray, text.replace, lp6e.html, large.jpg, f.k

#### The struct Binary-Data Module
- **Span:** PDF pp. 1016–1016 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** bytes, struct, binary, bytearray, module, str, typeerror, string, packed, pattern, match, groups
- **Key terms/APIs that appear:** bytes, bytearray, str, re.match, re, open, struct.unpack, pickle, struct.pack, data.bin, type, int

#### The pickle and json Serialization Modules
- **Span:** PDF pp. 1016–1017 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError, UnicodeDecodeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** bytes, pickle, binary, str, string, json, struct, module, typeerror, object, files, bytearray
- **Key terms/APIs that appear:** bytes, pickle, open, str, json, temp.pkl, bytearray, re.match, pickle.dump, re, struct.unpack, import

#### Filenames in open and Other Filename Tools
- **Span:** PDF pp. 1018–1020 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., OSError, UnicodeDecodeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** bytes, str, encoding, filenames, x84ck, tools, listdir, windows, default, xc4ck, unicode, filesystem
- **Key terms/APIs that appear:** bytes, open, str, os, os.listdir, sys, print, all, glob.glob, os.mkdir, sys.getfilesystemencoding, os.fsdecode

### The Unicode Twilight Zone
- **Span:** PDF pp. 1021–1026 (6 pages; moderate detail)
- **Breakdown:**
  - Dropping the BOM in Python
  - Unicode Normalization: Whither Standard?
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### Dropping the BOM in Python
- **Span:** PDF pp. 1021–1024 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., UnicodeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** encoding, ncode, default, windows, unicode, write, notepad, ascii, files, input, endian, specific
- **Key terms/APIs that appear:** open, temp.txt, code.txt, input, all, bytes, sys, type, e.g, except, str, re

#### Unicode Normalization: Whither Standard?
- **Span:** PDF pp. 1025–1026 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** unicode, character, points, standard, equality, forms, normalize, point, characters, u00f1, u006e, u0303
- **Key terms/APIs that appear:** boms.txt, e.g, open, len, bytes, all, import, set

### Chapter Summary
- **Span:** PDF pp. 1027–1027 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **Key concepts (from text):** unicode, string, binary, types, str, ascii, operations, bytes, files, bytearray, object, strings
- **Key terms/APIs that appear:** str, bytes, type, bytearray, set, all

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 1027–1027 (1 page; very brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** unicode, string, binary, types, str, ascii, operations, bytes, files, bytearray, object, strings
- **Key terms/APIs that appear:** str, bytes, type, bytearray, set, all

### Test Your Knowledge: Answers
- **Span:** PDF pp. 1027–1028 (2 pages; brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** unicode, string, ascii, binary, encoding, bytes, files, str, types, characters, strings, content
- **Key terms/APIs that appear:** bytes, str, bytearray, type, open, set, all, input, range, re, pickle, os

## Chapter 38. Managed Attributes
- **Span:** PDF pp. 1029–1068 (40 pages; extended treatment)
- **Breakdown:**
  - Why Manage Attributes?
  - Properties
  - Descriptors
  - __getattr__ and __getattribute__
  - Example: Attribute Validations
  - Chapter Summary
  - Test Your Knowledge: Quiz
- **Granularity:** 7 immediate subheadings; 22 leaf subsections underneath

### Why Manage Attributes?
- **Span:** PDF pp. 1029–1030 (2 pages; brief)
- **Breakdown:**
  - Inserting Code to Run on Attribute Access
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Inserting Code to Run on Attribute Access
- **Span:** PDF pp. 1030–1030 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** attribute, value, person, methods, tools, access, values, simple, changes, handling, getname, valid
- **Key terms/APIs that appear:** all, self.name, raise, person.getname, person.setname, re, property, any

### Properties
- **Span:** PDF pp. 1031–1034 (4 pages; moderate detail)
- **Breakdown:**
  - The Basics
  - A First Example
  - Computed Attributes
  - Coding Properties with Decorators
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### The Basics
- **Span:** PDF pp. 1031–1031 (1 page; very brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** attribute, property, attributes, class, function, none, first, properties, accesses, built, instance, techniques
- **Key terms/APIs that appear:** property, all, set, any, raise

#### A First Example
- **Span:** PDF pp. 1032–1032 (1 page; very brief)
- **Focus:** worked examples and usage patterns
- **Key concepts (from text):** property, print, person, attribute, class, fetch, jones, getname, setname, change, delname, demonstrate
- **Key terms/APIs that appear:** property, print, self._name, sue.name, person.py, person.name, bob.name, any, all

#### Computed Attributes
- **Span:** PDF pp. 1033–1033 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** value, class, property, instance, person, properties, state, information, attribute, super, methods, access
- **Key terms/APIs that appear:** property, self.value, p.x, super, print, computed.py, q.x, time

#### Coding Properties with Decorators
- **Span:** PDF pp. 1034–1034 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** property, decorator, automatically, person, setter, deleter, function, class, methods, print, properties, decorators
- **Key terms/APIs that appear:** property, self._name, print, name.setter, name.deleter, deco.py, re

### Descriptors
- **Span:** PDF pp. 1035–1044 (10 pages; detailed)
- **Breakdown:**
  - The Basics
  - A First Example
  - Computed Attributes
  - Using State Information in Descriptors
  - How Properties and Descriptors Relate
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### The Basics
- **Span:** PDF pp. 1036–1037 (2 pages; brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** descriptor, instance, class, attribute, subject, descriptors, methods, set, properties, classes, access, assigned
- **Key terms/APIs that appear:** x.attr, subject.attr, x.a, __main__.subject, c.a, __main__.descriptor, any, raise, all, print, instance.attr, class.attr

#### A First Example
- **Span:** PDF pp. 1038–1039 (2 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError)
- **Key concepts (from text):** class, instance, descriptor, attribute, print, person, set, delete, method, assign, methods, fetch
- **Key terms/APIs that appear:** print, sue.name, instance._name, all, x.a, c.a, person.py, self._name, set, any, super, name.__get__

#### Computed Attributes
- **Span:** PDF pp. 1040–1040 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, instance, value, descriptor, person, attribute, descsquare, using, nested, owner, set, delete
- **Key terms/APIs that appear:** self.value, c1.x, print, time, self._name, nested.py, person.name, name.__doc__, computed.py, any

#### Using State Information in Descriptors
- **Span:** PDF pp. 1041–1043 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** instance, descriptor, class, state, client, value, print, attribute, set, information, descstate, calcattrs
- **Key terms/APIs that appear:** print, obj.x, obj.z, set, obj.y, self.data, self.value, instance.data, i.managed, getattr, desc.py, self.z

#### How Properties and Descriptors Relate
- **Span:** PDF pp. 1044–1044 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** none, instance, property, attribute, class, print, properties, descriptors, raise, attributeerror, can't, value
- **Key terms/APIs that appear:** property, self.fget, self.fset, self.fdel, dir, print, raise, x.startswith, equiv.py, self.__doc__, x.name, getattr

### __getattr__ and __getattribute__
- **Span:** PDF pp. 1045–1057 (13 pages; detailed)
- **Breakdown:**
  - The Basics
  - A First Example
  - Computed Attributes
  - __getattr__ and __getattribute__ Compared
  - Management Techniques Compared
  - Intercepting Built-in Operation Attributes
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### The Basics
- **Span:** PDF pp. 1046–1047 (2 pages; brief)
- **Focus:** introduces core ideas and syntax
- **Key concepts (from text):** attribute, methods, getattr, getattribute, fetch, class, object, attributes, instance, method, setattr, value
- **Key terms/APIs that appear:** all, print, obj.name, set, a.k, x.pay, self.wrapped, getattr, x.job, x.append, x.wrapped, self.other

#### A First Example
- **Span:** PDF pp. 1048–1049 (2 pages; brief)
- **Focus:** worked examples and usage patterns
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., AttributeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** attribute, setattr, method, dict, getattribute, avoid, value, print, class, person, attributes, getattr
- **Key terms/APIs that appear:** print, set, self.__dict__, sue.name, any, person.py, self._name, obj.any, all, time, getattr, object.__getattribute__

#### Computed Attributes
- **Span:** PDF pp. 1050–1051 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., AttributeError)
- **Key concepts (from text):** getattribute, value, getattr, attribute, dict, setattr, py, object, using, fetches, avoid, print
- **Key terms/APIs that appear:** all, self.value, print, computed.py, a.x, set, person.py, object.__getattribute__, getattr, obj.any, self.__dict__, b.x

#### __getattr__ and __getattribute__ Compared
- **Span:** PDF pp. 1052–1052 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., AttributeError)
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** getattribute, print, getattr, attr1, class, value, attribute, attr2, return, attr3, inside, superclass
- **Key terms/APIs that appear:** print, getattr, self.value, object.__getattribute__, self.attr2, x.attr1, getattribute.py, x.attr2, x.attr3, time, raise, all

#### Management Techniques Compared
- **Span:** PDF pp. 1053–1054 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** square, value, instance, getattr, getattribute, attribute, class, return, attributes, names, attr3, version
- **Key terms/APIs that appear:** self._square, self._cube, property, instance._square, self.__dict__, print, all, x.attr2, x.attr3, getattribute.py, all_four_props.py, all_four_desc.py

#### Intercepting Built-in Operation Attributes
- **Span:** PDF pp. 1055–1057 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - calls out caveats and edge cases
- **Key concepts (from text):** getattr, getattribute, print, str, object, square, built, class, return, methods, attribute, classes
- **Key terms/APIs that appear:** getattr, print, all, lambda, except, object.__getattribute__, x.square, x.__add__, len, try, object.__setattr__, builtins.py

### Example: Attribute Validations
- **Span:** PDF pp. 1058–1066 (9 pages; detailed)
- **Breakdown:**
  - Using Properties to Validate
  - Using Descriptors to Validate
  - Using __getattr__ to Validate
  - Using __getattribute__ to Validate
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Using Properties to Validate
- **Span:** PDF pp. 1059–1060 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., TypeError, ValueError)
- **Key concepts (from text):** value, class, attributes, attribute, property, called, remain, cardholder, module, properties, return, print
- **Key terms/APIs that appear:** property, print, try, except, all, import, self.name, self.age, self.__name, self.__age, self.__acct, module.cardholder

#### Using Descriptors to Validate
- **Span:** PDF pp. 1061–1064 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError, TypeError, ValueError)
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** instance, class, value, descriptor, cardholder, set, state, attribute, remain, client, attributes, using
- **Key terms/APIs that appear:** raise, self.name, set, self.acct, self.age, all, validate_tester.py, validate_tester_plus.py, import, print, self.addr, value.lower

#### Using __getattr__ to Validate
- **Span:** PDF pp. 1065–1065 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** getattr, attribute, extra, attributes, method, descriptors, using, generic, properties, instance, setattr, class
- **Key terms/APIs that appear:** self.name, self.age, property, e.g, validate_getattr.py, self.acct, self.addr, self._acct, self.retireage, all, time, dir

#### Using __getattribute__ to Validate
- **Span:** PDF pp. 1066–1066 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., AttributeError, TypeError, ValueError)
  - includes performance/efficiency notes
- **Key concepts (from text):** value, version, class, attribute, raise, setattr, remain, output, py, getattribute, fetch, managed
- **Key terms/APIs that appear:** raise, all, except, value.lower, value.replace, self.acctlen, self.__dict__, validate_tester.py, validate_tester_plus.py, e.g, validate_getattribute.py, self.acct

### Chapter Summary
- **Span:** PDF pp. 1067–1067 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., TypeError, ValueError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** value, getattribute, superget, properties, class, return, remain, raise, getattr, match, stored, replace
- **Key terms/APIs that appear:** raise, all, set, except, object.__getattribute__, value.lower, value.replace, self.acctlen, self.__dict__, validate_tester.py, validate_tester_plus.py, len

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 1067–1068 (2 pages; brief)
- **Breakdown:**
  - Test Your Knowledge: Answers
- **Granularity:** 1 immediate subheadings; 1 leaf subsections underneath

#### Test Your Knowledge: Answers
- **Span:** PDF pp. 1068–1068 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** property, descriptors, attribute, properties, function, getattr, getattribute, attributes, fetches, fetch, specific, set
- **Key terms/APIs that appear:** property, set, all, i.e, any, dir

## Chapter 39. Decorators
- **Span:** PDF pp. 1069–1126 (58 pages; extended treatment)
- **Breakdown:**
  - What’s a Decorator?
  - The Basics
  - Coding Function Decorators
  - Coding Class Decorators
  - Example: “Private” and “Public” Attributes
  - Example: Validating Function Arguments
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 9 immediate subheadings; 31 leaf subsections underneath

### What’s a Decorator?
- **Span:** PDF pp. 1069–1071 (3 pages; brief)
- **Breakdown:**
  - Managing Calls and Instances
  - Managing Functions and Classes
  - Using and Defining Decorators
  - Why Decorators?
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### Managing Calls and Instances
- **Span:** PDF pp. 1070–1070 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** decorators, class, function, calls, objects, later, classes, wrapper, instance, creation, managing, manage
- **Key terms/APIs that appear:** a.k, property

#### Managing Functions and Classes
- **Span:** PDF pp. 1070–1070 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** decorators, class, function, calls, objects, later, classes, wrapper, instance, creation, managing, manage
- **Key terms/APIs that appear:** a.k, property

#### Using and Defining Decorators
- **Span:** PDF pp. 1070–1070 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** decorators, class, function, calls, objects, later, classes, wrapper, instance, creation, managing, manage
- **Key terms/APIs that appear:** a.k, property

#### Why Decorators?
- **Span:** PDF pp. 1071–1071 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** decorators, function, class, calls, augment, tasks, functions, object, interface, implement, objects, tools
- **Key terms/APIs that appear:** any

### The Basics
- **Span:** PDF pp. 1072–1080 (9 pages; detailed)
- **Breakdown:**
  - Function Decorator Basics
  - Class Decorator Basics
  - Decorator Nesting
  - Decorator Arguments
  - Decorators Manage Functions and Classes, Too
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Function Decorator Basics
- **Span:** PDF pp. 1072–1075 (4 pages; moderate detail)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** function, decorator, method, class, instance, callable, original, object, later, decorators, wrapper, decoration
- **Key terms/APIs that appear:** any, self.func, property, time, staticmethod, type, x.method, import, map

#### Class Decorator Basics
- **Span:** PDF pp. 1076–1077 (2 pages; brief)
- **Focus:** introduces core ideas and syntax
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, decorator, instance, decorators, callable, return, function, wrapper, original, getattr, manage, calls
- **Key terms/APIs that appear:** self.wrapped, self.c, getattr, wrapper.__init__, self.attr, x.attr, wrapper.__getattr__, a.k, print, type

#### Decorator Nesting
- **Span:** PDF pp. 1078–1079 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** function, instance, decorator, wrapper, return, decorators, original, multiple, class, creation, calls, following
- **Key terms/APIs that appear:** lambda, print, self.wrapped, all

#### Decorator Arguments
- **Span:** PDF pp. 1080–1080 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** decorator, callable, arguments, function, returns, class, state, calls, later, return, decorators, levels
- **Key terms/APIs that appear:** any

#### Decorators Manage Functions and Classes, Too
- **Span:** PDF pp. 1080–1080 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** decorator, callable, arguments, function, returns, class, state, calls, later, return, decorators, levels
- **Key terms/APIs that appear:** any

### Coding Function Decorators
- **Span:** PDF pp. 1081–1094 (14 pages; detailed)
- **Breakdown:**
  - Tracing Function Calls
  - Decorator State Retention Options
  - Class Pitfall: Decorating Methods
  - Timing Function Calls
  - Adding Decorator Arguments
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Tracing Function Calls
- **Span:** PDF pp. 1081–1081 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** decorator, function, calls, class, decorators, tracer, return, original, decorated, object, later, functions
- **Key terms/APIs that appear:** self.calls, self.func, print, any, decorator1.py, range

#### Decorator State Retention Options
- **Span:** PDF pp. 1082–1085 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** calls, function, tracer, state, wrapper, global, class, print, attributes, instance, scope, really
- **Key terms/APIs that appear:** print, func.__name__, self.calls, self.func, wrapper.calls, decorator_state_classes.py, decorator_state_globals.py, decorator_state_nonlocals.py, import, any, hack.calls, decorator1.tracer

#### Class Pitfall: Decorating Methods
- **Span:** PDF pp. 1086–1090 (5 pages; moderate detail)
- **Focus:** common pitfalls and edge cases
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, tracer, instance, method, function, calls, wrapper, giveraise, decorator, descriptor, methods, person
- **Key terms/APIs that appear:** self.calls, self.func, print, tracer.__call__, pat.giveraise, self.pay, all, import, wrapper.calls, self.name, self.desc, self.subj

#### Timing Function Calls
- **Span:** PDF pp. 1091–1092 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - calls out caveats and edge cases
- **Key concepts (from text):** calls, function, functions, alltime, methods, class, listcomp, mapcall, decorator, instance, return, decorators
- **Key terms/APIs that appear:** time, map, print, list, self.calls, self.meth, self.func, self.alltime, re, all, timerdeco1.py, time.perf_counter

#### Adding Decorator Arguments
- **Span:** PDF pp. 1093–1094 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** timer, listcomp, decorator, function, label, calls, enclosing, return, oncall, scope, print, result
- **Key terms/APIs that appear:** time, print, import, all, self.func, self.alltime, range, lambda, time.perf_counter, list, map, timer.total

### Coding Class Decorators
- **Span:** PDF pp. 1095–1101 (7 pages; moderate detail)
- **Breakdown:**
  - Singleton Classes
  - Tracing Object Interfaces
  - Class Pitfall: Retaining Multiple Instances
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Singleton Classes
- **Span:** PDF pp. 1095–1096 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - calls out caveats and edge cases
- **Key concepts (from text):** class, function, decorators, singleton, instances, person, instance, oncall, decorator, calls, coding, classes
- **Key terms/APIs that appear:** print, self.hours, self.rate, any, all, testseqs.py, singletons1.py, test.py, self.name, self.attr, sue.name, sue.pay

#### Tracing Object Interfaces
- **Span:** PDF pp. 1097–1099 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - calls out caveats and edge cases
- **Key concepts (from text):** instance, class, wrapper, object, print, trace, getattr, decorator, aclass, decorators, wrapped, oncall
- **Key terms/APIs that appear:** print, oncall.instance, self.instance, self.wrapped, all, getattr, self.aclass, interfacetracer.py, self.fetches, self.hours, self.rate, bob.name

#### Class Pitfall: Retaining Multiple Instances
- **Span:** PDF pp. 1100–1101 (2 pages; brief)
- **Focus:** common pitfalls and edge cases
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - calls out caveats and edge cases
- **Key concepts (from text):** class, instance, tracer, person, decorator, trace, mylist, triggers, creation, decorators, syntax, wrapper
- **Key terms/APIs that appear:** print, fail.py, list, x.append, x.wrapped, self.aclass, self.wrapped, bob.name, work.display, self.name, sue.name, type

### Example: “Private” and “Public” Attributes
- **Span:** PDF pp. 1102–1112 (11 pages; detailed)
- **Breakdown:**
  - Implementing Private Attributes
  - Implementation Details I
  - Generalizing for Public Declarations
  - Implementation Details II
  - Delegating Built-In Operations
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Implementing Private Attributes
- **Span:** PDF pp. 1102–1103 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** private, class, attribute, instance, decorator, doubler, attributes, print, wrapped, label, access, display
- **Key terms/APIs that appear:** print, self.data, raise, self.wrapped, all, self.label, x.display, y.label, y.display, getattr, access1.py, self.__dict__

#### Implementation Details I
- **Span:** PDF pp. 1104–1104 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, accesses, inside, attribute, outside, print, set, display, inheritance, wrapped, object, label
- **Key terms/APIs that appear:** print, set, x.size, x.data, __main__.doubler, y.data, y.size, access1.py, i.e, lambda, re

#### Generalizing for Public Declarations
- **Span:** PDF pp. 1105–1107 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - calls out caveats and edge cases
- **Key concepts (from text):** private, class, attributes, public, attribute, wrapped, names, oninstance, decorator, instance, outside, object
- **Key terms/APIs that appear:** any, all, x.name, x.age, set, self.__wrapped, setattr, getattr, self.name, self.age, time, raise

#### Implementation Details II
- **Span:** PDF pp. 1108–1108 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, version, wrapped, methods, attribute, privacy, though, access, operator, overloading, proxy, fully
- **Key terms/APIs that appear:** any, type, bob.pay, bob._oninstance__wrapped, e.g, x.__class__, try, all, isinstance, time

#### Delegating Built-In Operations
- **Span:** PDF pp. 1108–1112 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** wrapped, class, return, built, methods, operator, overloading, proxy, str, getattr, private, attribute
- **Key terms/APIs that appear:** sum, any, print, self.__wrapped, all, self._wrapped, self.__getattr__, self.sum, type, str, x.sum, x.__add__

### Example: Validating Function Arguments
- **Span:** PDF pp. 1113–1124 (12 pages; detailed)
- **Breakdown:**
  - The Goal
  - A Basic Range-Testing Decorator for Positional Arguments
  - Generalizing for Keywords and Defaults
  - Implementation Details
  - Open Issues
  - Decorator Arguments Versus Function Annotations
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

#### The Goal
- **Span:** PDF pp. 1114–1114 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** percent, decorator, class, inline, person, giveraise, int, validate, arguments, passed, method, tests
- **Key terms/APIs that appear:** self.pay, int, range, raise, any

#### A Basic Range-Testing Decorator for Positional Arguments
- **Span:** PDF pp. 1114–1115 (2 pages; brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** percent, decorator, class, rangetest, giveraise, function, person, int, method, inline, validate, arguments
- **Key terms/APIs that appear:** self.pay, int, main.py, raise, range, print, rangetest0.py, e.g, rangetest0_test.py, self.job, any, import

#### Generalizing for Keywords and Defaults
- **Span:** PDF pp. 1116–1119 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., TypeError)
  - includes performance/efficiency notes
- **Key concepts (from text):** arguments, argument, omitargs, passed, position, rangetest, giveraise, persinfo, birthday, py, decorator, defaults
- **Key terms/APIs that appear:** print, raise, rangetest_test.py, sue.giveraise, range, rangetest0_test.py, self.pay, all, sue.pay, bob.giveraise, any, rangetest.py

#### Implementation Details
- **Span:** PDF pp. 1120–1120 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** argument, names, arguments, function, expected, introspection, given, match, objects, object, catcher, appear
- **Key terms/APIs that appear:** all, code.co_varnames, set, func.__code__, code.co_nlocals, code.co_argcount, range, try, time, map, print, dir

#### Open Issues
- **Span:** PDF pp. 1121–1122 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
- **Key concepts (from text):** arguments, argument, passed, function, pargs, expected, kargs, positional, keyword, decorator, position, omitted
- **Key terms/APIs that appear:** all, list, any, code.co_argcount, code.co_varnames, func.__code__, tuple, try, code.co_nlocals, e.g, open, range

#### Decorator Arguments Versus Function Annotations
- **Span:** PDF pp. 1123–1124 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** decorator, function, arguments, rangetest, argument, print, oncall, annotations, argchecks, names, nesting, annotation
- **Key terms/APIs that appear:** print, range, f.__code__, annotation.py, any, func.__annotations__, dict, all, map

### Chapter Summary
- **Span:** PDF pp. 1125–1125 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - calls out caveats and edge cases
- **Key concepts (from text):** decorator, function, class, arguments, annotation, instance, decorators, functions, calls, methods, argument, single
- **Key terms/APIs that appear:** re, time, timerdeco2.py, all, range, any, type

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 1125–1125 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
  - calls out caveats and edge cases
- **Key concepts (from text):** decorator, function, class, arguments, annotation, instance, decorators, functions, calls, methods, argument, single
- **Key terms/APIs that appear:** re, time, timerdeco2.py, all, range, any, type

### Test Your Knowledge: Answers
- **Span:** PDF pp. 1126–1126 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - includes performance/efficiency notes
- **Key concepts (from text):** decorators, argument, class, py, passed, range, wrote, speed, decorator, command, arguments, validations
- **Key terms/APIs that appear:** range, all, access2.py, main.py, rangetest.py, _notes.txt, re, type

## Chapter 40. Metaclasses and Inheritance
- **Span:** PDF pp. 1127–1162 (36 pages; extended treatment)
- **Breakdown:**
  - To Metaclass or Not to Metaclass
  - The Metaclass Model
  - Coding Metaclasses
  - Inheritance: The Finale
  - Metaclass Methods
  - Chapter Summary
  - Test Your Knowledge: Quiz
  - Test Your Knowledge: Answers
- **Granularity:** 8 immediate subheadings; 22 leaf subsections underneath

### To Metaclass or Not to Metaclass
- **Span:** PDF pp. 1128–1130 (3 pages; brief)
- **Breakdown:**
  - The Downside of “Helper” Functions
  - Metaclasses Versus Class Decorators: Round 1
- **Granularity:** 2 immediate subheadings; 2 leaf subsections underneath

#### The Downside of “Helper” Functions
- **Span:** PDF pp. 1128–1129 (2 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, extra, metaclasses, classes, client1, function, method, metaclass, extras, helper, functions, client2
- **Key terms/APIs that appear:** all, x.extra, set, client1.extra, client2.extra, class.extra

#### Metaclasses Versus Class Decorators: Round 1
- **Span:** PDF pp. 1130–1130 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, extra, metaclass, metaclasses, extras, client1, client2, instances, return, client, methods, helper
- **Key terms/APIs that appear:** class.extra, x.extra, type, list, any

### The Metaclass Model
- **Span:** PDF pp. 1131–1134 (4 pages; moderate detail)
- **Breakdown:**
  - Classes Are Instances of type
  - Metaclasses Are Subclasses of type
  - Class Statements Call a type
  - Class Statements Can Choose a type
  - Metaclass Method Protocol
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Classes Are Instances of type
- **Span:** PDF pp. 1131–1131 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, decorators, classes, metaclasses, instances, extra, instance, client1, model, creation, extras, though
- **Key terms/APIs that appear:** re, class.extra, x.extra, any, time, all, type, random

#### Metaclasses Are Subclasses of type
- **Span:** PDF pp. 1132–1132 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, classes, instances, metaclasses, list, built, nonclass, created, types, metaclass, customize, inheritance
- **Key terms/APIs that appear:** type, list, __main__.hack, list.__class__, x.__class__, i.__class__, hack.__class__

#### Class Statements Call a type
- **Span:** PDF pp. 1133–1133 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, object, created, metaclass, inheritance, superclasses, attributes, method, classes, normal, instance, super
- **Key terms/APIs that appear:** type, all, super, type.__new__, type.__init__, self.data, tuple, time

#### Class Statements Can Choose a type
- **Span:** PDF pp. 1134–1134 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, metaclass, object, statement, default, create, module, automatically, super, superclasses, instead, normal
- **Key terms/APIs that appear:** type, __main__.hack, super, a.startswith, lambda, x.data, i.data, i.meth, c.__bases__, i.__class__, c.__dict__, tuple

#### Metaclass Method Protocol
- **Span:** PDF pp. 1135–1135 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, metaclass, method, calls, superclasses, metaclasses, object, statement, classname, attributedict, subclass, inherited
- **Key terms/APIs that appear:** type, super, meta.__new__, meta.__init__, self.data

### Coding Metaclasses
- **Span:** PDF pp. 1135–1145 (11 pages; detailed)
- **Breakdown:**
  - A Basic Metaclass
  - Customizing Construction and Initialization
  - Other Metaclass Coding Techniques
  - Managing Classes with Metaclasses and Decorators
- **Granularity:** 4 immediate subheadings; 4 leaf subsections underneath

#### A Basic Metaclass
- **Span:** PDF pp. 1135–1136 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, metaclass, method, classname, super, instance, metaone, calls, metaclasses, object, statement, return
- **Key terms/APIs that appear:** type, super, print, self.data, type.__new__, metaclass1.py, metaone.new, meta.__new__, meta.__init__, type.__call__, x.data, x.meth

#### Customizing Construction and Initialization
- **Span:** PDF pp. 1137–1137 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, metatwo, print, classname, supers, classdict, super, object, classes, instance, making, method
- **Key terms/APIs that appear:** print, super, type, metaclass2.py, metatwo.new, metatwo.init, __main__.super, hack.meth, time, type.__new__, class.__dict__, self.data

#### Other Metaclass Coding Techniques
- **Span:** PDF pp. 1138–1140 (3 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** class, supers, classname, classdict, metaclass, print, instance, function, super, making, metaobj, object
- **Key terms/APIs that appear:** print, type, super, __main__.super, hack.meth, all, metaclass3.py, self.data, x.data, x.meth, metaclass4.py, metaobj.call

#### Managing Classes with Metaclasses and Decorators
- **Span:** PDF pp. 1141–1145 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** class, decorator, metaclass, methods, return, decorators, value, person, timer, metaclasses, decorateall, tracer
- **Key terms/APIs that appear:** time, print, type, import, any, obj.value, self.value, self.name, self.pay, oncall.alltime, all, extend_meta.py

### Inheritance: The Finale
- **Span:** PDF pp. 1146–1155 (10 pages; detailed)
- **Breakdown:**
  - Metaclass Versus Superclass
  - Metaclass Inheritance
  - Python Inheritance Algorithm: The Simple Version
  - Python Inheritance Algorithm: The Less Simple Version
  - The Inheritance Wrap-Up
- **Granularity:** 5 immediate subheadings; 5 leaf subsections underneath

#### Metaclass Versus Superclass
- **Span:** PDF pp. 1148–1148 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, metaclass, instance, dict, inheritance, superclass, attribute, instances, true, supers, available, later
- **Key terms/APIs that appear:** type, c.attr, i.attr, c.__dict__, m.__dict__, s.__dict__, super

#### Metaclass Inheritance
- **Span:** PDF pp. 1149–1149 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError)
- **Key concepts (from text):** class, metaclass, inheritance, instance, classes, trees, attr3, nonclass, metaclasses, bases, inherits, attr1
- **Key terms/APIs that appear:** type, x.__name__, all, c.attr, i.attr, i.__class__, __main__.c, c.__bases__, __main__.s1, c.__class__, __main__.m, c.__mro__

#### Python Inheritance Algorithm: The Simple Version
- **Span:** PDF pp. 1150–1152 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, inheritance, dict, instance, attribute, bases, names, descriptor, search, rules, descriptors, metaclass
- **Key terms/APIs that appear:** i.__dict__, i.__class__, all, d.__get__, i.d, __main__.c, c.__class__, x.__dict__, type, print, x.__name__, c.__mro__

#### Python Inheritance Algorithm: The Less Simple Version
- **Span:** PDF pp. 1153–1154 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, inheritance, attribute, instance, built, descriptor, assignment, special, found, super, str, rules
- **Key terms/APIs that appear:** super, all, i.__str__, i.attr, str, a.k, any, print, lambda

#### The Inheritance Wrap-Up
- **Span:** PDF pp. 1155–1155 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, str, metaclass, object, built, inheritance, explicit, classes, default, return, start, super
- **Key terms/APIs that appear:** type, c.__str__, str, all, __main__.c, super, c.__class__, x.__name__, k.__mro__, print

### Metaclass Methods
- **Span:** PDF pp. 1156–1159 (4 pages; moderate detail)
- **Breakdown:**
  - Metaclass Methods Versus Class Methods
  - Operator Overloading in Metaclass Methods
  - Metaclass Methods Versus Instance Methods
- **Granularity:** 3 immediate subheadings; 3 leaf subsections underneath

#### Metaclass Methods Versus Class Methods
- **Span:** PDF pp. 1157–1157 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, methods, metaclass, method, object, bound, classes, accessible, attributeerror, attribute, though, visibility
- **Key terms/APIs that appear:** i.x, c.x, cls.x, classmethod, __main__.c, cls.y, cls.z, c.a, i.y, i.z, i.b, i.a

#### Operator Overloading in Metaclass Methods
- **Span:** PDF pp. 1158–1158 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, metaclass, classes, hours, methods, instance, getitem, method, instances, normal, operator, overloading
- **Key terms/APIs that appear:** self.hours, i.data, self.name, cls.data, c.__getitem__, m.__getitem__, __main__.c, c.data, self.data, self.rate, type, all

#### Metaclass Methods Versus Instance Methods
- **Span:** PDF pp. 1158–1159 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., AttributeError, TypeError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** class, metaclass, instance, classes, methods, hours, instances, normal, behavior, getitem, method, nonclass
- **Key terms/APIs that appear:** pat.pay, self.hours, pat2.pay, type, all, i.data, self.name, cls.hours, print, any, cls.data, c.__getitem__

### Chapter Summary
- **Span:** PDF pp. 1160–1160 (1 page; very brief)
- **Focus:** recap and checklist-style wrap-up
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, metaclasses, metaclass, classes, roles, inheritance, calling, arguments, instance, statement, conclusion, decorators
- **Key terms/APIs that appear:** all, pat2.pay, __main__.pat2, type, dict, sum, time

### Test Your Knowledge: Quiz
- **Span:** PDF pp. 1160–1160 (1 page; very brief)
- **Focus:** review questions / self-check
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** class, metaclasses, metaclass, classes, roles, inheritance, calling, arguments, instance, statement, conclusion, decorators
- **Key terms/APIs that appear:** all, pat2.pay, __main__.pat2, type, dict, sum, time

### Test Your Knowledge: Answers
- **Span:** PDF pp. 1161–1162 (2 pages; brief)
- **Focus:** review questions / self-check
- **Key concepts (from text):** class, classes, decorators, metaclasses, metaclass, creation, methods, behavior, instance, knowledge, answers, create
- **Key terms/APIs that appear:** type

## Chapter 41. All Good Things
- **Span:** PDF pp. 1163–1170 (8 pages; detailed)
- **Breakdown:**
  - The Python Tsunami
  - The Python Sandbox
  - The Python Upside
  - Closing Thoughts
  - Where to Go from Here
  - Encore: Print Your Own Completion Certificate!
- **Granularity:** 6 immediate subheadings; 6 leaf subsections underneath

### The Python Tsunami
- **Span:** PDF pp. 1163–1164 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** tools, string, dictionary, function, class, assignment, match, options, language, unpacking, attribute, redundancy
- **Key terms/APIs that appear:** all, set, async, super, list, except, sys.executable, str.format, string.template, open, type, sys

### The Python Sandbox
- **Span:** PDF pp. 1165–1165 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** sandbox, seems, language, software, additions, expected, mandatory, constantly, developers, users, people, churn
- **Key terms/APIs that appear:** all, type, raise

### The Python Upside
- **Span:** PDF pp. 1165–1165 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** sandbox, seems, language, software, additions, expected, mandatory, constantly, developers, users, people, churn
- **Key terms/APIs that appear:** all, type, raise

### Closing Thoughts
- **Span:** PDF pp. 1166–1166 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** language, programming, completion, practice, using, story, concerns, entirely, seems, afford, tools, resources
- **Key terms/APIs that appear:** except, time, open, any, print, all

### Where to Go from Here
- **Span:** PDF pp. 1166–1166 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** language, programming, completion, practice, using, story, concerns, entirely, seems, afford, tools, resources
- **Key terms/APIs that appear:** except, time, open, any, print, all

### Encore: Print Your Own Completion Certificate!
- **Span:** PDF pp. 1166–1170 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** html, htmltext, print, certificate, completion, fileto, browser, files, textto, replace, language, script
- **Key terms/APIs that appear:** open, print, time, all, os, it.py, htmltext.replace, time.sleep, fileto.close, except, any, import

# Part IX. Appendixes
- **Span:** PDF pp. 1171–1234 (64 pages; extended treatment)
- **Breakdown:**
  - Appendix A. Platform Usage Tips
  - Appendix B. Solutions to End-of-Part Exercises
- **Granularity:** 2 immediate subheadings; 14 leaf subsections underneath

## Appendix A. Platform Usage Tips
- **Span:** PDF pp. 1173–1194 (22 pages; deep dive)
- **Breakdown:**
  - Using Python on Windows
  - Using Python on macOS
  - Using Python on Linux
  - Using Python on Android
  - Using Python on iOS
  - Standalone Apps and Executables
  - Etcetera
- **Granularity:** 7 immediate subheadings; 7 leaf subsections underneath

### Using Python on Windows
- **Span:** PDF pp. 1173–1178 (6 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** windows, command, py, install, usage, start, platform, store, appendix, linux, version, editor
- **Key terms/APIs that appear:** all, e.g, any, re, import, type, open, a.k, filename.txt, i.e, idlelib.idle, sys.argv

### Using Python on macOS
- **Span:** PDF pp. 1179–1183 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** macos, windows, command, install, lines, python3, py, finder, script, platform, files, shell
- **Key terms/APIs that appear:** e.g, open, set, all, type, hack.py, a.k, input, any, script.py, list, os

### Using Python on Linux
- **Span:** PDF pp. 1184–1185 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
- **Key concepts (from text):** linux, install, python3, macos, platform, shell, ubuntu, files, command, windows, specific, terminal
- **Key terms/APIs that appear:** e.g, script.py, all, idlelib.idle, type, try, any, open, print, set

### Using Python on Android
- **Span:** PDF pp. 1186–1188 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** termux, android, command, install, pydroid, linux, shell, storage, source, platform, interactive, session
- **Key terms/APIs that appear:** all, open, e.g, script.py, try, time, any, re

### Using Python on iOS
- **Span:** PDF pp. 1189–1189 (1 page; very brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** android, tools, store, access, keyboards, options, proprietary, constraints, files, programming, explore, onscreen
- **Key terms/APIs that appear:** e.g, re, list, any, all, open

### Standalone Apps and Executables
- **Span:** PDF pp. 1190–1192 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** android, standalone, platform, running, macos, portable, coded, platforms, options, possible, appendix, usage
- **Key terms/APIs that appear:** e.g, any, quixotely.com, yield, all, open, range, try, re

### Etcetera
- **Span:** PDF pp. 1193–1194 (2 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** usage, using, start, details, platform, appendix, jupyter, alternative, implementations, webassembly, options, standalones
- **Key terms/APIs that appear:** re, all, time

## Appendix B. Solutions to End-of-Part Exercises
- **Span:** PDF pp. 1195–1234 (40 pages; extended treatment)
- **Breakdown:**
  - Part I, Getting Started
  - Part II, Objects and Operations
  - Part III, Statements and Syntax
  - Part IV, Functions and Generators
  - Part V, Modules and Packages
  - Part VI, Classes and OOP
  - Part VII, Exceptions
- **Granularity:** 7 immediate subheadings; 7 leaf subsections underneath

### Part I, Getting Started
- **Span:** PDF pp. 1195–1197 (3 pages; brief)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., NameError, ZeroDivisionError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** module, python3, py, hello, world, exercises, source, list, solutions, files, interaction, object
- **Key terms/APIs that appear:** list, script1.py, print, import, e.g, i.e, module1.py, try, all, l.append, any, re

### Part II, Objects and Operations
- **Span:** PDF pp. 1198–1202 (5 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., AttributeError, IndexError, KeyError, TypeError)
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** list, indexing, dictionary, strings, empty, tuple, index, sequence, assignment, exercises, string, objects
- **Key terms/APIs that appear:** list, type, tuple, e.g, open, myfile.txt, range, maker.py, reader.py, set, re, print

### Part III, Statements and Syntax
- **Span:** PDF pp. 1203–1204 (2 pages; brief)
- **Focus:** syntax forms and call/usage rules
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - spells out syntax forms and how calls/expressions are written
- **Key concepts (from text):** print, list, march, month, exercises, january, february, sorted, exercise, solutions, coding, basic
- **Key terms/APIs that appear:** print, list, sorted, map, x.append, selections.txt, e.g, d.keys, keys.sort, range, try, len

### Part IV, Functions and Generators
- **Span:** PDF pp. 1205–1214 (10 pages; detailed)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** print, range, return, py, found, exercises, yield, prime, function, solutions, solution, factor
- **Key terms/APIs that appear:** print, range, sum, yield, type, list, lambda, l.index, import, math, primes.py, map

### Part V, Modules and Packages
- **Span:** PDF pp. 1215–1218 (4 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** py, mymod, return, import, countchars, mypkg, countlines, windows, myclient, python3, part5, module
- **Key terms/APIs that appear:** mymod.py, import, open, len, print, input, __init__.py, all, file.readlines, file.seek, mypkg.mymod, re

### Part VI, Classes and OOP
- **Span:** PDF pp. 1219–1225 (7 pages; moderate detail)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - uses interactive-shell examples (REPL transcripts) to demonstrate behavior
  - shows common error modes / exceptions (e.g., TypeError)
  - compares alternative approaches and explains trade-offs
  - flags idioms and recommended usage patterns
- **Key concepts (from text):** class, print, return, import, set, py, recur2, adder, super, start, multiset, recur1
- **Key terms/APIs that appear:** print, import, set, super, self.data, all, x.add, self.adds, self.__class__, self.cust, self.food, type

### Part VII, Exceptions
- **Span:** PDF pp. 1226–1234 (9 pages; detailed)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - shows common error modes / exceptions (e.g., Exception, IndexError, KeyError, MyError)
  - compares alternative approaches and explains trade-offs
- **Key concepts (from text):** print, py, class, error, speak, exception, people, except, part7, caught, script, exercises
- **Key terms/APIs that appear:** print, except, sys, curs.execute, try, import, open, int, sys.exc_info, raise, os, input

# Index
- **Span:** PDF pp. 1235–1267 (33 pages; extended treatment)
- **Focus:** focused explanation with examples
- **What you’ll see:**
  - spells out syntax forms and how calls/expressions are written
  - shows common error modes / exceptions (e.g., ArithmeticError, Exception, LookupError, OSError)
  - compares alternative approaches and explains trade-offs
  - includes performance/efficiency notes
- **Key concepts (from text):** function, method, arguments, statement, assignments, argument, loops, attribute, nesting, syntax, class, validation
- **Key terms/APIs that appear:** type, async, list, try, print, lambda, map, except, yield, zip, mins.py, time

# About the Author
- **Span:** PDF pp. 1268–1268 (1 page; very brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** books, cover, author, experience, teaching, reilly, sixth, species, karen, montgomery, adobe, classic
- **Key terms/APIs that appear:** all, range

# Colophon
- **Span:** PDF pp. 1268–1269 (2 pages; brief)
- **Focus:** focused explanation with examples
- **Key concepts (from text):** reilly, books, cover, author, experience, teaching, sixth, species, karen, montgomery, based, adobe
- **Key terms/APIs that appear:** all, range, try
