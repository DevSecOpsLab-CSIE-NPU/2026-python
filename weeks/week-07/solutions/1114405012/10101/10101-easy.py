"""UVA/ZeroJudge 10101 簡單版（easy）。

與正式版同核心概念，但用較直觀命名：
- 先算目前左右差值 diff
- 嘗試「同位數內搬一根」
- 再嘗試「A 位移出一根，B 位補上一根」
只要讓 diff 變成 0 就回傳。
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


def bit_count(x: int) -> int:
    return bin(x).count("1")


def parse(expr: str):
    info = {}
    left = 0
    right = 0

    side = 0
    i = 0
    n = len(expr)
    while i < n:
        if expr[i] == "=":
            side = 1
            i += 1
            continue

        sign = 1
        if expr[i] == "+":
            i += 1
        elif expr[i] == "-":
            sign = -1
            i += 1

        st = i
        while i < n and expr[i].isdigit():
            i += 1

        num = expr[st:i]
        if not num:
            continue

        val = int(num)
        if side == 0:
            left += sign * val
        else:
            right += sign * val

        length = len(num)
        for j, c in enumerate(num):
            pos = st + j
            place = 10 ** (length - 1 - j)
            info[pos] = (side, sign, place, ord(c) - 48)

    return left, right, info


def build_moves():
    rm = [[] for _ in range(10)]
    ad = [[] for _ in range(10)]
    mv = [[] for _ in range(10)]

    for d in range(10):
        md = SEG[d]
        cd = bit_count(md)
        for x in range(10):
            if x == d:
                continue
            mx = SEG[x]
            cx = bit_count(mx)
            if cx == cd - 1 and (mx & md) == mx and bit_count(md ^ mx) == 1:
                rm[d].append(x)
            if cx == cd + 1 and (mx & md) == md and bit_count(md ^ mx) == 1:
                ad[d].append(x)
            if cx == cd and bit_count(md ^ mx) == 2:
                mv[d].append(x)

    return rm, ad, mv


def delta(info, nd):
    side, sign, place, old = info
    coef = sign * place if side == 0 else -sign * place
    return coef * (nd - old)


def solve(input_data: str) -> str:
    expr = input_data.split("#", 1)[0]
    if not expr:
        return "No"

    chars = list(expr)
    left, right, info = parse(expr)
    diff = left - right

    rm, ad, mv = build_moves()

    digits = [i for i, c in enumerate(chars) if c.isdigit()]

    for p in digits:
        od = ord(chars[p]) - 48
        for nd in mv[od]:
            if diff + delta(info[p], nd) == 0:
                out = chars.copy()
                out[p] = str(nd)
                return "".join(out) + "#"

    add_map = defaultdict(list)
    for p in digits:
        od = ord(chars[p]) - 48
        for nd in ad[od]:
            add_map[delta(info[p], nd)].append((p, nd))

    for src in digits:
        os = ord(chars[src]) - 48
        for ns in rm[os]:
            dsrc = delta(info[src], ns)
            want = -diff - dsrc
            for dst, nd in add_map.get(want, []):
                if dst == src:
                    continue
                out = chars.copy()
                out[src] = str(ns)
                out[dst] = str(nd)
                return "".join(out) + "#"

    return "No"


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()
