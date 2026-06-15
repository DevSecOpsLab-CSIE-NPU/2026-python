import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t_str = input_data[0]
    t = int(t_str)
    curr = 1

    for _ in range(t):
        n = int(input_data[curr])
        p = int(input_data[curr+1])
        curr += 2

        hartals = []
        for _ in range(p):
            hartals.append(int(input_data[curr]))
            curr += 1

        lost_days = 0
        for day in range(1, n + 1):
            # Friday is day 6, 13, ... (day % 7 == 6)
            # Saturday is day 7, 14, ... (day % 7 == 0)
            if day % 7 == 6 or day % 7 == 0:
                continue

            for h in hartals:
                if day % h == 0:
                    lost_days += 1
                    break
        print(lost_days)

if __name__ == "__main__":
    solve()
