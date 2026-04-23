import sys

def calculate_difference(a, b):
    """
    計算兩個整數的絕對差值。
    Python 內建支援大數運算，因此即使數字高達 2^63 也可直接相減並取絕對值。
    """
    return abs(a - b)

if __name__ == '__main__':
    # 讀取標準輸入，支援多筆測資
    for line in sys.stdin:
        # 移除頭尾空白並按空格切割
        parts = line.split()
        if len(parts) == 2:
            # 取得 Hashmat 與敵人的士兵數量
            a = int(parts[0])
            b = int(parts[1])
            # 計算並印出差值 (絕對值)
            print(calculate_difference(a, b))