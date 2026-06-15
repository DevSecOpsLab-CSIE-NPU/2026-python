import sys
from collections import Counter

def solve():
    # 讀取測試資料數量
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    # 處理所有文字內容，排除第一行的組數
    text = "".join(input_data[1:]).upper()

    # 只保留 A-Z
    letters = [char for char in text if char.isalpha()]

    # 統計頻率
    counts = Counter(letters)

    # 按照「次數降序」且「字母升序」排列 (CPE 經典要求)
    # x[0] 是字母, x[1] 是次數
    # key=lambda x: (-x[1], x[0])
    sorted_res = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for char, count in sorted_res:
        sys.stdout.write(f"{char} {count}\n")

if __name__ == "__main__":
    solve()
