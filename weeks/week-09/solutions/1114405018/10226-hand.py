import sys

def solve(text):
    vals = list(map(int, text.split()))
    if not vals:
        return ""
    
    it = iter(vals)
    out = []

    while True:
        k = next(it)
        n = next(it)
        if k == 0:
            break

        dp = [0]    
        ans = "More than 63 trials needed."

        for t in range(1, 64):
            for e in range(k, 0, -1):
                dp[e] = dp[e] + dp[e - 1] + 1
            if dp[k] >= n:
                ans = str(t)
                break

        out.append(ans)

    return "\n".join(out) + "\n"

def main():
    sys.stdout.write(solve(sys.stdin.read()))

if __name__ == "__main__":
    main()
    