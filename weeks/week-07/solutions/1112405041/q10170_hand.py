import sys
import math

def solve():
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            s, d = map(int, line.split())
            # S + (S+1) + ... + n >= D
            # Sum = (S + n) * (n - S + 1) / 2 >= D
            # n^2 + n - S^2 + S - 2D >= 0
            # n = (-1 + sqrt(1 - 4(1)(-S^2 + S - 2D))) / 2
            # Simplified: n = ceil((-1 + sqrt(1 + 4(S^2 - S + 2D))) / 2)

            n = math.ceil((-1 + math.sqrt(1 + 4 * (s*s - s + 2*d))) / 2)
            print(n)
        except EOFError:
            break
        except Exception:
            # Fallback to loop for very large numbers if precision fails
            curr_d = 0
            curr_s = s
            while True:
                curr_d += curr_s
                if curr_d >= d:
                    print(curr_s)
                    break
                curr_s += 1

if __name__ == "__main__":
    solve()
