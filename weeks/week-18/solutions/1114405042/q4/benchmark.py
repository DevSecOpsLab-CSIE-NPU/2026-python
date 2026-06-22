"""基准测试脚本，用于第4题的搜索性能评估

实现以下功能：
1. make_data: 生成指定大小和种类的测试数据
2. run_benchmark: 运行三种搜索算法的基准测试

使用 timeit 装饰器进行精确的时间测量，
并生成 JSON 格式的结果文件用于后续分析和绘图。
"""

import json
import random
from typing import Dict, List, Tuple
from timing import timeit
from search import linear_search, binary_search, set_search


def make_data(n: int, seed: int = 42) -> List[int]:
    """生成指定大小的测试数据

    参数:
        n: 数据列表的大小
        seed: 随机种子，用于确保实验可重现性

    返回:
        生成的包含 [0, n) 范围内随机整数的列表
    """
    if n < 0:
        raise ValueError("n 必须 >= 0")

    random.seed(seed)
    return random.sample(range(n), min(n, n))


def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries: int = 100) -> Dict:
    """运行三种搜索算法的基准测试

    参数:
        sizes: 要测试的不同数据规模，默认为 (1000, 5000, 20000, 80000)
        queries: 每次测试要查询的目标数量，默认为 100

    返回:
        包含基准测试结果的字典
    """
    result = {"data": {}, "results": {}}

    # 保存本次实验的参数
    result["data"]["sizes"] = sizes
    result["data"]["queries"] = queries
    result["data"]["seed"] = 42

    all_results = []

    for n in sizes:
        # 生成测试数据
        data = make_data(n)
        sorted_data = sorted(data)

        # 为每次测试准备随机查询目标
        random.seed(123)  # 固定查询目标，确保可重现
        targets = [random.randint(0, n * 2) for _ in range(queries)]

        # 线性搜索测试
        @timeit
        def linear_test():
            for target in targets:
                linear_search(data, target)

        linear_test()  # 运行并收集记录
        linear_result = {
            "total_time": sum(linear_test.records),
            "avg_time": linear_test.last_elapsed,
            "records": linear_test.records
        }

        # 二分搜索测试
        @timeit
        def binary_test():
            for target in targets:
                binary_search(sorted_data, target)

        binary_test()  # 运行并收集记录
        binary_result = {
            "total_time": sum(binary_test.records),
            "avg_time": binary_test.last_elapsed,
            "records": binary_test.records
        }

        # 集合搜索测试
        @timeit
        def set_test():
            data_set = set(data)
            for target in targets:
                _ = data_set.__contains__(target)

        set_test()  # 运行并收集记录
        set_result = {
            "total_time": sum(set_test.records),
            "avg_time": set_test.last_elapsed,
            "records": set_test.records
        }

        all_results.append({
            "n": n,
            "linear": linear_result,
            "binary": binary_result,
            "set": set_result
        })

    result["results"] = all_results
    return result


if __name__ == "__main__":
    # 运行基准测试
    benchmark_result = run_benchmark()

    # 打印结果
    print("基准测试结果：")
    for item in benchmark_result["results"]:
        n = item["n"]
        linear = item["linear"]
        binary = item["binary"]
        set_result = item["set"]

        print(f"\n数据规模 n={n}:")
        print(f"  线性搜索: 总耗时={linear['total_time']:.4f}秒, 平均耗时={linear['avg_time']:.6f}秒")
        print(f"  二分搜索: 总耗时={binary['total_time']:.4f}秒, 平均耗时={binary['avg_time']:.6f}秒")
        print(f"  集合搜索: 总耗时={set_result['total_time']:.4f}秒, 平均耗时={set_result['avg_time']:.6f}秒")

    # 保存结果到JSON文件
    with open("results.json", "w") as f:
        json.dump(benchmark_result, f, indent=2, default=str)

    print("\n结果已保存到results.json")