# Learning Python, 6th Edition — Mark Lutz (O'Reilly, 2025)

## Detailed Table of Contents

---

### Preface
- Python
- This Book
- This Edition
- Media Choices
- Updates and Examples
- Conventions and Reuse
- Acknowledgments

---

### Part I. Getting Started

#### Chapter 1. A Python Q&A Session
- Why Do People Use Python?
  - Software Quality
  - Developer Productivity
- Is Python a "Scripting Language"?
- OK, but What's the Downside?
- Who Uses Python Today?
- What Can I Do with Python?
  - Systems Programming
  - GUIs and UIs
  - Internet and Web Scripting
  - Component Integration
  - Database Access
  - Rapid Prototyping
  - Numeric and Scientific Programming
  - And More: AI, Games, Images, QA, Excel, Apps…
- What Are Python's Technical Strengths?
  - It's Object-Oriented and Functional
  - It's Free and Open
  - It's Portable
  - It's Powerful
  - It's Mixable
  - It's Relatively Easy to Use
  - It's Relatively Easy to Learn

#### Chapter 2. How Python Runs Programs
- Introducing the Python Interpreter
- Program Execution
  - The Programmer's View
  - Python's View
- Execution-Model Variations
  - Python Implementation Alternatives
  - Standalone Executables
  - Future Possibilities

#### Chapter 3. How You Run Programs
- Installing Python
- Interactive Code
  - Starting an Interactive REPL
  - Where to Run: Code Folders
  - What Not to Type: Prompts and Comments
  - Other Python REPLs
  - Running Code Interactively
  - Why the Interactive Prompt?
- Program Files
  - A First Script
  - Running Files with Command Lines
  - Command-Line Usage Variations
- Other Ways to Run Files
  - Clicking and Tapping File Icons
  - The IDLE Graphical User Interface
  - Other IDEs for Python
  - Smartphone Apps
  - WebAssembly for Browsers
  - Jupyter Notebooks for Science
  - Ahead-of-Time Compilers for Speed
  - Running Code in Code
  - Other Launch Options
- Which Option Should I Use?

---

### Part II. Objects and Operations

#### Chapter 4. Introducing Python Objects
- The Python Conceptual Hierarchy
- Why Use Built-in Objects?
- Python's Core Object Types
- Numbers
- Strings
  - Sequence Operations
  - Immutability
  - Type-Specific Methods
  - Getting Help
  - Other Ways to Code Strings
  - Unicode Strings
- Lists
  - Sequence Operations
  - Type-Specific Operations
  - Bounds Checking
  - Nesting
  - Comprehensions
- Dictionaries
  - Mapping Operations
  - Nesting Revisited
  - Missing Keys: if Tests
  - Item Iteration: for Loops
- Tuples
  - Why Tuples?
- Files
  - Unicode and Byte Files
  - Other File-Like Tools
- Other Object Types
  - Sets
  - Booleans and None
  - Types
  - Type Hinting
  - User-Defined Objects
  - And Everything Else

#### Chapter 5. Numbers and Expressions
- Numeric Object Basics
  - Numeric Literals
  - Built-in Numeric Tools
- Python Expression Operators
  - Mixed Operators: Precedence
  - Parentheses Group Subexpressions
  - Mixed Types Are Converted Up
  - Preview: Operator Overloading and Polymorphism
- Numbers in Action
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
- Other Numeric Objects
  - Decimal Objects
  - Fraction Objects
  - Set Objects
  - Boolean Objects
- Numeric Extensions

#### Chapter 6. The Dynamic Typing Interlude
- The Case of the Missing Declaration Statements
  - Variables, Objects, and References
  - Types Live with Objects, Not Variables
  - Objects Are Garbage-Collected
- Shared References
  - Shared References and In-Place Changes
  - Shared References and Equality
- Dynamic Typing Is Everywhere
- Type Hinting: Optional, Unused, and Why?

#### Chapter 7. String Fundamentals
- String Object Basics
- String Literals
  - Single and Double Quotes Are the Same
  - Escape Sequences Are Special Characters
  - Raw Strings Suppress Escapes
  - Triple Quotes and Multiline Strings
