"""UVA 10035 Primary Arithmetic - easy 版。

記法最簡單的方式：
從右邊一位一位加，超過 9 就記一次進位。
"""

import sys


def solve():
    out = []

    for line in sys.stdin.buffer.read().splitlines():
        if not line.strip():
            continue

        a, b = line.decode().split()
        if a == "0" and b == "0":
            break

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        count = 0

        while i >= 0 or j >= 0:
            da = int(a[i]) if i >= 0 else 0
            db = int(b[j]) if j >= 0 else 0
            s = da + db + carry
            if s >= 10:
                count += 1
                carry = 1
            else:
                carry = 0
            i -= 1
            j -= 1

        if count == 0:
            out.append("No carry operation.")
        elif count == 1:
            out.append("1 carry operation.")
        else:
            out.append(f"{count} carry operations.")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()