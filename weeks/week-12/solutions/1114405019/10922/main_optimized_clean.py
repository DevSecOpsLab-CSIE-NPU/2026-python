import sys
def solve():
    for line in sys.stdin:
        n = line.strip()
        if n == "0": break
        if not n: continue
        s = sum(int(d) for d in n)
        if s % 9 != 0:
            print(f"{n} is not a multiple of 9.")
            continue
        deg = 1
        while s > 9:
            s = sum(int(d) for d in str(s))
            deg += 1
        print(f"9-degree of {n} is {deg}.")
if __name__ == "__main__":
    solve()
