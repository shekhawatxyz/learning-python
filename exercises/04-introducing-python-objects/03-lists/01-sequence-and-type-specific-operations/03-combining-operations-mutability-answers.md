# Step 3: Combining operations, the mutability factor — Answer Key

## Snippet 1

**Expected output:**

```
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3]
```

**Rationale:**

This snippet tests the critical distinction between shared references and copies.

- First block: `M = L` does NOT copy the list. Both `L` and `M` point to the same list object in memory. When `L.append(4)` mutates that object, both names see the change. So both print `[1, 2, 3, 4]`.
- Second block: `M = L[:]` creates a shallow copy of L. Now L and M refer to different list objects (with the same contents). When `L.append(4)` mutates L's object, M's separate object is unaffected. So L prints `[1, 2, 3, 4]` but M prints `[1, 2, 3]`.

This is one of the most important concepts in Python: assignment creates shared references to the same object, not copies. The slice `[:]` is one way to make a copy.

## Snippet 2

**Expected output:**

```
[3, 1, 2]
[1, 2, 3]
[1, 2, 3]
```

**Rationale:**

- `sorted(original)` is a built-in function that returns a **new** sorted list. It does not modify `original`. So `original` remains `[3, 1, 2]` and `sorted_copy` is `[1, 2, 3]`.
- `original.sort()` is a method that sorts the list **in place** and returns `None`. After this call, `original` itself is now `[1, 2, 3]`.

The key distinction: `sorted()` creates a new list (non-destructive); `.sort()` mutates the existing list (destructive). Use `sorted()` when you need to preserve the original order; use `.sort()` when you don't.
