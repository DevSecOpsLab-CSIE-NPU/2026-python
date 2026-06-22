import sys


def process(arr, d):
    # dict.fromkeys 在插入時自動覆蓋重複 key，但保留「第一次出現」的插入順序，時間複雜度 O(n)
    deduped = list(dict.fromkeys(arr))

    # 0 % d == 0 永真，負數的 % 在 Python 中與數學定義一致，可直接用 == 0 判斷整除
    filtered = [x for x in deduped if x % d == 0]

    filtered.sort()
    return filtered


def main():
    D = 3
    data = sys.stdin.read().split()
    idx = 0
    out_lines = []

    while idx < len(data):
        n = int(data[idx])
        idx += 1
        if n == 0:
            break
        arr = [int(data[idx + i]) for i in range(n)]
        idx += n

        result = process(arr, D)
        out_lines.append(" ".join(map(str, result)) if result else "NONE")

    print("\n".join(out_lines))


if __name__ == "__main__":
    main()
