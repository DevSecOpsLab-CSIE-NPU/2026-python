import sys


def process_sequence(numbers: list[int], d: int) -> list[int]:
    """
    對數列完成三步處理：
    1. 去重（保留第一次出現順序）
    2. 只保留能被 d 整除的數
    3. 由大到小排序（降冪）
    """
    # Step 1: 去重，保留首次出現順序
    seen = set()
    deduped = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            deduped.append(num)

    # Step 2: 只保留能被 d 整除
    filtered = [num for num in deduped if num % d == 0]

    # Step 3: 由大到小排序
    filtered.sort(reverse=True)

    return filtered


def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return

    idx = 0
    d = int(data[idx])
    idx += 1

    out_lines = []
    while idx < len(data):
        n = int(data[idx])
        idx += 1
        if n == 0:
            break

        numbers = list(map(int, data[idx:idx + n]))
        idx += n

        result = process_sequence(numbers, d)
        if result:
            out_lines.append(" ".join(map(str, result)))
        else:
            out_lines.append("none")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()