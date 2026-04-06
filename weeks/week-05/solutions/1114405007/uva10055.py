from sys import stdin


# 這題讀到 EOF 為止，每行輸出兩數差的絕對值。
def solve(lines):
    results = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        left, right = map(int, stripped.split())
        results.append(str(abs(left - right)))

    return "\n".join(results)


def main():
    print(solve(stdin.readlines()))


if __name__ == "__main__":
    main()