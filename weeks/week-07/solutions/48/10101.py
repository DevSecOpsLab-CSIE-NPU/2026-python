"""UVA 10101 正式版。

只允許移動一根木棒，而且只能動到數字本身。
所以做法是：
1. 找出每個數字可以被移走一根後變成哪些數字。
2. 找出每個數字可以再加上一根後變成哪些數字。
3. 枚舉來源位置與目的位置，檢查等式是否成立。
"""

from __future__ import annotations

import sys


DIGIT_MASKS = {
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


def build_digit_options():
    remove_options = [[] for _ in range(10)]
    add_options = [[] for _ in range(10)]

    for digit, mask in DIGIT_MASKS.items():
        for next_digit, next_mask in DIGIT_MASKS.items():
            diff = mask ^ next_mask
            if diff.bit_count() != 1:
                continue
            if next_mask < mask:
                remove_options[digit].append(next_digit)
            elif next_mask > mask:
                add_options[digit].append(next_digit)

    for digit in range(10):
        remove_options[digit].sort()
        add_options[digit].sort()

    return remove_options, add_options


REMOVE_OPTIONS, ADD_OPTIONS = build_digit_options()


def parse_side(side: str, side_sign: int, offset: int):
    """解析一側的數字與每個數字位元對整體等式的影響。"""

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

        number_text = side[start:index]
        number_value = int(number_text)
        value += sign * number_value

        place = 1
        for local_index in range(len(number_text) - 1, -1, -1):
            global_index = offset + start + local_index
            digit = int(number_text[local_index])
            coefficient = side_sign * sign * place
            digits.append((global_index, digit, coefficient))
            place *= 10

        if index >= len(side):
            break

        operator = side[index]
        sign = 1 if operator == "+" else -1
        index += 1

    return value * side_sign, digits


def solve(text: str) -> str:
    expression = text.split("#", 1)[0]
    if not expression:
        return "No"

    equals_index = expression.index("=")
    left_text = expression[:equals_index]
    right_text = expression[equals_index + 1 :]

    left_value, left_digits = parse_side(left_text, 1, 0)
    right_value, right_digits = parse_side(right_text, -1, equals_index + 1)
    difference = left_value + right_value

    digits = left_digits + right_digits
    chars = list(expression)

    for source_index, source_digit, source_coeff in digits:
        for new_source_digit in REMOVE_OPTIONS[source_digit]:
            source_delta = source_coeff * (new_source_digit - source_digit)
            for target_index, target_digit, target_coeff in digits:
                if target_index == source_index:
                    continue
                for new_target_digit in ADD_OPTIONS[target_digit]:
                    total = difference + source_delta + target_coeff * (new_target_digit - target_digit)
                    if total != 0:
                        continue

                    chars[source_index] = str(new_source_digit)
                    chars[target_index] = str(new_target_digit)
                    return "".join(chars) + "#"

    return "No"


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()