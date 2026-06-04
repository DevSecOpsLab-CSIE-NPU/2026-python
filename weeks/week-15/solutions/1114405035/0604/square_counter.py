import math


def count_squares(a: int, b: int) -> int:
    """回傳區間 [a, b] 之間（含端點）有幾個完全平方數。"""
    if a > b:
        raise ValueError("a must be <= b")

    # 使用 math.isqrt 計算開根號整數，避免浮點數精度問題
    # 計算 ceil(sqrt(a))
    root_a = math.isqrt(a)
    ceil_sqrt_a = root_a if root_a * root_a == a else root_a + 1

    # 計算 floor(sqrt(b))
    floor_sqrt_b = math.isqrt(b)

    if ceil_sqrt_a > floor_sqrt_b:
        return 0
    return floor_sqrt_b - ceil_sqrt_a + 1
