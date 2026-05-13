#!/usr/bin/env python3
import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out_lines = []
    for _ in range(t):
        S = int(data[idx]); D = int(data[idx+1]); idx += 2
        if S < D or (S + D) % 2 != 0:
            out_lines.append("impossible")
        else:
            high = (S + D) // 2
            low = (S - D) // 2
            if low < 0:
                out_lines.append("impossible")
            else:
                out_lines.append(f"{high} {low}")
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    main()
