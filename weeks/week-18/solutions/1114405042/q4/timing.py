"""时间度量装饰器，用于测量函数执行时间

本装饰器用于第4题的性能评估，遵循以下规范：
- 被装饰函数的返回值保持不变
- 使用functools.wraps保留__name__/__doc__
- 每次调用实际运行repeat次（默认3次），每次耗时记录在f.records中
- f.last_elapsed = 本次repeat的平均耗时
- 装饰器内不准print
- repeat < 1 → raise ValueError
"""

import functools
import time


def timeit(func=None, *, repeat=3):
    """时间度量装饰器

    参数:
        func: 被装饰的函数
        repeat: 每次执行重复的次数，默认值为3

    返回:
        装饰后的函数
    """
    if repeat < 1:
        raise ValueError("repeat < 1")

    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            # 记录每次执行的耗时
            records = []

            for _ in range(repeat):
                start = time.perf_counter()
                result = f(*args, **kwargs)
                end = time.perf_counter()
                elapsed = end - start
                records.append(elapsed)

            # 计算平均耗时
            last_elapsed = sum(records) / len(records) if records else 0.0

            # 将时间信息附加到包装函数上
            wrapper.last_elapsed = last_elapsed
            wrapper.records = records

            return result

        return wrapper

    # 支持直接调用：@timeit或@timeit(repeat=5)
    if func is not None:
        return decorator(func)
    return decorator


if __name__ == "__main__":
    # 简单的测试
    @timeit
    def test_func(n):
        total = 0
        for i in range(n):
            total += i
        return total

    result, last_elapsed, records = test_func(1000)
    print(f"结果: {result}")
    print(f"平均耗时: {last_elapsed:.6f}秒")
    print(f"耗时记录: {records}")