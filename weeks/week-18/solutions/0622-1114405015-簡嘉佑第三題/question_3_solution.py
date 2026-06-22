"""
Question 3: Digital Root in Arbitrary Base
Student: 1114405015
Base for this student: 7

Input: one non-negative integer x per line until EOF.
Output: digital root of x in base 7, printed as decimal integer.
"""

BASE = 7


def sum_digits_in_base(x: int, base: int) -> int:
    """Return the sum of digits of x in the given base."""
    total = 0
    while x > 0:
        total += x % base
        x //= base
    return total


def digital_root_in_base(x: int, base: int) -> int:
    """Compute digital root in given base by repeated base-digit summation."""
    if x == 0:
        return 0

    while x >= base:
        x = sum_digits_in_base(x, base)
    return x


def solve(lines):
    """Parse input lines and return output lines."""
    out = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x = int(line)
        out.append(str(digital_root_in_base(x, BASE)))
    return out


def main():
    import sys

    result = solve(sys.stdin)
    sys.stdout.write("\n".join(result))


if __name__ == "__main__":
    main()
