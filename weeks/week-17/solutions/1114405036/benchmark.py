
"""Stage 2/3 — 用自製的 timeit 量三種搜尋，並（Stage 3）加上 baseline 與交叉點。
 
量測方式：固定 seed 產生「已排序、無重複」的整數 list，對每個 size 隨機抽
`queries` 個 target（一半存在、一半不存在），用 timing.timeit 量「跑完
queries 次查詢」的耗時，repeat 取平均。
 
Stage 3 baseline：
  - builtin_in：`target in data`（list 線性掃描的 C 版，linear 的對照）
  - bisect_search：用標準庫 `bisect`（binary 的標準版對照）
 
set / bisect 的優勢要查很多次才顯現，所以量的是「查 queries 次」的總時。
results.json 是 Stage 4 雷達圖的輸入。
"""
 
import bisect
import json
import random
from pathlib import Path
 
from search import binary_search, linear_search, set_search
from timing import timeit
 
RESULTS_PATH = Path(__file__).with_name("results.json")
 
 
def make_data(n: int, seed: int = 42) -> list:
    """產生已排序、無重複的整數 list，固定 seed 以便重現。
 
    輸入驗證（OpenSSF 03 Numbers / CWE-20）：明確拒絕非整數或負數的 n，丟出
    語意清楚的 ValueError，而不是讓 range()/random 拋出語意不清的 TypeError。
    bool 雖是 int 子類，但當長度用屬語意錯誤，一併擋掉。
    """
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError(f"n 必須是 >= 0 的整數，收到 {n!r}")
    rng = random.Random(seed)
    # 從較大的範圍取樣以保證無重複，再排序滿足 binary_search 的前提
    return sorted(rng.sample(range(n * 3 + 1), n))
 
 
def _make_queries(data: list, n: int, queries: int, seed: int = 7) -> list:
    """產生查詢目標：一半取自 data（存在）、一半取 data 外的值（不存在）。"""
    rng = random.Random(seed)
    present = [rng.choice(data) for _ in range(queries // 2)] if data else []
    absent = [-(i + 1) for i in range(queries - len(present))]  # 負數一定不在
    targets = present + absent
    rng.shuffle(targets)
    return targets
 
 
def builtin_in(data: list, target) -> bool:
    """baseline：內建 list 成員測試（C 層線性掃描）。"""
    return target in data
 
 
def bisect_search(data: list, target) -> int:
    """baseline：用標準庫 bisect 做二分搜尋，找不到回 -1。"""
    idx = bisect.bisect_left(data, target)
    if idx < len(data) and data[idx] == target:
        return idx
    return -1
 
 
def _time_over_queries(func, data, targets, repeat=3) -> float:
    @timeit(repeat=repeat)
    def run_all():
        for t in targets:
            func(data, t)
 
    run_all()
    return run_all.last_elapsed
 
 
def run_benchmark(sizes=(1000, 5000, 20000, 80000), queries=100) -> dict:
    """對每個 size 量五種方法查 queries 次的耗時，回傳結果 dict。"""
    methods = {
        "linear_search": linear_search,
        "binary_search": binary_search,
        "set_search": set_search,
        "builtin_in": builtin_in,
        "bisect_search": bisect_search,
    }
    results = {}
    for n in sizes:
        data = make_data(n)
        targets = _make_queries(data, n, queries)
        results[str(n)] = {
            name: _time_over_queries(func, data, targets)
            for name, func in methods.items()
        }
    return {"queries": queries, "sizes": list(sizes), "results": results}
 
 
def find_crossover(report: dict) -> dict:
    """估「先排序一次 + 之後每次 binary」何時開始贏過「每次 linear」。
 
    以每個 size 量到的單次成本推算：linear 總成本 ≈ q * t_linear_per_query；
    binary 路線 ≈ sort_cost + q * t_binary_per_query。回傳每個 size 下需要
    幾次查詢 q 才回本（sort_cost 用 sorted(data) 的實測時間估）。
    """
    crossover = {}
    for n_str in report["results"]:
        n = int(n_str)
        data = make_data(n)
        # 真實情境是把「未排序」的資料排序一次，所以對打散後的副本計時；
        # 直接 sorted() 已排序資料會觸發 Timsort 的最佳情況 O(n)，低估成本。
        shuffled = data[:]
        random.Random(99).shuffle(shuffled)
        timed_sort = timeit(sorted)
        timed_sort(shuffled)
        sort_cost = timed_sort.last_elapsed
        q = report["queries"]
        per_linear = report["results"][n_str]["linear_search"] / q
        per_binary = report["results"][n_str]["binary_search"] / q
        # sort_cost + q* per_binary < q * per_linear  → q > sort_cost/(per_linear-per_binary)
        gain = per_linear - per_binary
        breakeven = sort_cost / gain if gain > 0 else None
        crossover[n_str] = {
            "sort_cost": sort_cost,
            "per_query_linear": per_linear,
            "per_query_binary": per_binary,
            "breakeven_queries": breakeven,
        }
    return crossover
 
 
def load_results(path=RESULTS_PATH) -> dict:
    """讀回 results.json。
 
    安全考量：
      - 04 Neutralization / CWE-502：一律用 json，不用 pickle——後者在
        反序列化時會執行任意程式碼，json 只還原資料，安全得多。
      - 05 Exception Handling / CWE-396：對不存在的檔案，讓 FileNotFoundError
        自然傳出，不用 bare except 把它吞掉成 None。
    """
    with open(path, encoding="utf-8") as f:
        return json.load(f)
 
 
def main():
    report = run_benchmark()
    report["crossover"] = find_crossover(report)
    with open(RESULTS_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
 
    print(f"queries = {report['queries']}（每個 size 查這麼多次）")
    header = f"{'n':>8} | {'linear':>10} | {'binary':>10} | {'set':>10} | {'in':>10} | {'bisect':>10}"
    print(header)
    print("-" * len(header))
    for n_str in report["results"]:
        r = report["results"][n_str]
        print(
            f"{n_str:>8} | {r['linear_search']:>10.6f} | {r['binary_search']:>10.6f} | "
            f"{r['set_search']:>10.6f} | {r['builtin_in']:>10.6f} | {r['bisect_search']:>10.6f}"
        )
    print(f"\n結果已寫入 {RESULTS_PATH.name}")
 
 
if __name__ == "__main__":
    main()