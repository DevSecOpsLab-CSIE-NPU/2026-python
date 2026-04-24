# -*- coding: utf-8 -*-
import sys
import math

EARTH_RADIUS = 6440

def solve(s, a, unit):
    """
    計算衛星之間的弧長與弦長。
    :param s: 衛星距地表高度 (km)
    :param a: 夾角
    :param unit: 角度單位 ('deg' 或 'min')
    :return: 一個包含 (弧長, 弦長) 的元組
    """
    # 衛星軌道半徑
    r = EARTH_RADIUS + s

    # 統一將角度轉換為度 (degree)
    if unit == 'min':
        a /= 60.0

    # 兩點之間的最短距離所對應的圓心角不會超過 180 度
    if a > 180:
        a = 360 - a

    # 將角度轉為弧度 (radian) 以便計算
    angle_rad = math.radians(a)

    # 計算弧長: r * theta
    arc_length = r * angle_rad

    # 計算弦長: 2 * r * sin(theta / 2)
    chord_length = 2 * r * math.sin(angle_rad / 2)

    return arc_length, chord_length

if __name__ == '__main__':
    for line in sys.stdin:
        s, a, unit = line.strip().split()
        arc, chord = solve(float(s), float(a), unit)
        print(f"{arc:.6f} {chord:.6f}")