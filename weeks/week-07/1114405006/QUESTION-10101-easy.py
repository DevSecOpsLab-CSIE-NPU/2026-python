"""
QUESTION-10101-easy
更容易記憶的版本：
1) 算出目前等式誤差 F = 左式 - 右式
2) 試所有「移一根火柴」可能造成的數字變化
3) 只要讓 F 變成 0 就成功
"""

from __future__ import annotations

import sys
from collections import defaultdict


SEG = {
    0: 0b1111110,
    1: 0b0110000,
    2: 0b1101101,
    3: 0b1111001,
    4: 0b0110011,
    5: 0b1011011,
    6: 0b1011111,
    7: 0b1110000,
    8: 0b1111111,
    9: 0b1111011,
}


def build_change_tables() -> tuple[list[list[int]], list[list[int]], list[list[int]]]:
    # take[d] : d 拿掉一段可變成的數字
    # put[d]  : d 加上一段可變成的數字
    # move[d] : d 內部移動一段可變成的數字（先拿掉再補到別段）
    take = [[] for _ in range(10)]
    put = [[] for _ in range(10)]
    move = [[] for _ in range(10)]

    for d in range(10):
        s1 = SEG[d]
        for nd in range(10):
            if nd == d:
                continue
            s2 = SEG[nd]
            rm = (s1 & ~s2).bit_count()
            ad = (s2 & ~s1).bit_count()
            if rm == 1 and ad == 0:
                take[d].append(nd)
            elif rm == 0 and ad == 1:
                put[d].append(nd)
            elif rm == 1 and ad == 1:
                move[d].append(nd)

    return take, put, move


TAKE, PUT, MOVE = build_change_tables()


def eval_side(side: str) -> int:
    i = 0
    n = len(side)
    sign = 1
    total = 0

    while i < n:
        ch = side[i]
        if ch == "+":
            sign = 1
            i += 1
            continue
        if ch == "-":
            sign = -1
            i += 1
            continue

        j = i
        while j < n and side[j].isdigit():
            j += 1
        total += sign * int(side[i:j])
        sign = 1
        i = j

    return total


def parse_digit_weight(expr: str) -> tuple[list[int], list[int], int]:
    eq = expr.index("=")
    left, right = expr[:eq], expr[eq + 1 :]
    f0 = eval_side(left) - eval_side(right)

    pos = []
    weight = []

    def walk(side: str, offset: int, side_mul: int) -> None:
        i = 0
        n = len(side)
        sgn = 1
        while i < n:
            if side[i] == "+":
                sgn = 1
                i += 1
                continue
            if side[i] == "-":
                sgn = -1
                i += 1
                continue

            j = i
            while j < n and side[j].isdigit():
                j += 1

            length = j - i
            for k in range(length):
                idx = offset + i + k
                place = 10 ** (length - 1 - k)
                pos.append(idx)
                weight.append(side_mul * sgn * place)

            sgn = 1
            i = j

    walk(left, 0, +1)
    walk(right, eq + 1, -1)
    return pos, weight, f0


def solve(inp: str) -> str:
    end = inp.find("#")
    if end < 0:
        return "No"

    expr = "".join(inp[:end].split())
    if expr.count("=") != 1:
        return "No"

    pos, weight, f0 = parse_digit_weight(expr)
    cs = list(expr)
    ds = [int(cs[p]) for p in pos]

    # 1) 在同一個數字內部移動一根
    for i, p in enumerate(pos):
        d = ds[i]
        for nd in MOVE[d]:
            delta = weight[i] * (nd - d)
            if f0 + delta == 0:
                cs[p] = str(nd)
                return "".join(cs) + "#"

    # 2) 從某位拿一根，放到另一位
    gain_map: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for j in range(len(pos)):
        d = ds[j]
        for nd in PUT[d]:
            delta = weight[j] * (nd - d)
            gain_map[delta].append((j, nd))

    for i, p in enumerate(pos):
        d = ds[i]
        for nd in TAKE[d]:
            delta_i = weight[i] * (nd - d)
            need = -f0 - delta_i
            for j, ndj in gain_map.get(need, []):
                if j == i:
                    continue
                out = cs[:]
                out[p] = str(nd)
                out[pos[j]] = str(ndj)
                return "".join(out) + "#"

    return "No"


def main() -> None:
    text = sys.stdin.read()
    print(solve(text), end="")


if __name__ == "__main__":
    main()
