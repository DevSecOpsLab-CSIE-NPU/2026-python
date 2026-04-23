# 10008-easy.py
# UVA 10008：What's Cryptanalysis? (簡單版)

import sys

def solve():
    # 1. 讀入所有文字並轉大寫
    input_data = sys.stdin.read().upper()

    # 2. 統計 A-Z 出現次數
    counts = {}
    for char in input_data:
        if 'A' <= char <= 'Z':
            counts[char] = counts.get(char, 0) + 1

    # 3. 排序：先比次數 (大到小)，次數一樣比字母 (小到大)
    # Python sorted 的小技巧：x[1] 加負號代表降序，x[0] 正常代表升序
    items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    # 4. 輸出
    for char, count in items:
        print(f"{char} {count}")

if __name__ == "__main__":
    solve()
