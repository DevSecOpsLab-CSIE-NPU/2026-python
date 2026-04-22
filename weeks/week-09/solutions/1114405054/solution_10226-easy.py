#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
題目 10226 簡化版: 排列問題 (SIMPLIFIED)
使用更簡潔的代碼實現

核心邏輯：
1. 用 DFS 生成所有排列
2. 檢查位置限制
3. 輸出時跳過重複前綴
"""


def solve_10226():
    """
    簡化版解決方案：逐行讀取並處理
    """
    while True:
        n = int(input())
        if n == 0:
            break

        # 讀取限制
        forbidden = [set() for _ in range(n)]
        for i in range(n):
            while True:
                pos = int(input())
                if pos == 0:
                    break
                forbidden[i].add(pos - 1)  # 轉為 0-based

        # 生成有效排列
        perms = []

        def backtrack(used, current):
            """遞迴生成排列"""
            if len(current) == n:
                perms.append(current[:])
                return

            pos = len(current)
            for person in range(n):
                if used[person] or pos in forbidden[person]:
                    continue

                used[person] = True
                current.append(person)
                backtrack(used, current)
                current.pop()
                used[person] = False

        backtrack([False] * n, [])
        perms.sort()

        # 輸出
        prev = []
        for perm in perms:
            i = 0
            while i < len(prev) and i < len(perm) and prev[i] == perm[i]:
                i += 1

            # 只輸出不同部分
            output = ' '.join(chr(ord('A') + p) for p in perm[i:])
            print(output)
            prev = perm


if __name__ == '__main__':
    solve_10226()
