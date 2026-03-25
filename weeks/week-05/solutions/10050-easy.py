# 題目 10050 簡單版：罷會損失天數
# 簡單方式：直接模擬每一天，檢查條件

import sys

def solve():
    """
    主函數：處理所有輸入資料
    讀取測試案例數量 T，然後對於每組測試資料：
    - 讀取天數 N 和政黨數 P
    - 讀取 P 個罷會參數
    - 模擬每一天 d 從 1 到 N：
      - 計算星期：((d-1) % 7) + 1
      - 如果不是假日 (6=五, 7=六)，檢查是否有罷會
      - 如果有罷會，損失天數 +1
    - 輸出損失天數
    """
    # 讀取所有輸入資料
    data = sys.stdin.read().split()
    # 第一個數字是測試案例數量 T
    T = int(data[0])
    idx = 1  # 索引從 1 開始
    for _ in range(T):  # 對於每組測試資料
        N = int(data[idx])  # 讀取天數 N
        idx += 1
        P = int(data[idx])  # 讀取政黨數 P
        idx += 1
        # 讀取 P 個罷會參數
        hs = [int(data[idx + i]) for i in range(P)]
        idx += P
        lost = 0  # 初始化損失天數
        for d in range(1, N + 1):  # 對於每一天
            # 計算星期：1=日, 2=一, ..., 7=六
            wd = ((d - 1) % 7) + 1
            if wd not in [6, 7]:  # 如果是工作日 (非五六)
                # 檢查是否有政黨在這天罷會
                for h in hs:
                    if d % h == 0:  # 如果 d 是 h 的倍數
                        lost += 1  # 損失天數 +1
                        break  # 只要一個政黨罷會就夠了
        # 輸出這組測試資料的損失天數
        print(lost)

if __name__ == "__main__":
    solve()