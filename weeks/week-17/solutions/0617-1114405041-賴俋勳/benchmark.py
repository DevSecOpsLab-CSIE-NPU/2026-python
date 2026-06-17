import random
from timing import timeit
from search import linear_search, binary_search


@timeit
def measure_linear(data, target):
    return linear_search(data, target)


@timeit
def measure_binary(data, target):
    return binary_search(data, target)


def main():
    n = 1000000
    data = list(range(n))

    target = random.randint(0, n - 1)

    print(f"Data size: {n}")
    print(f"Target: {target}")
    print()

    measure_linear(data, target, repeat=5)
    print(f"linear_search: avg={measure_linear.last_elapsed:.6f}s")
    print(f"  records: {measure_linear.records}")

    measure_binary(data, target, repeat=5)
    print(f"binary_search: avg={measure_binary.last_elapsed:.6f}s")
    print(f"  records: {measure_binary.records}")


if __name__ == "__main__":
    main()
