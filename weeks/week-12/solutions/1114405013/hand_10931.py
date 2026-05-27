def solve(in_stream, out_stream):
    while True:
        s = in_stream.readline().strip()
        if s == '0':
            break

        n = int(s)                        
        b = bin(n)[2:]                    
        p = b.count('1')                  

        out_stream.write(f"The parity of {b} is {p} (mod 2).\n")


if __name__ == '__main__':
    import sys
    solve(sys.stdin, sys.stdout)
