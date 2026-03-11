import sys

# 題目提供的範例輸入，用來快速檢查程式是否正確。
SAMPLE_INPUT = """1 10
100 200
201 210
900 1000
"""

# 題目對應的範例輸出。
SAMPLE_OUTPUT = """1 10 20
100 200 125
201 210 89
900 1000 174"""

# 記憶化快取：memo[n] 代表數字 n 的 cycle length。
memo = {1: 1}


def cycle_length(n: int) -> int:
    # 保留原始輸入，最後要回傳原本 n 的答案。
    original = n
    # 記錄這次遞推過程中，尚未寫入快取的數字。
    path = []

    while n not in memo:
        path.append(n)
        if n % 2 == 1:
            # 奇數套用 3n + 1。
            n = 3 * n + 1
        else:
            # 偶數除以 2。
            n //= 2

    # 找到已知答案後，倒著把整條路徑的答案回填進快取。
    length = memo[n]
    for value in reversed(path):
        length += 1
        memo[value] = length

    return memo[original]


def max_cycle_length(i: int, j: int) -> int:
    # 計算時先取正確區間，但輸出時仍保留原始 i、j 的順序。
    start, end = sorted((i, j))
    best = 0

    for number in range(start, end + 1):
        best = max(best, cycle_length(number))

    return best


def solve(text: str) -> str:
    output = []

    for line in text.splitlines():
        # 跳過空白行，避免 split 發生錯誤。
        if not line.strip():
            continue
        # 每一行都是一組 i、j。
        i, j = map(int, line.split())
        output.append(f"{i} {j} {max_cycle_length(i, j)}")

    return "\n".join(output)


def run_sample_test() -> None:
    # 直接比對題目範例，方便本機快速自我測試。
    result = solve(SAMPLE_INPUT)
    print(result)
    assert result == SAMPLE_OUTPUT, "範例測試未通過"


if __name__ == "__main__":
    # 在互動式終端直接執行時，沒有輸入就改跑範例測試。
    if sys.stdin.isatty():
        run_sample_test()
    else:
        data = sys.stdin.read()
        if not data.strip():
            sys.exit(0)
        # 有標準輸入時，依題目格式輸出答案。
        print(solve(data))
