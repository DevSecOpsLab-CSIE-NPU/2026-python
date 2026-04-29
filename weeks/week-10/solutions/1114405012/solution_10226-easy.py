# -*- coding: utf-8 -*-
"""
UVA 10226 - Permutation 簡化版
核心邏輯：用回溯法列出所有排列，依字典序排列，只輸出不同部分
"""

def get_all_perms(n, forbidden):
    """
    產生所有合法排列（字典序）
    n: 人數
    forbidden: forbidden[i] = 第 i 個人禁止的位置集合（1-based）
    """
    letters = [chr(ord('A') + i) for i in range(n)]
    used = [False] * n
    current = []
    results = []
    
    def backtrack(pos):
        if pos == n:
            results.append(''.join(current))
            return
        
        for i in range(n):
            if not used[i] and (pos + 1) not in forbidden[i]:
                used[i] = True
                current.append(letters[i])
                backtrack(pos + 1)
                current.pop()
                used[i] = False
    
    backtrack(0)
    return results


def compress(perms):
    """
    輸出壓縮：第一個完整，後續只輸出不同部分
    """
    if not perms:
        return ''
    
    lines = [perms[0]]
    for i in range(1, len(perms)):
        # 找到第一個不同位置
        j = 0
        while j < len(perms[i]) and perms[i-1][j] == perms[i][j]:
            j += 1
        lines.append(perms[i][j:])
    
    return '\n'.join(lines) + '\n'


def solve(inp):
    """解題主函式"""
    lines = inp.strip().split('\n')
    idx = 0
    outputs = []
    
    while idx < len(lines):
        n = int(lines[idx])
        idx += 1
        
        forbidden = []
        for _ in range(n):
            parts = list(map(int, lines[idx].split()))
            idx += 1
            s = set()
            for p in parts:
                if p == 0:
                    break
                s.add(p)
            forbidden.append(s)
        
        perms = get_all_perms(n, forbidden)
        outputs.append(compress(perms))
    
    return ''.join(outputs)


if __name__ == '__main__':
    import sys
    print(solve(sys.stdin.read()), end='')
