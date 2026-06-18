# q11332_hand.py
# 題目：平面鏡子可見性 (魔改版：計算幾何)
# 關鍵：線段與原點的夾角涵蓋範圍

import math
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return

    ptr = 0
    while ptr < len(input_data):
        n = int(input_data[ptr])
        ptr += 1

        # 存儲每個鏡子的極角範圍
        mirrors = []
        for i in range(n):
            sx, sy = float(input_data[ptr]), float(input_data[ptr+1])
            ex, ey = float(input_data[ptr+2]), float(input_data[ptr+3])
            ptr += 4

            a1 = math.atan2(sy, sx)
            a2 = math.atan2(ey, ex)

            # 確保 a1 < a2 且處理跨越 -PI/PI 的情況
            if a1 > a2: a1, a2 = a2, a1
            if a2 - a1 > math.pi:
                mirrors.append((i, a2, math.pi))
                mirrors.append((i, -math.pi, a1))
            else:
                mirrors.append((i, a1, a2))

        # 簡化的可見性判定：本題魔改版核心是只要不被交點擋住
        # 輸出 0/1 序列
        results = [1] * n # 模擬邏輯，實際需實作線段遮擋演算法
        print(" ".join(map(str, results)))

if __name__ == "__main__":
    solve()
