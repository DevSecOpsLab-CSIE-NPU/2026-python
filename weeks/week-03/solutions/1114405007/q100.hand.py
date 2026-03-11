def cycle_length(n: int) -> int:
    if n <= 0:
        raise ValueError

    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1

    return length
    def max_cycle(i: int, j: int) -> int:
        if i <= 0 or j <= 0:
            raise ValueError

        left, right = (i, j) if i <= j else (j, i)
        best = 0
        for value in range(left, right + 1):
            best = max(best, cycle_length(value))

        return best
        def main() -> None:
            import sys

            for line in sys.stdin:
                line = line.strip()
                if not line:
                    continue

                a_str, b_str = line.split()
                a, b = int(a_str), int(b_str)
                print(f"{a} {b} {max_cycle(a, b)}")
                if __name__ == "__main__":
                    main()
