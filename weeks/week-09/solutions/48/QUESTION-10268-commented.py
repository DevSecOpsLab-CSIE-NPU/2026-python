import sys


# 回傳最少丟幾次可測到 n 層；若 63 次內做不到則回傳 None
def min_trials(k, n):
    # prev[e] = 用 e 顆球、t-1 次可測層數
    prev = [0] * (k + 1)

    for t in range(1, 64):
        cur = [0] * (k + 1)
        for e in range(1, k + 1):
            # 經典轉移：破/不破兩種情況 + 當前層
            cur[e] = prev[e - 1] + prev[e] + 1

        if cur[k] >= n:
            return t
        prev = cur

    return None


def solve():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        k, n = map(int, line.split())
        if k == 0:
            break

        ans = min_trials(k, n)
        if ans is None:
            out.append("More than 63 trials needed.")
        else:
            out.append(str(ans))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
