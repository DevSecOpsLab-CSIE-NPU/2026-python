# 題目 10056 簡單版：玩家獲勝機率
# 簡單方式：直接套公式計算

import sys

def main():
    """
    主函數：處理所有輸入資料
    讀取測試案例數量 S，然後對於每組測試資料：
    - 讀取玩家數 N，成功機率 p，玩家編號 i
    - 計算失敗機率 q = 1 - p
    - 如果 p == 0，機率為 0
    - 如果 q^N == 1 (即 p==1)，只有第一個玩家機率 1，其他 0
    - 否則，使用公式：p * q^(i-1) / (1 - q^N)
    - 輸出機率，四捨五入到小數點後四位
    """
    # 讀取所有輸入資料
    data = sys.stdin.read().split()
    S = int(data[0])  # 測試案例數量
    idx = 1  # 索引從 1 開始
    for _ in range(S):  # 對於每組測試資料
        N = int(data[idx])  # 玩家數
        p = float(data[idx + 1])  # 成功機率
        i = int(data[idx + 2])  # 玩家編號 (1-based)
        idx += 3
        q = 1 - p  # 失敗機率
        if p == 0:  # 永遠失敗
            prob = 0.0
        elif q ** N == 1:  # p==1，永遠成功，只有第一個玩家贏
            prob = 1.0 if i == 1 else 0.0
        else:  # 一般情況，使用幾何分佈公式
            prob = p * (q ** (i - 1)) / (1 - q ** N)
        # 輸出機率，四捨五入到小數點後四位
        print(f"{prob:.4f}")

if __name__ == "__main__":
    main()