"""10101 的好記憶版本。

先把每個數字能少一根木棒後變成什麼、
以及能多一根木棒後變成什麼列出來，
再逐一嘗試移動位置。
"""

from __future__ import annotations

import sys


MASKS = {
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


def make_options():
    remove = [[] for _ in range(10)]
    add = [[] for _ in range(10)]
    for digit, mask in MASKS.items():
        for next_digit, next_mask in MASKS.items():
            if (mask ^ next_mask).bit_count() != 1:
                continue
            if next_mask < mask:
                remove[digit].append(next_digit)
            else:
                add[digit].append(next_digit)
    return remove, add


REMOVE, ADD = make_options()


def parse_value(side: str) -> int:
    value = 0
    index = 0
    sign = 1
    if index < len(side) and side[index] == "-":
        sign = -1
        index += 1
    while index < len(side):
        start = index
        while index < len(side) and side[index].isdigit():
            index += 1
        value += sign * int(side[start:index])
        if index >= len(side):
            break
        sign = 1 if side[index] == "+" else -1
        index += 1
    return value


def parse_side(side: str, side_sign: int, offset: int):
    value = 0
    digits = []
    index = 0
    sign = 1
    if index < len(side) and side[index] == "-":
        sign = -1
        index += 1
    while index < len(side):
        start = index
        while index < len(side) and side[index].isdigit():
            index += 1
        number = side[start:index]
        value += sign * int(number)
        place = 1
        for local in range(len(number) - 1, -1, -1):
            digits.append((offset + start + local, int(number[local]), side_sign * sign * place))
            place *= 10
        if index >= len(side):
            break
        sign = 1 if side[index] == "+" else -1
        index += 1
    return value * side_sign, digits


def solve(text: str) -> str:
    expr = text.split("#", 1)[0]
    if not expr:
        return "No"

    eq = expr.index("=")
    left = expr[:eq]
    right = expr[eq + 1 :]
    left_value, left_digits = parse_side(left, 1, 0)
    right_value, right_digits = parse_side(right, -1, eq + 1)
    diff = left_value + right_value

    digits = left_digits + right_digits
    chars = list(expr)

    for source_pos, source_digit, source_coeff in digits:
        for new_source_digit in REMOVE[source_digit]:
            source_delta = source_coeff * (new_source_digit - source_digit)
            for target_pos, target_digit, target_coeff in digits:
                if source_pos == target_pos:
                    continue
                for new_target_digit in ADD[target_digit]:
                    if diff + source_delta + target_coeff * (new_target_digit - target_digit) != 0:
                        continue
                    chars[source_pos] = str(new_source_digit)
                    chars[target_pos] = str(new_target_digit)
                    return "".join(chars) + "#"

    return "No"


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()