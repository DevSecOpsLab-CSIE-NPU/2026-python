def main() -> None:
    import sys
arr = [line.rstrip("\n") for line in sys.stdin]
if not arr:
    return
max_len = max(len(s) for s in arr)
for c in range(max_len):
    out = []
    for r in range(len(arr) - 1, -1, -1):
        if c < len(arr[r]):
            out.append(arr[r][c])
        else:
            out.append(" ")
    print("".join(out).rstrip())
if __name__ == "__main__":
    main()