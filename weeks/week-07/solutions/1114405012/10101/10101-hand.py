"""10101 easy 手打版。"""

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

        token = expr[st:i]
        if not token:
            continue

        val = int(token)
        if side == 0:
            left += sign * val
        else:
            right += sign * val

        length = len(token)
        for j, c in enumerate(token):
            pos = st + j
            place = 10 ** (length - 1 - j)
            info[pos] = (side, sign, place, int(c))

    return left, right, info


def build_moves():
    remove_one = [[] for _ in range(10)]
    add_one = [[] for _ in range(10)]
    move_inside = [[] for _ in range(10)]

    for d in range(10):
        md = SEG[d]
        cd = bit_count(md)
        for x in range(10):
            if x == d:
                continue
            mx = SEG[x]
            cx = bit_count(mx)

            if cx == cd - 1 and (mx & md) == mx and bit_count(md ^ mx) == 1:
                remove_one[d].append(x)
            if cx == cd + 1 and (mx & md) == md and bit_count(md ^ mx) == 1:
                add_one[d].append(x)
            if cx == cd and bit_count(md ^ mx) == 2:
                move_inside[d].append(x)

    return remove_one, add_one, move_inside


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
    digits = [i for i, ch in enumerate(chars) if ch.isdigit()]

    for p in digits:
        old = int(chars[p])
        for nd in mv[old]:
            if diff + delta(info[p], nd) == 0:
                out = chars.copy()
                out[p] = str(nd)
                return "".join(out) + "#"

    add_map = defaultdict(list)
    for p in digits:
        old = int(chars[p])
        for nd in ad[old]:
            add_map[delta(info[p], nd)].append((p, nd))

    for src in digits:
        old = int(chars[src])
        for nd_src in rm[old]:
            dsrc = delta(info[src], nd_src)
            need = -diff - dsrc
            for dst, nd_dst in add_map.get(need, []):
                if dst == src:
                    continue
                out = chars.copy()
                out[src] = str(nd_src)
                out[dst] = str(nd_dst)
                return "".join(out) + "#"

    return "No"


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        print(out)


if __name__ == "__main__":
    main()
