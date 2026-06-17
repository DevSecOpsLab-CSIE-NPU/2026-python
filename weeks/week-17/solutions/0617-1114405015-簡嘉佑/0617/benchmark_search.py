from search import binary_search, linear_search
from timing import timeit


N = 200_000
DATA_SORTED = list(range(N))
TARGET = N - 1


@timeit(repeat=5)
def run_linear(data, target):
    return linear_search(data, target)


@timeit(repeat=5)
def run_binary(data, target):
    return binary_search(data, target)


if __name__ == "__main__":
    idx_linear = run_linear(DATA_SORTED, TARGET)
    idx_binary = run_binary(DATA_SORTED, TARGET)

    print("linear index:", idx_linear)
    print("binary index:", idx_binary)
    print("linear records:", run_linear.records)
    print("binary records:", run_binary.records)
    print("linear avg:", run_linear.last_elapsed)
    print("binary avg:", run_binary.last_elapsed)
    print("speedup (linear/binary):", run_linear.last_elapsed / run_binary.last_elapsed)
