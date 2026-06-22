import functools
import time


def timeit(func=None, *, repeat=3):
    """為函式增加計時功能。

    Args:
        func: 要裝飾的函式
        repeat: 每呼叫一次時實際跑的次數，預設 3

    Returns:
        裝飾後的函式

    Raises:
        ValueError: repeat < 1
    """
    if func is None:
        # Called as @timeit(repeat=5)
        def decorator(func_to_decorate):
            return timeit(func_to_decorate, repeat=repeat)

        return decorator

    if repeat < 1:
        raise ValueError(f"repeat 必須 >= 1，但得到 {repeat}")

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        records = []
        for _ in range(repeat):
            start_time = time.time()
            result = func(*args, **kwargs)
            elapsed = time.time() - start_time
            records.append(elapsed)
        wrapper.records = records
        wrapper.last_elapsed = sum(records) / len(records)
        return result

    return wrapper


if __name__ == "__main__":
    # 簡單測試
    @timeit
    def test():
        return "hello"

    print(f"Result: {test()}")
    print(f"Records: {test.records}")
    print(f"Last elapsed: {test.last_elapsed}")
