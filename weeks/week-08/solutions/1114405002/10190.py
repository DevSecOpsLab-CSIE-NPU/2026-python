import sys

def merge_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            merged[-1] = (last[0], max(last[1], current[1]))
        else:
            merged.append(current)
    total = sum(end - start for start, end in merged)
    return total

def main():
    lines = sys.stdin.readlines()
    data = []
    for line in lines:
        data.extend(line.split())
    index = 0
    N = int(data[index])
    index += 1
    W = int(data[index])
    index += 1
    T = int(data[index])
    index += 1
    V = float(data[index])
    index += 1
    intervals = []
    for _ in range(N):
        x = int(data[index])
        index += 1
        l = int(data[index])
        index += 1
        v = int(data[index])  # ignored
        index += 1
        intervals.append((x, x + l))
    covered = merge_intervals(intervals)
    uncovered = W - covered
    volume = V * uncovered * T
    print(f"{volume:.2f}")

if __name__ == "__main__":
    main()