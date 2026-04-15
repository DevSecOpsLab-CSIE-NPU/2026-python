"""
UVA 10101 - 木棒拼等式（正式版）

題意：
給一條不成立的等式（只含數字、+、-、=），
要把「一根」木棒從某個數字移到另一個數字，讓等式成立。

本版採用的模型：
1. 只允許改動數字字元（0~9），運算符不變。
2. 一次移動一根木棒 = 一個數字木棒數 -1，另一個數字木棒數 +1。
3. 改完後用整個等式字串重新計算左右值，若相等即為答案。
"""

from __future__ import annotations

from typing import Optional


# 七段顯示器每個數字所需木棒數
STICKS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def _digit_positions(expr: str) -> list[int]:
    """回傳字串中所有數字字元的位置。"""
    return [idx for idx, ch in enumerate(expr) if ch.isdigit()]


def _delta(from_digit: int, to_digit: int) -> int:
    """回傳木棒差：to - from。若不是正負 1，代表不能只靠搬一根完成。"""
    d = STICKS[to_digit] - STICKS[from_digit]
    return d if abs(d) == 1 else 0


def _is_valid_equation(expr: str) -> bool:
    """檢查等式是否成立。"""
    try:
        left, right = expr.split("=", 1)
        return eval(left) == eval(right)
    except Exception:
        return False


def solve_equation(equation: str) -> Optional[str]:
    """找出任一可行解；若無解回傳 None。"""
    if equation.count("=") != 1:
        return None

    positions = _digit_positions(equation)
    chars = list(equation)

    # i: 失去一根木棒的數字位置，j: 得到一根木棒的數字位置
    for i in positions:
        from_i = ord(chars[i]) - ord("0")
        for to_i in range(10):
            if to_i == from_i or _delta(from_i, to_i) != -1:
                continue

            chars_i = chars[:]
            chars_i[i] = str(to_i)

            for j in positions:
                if j == i:
                    continue
                from_j = ord(chars[j]) - ord("0")
                for to_j in range(10):
                    if to_j == from_j or _delta(from_j, to_j) != 1:
                        continue

                    chars_j = chars_i[:]
                    chars_j[j] = str(to_j)
                    candidate = "".join(chars_j)
                    if _is_valid_equation(candidate):
                        return candidate

    return None


def main() -> None:
    """讀取一行，以 # 前面的等式為輸入。"""
    import sys

    raw = sys.stdin.read().strip()
    equation = raw.split("#", 1)[0]

    ans = solve_equation(equation)
    if ans is None:
        sys.stdout.write("No\n")
    else:
        sys.stdout.write(ans + "#\n")


if __name__ == "__main__":
    main()
