import sys


def main():
    t = sys.stdin.read().split()
    i = 0
    ans = []

    while i < len(t):
        n = int(t[i])
        i += 1

        arr = list(map(int, t[i:i + n]))
        i += n

        if n <= 1:
            ans.append("Jolly")
            continue

        s = set()
        for k in range(1, n):
            d = abs(arr[k] - arr[k - 1])
            if 1 <= d <= n - 1:
                s.add(d)

        if len(s) == n - 1:
            ans.append("Jolly")
        else:
            ans.append("Not jolly")

    print("\n".join(ans))


if __name__ == "__main__":
    main()