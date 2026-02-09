# Files: Basic Writing and Reading — Answers

## Snippet 1

**Expected output:**
```
'Hello\nWorld\n'
['Hello', 'World', '']
```

**Rationale:**
- `f.write("Hello\n")` writes the string `Hello\n` to the file. `f.write("World\n")` appends `World\n`. The file now contains `Hello\nWorld\n`.
- `f.read()` reads the entire file as a single string. `repr(content)` shows the string with escape characters visible: `'Hello\nWorld\n'`.
- `content.split("\n")` splits on every newline character. The string `"Hello\nWorld\n"` has newlines after "Hello" and after "World". Splitting on `"\n"` yields `['Hello', 'World', '']`. The trailing empty string appears because the string ends with `\n` — splitting `"X\n"` on `"\n"` gives `['X', '']`. This is a common gotcha with `.split("\n")` on files that end with a newline.

## Snippet 2

**Expected output:**
```
'Hello\n'
'World\n'
''
['Hello\n', 'World\n']
```

**Rationale:**
- `f.readline()` reads one line at a time, including the trailing newline character. The first call returns `'Hello\n'`, the second returns `'World\n'`.
- The third `f.readline()` call returns `''` (an empty string) because the file cursor has reached the end of the file. An empty string from `readline()` signals end-of-file. This is distinct from a blank line, which would return `'\n'`.
- `f.readlines()` (on a freshly opened file) reads all lines into a list, with each line retaining its trailing newline: `['Hello\n', 'World\n']`.
