import json
import random
from timing import timeit
from search import linear_search, binary_search, set_search


def make_data(n: int, seed: int = 42) -> list:
    random.seed(seed)
    data = [random.randint(1, n * 10) for _ in range(n)]
    data.sort()
    return data


def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries=100) -> dict:
    results = {
        "sizes": list(sizes),
        "linear": [],
        "binary": [],
        "set": []
    }

    # 固定隨機數種子以使查詢目標一致
    random.seed(12345)

    for size in sizes:
        data = make_data(size)

        # 產生查詢目標 (50% 存在於 data 中，50% 為隨機數)
        targets = []
        for _ in range(queries):
            if random.random() < 0.5 and len(data) > 0:
                targets.append(random.choice(data))
            else:
                targets.append(random.randint(1, size * 10))

        @timeit(repeat=3)
        def time_linear():
            for t in targets:
                linear_search(data, t)

        @timeit(repeat=3)
        def time_binary():
            for t in targets:
                binary_search(data, t)

        @timeit(repeat=3)
        def time_set():
            for t in targets:
                set_search(data, t)

        time_linear()
        time_binary()
        time_set()

        results["linear"].append(time_linear.last_elapsed)
        results["binary"].append(time_binary.last_elapsed)
        results["set"].append(time_set.last_elapsed)

    return results


def print_table(results):
    print(f"{'Size':<10} | {'Linear (s)':<12} | {'Binary (s)':<12} | {'Set (s)':<12}")
    print("-" * 55)
    for i, size in enumerate(results["sizes"]):
        print(
            f"{size:<10} | "
            f"{results['linear'][i]:<12.6f} | "
            f"{results['binary'][i]:<12.6f} | "
            f"{results['set'][i]:<12.6f}"
        )


if __name__ == "__main__":
    results = run_benchmark()
    print_table(results)
    with open("results.json", "w") as f:
        json.dump(results, f, indent=4)
