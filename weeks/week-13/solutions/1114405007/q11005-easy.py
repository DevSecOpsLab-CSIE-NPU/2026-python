"""11005 簡單版：找最便宜進位。

重點：
1) 試所有進位 2~36
2) 算出此進位表示法的每一位成本總和
3) 挑最小成本，平手就全部列出
"""

import sys


def cost_in_base(n, base, costs):
    # 數字 0 的表示就是 "0"，成本直接是 costs[0]
    if n == 0:
        return costs[0]

    total = 0
    while n > 0:
        n, d = divmod(n, base)
        total += costs[d]
    return total


def solve(text):
    arr = text.split()
    if not arr:
        return ""

    p = 0
    t = int(arr[p])
    p += 1
    out = []

    for case_id in range(1, t + 1):
        # 題目給 36 個成本：0~9, A~Z
        costs = list(map(int, arr[p : p + 36]))
        p += 36

        q = int(arr[p])
        p += 1

        out.append(f"Case {case_id}:")

        for _ in range(q):
            n = int(arr[p])
            p += 1

            best = 10**18
            ans = []

            for base in range(2, 37):
                c = cost_in_base(n, base, costs)
                if c < best:
                    best = c
                    ans = [base]
                elif c == best:
                    ans.append(base)

            out.append(
                f"Cheapest base(s) for number {n}: " + " ".join(map(str, ans))
            )

        if case_id != t:
            out.append("")

    return "\n".join(out)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
