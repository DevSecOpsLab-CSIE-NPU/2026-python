def solve() -> None:
    import sys

    for line in sys.stdin:
        s = line.strip()
        if not s:
            continue
        if s == "0":
            break

        n = int(s)
        binary = format(n, "b")
        count_ones = binary.count("1")
        sys.stdout.write(f"The parity of {binary} is {count_ones} (mod 2).\n")


if __name__ == "__main__":
    solve()
