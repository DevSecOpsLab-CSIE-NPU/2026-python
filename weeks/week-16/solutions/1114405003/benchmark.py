import json
from timing import timeit
from sorts import bubble_sort, quick_sort, merge_sort, make_data


@timeit
def timed_bubble(data):
    return bubble_sort(data)


@timeit
def timed_quick(data):
    return quick_sort(data)


@timeit
def timed_merge(data):
    return merge_sort(data)


def run_benchmark(sizes=(500, 1000, 2000, 4000), repeats=3) -> dict:
    results = {}
    for n in sizes:
        data = make_data(n)
        row = {}
        for label, func in [("bubble", timed_bubble),
                            ("quick", timed_quick),
                            ("merge", timed_merge)]:
            func.records.clear()
            for _ in range(repeats):
                func(data)
            avg = sum(func.records) / len(func.records)
            row[label] = round(avg, 6)
        results[n] = row
    return results


def main():
    results = run_benchmark()
    header = f"{'n':>6} | {'bubble':>10} | {'quick':>10} | {'merge':>10}"
    sep = "-" * len(header)
    print(header)
    print(sep)
    for n, row in results.items():
        print(f"{n:>6} | {row['bubble']:>10.6f} | {row['quick']:>10.6f} | {row['merge']:>10.6f}")
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
