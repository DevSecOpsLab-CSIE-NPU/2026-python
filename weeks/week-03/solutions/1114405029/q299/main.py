import sys

# 進階實作版：使用標準泡沫排序法計算交換次數
# 核心邏輯：相鄰交換的最少次數等於逆序對的數量
def solve():
    # 讀取測試資料組數 N
    line = sys.stdin.readline()
    if not line:
        return
    
    try:
        num_test_cases = int(line.strip())
    except ValueError:
        return

    for _ in range(num_test_cases):
        # 讀取火車長度 L
        length_line = sys.stdin.readline()
        if not length_line:
            break
        L = int(length_line.strip())
        
        # 讀取車廂順序（處理可能跨行或多餘空格的情況）
        train = []
        while len(train) < L:
            train.extend(map(int, sys.stdin.readline().split()))
            
        swap_count = 0
        
        # 執行泡沫排序 (Bubble Sort)
        # 外部迴圈跑 L-1 輪
        for i in range(L - 1):
            # 內部迴圈比較相鄰元素
            for j in range(L - 1 - i):
                if train[j] > train[j + 1]:
                    # 發現逆序，進行交換
                    train[j], train[j + 1] = train[j + 1], train[j]
                    swap_count += 1
        
        # 依照題目要求格式輸出結果
        print(f"Optimal train swapping takes {swap_count} swaps.")

if __name__ == "__main__":
    solve()