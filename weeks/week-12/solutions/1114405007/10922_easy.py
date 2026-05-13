# UVA 10922 - 2 the 9s
# 簡單版本（含中文註解）

import sys


def digit_sum(s: str) -> int:
    total = 0
    for ch in s:
        total += ord(ch) - ord("0")
    return total


def main() -> None:
    out = []

    for raw in sys.stdin:
        num = raw.strip()
        if not num:
            continue
        if num == "0":
            break

        first_sum = digit_sum(num)

        # 不是 9 的倍數
        if first_sum % 9 != 0:
            out.append(f"{num} is not a multiple of 9.")
            continue

        # 是 9 的倍數，計算 9-degree
        degree = 1
        value = first_sum

        while value != 9:
            value = digit_sum(str(value))
            degree += 1

        out.append(f"{num} is a multiple of 9 and has 9-degree {degree}.")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
