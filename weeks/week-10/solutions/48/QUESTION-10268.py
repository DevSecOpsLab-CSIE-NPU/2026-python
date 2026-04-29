import sys


def min_trials(k, n):
    # 優化點：改用「可測樓層數」的 DP，避免枚舉樓層與重複計算。
    prev = [0] * (k + 1)
    for t in range(1, 64):
        cur = [0] * (k + 1)
        for e in range(1, k + 1):
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
