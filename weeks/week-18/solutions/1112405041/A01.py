def clean_data(nums, D):
    seen = set()
    deduped = []
    for x in nums:
        if x not in seen:
            deduped.append(x)
            seen.add(x)
    filtered = [x for x in deduped if x % D == 0]
    return sorted(filtered)


def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        data = list(map(int, sys.stdin.readline().split()))
        result = clean_data(data, D=3)
        if not result:
            print("NONE")
        else:
            print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
