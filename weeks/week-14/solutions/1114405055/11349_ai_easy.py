import sys

# 讀取全部資料
data = sys.stdin.read().split()
if data:
    t = int(data[0])
    idx = 1
    for case_num in range(1, t + 1):
        idx += 2 # 跳過 "N" 和 "="
        n = int(data[idx])
        idx += 1
        
        # 取得二維轉一維的矩陣內容
        matrix = [int(x) for x in data[idx:idx + n * n]]
        idx += n * n
        
        # 檢查是否所有元素非負，且正反向順序相同
        is_sym = all(x >= 0 for x in matrix) and matrix == matrix[::-1]
        print(f"Test #{case_num}: {'Symmetric.' if is_sym else 'Non-symmetric.'}")
