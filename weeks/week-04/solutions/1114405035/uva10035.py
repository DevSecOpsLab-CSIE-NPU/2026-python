#!/usr/bin/env python3


def process_input(input_text: str) -> str:
    tokens = input_text.strip().split()
    idx = 0
    results = []
    while idx < len(tokens):
        x = int(tokens[idx])
        y = int(tokens[idx + 1])
        idx += 2
        if x == 0 and y == 0:
            break
        carry = 0
        while x > 0 or y > 0:
            digit_x = x % 10
            digit_y = y % 10
            if digit_x + digit_y + carry >= 10:
                carry = 1
            else:
                carry = 0
            x //= 10
            y //= 10
        results.append(str(carry))
    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
def count_carry_operations(a: str, b: str) -> int:
    a, b = a[::-1], b[::-1]
    carry = 0
    carry_count = 0
    max_len = max(len(a), len(b))

    for i in range(max_len):
        da = int(a[i]) if i < len(a) else 0
        db = int(b[i]) if i < len(b) else 0
        if da + db + carry >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
    return carry_count


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.splitlines() if line.strip()]
    results = []
    for line in lines:
        a, b = line.split()
        if a == '0' and b == '0':
            break
        count = count_carry_operations(a, b)
        if count == 0:
            results.append('No carry operation.')
        elif count == 1:
            results.append('1 carry operation.')
        else:
            results.append(f'{count} carry operations.')
    return '\n'.join(results)


def main() -> None:
    import sys
    print(process_input(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()
