"""UVA 10035: Carry Operation。"""

import sys


def count_carries(left: str, right: str) -> int:
    """模擬直式加法，計算總進位次數。"""
    carry = 0
    carry_count = 0

    index_left = len(left) - 1
    index_right = len(right) - 1

    while index_left >= 0 or index_right >= 0:
        digit_left = int(left[index_left]) if index_left >= 0 else 0
        digit_right = int(right[index_right]) if index_right >= 0 else 0

        # 把上一位的進位也一起加進來，完全模擬手算方式。
        total = digit_left + digit_right + carry
        if total >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0

        index_left -= 1
        index_right -= 1

    return carry_count


def format_answer(carry_count: int) -> str:
    """依照題目要求輸出英文句型。"""
    if carry_count == 0:
        return "No carry operation."
    if carry_count == 1:
        return "1 carry operation."
    return f"{carry_count} carry operations."


def solve(text: str) -> str:
    outputs: list[str] = []

    for line in text.splitlines():
        parts = line.split()
        if len(parts) != 2:
            continue

        left, right = parts
        if left == "0" and right == "0":
            # 題目規定 0 0 是結束標記，不需要輸出。
            break

        outputs.append(format_answer(count_carries(left, right)))

    return "\n".join(outputs)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))