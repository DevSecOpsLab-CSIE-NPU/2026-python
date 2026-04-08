from __future__ import annotations

import math
import sys
from typing import Iterable, List, Tuple


def answer(s: int, d: int) -> int:
    """回傳第 d 天入住的旅行團人數。"""

    # 設目標團人數為 n。
    # 從 S 人團一路到 n 人團，總入住天數為：
    #   1+2+...+n - (1+2+...+(s-1))
    # 需找到最小 n，使上述天數 >= d。
    need = d + s * (s - 1) // 2

    # 先用平方根估計，再微調到最小可行 n
    n = (math.isqrt(1 + 8 * need) - 1) // 2
    while n * (n + 1) // 2 < need:
        n += 1
    return n


def solve_case(s: int, d: int) -> int:
    """單筆查詢介面。"""
    return answer(s, d)


def _parse_text(data: str) -> List[Tuple[int, int]]:
    """把整段輸入文字解析成 (S, D) 清單。"""

    nums = [int(x) for x in data.split()]
    cases: List[Tuple[int, int]] = []

    # 題目輸入是成對出現：S D
    for i in range(0, len(nums) - 1, 2):
        cases.append((nums[i], nums[i + 1]))
    return cases


def solve(data):
    """通用介面：支援文字輸入與可迭代的 (s, d) 輸入。"""

    # 支援 solve("text")：回傳符合 OJ 格式的多行字串
    if isinstance(data, str):
        cases = _parse_text(data)
        return "\n".join(str(answer(s, d)) for s, d in cases)

    # 若傳入可迭代的 (s,d)
    try:
        return [answer(int(s), int(d)) for s, d in data]  # type: ignore[misc]
    except Exception:
        return []


def main() -> None:
    # OJ 模式：讀到 EOF，逐行輸出答案
    data = sys.stdin.read()
    out = solve(data)
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