- Strings in Action
  - Basic Operations
  - Indexing and Slicing
  - String Conversion Tools
  - "Changing" Strings Part 1: Sequence Operations
- String Methods
  - Method Call Syntax
  - All String Methods (Today)
  - "Changing" Strings, Part 2: String Methods
  - More String Methods: Parsing Text
  - Other Common String Methods
- String Formatting: The Triathlon
  - String-Formatting Options
  - The String-Formatting Expression
  - The String-Formatting Method
  - The F-String Formatting Literal
  - And the Winner Is…
- General Type Categories
  - Types Share Operation Sets by Categories
  - Mutable Types Can Be Changed in Place

#### Chapter 8. Lists and Dictionaries
- Lists
- Lists in Action
  - Basic List Operations
  - Indexing and Slicing
  - Changing Lists in Place
  - More List Methods
  - Iteration, Comprehensions, and Unpacking
  - Other List Operations
- Dictionaries
- Dictionaries in Action
  - Basic Dictionary Operations
  - Changing Dictionaries in Place
  - More Dictionary Methods
  - Other Dictionary Makers
  - Dictionary Comprehensions
  - Key Insertion Ordering
  - Dictionary "Union" Operator
  - Intermission: Books Database
  - Dictionary Usage Tips

#### Chapter 9. Tuples, Files, and Everything Else
- Tuples
  - Tuples in Action
  - Why Lists and Tuples?
  - Records Revisited: Named Tuples
- Files
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
- Core Types Review and Summary
  - Object Flexibility
  - References Versus Copies
  - Comparisons, Equality, and Truth
  - The Meaning of True and False in Python
  - Python's Type Hierarchies
  - Type Objects
- Other Types in Python
- Built-in Type Gotchas
  - Assignment Creates References, Not Copies
  - Repetition Adds One Level Deep
  - Beware of Cyclic Data Structures
  - Immutable Types Can't Be Changed in Place

---

### Part III. Statements and Syntax

#### Chapter 10. Introducing Python Statements
- The Python Conceptual Hierarchy Revisited
- Python's Statements
- A Tale of Two ifs
  - What Python Adds
  - What Python Removes
  - Why Indentation Syntax?
  - A Few Special Cases
- A Quick Example: Interactive Loops
  - A Simple Interactive Loop
  - Doing Math on User Inputs
  - Handling Errors by Testing Inputs
  - Handling Errors with try Statements
  - Supporting Floating-Point Numbers
  - Nesting Code Three Levels Deep

#### Chapter 11. Assignments, Expressions, and Prints
- Assignments
  - Assignment Syntax Forms
  - Basic Assignments
  - Sequence Assignments
  - Extended-Unpacking Assignments
  - Multiple-Target Assignments
  - Augmented Assignments
  - Named Assignment Expressions
  - Variable Name Rules
- Expression Statements
  - Expression Statements and In-Place Changes
- Print Operations
  - The print Function
  - Print Stream Redirection

#### Chapter 12. if and match Selections
- if Statements
  - General Format
  - Basic Examples
  - Multiple-Choice Selections
- match Statements
  - Basic match Usage
  - Advanced match Usage
- Python Syntax Revisited
  - Block Delimiters: Indentation Rules
  - Statement Delimiters: Lines and Continuations
  - Special Syntax Cases in Action
- Truth Values Revisited
- The if/else Ternary Expression

#### Chapter 13. while and for Loops
- while Loops
  - General Format
  - Examples
- break, continue, pass, and the Loop else
  - General Loop Format
  - pass
  - continue
  - break
  - Loop else
- for Loops
  - General Format
  - Examples
- Loop Coding Techniques
  - Counter Loops: range
  - Sequence Scans: while, range, and for
  - Sequence Shufflers: range and len
  - Skipping Items: range and Slices
  - Changing Lists: range and Comprehensions
  - Parallel Traversals: zip
  - Offsets and Items: enumerate

#### Chapter 14. Iterations and Comprehensions
- Iterations
  - The Iteration Protocol
  - Other Built-in Iterables
- Comprehensions
  - List Comprehension Basics
  - List Comprehensions and Files
  - Extended List Comprehension Syntax
  - Comprehensions Cliff-Hanger
- Iteration Tools
- Other Iteration Topics

