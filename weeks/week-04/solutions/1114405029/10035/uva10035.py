def count_carry(a: int, b: int) -> int:
    carry = 0
    count = 0

    while a > 0 or b > 0:
        digit_sum = a % 10 + b % 10 + carry
        if digit_sum >= 10:
            count += 1
            carry = 1
        else:
            carry = 0

        a //= 10
        b //= 10

    return count


def solve(data: str) -> str:
    answers = []

    for line in data.strip().splitlines():
        a, b = map(int, line.split())

        if a == 0 and b == 0:
            break

        carry_count = count_carry(a, b)

        if carry_count == 0:
            answers.append("No carry operation.")
        elif carry_count == 1:
            answers.append("1 carry operation.")
        else:
            answers.append(f"{carry_count} carry operations.")

    return "\n".join(answers)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))