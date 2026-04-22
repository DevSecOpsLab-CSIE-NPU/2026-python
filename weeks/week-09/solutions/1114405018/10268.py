import sys


def solve(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    out = []

    for line in lines:
        k, n = map(int, line.split())
        if k == 0:
            break

        # dp[e] 代表目前試驗次數下，e 顆水球最多可測出幾層樓
        dp = [0] * (k + 1)
        ans = None

        for t in range(1, 64):
            for e in range(k, 0, -1):
                dp[e] = dp[e] + dp[e - 1] + 1
            if dp[k] >= n:
                ans = str(t)
                break

        if ans is None:
            out.append("More than 63 trials needed.")
        else:
            out.append(ans)

    return "\n".join(out) + ("\n" if out else "")


def main():
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