#### Chapter 15. The Documentation Interlude
- Python Documentation Sources
  - \# Comments
  - The dir Function
  - Docstrings and \_\_doc\_\_
  - Pydoc: The help Function
  - Pydoc: HTML Reports
  - Beyond Docstrings: Sphinx
  - The Standard Manuals
  - Web Resources
- Common Coding Gotchas

---

### Part IV. Functions and Generators

#### Chapter 16. Function Basics
- Why Use Functions?
- Function Coding Overview
  - Basic Function Tools
  - Advanced Function Tools
  - General Function Concepts
  - def Statements
  - return Statements
  - def Executes at Runtime
  - lambda Makes Anonymous Functions
- A First Example: Definitions and Calls
  - Definition
  - Calls
  - Polymorphism in Python
- A Second Example: Intersecting Sequences
  - Definition
  - Calls
  - Polymorphism Revisited
  - Segue: Local Variables

#### Chapter 17. Scopes
- Python Scopes Basics
  - Scopes Overview
  - Name Resolution: The LEGB Rule
  - Scopes Examples
  - The Built-in Scope
- The global Statement
  - Program Design: Minimize Global Variables
  - Program Design: Minimize Cross-File Changes
  - Other Ways to Access Globals
- Nested Functions and Scopes
  - Nested Scopes Overview
  - Nested Scopes Examples
  - Closures and Factory Functions
  - Arbitrary Scope Nesting
- The nonlocal Statement
  - nonlocal Basics
  - nonlocal in Action
  - nonlocal Boundary Cases
- State-Retention Options
  - Nonlocals: Changeable, Per-Call, LEGB
  - Globals: Changeable but Shared
  - Function Attributes: Changeable, Per-Call, Explicit
  - Classes: Changeable, Per-Call, OOP
  - And the Winner Is…
- Scopes and Argument Defaults
  - Loops Require Defaults, Not Scopes

#### Chapter 18. Arguments
- Argument-Passing Basics
  - Arguments and Shared References
  - Avoiding Mutable Argument Changes
  - Simulating Output Parameters and Multiple Results
- Special Argument-Matching Modes
  - Argument Matching Overview
  - Argument Matching Syntax
  - Argument Passing Details
  - Keyword and Default Examples
  - Arbitrary Arguments Examples
  - Keyword-Only Arguments
  - Positional-Only Arguments
- Argument Ordering: The Gritty Details
  - Definition Ordering
  - Calls Ordering
- Example: The min Wakeup Call
  - Full Credit
  - Bonus Points
  - The Punch Line
- Example: Generalized Set Functions
  - Testing the Code
- Example: Rolling Your Own Print
  - Using Keyword-Only Arguments

#### Chapter 19. Function Odds and Ends
- Function Design Concepts
- Recursive Functions
  - Summation with Recursion
  - Coding Alternatives
  - Loop Statements Versus Recursion
  - Handling Arbitrary Structures
- Function Tools: Attributes, Annotations, Etc.
  - The First-Class Object Model
  - Function Introspection
  - Function Attributes
  - Function Annotations and Decorations
- Anonymous Functions: lambda
  - lambda Basics
  - Why Use lambda?
  - How (Not) to Obfuscate Your Python Code
  - Scopes: lambdas Can Be Nested Too
- Functional Programming Tools
  - Mapping Functions over Iterables: map
  - Selecting Items in Iterables: filter
  - Combining Items in Iterables: reduce

#### Chapter 20. Comprehensions and Generations
- Comprehensions: The Final Act
  - List Comprehensions Review
  - Formal Comprehension Syntax
  - Example: List Comprehensions and Matrixes
- Generator Functions and Expressions
  - Generator Functions: yield Versus return
  - Generator Expressions: Iterables Meet Comprehensions
  - Generator Functions Versus Generator Expressions
  - Generator Odds and Ends
- Example: Shuffling Sequences
  - Scrambling Sequences
  - Permutating Sequences
- Example: Emulating zip and map
  - Coding Your Own map
  - Coding Your Own zip and 2.X map
- Asynchronous Functions: The Short Story
  - Async Basics
  - The Async Wrap-Up

