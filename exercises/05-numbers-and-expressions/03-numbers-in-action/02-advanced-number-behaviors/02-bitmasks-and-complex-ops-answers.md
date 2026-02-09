# Step 2: Bitmasks and complex operations — Answer Key

## Snippet 1

**Expected output:**

```text
5 0b101
False True
1
```

**Rationale:** Bit flags are combined with `|`, tested with `&`, and toggled with `^`. Boolean conversion of a masked result tells whether a flag is set.

## Snippet 2

**Expected output:**

```text
53
172
41
```

**Rationale:** Shifts move bit patterns left/right. Because Python integers are unbounded, `~` produces an infinite two's-complement negative value conceptually, so masking with `& 0xFF` is used to keep a byte-sized result.
