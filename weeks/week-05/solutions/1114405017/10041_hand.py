import sys
def solve():
    t = int(input())
    for _ in range(t):
        data = list(map(int, input().split()))
        r = data[0]
        streets = sorted(data[1:])
        median = streets[r // 2]
        print(sum(abs(s - median) for s in streets))
if __name__ == "__main__":
    solve()