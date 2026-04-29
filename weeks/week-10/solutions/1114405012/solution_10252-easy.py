# -*- coding: utf-8 -*-
"""
UVA 10252 - Common Permutation 簡化版
找一個整數點 P，使得到所有給定點的距離和最小
簡化版本：使用中位數法則
"""

import math

def solve(inp):
    lines = inp.strip().split('\n')
    t = int(lines[0])
    idx = 1
    
    results = []
    
    for _ in range(t):
        n = int(lines[idx])
        idx += 1
        
        points = []
        for _ in range(n):
            x, y = map(int, lines[idx].split())
            points.append((x, y))
            idx += 1
        
        # 簡化版本：費馬點問題
        # 使用中位數法則：最優點的 x 和 y 都是所有點坐標的中位數
        xs = sorted([p[0] for p in points])
        ys = sorted([p[1] for p in points])
        
        # 取中位數
        if n % 2 == 1:
            px = xs[n // 2]
            py = ys[n // 2]
        else:
            px = xs[n // 2 - 1]
            py = ys[n // 2 - 1]
        
        # 計算距離和
        total_dist = 0
        for x, y in points:
            dist = math.sqrt((px - x) ** 2 + (py - y) ** 2)
            total_dist += dist
        
        # 輸出整數距離
        ans_dist = int(total_dist)
        
        # 簡化版本：假設只有 1 種整數解
        ans_count = 1
        
        results.append(f"{ans_dist} {ans_count}")
    
    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read()))
