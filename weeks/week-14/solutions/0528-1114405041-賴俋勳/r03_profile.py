"""
R03 拆分版：效能測量基本用法。

重點：
1. 計時（perf_counter）
2. timeit 比較寫法
3. cProfile + pstats 熱點資訊
"""

from __future__ import annotations

import cProfile
import io
import math
import pstats
import time
import timeit
from functools import wraps
from typing import Any, Callable


def timed(func: Callable[..., Any]) -> Callable[..., tuple[Any, float]]:
    """計時裝飾器，回傳 (結果, 秒數)。"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> tuple[Any, float]:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return result, elapsed

    return wrapper


@timed
def sum_of_squares(n: int) -> int:
    """計算 0 到 n-1 的平方和。"""
    return sum(i * i for i in range(n))


def bench_timeit(n: int = 10_000, number: int = 100) -> dict[str, float]:
    """比較生成式與 map+lambda 的執行時間。"""
    genexp_time = timeit.timeit(
        "sum(i*i for i in range(n))", globals={"n": n}, number=number
    )
    map_lambda_time = timeit.timeit(
        "sum(map(lambda i: i*i, range(n)))", globals={"n": n}, number=number
    )
    return {"genexp": genexp_time, "map_lambda": map_lambda_time}


def workload(limit: int = 5000) -> float:
    """提供 profile 的穩定工作負載。"""
    total = 0.0
    for i in range(1, limit):
        total += math.sqrt(i) * math.sin(i)
    return total


def bench_cprofile(limit: int = 5000, top_n: int = 5) -> str:
    """執行 cProfile，回傳報表字串。"""
    pr = cProfile.Profile()
    pr.enable()
    workload(limit)
    pr.disable()

    buf = io.StringIO()
    pstats.Stats(pr, stream=buf).sort_stats("cumulative").print_stats(top_n)
    return buf.getvalue()
