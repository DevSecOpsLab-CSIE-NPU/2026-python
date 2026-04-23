# 簡單版衛星距離計算程式
# 使用繁體中文註解說明

import sys
import math

def main():
    for line in sys.stdin:
        parts = line.split()
        s = int(parts[0])  # 衛星距地表高度
        a = float(parts[1])  # 角度
        unit = parts[2]  # 單位
        r = 6440 + s  # 衛星到地心距離
        if unit == 'min':
            a_deg = a / 60.0  # 分轉度
        else:
            a_deg = a  # 已是度
        a_rad = math.radians(a_deg)  # 轉弧度
        arc = r * a_rad  # 弧長
        chord = 2 * r * math.sin(a_rad / 2)  # 弦長
        print(f"{arc:.6f} {chord:.6f}")  # 輸出

if __name__ == "__main__":
    main()