import sys

def solve(N, W, T, V, umbrellas):
    if N == 0:
        return f"{W * T * V:.2f}"

    intervals = sorted([[u[0], u[0] + u[1]] for u in umbrellas])

    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    total_covered_length = sum(end - start for start, end in merged)

    uncovered_length = max(0, W - total_covered_length)
    total_rain_volume = uncovered_length * T * V

    return f"{total_rain_volume:.2f}"

if __name__ == '__main__':
    data = sys.stdin.read().split()
    idx = 0
    while idx < len(data):
        N, W, T, V = int(data[idx]), int(data[idx+1]), int(data[idx+2]), int(data[idx+3])
        idx += 4
        umbrellas = [tuple(map(int, data[idx+i*3 : idx+i*3+3])) for i in range(N)]
        idx += N * 3
        print(solve(N, W, T, V, umbrellas))