"""10101 手打版。

先把七段顯示器的變化關係建好，
再枚舉「哪一個數字拿走一根、哪一個數字補上一根」，
最後檢查整個等式是否成立。
"""

from __future__ import annotations

import sys


SEGMENTS = {
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


def build_moves():
    remove = [[] for _ in range(10)]
    add = [[] for _ in range(10)]
    for old_digit, old_mask in SEGMENTS.items():
        for new_digit, new_mask in SEGMENTS.items():
            if (old_mask ^ new_mask).bit_count() != 1:
                continue
            if new_mask < old_mask:
                remove[old_digit].append(new_digit)
            else:
                add[old_digit].append(new_digit)
    return remove, add


REMOVE, ADD = build_moves()


def parse_side(side: str, sign_factor: int, offset: int):
    value = 0
    digit_info = []
    index = 0
    sign = 1

    if index < len(side) and side[index] == "-":
        sign = -1
        index += 1

    while index < len(side):
        start = index
        while index < len(side) and side[index].isdigit():
            index += 1

        number_text = side[start:index]
        value += sign * int(number_text)

        place = 1
        for local_index in range(len(number_text) - 1, -1, -1):
            digit_info.append((offset + start + local_index, int(number_text[local_index]), sign_factor * sign * place))
            place *= 10

        if index >= len(side):
            break

        sign = 1 if side[index] == "+" else -1
        index += 1

    return value * sign_factor, digit_info


def solve(text: str) -> str:
    expr = text.split("#", 1)[0]
    if not expr:
        return "No"

    eq = expr.index("=")
    left_value, left_info = parse_side(expr[:eq], 1, 0)
    right_value, right_info = parse_side(expr[eq + 1 :], -1, eq + 1)
    diff = left_value + right_value

    digit_info = left_info + right_info
    chars = list(expr)

    for source_pos, source_digit, source_coeff in digit_info:
        for new_source_digit in REMOVE[source_digit]:
            source_delta = source_coeff * (new_source_digit - source_digit)
            for target_pos, target_digit, target_coeff in digit_info:
                if target_pos == source_pos:
                    continue
                for new_target_digit in ADD[target_digit]:
                    total = diff + source_delta + target_coeff * (new_target_digit - target_digit)
                    if total != 0:
                        continue
                    chars[source_pos] = str(new_source_digit)
                    chars[target_pos] = str(new_target_digit)
                    return "".join(chars) + "#"

    return "No"


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()