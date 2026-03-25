# 題目 10041 簡單版：Vito 的房子問題
# 使用更簡單、更容易記憶的方式：直接排序後取中位數計算

import sys

# 簡單函數：讀取、排序、計算中位數、求總距離
def solve():
    """
    主函數：處理所有輸入資料
    讀取測試案例數量 T，然後對於每組測試資料：
    - 讀取親戚數量 r
    - 讀取 r 個地址
    - 排序地址
    - 取中位數 (r//2)
    - 計算所有地址到中位數的絕對距離總和
    - 輸出結果
    """
    # 讀取所有輸入資料
    data = sys.stdin.read().split()
    # 第一個數字是測試案例數量 T
    T = int(data[0])
    idx = 1  # 索引從 1 開始
    for _ in range(T):  # 對於每組測試資料
        r = int(data[idx])  # 讀取親戚數量 r
        idx += 1
        # 讀取 r 個地址
        nums = [int(data[idx + i]) for i in range(r)]
        idx += r
        # 排序地址，以便找到中位數
        nums.sort()
        # 中位數是排序後的第 r//2 個元素（對於偶數，取前一個）
        if r % 2 == 1:
            mid = nums[r // 2]
        else:
            mid = nums[r // 2 - 1]
        # 計算總距離：每個地址到中位數的絕對距離總和
        total = sum(abs(x - mid) for x in nums)
        # 輸出結果
        print(total)

if __name__ == "__main__":
    solve()