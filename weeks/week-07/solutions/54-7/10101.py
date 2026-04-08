import sys

SEGMENT_MAP = {
    "0": 0b1110111,
    "1": 0b0010010,
    "2": 0b1011101,
    "3": 0b1011011,
    "4": 0b0111010,
    "5": 0b1101011,
    "6": 0b1101111,
    "7": 0b1010010,
    "8": 0b1111111,
    "9": 0b1111011,
}

REMOVE_ONE: dict[str, list[str]] = {}
ADD_ONE: dict[str, list[str]] = {}
CHANGE_ONE: dict[str, list[str]] = {}

for digit, pattern in SEGMENT_MAP.items():
    REMOVE_ONE[digit] = []
    ADD_ONE[digit] = []
    CHANGE_ONE[digit] = []

for d1, p1 in SEGMENT_MAP.items():
    for d2, p2 in SEGMENT_MAP.items():
        if d1 == d2:
            continue
        diff = p1 ^ p2
        if diff == 0:
            continue
        if p2 & p1 == p2 and diff.bit_count() == 1:
            REMOVE_ONE[d1].append(d2)
        if p1 & p2 == p1 and diff.bit_count() == 1:
            ADD_ONE[d1].append(d2)
        if diff.bit_count() == 2 and p1.bit_count() == p2.bit_count():
            CHANGE_ONE[d1].append(d2)


def eval_expression(expr: str) -> int | None:
    idx = 0
    length = len(expr)
    if length == 0:
        return None

    total = 0
    sign = 1
    if expr[0] == "-":
        sign = -1
        idx = 1

    while idx < length:
        if not expr[idx].isdigit():
            return None
        start = idx
        while idx < length and expr[idx].isdigit():
            idx += 1
        total += sign * int(expr[start:idx])
        if idx == length:
            break
        if expr[idx] == "+":
            sign = 1
        elif expr[idx] == "-":
            sign = -1
        else:
            return None
        idx += 1

    return total


def equation_holds(expr: str) -> bool:
    if "=" not in expr:
        return False
    left, right = expr.split("=", 1)
    left_value = eval_expression(left)
    right_value = eval_expression(right)
    return left_value is not None and right_value is not None and left_value == right_value


def solve_line(line: str) -> str:
    hash_index = line.find("#")
    if hash_index == -1:
        return "No"

    expr = line[:hash_index]
    chars = list(expr)
    positions = [i for i, c in enumerate(chars) if c.isdigit()]
    if not positions:
        return "No"

    if equation_holds(expr):
        return expr + "#"

    for pos in positions:
        original_digit = chars[pos]
        for new_digit in CHANGE_ONE[original_digit]:
            chars[pos] = new_digit
            modified = "".join(chars)
            if equation_holds(modified):
                return modified + "#"
            chars[pos] = original_digit

    for i, src_pos in enumerate(positions):
        for j, dst_pos in enumerate(positions):
            if i == j:
                continue
            src_digit = chars[src_pos]
            dst_digit = chars[dst_pos]
            for src_new in REMOVE_ONE[src_digit]:
                chars[src_pos] = src_new
                for dst_new in ADD_ONE[dst_digit]:
                    chars[dst_pos] = dst_new
                    modified = "".join(chars)
                    if equation_holds(modified):
                        return modified + "#"
                chars[dst_pos] = dst_digit
            chars[src_pos] = src_digit

    return "No"


def main() -> None:
    raw_line = sys.stdin.readline()
    if not raw_line:
        return
    raw_line = raw_line.strip()
    print(solve_line(raw_line))


if __name__ == "__main__":
    main()
