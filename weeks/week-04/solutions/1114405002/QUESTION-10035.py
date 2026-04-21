"""UVA 10035 Primary Arithmetic 標準版。

逐位相加並模擬進位，直接計算 carry 次數。
"""

import sys


def count_carries(a, b):
    carry = 0
    count = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0:
        x = ord(a[i]) - 48 if i >= 0 else 0
        y = ord(b[j]) - 48 if j >= 0 else 0
        total = x + y + carry
        if total >= 10:
            count += 1
            carry = 1
        else:
            carry = 0
        i -= 1
        j -= 1

    return count


def solve():
    out = []
    for line in sys.stdin.buffer.read().splitlines():
        if not line.strip():
            continue
        a, b = line.split()
        if a == b == b"0":
            break

        carry_count = count_carries(a.decode(), b.decode())
        if carry_count == 0:
            out.append("No carry operation.")
        elif carry_count == 1:
            out.append("1 carry operation.")
        else:
            out.append(f"{carry_count} carry operations.")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()