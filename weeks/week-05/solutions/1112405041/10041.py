import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    idx = 1
    for _ in range(t):
        r = int(input_data[idx])
        idx += 1
        s = sorted([int(x) for x in input_data[idx:idx+r]])
        idx += r

        median = s[r // 2]
        total_distance = sum(abs(x - median) for x in s)
        print(total_distance)

if __name__ == "__main__":
    solve()
