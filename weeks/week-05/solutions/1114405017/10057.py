import sys

def solve():
    # 使用 sys.stdin 讀取所有輸入，處理多組測資
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    while idx < len(input_data):
        try:
            n = int(input_data[idx])
            idx += 1
            # 讀取接下來的 n 個數字
            nums = []
            for _ in range(n):
                nums.append(int(input_data[idx]))
                idx += 1
            
            # 1. 排序
            nums.sort()
            
            # 2. 找出中位數範圍的兩個關鍵索引
            # 若 n=4, mid1 索引為 1, mid2 索引為 2
            # 若 n=5, mid1 索引為 2, mid2 索引為 2
            mid1 = nums[(n - 1) // 2]
            mid2 = nums[n // 2]
            
            # 3. 計算輸入中落在 [mid1, mid2] 範圍內的數字數量
            count = 0
            for x in nums:
                if mid1 <= x <= mid2:
                    count += 1
            
            # 4. 計算 A 的可能整數種類
            possible_a_count = mid2 - mid1 + 1
            
            # 格式化輸出
            print(f"{mid1} {count} {possible_a_count}")
            
        except (ValueError, IndexError):
            break

if __name__ == "__main__":
    solve()