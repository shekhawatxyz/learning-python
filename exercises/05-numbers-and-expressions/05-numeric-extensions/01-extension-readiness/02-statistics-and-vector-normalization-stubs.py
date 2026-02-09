# Step 2: Statistics and vector normalization
# Complete each stub according to the requirements.

# --- Stub 1 ---
# Implement:
# - mean(data): arithmetic mean
# - centered(data): each value minus mean(data)


def mean(data):
    ...


def centered(data):
    ...


sample = [10, 13, 15, 22]

sample_mean = mean(sample)
sample_centered = centered(sample)


# --- Stub 2 ---
# Implement cosine similarity:
# cos(a, b) = dot(a, b) / (||a|| * ||b||)


def cosine_similarity(a, b):
    ...


a = [1, 2, 3]
b = [4, 5, 6]

cos_ab = cosine_similarity(a, b)
cos_orthogonal = cosine_similarity([1, 0], [0, 1])


# --- Tests ---

assert sample_mean == 15.0, (
    f"Expected sample_mean 15.0, got {sample_mean!r}."
)

assert sample_centered == [-5.0, -2.0, 0.0, 7.0], (
    f"Expected centered sample [-5.0, -2.0, 0.0, 7.0], got {sample_centered!r}."
)

assert abs(cos_ab - 0.9746318461970762) < 1e-12, (
    f"Expected cos_ab about 0.9746318461970762, got {cos_ab!r}."
)

assert cos_orthogonal == 0.0, (
    f"Expected cos_orthogonal 0.0, got {cos_orthogonal!r}."
)

print("All tests passed!")
