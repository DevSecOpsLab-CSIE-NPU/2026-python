def count_carries(left, right):
    left_digits = left[::-1]
    right_digits = right[::-1]
    carry = 0
    carry_count = 0
    length = max(len(left_digits), len(right_digits))

    for index in range(length):
        digit_left = int(left_digits[index]) if index < len(left_digits) else 0
        digit_right = int(right_digits[index]) if index < len(right_digits) else 0

        if digit_left + digit_right + carry >= 10:
            carry_count += 1
            carry = 1
        else:
            carry = 0

    return carry_count


def solve(data):
    answers = []

    for line in data.splitlines():
        if not line.strip():
            continue

        left, right = line.split()
        if left == "0" and right == "0":
            break

        carry_count = count_carries(left, right)
        if carry_count == 0:
            answers.append("No carry operation.")
        elif carry_count == 1:
            answers.append("1 carry operation.")
        else:
            answers.append(f"{carry_count} carry operations.")

    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()), end="")