import sys
import math

# 衛星距離計算 - 大一小萌新版
# 我們要算兩個衛星之間的「弧長」和「弦長」

def main():
    # 讀取輸入內容
    input_text = sys.stdin.read().split()
    if not input_text:
        return

    idx = 0
    while idx < len(input_text):
        # s: 高度, a: 角度, unit: 單位 (deg 或 min)
        s = float(input_text[idx])
        a = float(input_text[idx + 1])
        unit = input_text[idx + 2]
        idx += 3

        # 1. 算出半徑 r
        # 地球半徑是 6440
        radius = 6440.0 + s

        # 2. 處理角度，全部換成度數 (degree)
        if unit == 'min':
            # 1 度 = 60 分
            angle_in_deg = a / 60.0
        else:
            angle_in_deg = a

        # 關鍵陷阱：如果角度大於 180 度，要取比較小的那個弧
        if angle_in_deg > 180:
            angle_in_deg = 360.0 - angle_in_deg

        # 3. 轉成弧度 (radian)，因為 Python 的 math 函式要用弧度
        angle_in_rad = angle_in_deg * math.pi / 180.0

        # 4. 計算弧長 = 半徑 * 弧度
        arc_length = radius * angle_in_rad

        # 5. 計算弦長 = 2 * 半徑 * sin(角度的一半)
        chord_length = 2.0 * radius * math.sin(angle_in_rad / 2.0)

        # 輸出結果，保留小數點後六位
        print("{:.6f} {:.6f}".format(arc_length, chord_length))

if __name__ == "__main__":
    main()
