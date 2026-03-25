# 題目 10055 簡單版：函數增減性
# 簡單方式：用 list 維護狀態，每次查詢計算區間減函數數

import sys

def main():
    """
    主函數：處理所有輸入資料
    讀取函數數量 N 和操作數量 Q
    初始化 funcs 列表，索引 1 到 N，初始值 0 (增函數)
    對於每項操作：
    - 如果 v=1，反轉 funcs[i] (0<->1)
    - 如果 v=2，計算 funcs[L..R] 的總和 % 2，記錄結果
    最後輸出所有查詢結果
    注意：這個簡單版本對於大 N 和 Q 可能較慢，但容易理解
    """
    # 讀取所有輸入資料
    data = sys.stdin.read().split()
    idx = 0
    N = int(data[idx])  # 函數數量
    idx += 1
    Q = int(data[idx])  # 操作數量
    idx += 1
    # 初始化函數狀態：1-based 索引，0=增, 1=減
    funcs = [0] * (N + 1)
    results = []  # 儲存查詢結果
    for _ in range(Q):  # 對於每項操作
        v = int(data[idx])  # 操作類型
        idx += 1
        if v == 1:  # 反轉操作
            i = int(data[idx])  # 函數索引
            idx += 1
            funcs[i] ^= 1  # 反轉 0<->1
        else:  # 查詢操作
            L = int(data[idx])  # 左界
            idx += 1
            R = int(data[idx])  # 右界
            idx += 1
            # 計算區間 [L, R] 減函數數量 % 2
            dec_count = sum(funcs[L:R+1])
            is_dec = dec_count % 2  # 0=增, 1=減
            results.append(str(is_dec))  # 記錄結果
    # 輸出所有查詢結果，每行一個
    print('\n'.join(results))

if __name__ == "__main__":
    main()