#### Chapter 21. The Benchmarking Interlude
- Benchmarking with Homegrown Tools
  - Timer Module: Take 1
  - Timer Module: Take 2
  - Timing Runner and Script
  - Iteration Results
  - More Module Mods
- Benchmarking with Python's timeit
  - Basic timeit Usage
  - Automating timeit Benchmarking
- Function Gotchas
  - Local Names Are Detected Statically
  - Defaults and Mutable Objects
  - Functions Without returns
  - Miscellaneous Function Gotchas

---

### Part V. Modules and Packages

#### Chapter 22. Modules: The Big Picture
- Module Essentials
- Why Use Modules?
- Python Program Architecture
  - How to Structure a Program
  - Imports and Attributes
  - Standard-Library Modules
- How Imports Work
  - Step 1: Find It
  - Step 2: Compile It (Maybe)
  - Step 3: Run It
- The Module Search Path
  - Search-Path Components
  - Configuring the Search Path
  - The sys.path List
  - Module File Selection
  - Path Outliers: Standalones and Packages

#### Chapter 23. Module Coding Basics
- Creating Modules
  - Module Filenames
  - Other Kinds of Modules
- Using Modules
  - The import Statement
  - The from Statement
  - The from \* Statement
  - Imports Happen Only Once
  - Imports Are Runtime Assignments
  - import and from Equivalence
  - Potential Pitfalls of the from Statement
- Module Namespaces
  - How Files Generate Namespaces
  - Namespace Dictionaries: \_\_dict\_\_
  - Attribute Name Qualification
  - Imports Versus Scopes
  - Namespace Nesting
- Reloading Modules
  - reload Basics
  - reload Example
  - reload Odds and Ends

#### Chapter 24. Module Packages
- Using Packages
  - Package Imports
  - Packages and the Module Search Path
- Creating Packages
  - Basic Package Structure
  - Package \_\_init\_\_.py Files
  - Package \_\_main\_\_.py Files
- Why Packages?
  - A Tale of Two Systems
- The Roles of \_\_init\_\_.py Files
- Package-Relative Imports
  - Relative and Absolute Imports
  - Relative-Import Rationales and Trade-Offs
  - Package-Relative Imports in Action
- Namespace Packages
  - Python Import Models
  - Namespace-Package Rationales
  - The Module Search Algorithm
  - Namespace Packages in Action

#### Chapter 25. Module Odds and Ends
- Module Design Concepts
- Data Hiding in Modules
  - Minimizing from \* Damage: \_X and \_\_all\_\_
  - Managing Attribute Access: \_\_getattr\_\_ and \_\_dir\_\_
- Enabling Language Changes: \_\_future\_\_
- Dual-Usage Modes: \_\_name\_\_ and \_\_main\_\_
  - Example: Unit Tests with \_\_name\_\_
- The as Extension for import and from
- Module Introspection
  - Example: Listing Modules with \_\_dict\_\_
- Importing Modules by Name String
  - Running Code Strings
  - Direct Calls: Two Options
  - Example: Transitive Module Reloads
- Module Gotchas
  - Module Name Clashes: Package and Package-Relative Imports
  - Statement Order Matters in Top-Level Code
  - from Copies Names but Doesn't Link
  - from \* Can Obscure the Meaning of Variables
  - reload May Not Impact from Imports
  - reload, from, and Interactive Testing
  - Recursive from Imports May Not Work

---

### Part VI. Classes and OOP

#### Chapter 26. OOP: The Big Picture
- Why Use Classes?
- OOP from 30,000 Feet
  - Attribute Inheritance Search
  - Classes and Instances
  - Method Calls
  - Coding Class Trees
  - Operator Overloading
  - OOP Is About Code Reuse

#### Chapter 27. Class Coding Basics
- Classes Generate Multiple Instance Objects
  - Class Objects Provide Default Behavior
  - Instance Objects Are Concrete Items
  - A First Example
- Classes Are Customized by Inheritance
  - A Second Example
  - Classes Are Attributes in Modules
- Classes Can Intercept Python Operators
  - A Third Example
- The World's Simplest Python Class
  - Classes: Under the Hood
  - Records Revisited: Classes Versus Dictionaries

