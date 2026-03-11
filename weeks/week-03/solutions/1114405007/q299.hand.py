def main() -> None:
    import sys
lines = [line.strip() for line in sys.stdin if line.strip()]
if not lines:
    return
t = int(lines[0])
p = 1
for _ in range(t):
    l = int(lines[p])
    p += 1
    arr = list(map(int, lines[p].split()))
    p += 1
    swaps = 0
    for i in range(l):
        for j in range(i + 1, l):
            if arr[i] > arr[j]:
                swaps += 1
    print(f"Optimal train swapping takes {swaps} swaps.")
if __name__ == "__main__":
    main()