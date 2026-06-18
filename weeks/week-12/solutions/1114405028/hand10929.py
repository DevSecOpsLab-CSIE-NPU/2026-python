def solve() -> None:
    import sys

    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        if s == "0":
            break

        odd_sum = sum(int(s[i]) for i in range(0, len(s), 2))
        even_sum = sum(int(s[i]) for i in range(1, len(s), 2))
        if abs(odd_sum - even_sum) % 11 == 0:
            sys.stdout.write(f"{s} is a multiple of 11.\n")
        else:
            sys.stdout.write(f"{s} is not a multiple of 11.\n")


if __name__ == "__main__":
    solve()
