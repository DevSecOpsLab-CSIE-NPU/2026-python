from collections import Counter
import sys


def solve(data: str) -> str:
    """
    簡單版寫法：
    1. 每次處理一行。
    2. 用 Counter 數每個字元出現幾次。
    3. 依照「頻率小到大、ASCII 大到小」排序。
    4. 把 ASCII 編碼與次數印出來。
    """
    outputs = []

    for line in data.splitlines():
        counts = Counter(line)
        pairs = sorted(counts.items(), key=lambda item: (item[1], -ord(item[0])))
        outputs.append("\n".join(f"{ord(char)} {count}" for char, count in pairs))

    return "\n\n".join(outputs)


def main() -> None:
    # 這題沒有固定測資筆數，所以直接讀到 EOF 最好記。
    raw_data = sys.stdin.read()
    sys.stdout.write(solve(raw_data))


if __name__ == "__main__":
    main()