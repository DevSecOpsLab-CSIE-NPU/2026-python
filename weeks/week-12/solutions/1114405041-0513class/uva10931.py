"""
UVA 10931 - Parity

輸入整數 I，輸出其二進位字串與 1 的個數。
"""

from __future__ import annotations


def parity_line(n: int) -> str:
    """回傳單筆輸出格式字串。"""
    b = bin(n)[2:]
    ones = b.count("1")
    return f"The parity of {b} is {ones} (mod 2)."


def solve_io(data: str) -> str:
    out: list[str] = []
    for line in data.splitlines():
        s = line.strip()
        if not s:
            continue

        n = int(s)
        if n == 0:
            break

        out.append(parity_line(n))

    return "\n".join(out)


def main() -> None:
    import sys

    sys.stdout.write(solve_io(sys.stdin.read()))


if __name__ == "__main__":
    main()
