from __future__ import annotations

import sys


def count_carry(a: str, b: str) -> int:
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    count = 0

    while i >= 0 or j >= 0:
        da = ord(a[i]) - ord("0") if i >= 0 else 0
        db = ord(b[j]) - ord("0") if j >= 0 else 0
        total = da + db + carry

        if total >= 10:
            carry = 1
            count += 1
        else:
            carry = 0

        i -= 1
        j -= 1

    return count


def format_answer(carry_count: int) -> str:
    if carry_count == 0:
        return "No carry operation."
    if carry_count == 1:
        return "1 carry operation."
    return f"{carry_count} carry operations."


def solve(data: str) -> str:
    answers = []

    for raw in data.splitlines():
        line = raw.strip()
        if not line:
            continue

        left, right = line.split()
        if left == "0" and right == "0":
            break

        answers.append(format_answer(count_carry(left, right)))

    if not answers:
        return ""

    return "\n".join(answers) + "\n"


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()