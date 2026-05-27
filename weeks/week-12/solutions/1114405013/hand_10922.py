def solve(in_stream, out_stream):
    while True:
        s = in_stream.readline().strip()
        if s == '0':
            break
        orig = s                     

        deg = 0                      
        while len(s) > 1:
            s = str(sum(int(x) for x in s))
            deg += 1

        deg = deg if deg > 0 else 1

        if s == '9':
            out_stream.write(f"9-degree of {orig} is {deg}.\n")
        else:
            out_stream.write(f"{orig} is not a multiple of 9.\n")


if __name__ == '__main__':
    import sys
    solve(sys.stdin, sys.stdout)
