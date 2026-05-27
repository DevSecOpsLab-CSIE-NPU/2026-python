def solve(in_stream, out_stream):
    n = int(in_stream.readline())

    for _ in range(n):
        s, d = map(int, in_stream.readline().split())

        if (s + d) % 2:
            out_stream.write("impossible\n")
            continue

        big = (s + d) // 2
        small = s - big

        if small < 0:
            out_stream.write("impossible\n")
            continue

        out_stream.write(f"{big} {small}\n")


if __name__ == "__main__":
    import sys

    solve(sys.stdin, sys.stdout)
