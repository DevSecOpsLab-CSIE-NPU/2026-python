import sys

# 詳細繁體中文註解說明：
# 這題的目標是找出在數字 i 到 j 之間，哪一個數字跑「3n+1」流程最久。
# 流程規則：
# 1. 偶數就除以 2
# 2. 奇數就乘 3 再加 1
# 3. 算到變成 1 為止

def solve():
    # 使用 sys.stdin 讀取每一行輸入
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue
            
        # 讀入原始的 i 和 j
        num1 = int(parts[0])
        num2 = int(parts[1])
        
        # 確保我們是從小數字跑迴圈到大數字
        start = min(num1, num2)
        end = max(num1, num2)
        
        max_length = 0
        
        # 檢查區間內的每一個數字 n
        for n in range(start, end + 1):
            current_n = n
            count = 1 # 初始長度包含數字自己
            
            # 開始跑 3n + 1 演算法，直到變成 1
            while current_n != 1:
                if current_n % 2 == 0:
                    current_n = current_n // 2
                else:
                    current_n = 3 * current_n + 1
                count += 1
            
            # 如果這次算的長度比之前記錄的還長，就更新最大值
            if count > max_length:
                max_length = count
        
        # 按照題目要求格式輸出：原本的兩數 + 最大長度
        print(f"{num1} {num2} {max_length}")

if __name__ == "__main__":
    solve()