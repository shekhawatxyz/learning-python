# Step 2: Precedence and promotion — Answer Key

## Snippet 1

**Expected output:**

```text
True
True
```

**Rationale:** Arithmetic operators run before comparisons, and comparisons before `and`. `not` binds tighter than `and`, so logical grouping matters.

## Snippet 2

**Expected output:**

```text
20.0
50.0
(8+2j)
float complex
```

**Rationale:** Parentheses change arithmetic grouping. Mixed arithmetic promotes `int -> float -> complex` as needed, and the resulting runtime types reflect that promotion.
