def solve(in_stream, out_stream):
    while True:
        s = in_stream.readline().strip()
        if s == '0':
            break

        remainder = 0
        for ch in s:
            digit = ord(ch) - 48  
            remainder = (remainder * 10 + digit) % 11

        if remainder == 0:
            out_stream.write(f"{s} is a multiple of 11.\n")
        else:
            out_stream.write(f"{s} is not a multiple of 11.\n")


if __name__ == '__main__':
    import sys
    solve(sys.stdin, sys.stdout)
