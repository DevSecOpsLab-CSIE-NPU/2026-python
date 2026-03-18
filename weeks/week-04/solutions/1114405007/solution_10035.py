from __future__ import annotations


def count_carries(left: str, right: str) -> int:
    carry = 0
    total_carries = 0

    index_left = len(left) - 1
    index_right = len(right) - 1

    while index_left >= 0 or index_right >= 0:
        digit_left = int(left[index_left]) if index_left >= 0 else 0
        digit_right = int(right[index_right]) if index_right >= 0 else 0

        # 模擬直式加法，若這一位總和超過 9 就會產生進位。
        current_sum = digit_left + digit_right + carry
        if current_sum >= 10:
            total_carries += 1
            carry = 1
        else:
            carry = 0

        index_left -= 1
        index_right -= 1

    return total_carries


def format_answer(carry_count: int) -> str:
    if carry_count == 0:
        return "No carry operation."
    if carry_count == 1:
        return "1 carry operation."
    return f"{carry_count} carry operations."


def solve(data: str) -> str:
    answers: list[str] = []

    for line in data.splitlines():
        if not line.strip():
            continue
        left, right = line.split()

        # 讀到 0 0 代表所有測試資料結束。
        if left == "0" and right == "0":
            break
        answers.append(format_answer(count_carries(left, right)))

    return "\n".join(answers)


def main() -> None:
    import sys

    # 逐列讀取兩個整數，計算直式加法的進位次數。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()