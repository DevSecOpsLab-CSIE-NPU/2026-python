"""UVA/ZeroJudge 10101 解答。

需求：只能移動「一根」構成數字的木棒，讓等式成立。
- 不能改變 + - = 的位置。
- 數字必須維持七段顯示器合法型態。
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


def parse_expression(expr: str):
    """解析等式，回傳：(left_sum, right_sum, pos_info)。

    pos_info[pos] = (side, sign, place, old_digit)
    side: 0=左式, 1=右式
    """
    n = len(expr)
    pos_info = {}

    left_sum = 0
    right_sum = 0

    side = 0
    i = 0
    while i < n:
        ch = expr[i]
        if ch == "=":
            side = 1
            i += 1
            continue

        sign = 1
        if ch == "+":
            i += 1
        elif ch == "-":
            sign = -1
            i += 1

        start = i
        while i < n and expr[i].isdigit():
            i += 1

        num_str = expr[start:i]
        if not num_str:
            # 題目保證輸入合法，這裡防守式處理
            continue

        value = int(num_str)
        if side == 0:
            left_sum += sign * value
        else:
            right_sum += sign * value

        length = len(num_str)
        for j, c in enumerate(num_str):
            pos = start + j
            place = 10 ** (length - 1 - j)
            pos_info[pos] = (side, sign, place, ord(c) - 48)

    return left_sum, right_sum, pos_info


def make_transitions():
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

            # d -> x：移除一根
            if cx == cd - 1 and (mx & md) == mx and bit_count(md ^ mx) == 1:
                remove_one[d].append(x)

            # d -> x：新增一根
            if cx == cd + 1 and (mx & md) == md and bit_count(md ^ mx) == 1:
                add_one[d].append(x)

            # d -> x：在同一個數字內部搬一根（總根數不變）
            if cx == cd and bit_count(md ^ mx) == 2:
                move_inside[d].append(x)

    return remove_one, add_one, move_inside


def delta_diff(info, new_digit: int) -> int:
    side, sign, place, old_digit = info
    coeff = sign * place if side == 0 else -sign * place
    return coeff * (new_digit - old_digit)


def solve(input_data: str) -> str:
    expr = input_data.split("#", 1)[0]
    if not expr:
        return "No"

    chars = list(expr)
    left_sum, right_sum, pos_info = parse_expression(expr)
    diff0 = left_sum - right_sum

    remove_one, add_one, move_inside = make_transitions()

    digit_positions = [i for i, c in enumerate(chars) if c.isdigit()]
    if not digit_positions:
        return "No"

    # 1) 同一個數字內部搬一根
    for pos in digit_positions:
        old_d = ord(chars[pos]) - 48
        info = pos_info[pos]
        for nd in move_inside[old_d]:
            if diff0 + delta_diff(info, nd) == 0:
                out = chars.copy()
                out[pos] = str(nd)
                return "".join(out) + "#"

    # 2) 從某數字移出一根，移到另一數字
    add_by_delta = defaultdict(list)
    for pos in digit_positions:
        old_d = ord(chars[pos]) - 48
        info = pos_info[pos]
        for nd in add_one[old_d]:
            dd = delta_diff(info, nd)
            add_by_delta[dd].append((pos, nd))

    for src_pos in digit_positions:
        old_src = ord(chars[src_pos]) - 48
        src_info = pos_info[src_pos]

        for src_new in remove_one[old_src]:
            dsrc = delta_diff(src_info, src_new)
            need = -diff0 - dsrc

            for dst_pos, dst_new in add_by_delta.get(need, []):
                if dst_pos == src_pos:
                    continue

                out = chars.copy()
                out[src_pos] = str(src_new)
                out[dst_pos] = str(dst_new)
                return "".join(out) + "#"

    return "No"


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        sys.stdout.write(out + "\n")


if __name__ == "__main__":
    main()
