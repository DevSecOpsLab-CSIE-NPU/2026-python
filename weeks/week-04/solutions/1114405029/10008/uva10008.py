from collections import Counter


def solve(data: str) -> str:
    lines = data.splitlines()
    n = int(lines[0])
    counter = Counter()

    for i in range(1, n + 1):
        for ch in lines[i].upper():
            if "A" <= ch <= "Z":
                counter[ch] += 1

    result = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join(f"{ch} {count}" for ch, count in result)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))