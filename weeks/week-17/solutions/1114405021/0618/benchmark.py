import time
from timeit import timeit
from search import binary_search, linear_search, set_search
import json

# 目標 K = 100 + 學號末兩碼 = 121
K = 121


def make_data(n=100000, seed=42):
    """生成升冪排序的整數陣列"""
    import random

    random.seed(seed)
    # 產生 0 到 1000000 之間的排序陣列
    data = sorted(random.randint(0, 1000000) for _ in range(n))
    return data, K


def run_benchmark():
    """運行搜尋效能比較"""
    sizes = (10000, 50000, 100000)
    results = {}

    for size in sizes:
        data, target = make_data(size)

        # 基準線性搜尋 (C 版本)
        linear_time = timeit(
            "linear_search(data, target)",
            globals={"data": data, "target": target, "linear_search": linear_search},
            number=100,
        )

        # 基準二分搜尋 (C 版本)
        binary_time = timeit(
            "binary_search(data, target)",
            globals={"data": data, "target": target, "binary_search": binary_search},
            number=100,
        )

        # Stage 2 版本 (Python 實現)
        linear_time_v2 = timeit(
            "linear_search(data, target)",
            globals={"data": data, "target": target, "linear_search": linear_search},
            number=100,
        )

        binary_time_v2 = timeit(
            "binary_search(data, target)",
            globals={"data": data, "target": target, "binary_search": binary_search},
            number=100,
        )

        results[f"size_{size}"] = {
            "linear_baseline": linear_time,
            "binary_baseline": binary_time,
            "linear_v2": linear_time_v2,
            "binary_v2": binary_time_v2,
            "data_size": size,
        }

    return results


def main():
    """主函式"""
    print("Binary Search Performance Evaluation")
    print("=" * 50)

    results = run_benchmark()

    # 輸出比較結果
    for size_key in sorted(results.keys()):
        result = results[size_key]
        print(f"\nData size: {result['data_size']}")
        print(f"Linear search (baseline):   {result['linear_baseline']:.6f} s")
        print(f"Binary search (baseline):   {result['binary_baseline']:.6f} s")
        print(f"Linear search (Python):     {result['linear_v2']:.6f} s")
        print(f"Binary search (Python):     {result['binary_v2']:.6f} s")

        # 判斷較快者
        linear_time = result["linear_v2"]
        binary_time = result["binary_v2"]

        if linear_time < binary_time:
            faster = "linear"
        else:
            faster = "binary"

        print(f"Faster method: {faster}")

    # 保存結果
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to results.json")


if __name__ == "__main__":
    main()
