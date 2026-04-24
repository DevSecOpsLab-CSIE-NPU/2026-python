# -*- coding: utf-8 -*-
# 這是 UVA 10221 (Satellites) 的簡易好記版 (Easy Version)
import sys
import math

EARTH_RADIUS = 6440

def solve(s, a, unit):
    """
    簡易好記秘訣：【單位換算SOP + 公式】
    1. 算半徑：總半徑 = 地球半徑(6440) + 衛星高度(s)
    2. 單位統一：把 'min' 換算成 'deg' (除以 60)。
    3. 角度正規化：取小於 180 度的夾角 (用 360-a)。
    4. 轉弧度：Python 的 math 函式庫都用弧度，所以用 math.radians()。
    5. 套公式：
       - 弧長 = r * 弧度
       - 弦長 = 2 * r * sin(弧度 / 2)
    """
    # 1. 計算總半徑
    r = EARTH_RADIUS + s

    # 2. 角度單位統一為 'deg'
    if unit == 'min':
        a /= 60.0

    # 3. 角度正規化 (取最短路徑的夾角)
    if a > 180:
        a = 360 - a

    # 4. 角度轉弧度
    angle_rad = math.radians(a)

    # 5. 套公式
    arc_length = r * angle_rad
    chord_length = 2 * r * math.sin(angle_rad / 2)

    return arc_length, chord_length

if __name__ == '__main__':
    for line in sys.stdin:
        s, a, unit = line.strip().split()
        arc, chord = solve(float(s), float(a), unit)
        print(f"{arc:.6f} {chord:.6f}")