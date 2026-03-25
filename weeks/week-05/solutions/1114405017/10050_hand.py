def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = int(input())
        all_hartals = set()
        for _ in range(P):
            h = int(input())
            all_hartals.update(range(h, N + 1, h))
        lost_days = [day for day in all_hartals 
                     if day % 7 != 6 and day % 7 != 0]
        print(len(lost_days))
if __name__ == "__main__":
    solve()