from __future__ import annotations

import sys
from collections import defaultdict


SEGMENTS = {
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

SET_TO_DIGIT = {v: k for k, v in SEGMENTS.items()}


def build_transitions() -> tuple[dict[str, list[str]], dict[str, list[str]], dict[str, list[str]]]:
    remove_map: dict[str, list[str]] = {}
    add_map: dict[str, list[str]] = {}
    move_map: dict[str, list[str]] = {}

    for d, segs in SEGMENTS.items():
        rem = set()
        add = set()
        move = set()

        for x in segs:
            t = set(segs)
            t.remove(x)
            k = SET_TO_DIGIT.get(frozenset(t))
            if k is not None:
                rem.add(k)

        for y in "abcdefg":
            if y in segs:
                continue
            t = set(segs)
            t.add(y)
            k = SET_TO_DIGIT.get(frozenset(t))
            if k is not None:
                add.add(k)

        for x in segs:
            for y in "abcdefg":
                if y in segs or x == y:
                    continue
                t = set(segs)
                t.remove(x)
                t.add(y)
                k = SET_TO_DIGIT.get(frozenset(t))
                if k is not None:
                    move.add(k)

        remove_map[d] = sorted(rem)
        add_map[d] = sorted(add)
        move_map[d] = sorted(move)

    return remove_map, add_map, move_map


REMOVE_MAP, ADD_MAP, MOVE_MAP = build_transitions()


def parse_expression(expr: str) -> tuple[list[dict[str, int]], int]:
    eq_pos = expr.index("=")
    tokens: list[dict[str, int]] = []

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

            txt = expr[i:j]
            value = int(txt)
            coef = side_coef * sign

            length = j - i
            for k in range(length):
                pos = i + k
                place = 10 ** (length - 1 - k)
                tokens.append({"pos": pos, "coef": coef, "place": place})

            if j >= end:
                break
            op = expr[j]
            sign = 1 if op == "+" else -1
            i = j + 1

    parse_side(0, eq_pos, +1)
    parse_side(eq_pos + 1, len(expr), -1)

    balance = 0
    i = 0
    side_coef = +1
    while i < len(expr):
        if expr[i] == "=":
            side_coef = -1
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
        num = int(expr[i:j])
        balance += side_coef * sign * num
        i = j

    return tokens, balance


def solve(data: str) -> str:
    if not data:
        return ""
    line = data.splitlines()[0]
    hash_pos = line.find("#")
    if hash_pos == -1:
        return "No"

    expr = line[:hash_pos]
    chars = list(expr)

    tokens, balance = parse_expression(expr)
    info_by_pos = {t["pos"]: t for t in tokens}
    digit_positions = [i for i, ch in enumerate(chars) if ch.isdigit()]

    move_options_by_pos: dict[int, list[tuple[str, int]]] = {}
    remove_options_by_pos: dict[int, list[tuple[str, int]]] = {}
    add_options_by_pos: dict[int, list[tuple[str, int]]] = {}

    for pos in digit_positions:
        d = chars[pos]
        info = info_by_pos[pos]
        coef = info["coef"]
        place = info["place"]
        old_num = ord(d) - ord("0")

        moves = []
        for nd in MOVE_MAP[d]:
            delta = coef * ((ord(nd) - ord("0") - old_num) * place)
            moves.append((nd, delta))
        move_options_by_pos[pos] = moves

        rems = []
        for nd in REMOVE_MAP[d]:
            delta = coef * ((ord(nd) - ord("0") - old_num) * place)
            rems.append((nd, delta))
        remove_options_by_pos[pos] = rems

        adds = []
        for nd in ADD_MAP[d]:
            delta = coef * ((ord(nd) - ord("0") - old_num) * place)
            adds.append((nd, delta))
        add_options_by_pos[pos] = adds

    for pos in digit_positions:
        for nd, delta in move_options_by_pos[pos]:
            if balance + delta == 0:
                out = chars[:]
                out[pos] = nd
                return "".join(out) + "#"

    add_by_delta: dict[int, list[tuple[int, str]]] = defaultdict(list)
    for pos in digit_positions:
        for nd, delta in add_options_by_pos[pos]:
            add_by_delta[delta].append((pos, nd))

    for src_pos in digit_positions:
        for src_nd, src_delta in remove_options_by_pos[src_pos]:
            need = -balance - src_delta
            for dst_pos, dst_nd in add_by_delta.get(need, []):
                if dst_pos == src_pos:
                    continue
                out = chars[:]
                out[src_pos] = src_nd
                out[dst_pos] = dst_nd
                return "".join(out) + "#"

    return "No"


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
