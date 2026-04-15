"""
UVA 10101 - 木棒拼等式（easy 版）

用最直觀方式做：
- 找出所有數字位置
- 選一個數字減一根木棒
- 再選另一個數字加一根木棒
- 重新檢查等式是否成立
"""

from __future__ import annotations

from typing import Optional


STICKS = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def stick_diff(a: int, b: int) -> int:
    """回傳 b-a，只有正負 1 才代表可用一根木棒改變。"""
    d = STICKS[b] - STICKS[a]
    return d if abs(d) == 1 else 0


def ok(eq: str) -> bool:
    """等式是否成立。"""
    try:
        l, r = eq.split("=", 1)
        return eval(l) == eval(r)
    except Exception:
        return False


def solve(equation: str) -> Optional[str]:
    """回傳任一可行答案，無解回傳 None。"""
    if equation.count("=") != 1:
        return None

    pos = [i for i, ch in enumerate(equation) if ch.isdigit()]
    arr = list(equation)

    for i in pos:
        a = ord(arr[i]) - ord("0")
        for na in range(10):
            if na == a or stick_diff(a, na) != -1:
                continue

            arr1 = arr[:]
            arr1[i] = str(na)

            for j in pos:
                if j == i:
                    continue
                b = ord(arr[j]) - ord("0")
                for nb in range(10):
                    if nb == b or stick_diff(b, nb) != 1:
                        continue

                    arr2 = arr1[:]
                    arr2[j] = str(nb)
                    cand = "".join(arr2)
                    if ok(cand):
                        return cand

    return None


def main() -> None:
    import sys

    raw = sys.stdin.read().strip()
    equation = raw.split("#", 1)[0]
    ans = solve(equation)
    if ans is None:
        sys.stdout.write("No\n")
    else:
        sys.stdout.write(ans + "#\n")


if __name__ == "__main__":
    main()
