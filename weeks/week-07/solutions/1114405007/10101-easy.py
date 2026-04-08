from __future__ import annotations

import sys
from collections import defaultdict


# 七段顯示器：每個數字會亮的線段集合。
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
    """預先建立三種變換：
    1) remove：拿掉一根火柴後可變成哪些數字
    2) add：加上一根火柴後可變成哪些數字
    3) move：在同一個數字內搬一根（先拿掉再加到另一段）
    """
    remove_map: dict[str, list[str]] = {}
    add_map: dict[str, list[str]] = {}
    move_map: dict[str, list[str]] = {}

    for d, segs in SEG.items():
        remove_set = set()
        add_set = set()
        move_set = set()

        for x in segs:
            t = set(segs)
            t.remove(x)
            nd = REV.get(frozenset(t))
            if nd is not None:
                remove_set.add(nd)

        for y in "abcdefg":
            if y in segs:
                continue
            t = set(segs)
            t.add(y)
            nd = REV.get(frozenset(t))
            if nd is not None:
                add_set.add(nd)

        for x in segs:
            for y in "abcdefg":
                if y in segs or y == x:
                    continue
                t = set(segs)
                t.remove(x)
                t.add(y)
                nd = REV.get(frozenset(t))
                if nd is not None:
                    move_set.add(nd)

        remove_map[d] = sorted(remove_set)
        add_map[d] = sorted(add_set)
        move_map[d] = sorted(move_set)

    return remove_map, add_map, move_map


REMOVE_MAP, ADD_MAP, MOVE_MAP = build_maps()


def parse_for_balance(expr: str) -> tuple[dict[int, tuple[int, int]], int]:
    """回傳：
    1) 每個數字位置 pos 對應 (coef, place)
    2) 原始等式左右差值 balance = left - right
    """
    equal_pos = expr.index("=")
    info_by_pos: dict[int, tuple[int, int]] = {}

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

            length = j - i
            coef = side_coef * sign
            for k in range(length):
                pos = i + k
                place = 10 ** (length - 1 - k)
                info_by_pos[pos] = (coef, place)

            if j >= end:
                break
            sign = 1 if expr[j] == "+" else -1
            i = j + 1

    parse_side(0, equal_pos, +1)
    parse_side(equal_pos + 1, len(expr), -1)

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
        value = int(expr[i:j])
        balance += side_coef * sign * value
        i = j

    return info_by_pos, balance


def solve(data: str) -> str:
    if not data:
        return ""

    first_line = data.splitlines()[0]
    hash_pos = first_line.find("#")
    if hash_pos == -1:
        return "No"

    expr = first_line[:hash_pos]
    chars = list(expr)
    digit_positions = [i for i, ch in enumerate(chars) if ch.isdigit()]

    info_by_pos, balance = parse_for_balance(expr)

    # 每個位置預先算出：改成某個數字後，對 balance 的變化量。
    move_opts: dict[int, list[tuple[str, int]]] = {}
    remove_opts: dict[int, list[tuple[str, int]]] = {}
    add_opts: dict[int, list[tuple[str, int]]] = {}

    for pos in digit_positions:
        d = chars[pos]
        coef, place = info_by_pos[pos]
        old_num = ord(d) - ord("0")

        lst = []
        for nd in MOVE_MAP[d]:
            delta = coef * ((ord(nd) - ord("0") - old_num) * place)
            lst.append((nd, delta))
        move_opts[pos] = lst

        lst = []
        for nd in REMOVE_MAP[d]:
            delta = coef * ((ord(nd) - ord("0") - old_num) * place)
            lst.append((nd, delta))
        remove_opts[pos] = lst

        lst = []
        for nd in ADD_MAP[d]:
            delta = coef * ((ord(nd) - ord("0") - old_num) * place)
            lst.append((nd, delta))
        add_opts[pos] = lst

    # 情況 A：同一個數字內搬一根火柴。
    for pos in digit_positions:
        for nd, delta in move_opts[pos]:
            if balance + delta == 0:
                out = chars[:]
                out[pos] = nd
                return "".join(out) + "#"

    # 情況 B：從某數字拿一根，搬到另一個數字。
    # 先把「加一根」依照 delta 分桶，查找會很快。
    add_by_delta: dict[int, list[tuple[int, str]]] = defaultdict(list)
    for pos in digit_positions:
        for nd, delta in add_opts[pos]:
            add_by_delta[delta].append((pos, nd))

    for src_pos in digit_positions:
        for src_nd, src_delta in remove_opts[src_pos]:
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
    result = solve(data)
    if result:
        sys.stdout.write(result)


if __name__ == "__main__":
    main()
