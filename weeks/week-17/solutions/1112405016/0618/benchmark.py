import json
import random
from timing import timeit
from search import linear_search, binary_search, set_search


def make_data(n: int, seed: int = 42) -> list:
    """產生指定長度且具備固定亂數種子的資料"""
    random.seed(seed)
    return [random.randint(0, n * 10) for _ in range(n)]


def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries=100) -> dict:
    """對三種搜尋演算法進行效能評估，量測查詢指定次數的總平均時間，並輸出結果"""
    results = {}

    for size in sizes:
        results[size] = {}
        data = make_data(size)
        sorted_data = sorted(data)

        # 產生固定的隨機查詢目標（一半在資料中，一半不在）
        random.seed(size)
        targets_in = random.sample(data, min(size, queries // 2))
        targets_out = [
            random.randint(size * 10 + 1, size * 20)
            for _ in range(queries - len(targets_in))
        ]
        targets = targets_in + targets_out
        random.shuffle(targets)

        # 1. 測試手寫 Linear Search 的總時間
        @timeit(repeat=3)
        def run_linear():
            for t in targets:
                linear_search(data, t)

        run_linear()
        results[size]["linear"] = run_linear.last_elapsed

        # 2. 測試手寫 Binary Search 的總時間
        @timeit(repeat=3)
        def run_binary():
            for t in targets:
                binary_search(sorted_data, t)

        run_binary()
        results[size]["binary"] = run_binary.last_elapsed

        # 3. 測試手寫 Set Search 的總時間（此處每次呼叫都會建 set）
        @timeit(repeat=3)
        def run_set():
            for t in targets:
                set_search(data, t)

        run_set()
        results[size]["set"] = run_set.last_elapsed

    # 印出精美的效能比較表
    print(f"\n{'='*55}")
    print(f" 搜尋效能評估表 (查詢次數: {queries} 次)")
    print(f"{'='*55}")
    print(f"{'N':<10} | {'Linear (s)':<12} | {'Binary (s)':<12} | {'Set (s)':<12}")
    print(f"{'-'*55}")
    for size in sizes:
        t_linear = results[size]["linear"]
        t_binary = results[size]["binary"]
        t_set = results[size]["set"]
        print(
            f"{size:<10} | {t_linear:<12.6f} | {t_binary:<12.6f} | {t_set:<12.6f}"
        )
    print(f"{'='*55}\n")

    # 存檔成 results.json
    # 將 dict key 轉成 str (json 限制)
    serializable_results = {str(k): v for k, v in results.items()}
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(serializable_results, f, indent=4)

    return results


if __name__ == "__main__":
    run_benchmark()
