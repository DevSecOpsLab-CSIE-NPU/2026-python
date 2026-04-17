# UVA 299: Optimal train swapping
# 計算排序所需的最少相鄰交換次數

def count_swaps(cars):
    swaps = 0
    arr = list(cars)
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps


def solve_299(input_text):
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''
    t = int(lines[0])
    output = []
    idx = 1
    for _ in range(t):
        l = int(lines[idx])
        idx += 1
        cars = list(map(int, lines[idx].split()))
        idx += 1
        output.append(f"Optimal train swapping takes {count_swaps(cars)} swaps.")
    return "\n".join(output)


def main():
    import sys
    print(solve_299(sys.stdin.read()))


if __name__ == '__main__':
    main()
