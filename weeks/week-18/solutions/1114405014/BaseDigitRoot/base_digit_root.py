import sys


BASE = 5


def validate_base(base: int) -> None:
    if base < 2:
        raise ValueError("base must be greater than or equal to 2")


def validate_number(n: int) -> None:
    if n < 0:
        raise ValueError("n must be a non-negative integer")


def to_base_digits(n: int, base: int) -> list[int]:
    """
    Convert a decimal non-negative integer to a list of digits in the given base.

    Example:
        to_base_digits(24, 5) -> [4, 4]
        because 24(decimal) = 44(base 5)
    """
    validate_base(base)
    validate_number(n)

    if n == 0:
        return [0]

    digits = []

    while n > 0:
        digits.append(n % base)
        n //= base

    return digits[::-1]


def digit_root_in_base(n: int, base: int) -> int:
    """
    Compute the digit root of n in the given base.

    Process:
        1. Convert n to the given base.
        2. Sum all digits.
        3. Repeat until the value is one digit in that base.

    A value is one digit in base b when:
        0 <= value < b
    """
    validate_base(base)
    validate_number(n)

    while n >= base:
        digits = to_base_digits(n, base)
        n = sum(digits)

    return n


def solve(input_text: str, base: int = BASE) -> str:
    """
    Read multiple decimal non-negative integers and output one digit root per line.

    Input may be separated by spaces or newlines.
    """
    validate_base(base)

    tokens = input_text.split()

    if not tokens:
        return ""

    results = []

    for token in tokens:
        n = int(token)
        result = digit_root_in_base(n, base)
        results.append(str(result))

    return "\n".join(results)


def main() -> None:
    input_text = sys.stdin.read()
    output = solve(input_text, BASE)

    if output:
        print(output)


if __name__ == "__main__":
    main()