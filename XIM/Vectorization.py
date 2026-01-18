import numpy as np
import random

# --- a. Pure Python version ---
def sum_squares_python(x: list[float]) -> float:
    total = 0.0
    for xi in x:
        total += xi * xi
    return total

# --- b. NumPy vectorized version ---
def sum_squares_numpy(x: np.ndarray) -> float:
    return np.sum(x ** 2)

# --- Benchmarking ---
sizes = [1000, 10000, 100000, 1000000]

for n in sizes:
    print(f"\nArray size: {n}")

    # Generate test data
    x_list = [random.random() for _ in range(n)]
    x_np = np.array(x_list)

    print("Python loop:")
    %timeit sum_squares_python(x_list)

    print("NumPy vectorized:")
    %timeit sum_squares_numpy(x_np)
