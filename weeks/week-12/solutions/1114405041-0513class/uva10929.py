"""
UVA 10929 - You can say 11

由於數字可能非常長，使用字串加上交錯加減法判斷是否為 11 的倍數。
"""

from __future__ import annotations


def is_multiple_of_11(num_str: str) -> bool:
    """利用交錯和判斷：sum(奇位) - sum(偶位) 是否可被 11 整除。"""
    alt_sum = 0
    sign = 1

    for ch in num_str:
        alt_sum += sign * (ord(ch) - ord("0"))
        sign *= -1

    return alt_sum % 11 == 0


def solve_io(data: str) -> str:
    out: list[str] = []
    for line in data.splitlines():
        s = line.strip()
        if not s:
            continue
        if s == "0":
            break

        if is_multiple_of_11(s):
            out.append(f"{s} is a multiple of 11.")
        else:
            out.append(f"{s} is not a multiple of 11.")

    return "\n".join(out)


def main() -> None:
    import sys

    sys.stdout.write(solve_io(sys.stdin.read()))


if __name__ == "__main__":
    main()
