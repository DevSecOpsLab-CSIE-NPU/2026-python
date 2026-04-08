from __future__ import annotations

import sys
from collections import defaultdict


SEG = {
    "0": frozenset("abcefd"),
    "1": frozenset("cf"),
    "2": frozenset("acdeg"),
    "3": frozenset("acdfg"),
    "4": frozenset("bcdf"),
    "5": frozenset("abdfg"),
    "6": frozenset("abdefg"),
    "7": frozenset("acf"),
    "8": frozenset("abcdefg"),
    "9": frozenset("abcdfg"),
}
REV = {v: k for k, v in SEG.items()}


def build_maps() -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, list[str]]]:
    rm: dict[str, list[str]] = {}
    am: dict[str, list[str]] = {}
    mm: dict[str, list[str]] = {}

    for d, segs in SEG.items():
        rem, add, move = set(), set(), set()
        for x in segs:
            t = set(segs)
            t.remove(x)
            nd = REV.get(frozenset(t))
            if nd is not None:
                rem.add(nd)
        for y in "abcdefg":
            if y in segs:
                continue
            t = set(segs)
            t.add(y)
            nd = REV.get(frozenset(t))
            if nd is not None:
                add.add(nd)
        for x in segs:
            for y in "abcdefg":
                if y in segs or y == x:
                    continue
                t = set(segs)
                t.remove(x)
                t.add(y)
                nd = REV.get(frozenset(t))
                if nd is not None:
                    move.add(nd)
        rm[d] = sorted(rem)
        am[d] = sorted(add)
        mm[d] = sorted(move)
    return rm, am, mm


RM, AM, MM = build_maps()


def parse(expr: str) -> tuple[dict[int, tuple[int, int]], int]:
    eq = expr.index("=")
    info: dict[int, tuple[int, int]] = {}

    def parse_side(start: int, end: int, side_coef: int) -> None:
        i = start
        sign = 1
        if i < end and expr[i] == "-":
            sign = -1
            i += 1
        while i < end:
            j = i
            while j < end and expr[j].isdigit():
                j += 1
            coef = side_coef * sign
            length = j - i
            for k in range(length):
                pos = i + k
                place = 10 ** (length - 1 - k)
                info[pos] = (coef, place)
            if j >= end:
                break
            sign = 1 if expr[j] == "+" else -1
            i = j + 1

    parse_side(0, eq, +1)
    parse_side(eq + 1, len(expr), -1)

    bal = 0
    i = 0
    side = +1
    while i < len(expr):
        if expr[i] == "=":
            side = -1
            i += 1
            continue
        sign = 1
        if expr[i] == "+":
            i += 1
        elif expr[i] == "-":
            sign = -1
            i += 1
        j = i
        while j < len(expr) and expr[j].isdigit():
            j += 1
        bal += side * sign * int(expr[i:j])
        i = j

    return info, bal


def solve(data: str) -> str:
    line = data.splitlines()[0] if data else ""
    p = line.find("#")
    if p == -1:
        return "No"
    expr = line[:p]
    chars = list(expr)
    pos_list = [i for i, ch in enumerate(chars) if ch.isdigit()]
    info, bal = parse(expr)

    move_opts: dict[int, list[tuple[str, int]]] = {}
    rem_opts: dict[int, list[tuple[str, int]]] = {}
    add_opts: dict[int, list[tuple[str, int]]] = {}

    for pos in pos_list:
        d = chars[pos]
        coef, place = info[pos]
        old = ord(d) - ord("0")
        move_opts[pos] = [
            (nd, coef * ((ord(nd) - ord("0") - old) * place)) for nd in MM[d]
        ]
        rem_opts[pos] = [
            (nd, coef * ((ord(nd) - ord("0") - old) * place)) for nd in RM[d]
        ]
        add_opts[pos] = [
            (nd, coef * ((ord(nd) - ord("0") - old) * place)) for nd in AM[d]
        ]

    for pos in pos_list:
        for nd, delta in move_opts[pos]:
            if bal + delta == 0:
                out = chars[:]
                out[pos] = nd
                return "".join(out) + "#"

    add_by_delta: dict[int, list[tuple[int, str]]] = defaultdict(list)
    for pos in pos_list:
        for nd, delta in add_opts[pos]:
            add_by_delta[delta].append((pos, nd))

    for sp in pos_list:
        for snd, sdelta in rem_opts[sp]:
            need = -bal - sdelta
            for dp, dnd in add_by_delta.get(need, []):
                if dp == sp:
                    continue
                out = chars[:]
                out[sp] = snd
                out[dp] = dnd
                return "".join(out) + "#"
    return "No"


if __name__ == "__main__":
    out = solve(sys.stdin.read())
    if out:
        sys.stdout.write(out)