#### Chapter 28. A More Realistic Example
- Step 1: Making Instances
  - Coding Constructors
  - Testing as You Go
  - Using Code Two Ways
- Step 2: Adding Behavior Methods
  - Coding Methods
- Step 3: Operator Overloading
  - Providing Print Displays
- Step 4: Customizing Behavior by Subclassing
  - Coding Subclasses
  - Augmenting Methods: The Bad Way
  - Augmenting Methods: The Good Way
  - Polymorphism in Action
  - Inherit, Customize, and Extend
  - OOP: The Big Idea
- Step 5: Customizing Constructors, Too
  - OOP Is Simpler Than You May Think
  - Other Ways to Combine Classes: Composites
- Step 6: Using Introspection Tools
  - Special Class Attributes
  - A Generic Display Tool
  - Instance Versus Class Attributes
  - Name Considerations in Tool Classes
  - Our Classes' Final Form
- Step 7 (Final): Storing Objects in a Database
  - Pickles and Shelves
  - Storing Objects on a shelve Database
  - Exploring Shelves Interactively
  - Updating Objects on a Shelf
- Future Directions

#### Chapter 29. Class Coding Details
- The class Statement
  - General Syntax and Usage
  - Example: Class Attributes
- Methods
  - Method Example
  - Other Method-Call Possibilities
- Inheritance
  - Attribute Tree Construction
  - Inheritance Fine Print
  - Specializing Inherited Methods
  - Class Interface Techniques
  - Abstract Superclasses
- Namespaces: The Conclusion
  - Simple Names: Global Unless Assigned
  - Attribute Names: Object Namespaces
  - The "Zen" of Namespaces: Assignments Classify Names
  - Nested Classes: The LEGB Scopes Rule Revisited
  - Namespace Dictionaries: Review
  - Namespace Links: A Tree Climber
- Documentation Strings Revisited
- Classes Versus Modules

#### Chapter 30. Operator Overloading
- The Basics
  - Constructors and Expressions: \_\_init\_\_ and \_\_sub\_\_
  - Common Operator-Overloading Methods
- Indexing and Slicing: \_\_getitem\_\_ and \_\_setitem\_\_
  - Intercepting Slices
  - Intercepting Item Assignments
  - But \_\_index\_\_ Means As-Integer
- Index Iteration: \_\_getitem\_\_
- Iterable Objects: \_\_iter\_\_ and \_\_next\_\_
  - User-Defined Iterables
  - Multiple Iterators on One Object
  - Coding Alternative: \_\_iter\_\_ Plus yield
- Membership: \_\_contains\_\_, \_\_iter\_\_, and \_\_getitem\_\_
- Attribute Access: \_\_getattr\_\_ and \_\_setattr\_\_
  - Attribute Reference
  - Attribute Assignment and Deletion
  - Other Attribute-Management Tools
  - Emulating Privacy for Instance Attributes: Part 1
- String Representation: \_\_repr\_\_ and \_\_str\_\_
  - Why Two Display Methods?
  - Display Usage Notes
- Right-Side and In-Place Ops: \_\_radd\_\_ and \_\_iadd\_\_
  - Right-Side Addition
  - In-Place Addition
- Call Expressions: \_\_call\_\_
  - Function Interfaces and Callback-Based Code
- Comparisons: \_\_lt\_\_, \_\_gt\_\_, and Others
- Boolean Tests: \_\_bool\_\_ and \_\_len\_\_
- Object Destruction: \_\_del\_\_
  - Destructor Usage Notes

#### Chapter 31. Designing with Classes
- Python and OOP
  - Polymorphism Means Interfaces, Not Call Signatures
- OOP and Inheritance: "Is-a" Relationships
- OOP and Composition: "Has-a" Relationships
  - Stream Processors Revisited
- OOP and Delegation: "Like-a" Relationships
- Pseudoprivate Class Attributes
  - Name Mangling Overview
  - Why Use Pseudoprivate Attributes?
- Method Objects: Bound or Not
  - Bound Methods in Action
- Classes Are Objects: Generic Object Factories
  - Why Factories?
- Multiple Inheritance and the MRO
  - How Multiple Inheritance Works
  - How the MRO Works
  - Attribute Conflict Resolution
  - Example: "Mix-in" Attribute Listers
  - Example: Mapping Attributes to Inheritance Sources

