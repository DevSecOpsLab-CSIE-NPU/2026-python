"""UVA 10035 手打版。"""

import sys


def solve():
    ans = []
    data = sys.stdin.buffer.read().splitlines()

    for line in data:
        if not line.strip():
            continue

        a, b = line.decode().split()
        if a == "0" and b == "0":
            break

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        cnt = 0

        while i >= 0 or j >= 0:
            x = 0 if i < 0 else int(a[i])
            y = 0 if j < 0 else int(b[j])
            total = x + y + carry

            if total >= 10:
                cnt += 1
                carry = 1
            else:
                carry = 0

            i -= 1
            j -= 1

        if cnt == 0:
            ans.append("No carry operation.")
        elif cnt == 1:
            ans.append("1 carry operation.")
        else:
            ans.append(str(cnt) + " carry operations.")

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    solve()
