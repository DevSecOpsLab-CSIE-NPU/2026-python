import sys


def carry_count(a: str, b: str) -> int:
    # 從個位數開始做直式加法
    i = len(a) - 1
    j = len(b) - 1

    carry = 0
    total = 0

    while i >= 0 or j >= 0:
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0

        s = x + y + carry
        if s >= 10:
            total += 1
            carry = 1
        else:
            carry = 0

        i -= 1
        j -= 1

    return total


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        a, b = line.split()
        if a == "0" and b == "0":
            break

        c = carry_count(a, b)

        if c == 0:
            print("No carry operation.")
        elif c == 1:
            print("1 carry operation.")
        else:
            print(f"{c} carry operations.")


if __name__ == "__main__":
    main()
