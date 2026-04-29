"""
UVA 10252 - The Closest Points Problem (Easy Version)
==================================================

題目說明：
- 給定 N 個點的座標 (Xi, Yi)
- 找一個整數點 P，使得 P 到所有點的 Euclidean 距離和最小
- 輸出：最小距離和（四捨五入到整數）+ 有幾個整數點可達到這個最小值

解題思路（Easy 版本）：
- 這是 2D 幾何中位數問題，沒有封閉解
- 但最優整數點會在輸入點的凸包附近
- 直接暴力搜索輸入點的座標範圍即可
"""

import sys
import math

def solve():
    """
    主函式：讀取輸入、處理測資、輸出結果
    
    輸入格式：
    - T：測試組數
    - 每組：N + N 行（點座標）
    """
    # 讀取所有非空白行
    lines = [l.strip() for l in sys.stdin if l.strip()]
    if not lines:
        return
    
    T = int(lines[0])  # 測試組數
    idx = 1            # 目前讀取的行索引
    
    # 處理每組測資
    for _ in range(T):
        N = int(lines[idx])  # 這組的點數量
        idx += 1
        
        # 讀取 N 個點的座標
        pts = []
        for _ in range(N):
            x, y = map(int, lines[idx].split())
            idx += 1
            pts.append((x, y))
        
        # 計算並輸出答案
        best, cnt = find_min(pts)
        print(best, cnt)

def find_min(pts):
    """
    找到最小距離和及達成點數
    
    參數：
    - pts：輸入點的列表，每個點是 (x, y) 的 tuple
    
    回傳：
    - (最小距離和, 達成點數)
    """
    N = len(pts)
    
    # 取出所有點的 x, y 座標
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    
    # ========================================
    # 決定搜索範圍
    # ========================================
    # 搜索輸入點座標範圍周圍的整數點
    # 往外擴展 5 格，確保能找到最優點
    sx, ex = min(xs) - 5, max(xs) + 5  # x 的搜索範圍
    sy, ey = min(ys) - 5, max(ys) + 5  # y 的搜索範圍
    
    def dsum(px, py):
        """
        計算點 (px, py) 到所有輸入點的 Euclidean 距離和
        使用 math.hypot 計算 sqrt(dx^2 + dy^2)
        """
        return sum(math.hypot(px - x, py - y) for x, y in pts)
    
    # ========================================
    # 找最小距離和
    # ========================================
    # 枚舉所有候選點，找最小的距離和
    best = float('inf')
    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            best = min(best, dsum(x, y))
    
    # 四捨五入到整數
    # Python 的 round() 在某些情況會有問題，用 +0.5 法則
    best = int(best + 0.5)
    
    # ========================================
    # 數有幾個點達到最小值
    # ========================================
    # 計算有多少整數點的距離和（，四捨五入）等於 best
    cnt = sum(1 for x in range(sx, ex + 1) for y in range(sy, ey + 1) 
            if int(dsum(x, y) + 0.5) == best)
    
    return best, cnt

if __name__ == "__main__":
    solve()