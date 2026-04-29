"""
註解版本：雞蛋掉落問題（經典）。使用動態規劃計算在 t 次丟擲、e 顆蛋下
最多可測試的樓層數，反向找最小 t 使得可測樓層數 >= n。
"""
import sys


def min_trials(k, n):
    prev = [0] * (k + 1)
    for t in range(1, 64):
        cur = [0] * (k + 1)
        for e in range(1, k + 1):
            # cur[e] = prev[e-1] (如果破) + prev[e] (如果不破) + 1 (當前層)
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
