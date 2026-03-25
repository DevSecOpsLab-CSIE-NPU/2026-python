"""
UVA 10038: Jolly Jumpers
題目:
判斷一個長度為 n 的整數序列是否為 "Jolly Jumper"。
如果相鄰兩元素的差的絕對值剛好包含了 1 到 n-1 之間的所有整數。

輸入:
每行開頭是一個整數 n (n < 3000)。
接著後面有 n 個整數，代表該序列。
輸入直到檔案結束 (EOF)。

輸出:
如果是 Jolly Jumper，輸出 Jolly
如果不是，輸出 Not jolly
"""

import sys

def solve():
    # 讀取標準輸入的每一行
    for line in sys.stdin:
        # 去除頭尾空白
        line = line.strip()
        if not line:
            continue
            
        try:
            # 解析整行輸入為數字列表
            parts = list(map(int, line.split()))
            
            # 第一個數字是 n
            if not parts:
                continue
                
            n = parts[0]
            
            # 序列內容是剩下的數字 
            sequence = parts[1:]
            
            # 題目可能給 n 但序列數字可能分在不同行?
            # 簡單起見假設題目是一行一組測試資料，或者所有數字都在同一行
            # 根據常見 UVA 10038 格式，通常是一行一組 (n 接著 n 個數)
            
            # 邊界情況: 如果 n=1，題目定義為 Jolly (因為不需要任何差值)
            if n == 1:
                print("Jolly")
                continue
                
            # 計算所有相鄰差的絕對值
            diffs = []
            for i in range(len(sequence) - 1):
                diff = abs(sequence[i] - sequence[i+1])
                diffs.append(diff)
            
            # 檢查差值集合是否剛好等於 {1, 2, ..., n-1}
            diff_set = set(diffs)
            expected_set = set(range(1, n))
            
            if diff_set == expected_set:
                print("Jolly")
            else:
                print("Not jolly")
                
        except ValueError:
            pass

if __name__ == '__main__':
    solve()