#### Chapter 32. Class Odds and Ends
- Extending Built-in Object Types
  - Extending Types by Embedding
  - Extending Types by Subclassing
- The Python Object Model
  - Classes Are Types Are Classes
  - Some Instances Are More Equal Than Others
  - The Inheritance Bifurcation
  - The Metaclass/Class Dichotomy
  - And One "object" to Rule Them All
- Advanced Attribute Tools
  - Slots: Attribute Declarations
  - Properties: Attribute Accessors
  - \_\_getattribute\_\_ and Descriptors: Attribute Implementations
- Static and Class Methods
  - Why the Special Methods?
  - Plain-Function Methods
  - Static Method Alternatives
  - Using Static and Class Methods
  - Counting Instances with Static Methods
  - Counting Instances with Class Methods
- Decorators and Metaclasses
  - Function Decorator Basics
  - A First Look at User-Defined Function Decorators
  - A First Look at Class Decorators and Metaclasses
  - For More Details
- The super Function
  - The super Basics
  - The super Details
  - The super Wrap-Up
- Class Gotchas
  - Changing Class Attributes Can Have Side Effects
  - Changing Mutable Class Attributes Can Have Side Effects, Too
  - Multiple Inheritance: Order Matters
  - Scopes in Methods and Classes
  - Miscellaneous Class Gotchas
  - "Overwrapping-itis"

---

### Part VII. Exceptions

#### Chapter 33. Exception Basics
- Why Use Exceptions?
  - Exception Roles
- Exceptions: The Short Story
  - Default Exception Handler
  - Catching Exceptions
  - Raising Exceptions
  - User-Defined Exceptions
  - Termination Actions

#### Chapter 34. Exception Coding Details
- The try Statement
  - try Statement Clauses
  - The except and else Clauses
  - The finally Clause
  - Combined try Clauses
- The raise Statement
  - Raising Exceptions
  - The except as hook
  - Scopes and except as
  - Propagating Exceptions with raise
  - Exception Chaining: raise from
- The assert Statement
  - Example: Trapping Constraints (but Not Errors!)
- The with Statement and Context Managers
  - Basic with Usage
  - The Context-Management Protocol
  - Multiple Context Managers
  - The Termination-Handlers Shoot-Out

#### Chapter 35. Exception Objects
- Exception Classes
  - Coding Exceptions Classes
  - Why Exception Hierarchies?
- Built-in Exception Classes
  - Built-in Exception Categories
  - Default Printing and State
- Custom Print Displays
- Custom State and Behavior
  - Providing Exception Details
  - Providing Exception Methods
- Exception Groups: Yet Another Star!

#### Chapter 36. Exception Odds and Ends
- Nesting Exception Handlers
  - Example: Control-Flow Nesting
  - Example: Syntactic Nesting
- Exception Idioms
  - Breaking Out of Multiple Nested Loops: "go to"
  - Exceptions Aren't Always Errors
  - Functions Can Signal Conditions with raise
  - Closing Files and Server Connections
  - Debugging with Outer try Statements
  - Running In-Process Tests
  - More on sys.exc\_info
  - Displaying Errors and Tracebacks
- Exception Design Tips and Gotchas
  - What Should Be Wrapped
  - Catching Too Much: Avoid Empty except and Exception
  - Catching Too Little: Use Class-Based Categories
- Core Language Wrap-Up
  - The Python Toolset
  - Development Tools for Larger Projects

---

### Part VIII. Advanced Topics

#### Chapter 37. Unicode and Byte Strings
- Unicode Foundations
  - Character Representations
  - Character Encodings
- Introducing Python String Tools
  - The str Object
  - The bytes Object
  - The bytearray Object
  - Text and Binary Files
- Using Text Strings
  - Literals and Basic Properties
  - String Type Conversions
  - Coding Unicode Strings in Python
  - Source-File Encoding Declarations
- Using Byte Strings
  - Methods
  - Sequence Operations
  - Formatting
  - Other Ways to Make Bytes
  - Mixing String Types
  - The bytearray Object
- Using Text and Binary Files
  - Text-File Basics
  - Text and Binary Modes
  - Unicode-Text Files
