# 題目 10057 簡單版：夢中密碼
# 簡單方式：排序後取中位數計算

import sys

def main():
    """
    主函數：處理多組測試資料，直到 n=0
    對於每組資料：
    - 讀取 n，如果 n==0 結束
    - 讀取 n 個數字
    - 排序數字
    - 如果 n 奇數，中位數 = nums[n//2]
    - 如果 n 偶數，中位數 = nums[n//2 - 1] (取前一個)
    - 計算 sum |x - med| for all x
    - 可能的 A 數量：奇數=1，偶數=2
    - 輸出 med, total, poss
    """
    for line in sys.stdin:  # 逐行讀取
        n = int(line.strip())  # 讀取數字個數 n
        if n == 0:  # 如果 n==0，結束程式
            break
        # 讀取 n 個數字
        nums = list(map(int, sys.stdin.readline().split()))
        # 排序數字以找到中位數
        nums.sort()
        if n % 2 == 1:  # 奇數個數字
            med = nums[n // 2]  # 中位數是中間的
        else:  # 偶數個數字
            med = nums[n // 2 - 1]  # 取前一個中位數
        # 計算最小距離總和
        total = sum(abs(x - med) for x in nums)
        # 可能的 A 數量
        poss = 1 if n % 2 == 1 else 2
        # 輸出結果：A, 最小總和, 可能的數量
        print(med, total, poss)

if __name__ == "__main__":
    main()