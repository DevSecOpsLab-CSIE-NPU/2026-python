def clean_data(nums: list, d: int) -> list:
    seen = set()
    unique = []
    for x in nums:
        if x not in seen:
            seen.add(x)
            unique.append(x)
    filtered = [x for x in unique if x % d == 0]
    filtered.sort()
    return filtered


def main():
    while True:
        line = input().strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break
        arr = list(map(int, input().split()))
        result = clean_data(arr, 2)
        if not result:
            print("NONE")
        else:
            print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
