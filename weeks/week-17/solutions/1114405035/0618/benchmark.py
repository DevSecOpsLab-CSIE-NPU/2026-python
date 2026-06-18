import json
import random
from timing import timeit
from search import (
    linear_search,
    binary_search,
    set_search,
    builtin_linear_search,
    builtin_binary_search,
)


def make_data(n: int, seed: int = 42) -> list:
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n 必須是正整數")
    random.seed(seed)
    data = [random.randint(1, n * 10) for _ in range(n)]
    data.sort()
    return data



def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries=100) -> dict:
    results = {
        "sizes": list(sizes),
        "linear": [],
        "binary": [],
        "set": [],
        "builtin_linear": [],
        "builtin_binary": [],
        "set_optimized": [],
    }

    random.seed(12345)

    for size in sizes:
        data = make_data(size)

        # 產生查詢目標
        targets = []
        for _ in range(queries):
            if random.random() < 0.5 and len(data) > 0:
                targets.append(random.choice(data))
            else:
                targets.append(random.randint(1, size * 10))

        # 1. Custom Linear Search
        @timeit(repeat=3)
        def time_linear():
            for t in targets:
                linear_search(data, t)

        # 2. Custom Binary Search
        @timeit(repeat=3)
        def time_binary():
            for t in targets:
                binary_search(data, t)

        # 3. Custom Set Search (每次內部轉 set)
        @timeit(repeat=3)
        def time_set():
            for t in targets:
                set_search(data, t)

        # 4. Built-in Linear (C-based list.index)
        @timeit(repeat=3)
        def time_builtin_linear():
            for t in targets:
                builtin_linear_search(data, t)

        # 5. Built-in Binary (bisect)
        @timeit(repeat=3)
        def time_builtin_binary():
            for t in targets:
                builtin_binary_search(data, t)

        # 6. Optimized Set (外面先建好 set)
        @timeit(repeat=3)
        def time_set_optimized():
            prebuilt_set = set(data)
            for t in targets:
                t in prebuilt_set

        time_linear()
        time_binary()
        time_set()
        time_builtin_linear()
        time_builtin_binary()
        time_set_optimized()

        results["linear"].append(time_linear.last_elapsed)
        results["binary"].append(time_binary.last_elapsed)
        results["set"].append(time_set.last_elapsed)
        results["builtin_linear"].append(time_builtin_linear.last_elapsed)
        results["builtin_binary"].append(time_builtin_binary.last_elapsed)
        results["set_optimized"].append(time_set_optimized.last_elapsed)

    return results


def run_crossover_experiment(queries=100) -> dict:
    # 測試一系列小規模 size，找出交叉點
    sizes_to_test = [10, 50, 100, 200, 500, 1000, 2000, 5000]
    crossover_results = {
        "sizes": sizes_to_test,
        "linear_total": [],
        "sort_and_binary_total": [],
    }

    random.seed(999)
    for size in sizes_to_test:
        # 產生隨機未排序資料
        data = [random.randint(1, size * 10) for _ in range(size)]

        targets = [
            random.choice(data) if random.random() < 0.5 else random.randint(1, size * 10)
            for _ in range(queries)
        ]

        # 策略 A: 直接 linear_search
        @timeit(repeat=3)
        def run_linear():
            for t in targets:
                linear_search(data, t)

        # 策略 B: 排序一次 + binary_search
        @timeit(repeat=3)
        def run_sort_and_binary():
            data_copy = data.copy()
            data_copy.sort()
            for t in targets:
                binary_search(data_copy, t)

        run_linear()
        run_sort_and_binary()

        crossover_results["linear_total"].append(run_linear.last_elapsed)
        crossover_results["sort_and_binary_total"].append(run_sort_and_binary.last_elapsed)

    # 找出交叉點 N
    crossover_n = None
    for i, size in enumerate(sizes_to_test):
        t_linear = crossover_results["linear_total"][i]
        t_sort_binary = crossover_results["sort_and_binary_total"][i]
        if t_sort_binary < t_linear:
            crossover_n = size
            break

    crossover_results["crossover_n"] = crossover_n
    return crossover_results


def print_tables(results, crossover):
    print("=== Main Benchmark ===")
    headers = ["Size", "Linear(s)", "Binary(s)", "Set(s)", "Builtin-Lin(s)", "Builtin-Bin(s)", "Set-Opt(s)"]
    print(f"{headers[0]:<8} | {headers[1]:<11} | {headers[2]:<11} | {headers[3]:<11} | {headers[4]:<14} | {headers[5]:<14} | {headers[6]:<11}")
    print("-" * 95)
    for i, size in enumerate(results["sizes"]):
        print(
            f"{size:<8} | "
            f"{results['linear'][i]:<11.6f} | "
            f"{results['binary'][i]:<11.6f} | "
            f"{results['set'][i]:<11.6f} | "
            f"{results['builtin_linear'][i]:<14.6f} | "
            f"{results['builtin_binary'][i]:<14.6f} | "
            f"{results['set_optimized'][i]:<11.6f}"
        )

    print("\n=== Crossover Experiment (Sort + Binary vs Linear) ===")
    print(f"{'Size (N)':<10} | {'Linear Total (s)':<18} | {'Sort + Binary (s)':<18} | {'Winner':<10}")
    print("-" * 62)
    for i, size in enumerate(crossover["sizes"]):
        t_lin = crossover["linear_total"][i]
        t_bin = crossover["sort_and_binary_total"][i]
        winner = "Binary" if t_bin < t_lin else "Linear"
        print(f"{size:<10} | {t_lin:<18.6f} | {t_bin:<18.6f} | {winner:<10}")

    print(f"\n[Crossover Point] 'Sort + Binary' wins starting at N = {crossover['crossover_n']}")


if __name__ == "__main__":
    results = run_benchmark()
    crossover = run_crossover_experiment()
    print_tables(results, crossover)

    output = {"benchmark": results, "crossover": crossover}
    with open("results.json", "w") as f:
        json.dump(output, f, indent=4)