- Unicode, Bytes, and Other String Tools
  - The re Pattern-Matching Module
  - The struct Binary-Data Module
  - The pickle and json Serialization Modules
  - Filenames in open and Other Filename Tools
- The Unicode Twilight Zone
  - Dropping the BOM in Python
  - Unicode Normalization: Whither Standard?

#### Chapter 38. Managed Attributes
- Why Manage Attributes?
  - Inserting Code to Run on Attribute Access
- Properties
  - The Basics
  - A First Example
  - Computed Attributes
  - Coding Properties with Decorators
- Descriptors
  - The Basics
  - A First Example
  - Computed Attributes
  - Using State Information in Descriptors
  - How Properties and Descriptors Relate
- \_\_getattr\_\_ and \_\_getattribute\_\_
  - The Basics
  - A First Example
  - Computed Attributes
  - \_\_getattr\_\_ and \_\_getattribute\_\_ Compared
  - Management Techniques Compared
  - Intercepting Built-in Operation Attributes
- Example: Attribute Validations
  - Using Properties to Validate
  - Using Descriptors to Validate
  - Using \_\_getattr\_\_ to Validate
  - Using \_\_getattribute\_\_ to Validate

#### Chapter 39. Decorators
- What's a Decorator?
  - Managing Calls and Instances
  - Managing Functions and Classes
  - Using and Defining Decorators
  - Why Decorators?
- The Basics
  - Function Decorator Basics
  - Class Decorator Basics
  - Decorator Nesting
  - Decorator Arguments
  - Decorators Manage Functions and Classes, Too
- Coding Function Decorators
  - Tracing Function Calls
  - Decorator State Retention Options
  - Class Pitfall: Decorating Methods
  - Timing Function Calls
  - Adding Decorator Arguments
- Coding Class Decorators
  - Singleton Classes
  - Tracing Object Interfaces
  - Class Pitfall: Retaining Multiple Instances
- Example: "Private" and "Public" Attributes
  - Implementing Private Attributes
  - Implementation Details I
  - Generalizing for Public Declarations
  - Implementation Details II
  - Delegating Built-In Operations
- Example: Validating Function Arguments
  - The Goal
  - A Basic Range-Testing Decorator for Positional Arguments
  - Generalizing for Keywords and Defaults
  - Implementation Details
  - Open Issues
  - Decorator Arguments Versus Function Annotations

#### Chapter 40. Metaclasses and Inheritance
- To Metaclass or Not to Metaclass
  - The Downside of "Helper" Functions
  - Metaclasses Versus Class Decorators: Round 1
- The Metaclass Model
  - Classes Are Instances of type
  - Metaclasses Are Subclasses of type
  - Class Statements Call a type
  - Class Statements Can Choose a type
  - Metaclass Method Protocol
- Coding Metaclasses
  - A Basic Metaclass
  - Customizing Construction and Initialization
  - Other Metaclass Coding Techniques
  - Managing Classes with Metaclasses and Decorators
- Inheritance: The Finale
  - Metaclass Versus Superclass
  - Metaclass Inheritance
  - Python Inheritance Algorithm: The Simple Version
  - Python Inheritance Algorithm: The Less Simple Version
  - The Inheritance Wrap-Up
- Metaclass Methods
  - Metaclass Methods Versus Class Methods
  - Operator Overloading in Metaclass Methods
  - Metaclass Methods Versus Instance Methods

#### Chapter 41. All Good Things
- The Python Tsunami
- The Python Sandbox
- The Python Upside
- Closing Thoughts
- Where to Go from Here
- Encore: Print Your Own Completion Certificate!

---

### Part IX. Appendixes

#### Appendix A. Platform Usage Tips
- Using Python on Windows
- Using Python on macOS
- Using Python on Linux
- Using Python on Android
- Using Python on iOS
- Standalone Apps and Executables
- Etcetera

#### Appendix B. Solutions to End-of-Part Exercises
- Part I, Getting Started
- Part II, Objects and Operations
- Part III, Statements and Syntax
- Part IV, Functions and Generators
- Part V, Modules and Packages
- Part VI, Classes and OOP
- Part VII, Exceptions

---

### Index
### About the Author
