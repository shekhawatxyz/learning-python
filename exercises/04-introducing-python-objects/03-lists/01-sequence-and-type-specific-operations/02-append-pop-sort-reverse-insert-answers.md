# Step 2: append, pop, sort, reverse, insert — Answer Key

## Snippet 1

**Expected output:**

```
[3, 1, 4, 1, 5, 9]
[1, 1, 3, 4, 5, 9]
[9, 5, 4, 3, 1, 1]
1
```

**Rationale:**

- `L.append(9)` adds 9 to the end of L in place: `[3, 1, 4, 1, 5, 9]`.
- `L.sort()` sorts L in ascending order in place: `[1, 1, 3, 4, 5, 9]`.
- `L.reverse()` reverses L in place: `[9, 5, 4, 3, 1, 1]`.
- `L.pop()` removes and returns the **last** element: `1`. After this, L is `[9, 5, 4, 3, 1]`. Note that `.pop()` always removes from the end — the `9` at the front is not affected.
- All of these methods mutate the list in place. The key point is that the list object is being changed each time; these are not creating new lists.

## Snippet 2

**Expected output:**

```
None
[10, 20, 30, 40]
[10, 15, 20, 30, 40]
```

**Rationale:**

- `result = L.append(40)`: `.append()` modifies L in place and returns `None`. This is a common gotcha — in-place list methods do not return the modified list; they return `None`. So `result` is `None`.
- After the append, `L` is `[10, 20, 30, 40]`.
- `L.insert(1, 15)` inserts the value 15 at index 1, shifting everything from index 1 onward to the right: `[10, 15, 20, 30, 40]`. The first argument to `.insert()` is the index the new element will occupy.
