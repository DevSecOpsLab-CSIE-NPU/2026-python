"""
UVA 10226 - 排列生成問題 (簡化版本)

核心概念：
使用 DFS + 位掩碼 (Bitmask DP) 生成所有可能的排列。
- 位掩碼效率高：O(1) 檢查是否已使用某人
- DFS 保證自動的回溯機制
- 集合儲存限制位置：O(1) 檢查某人是否可在某位置
"""

import sys
from typing import List, Set, Tuple


def generate_perms(n: int, avoid: List[Set[int]]) -> List[List[str]]:
    """
    使用 DFS + 位掩碼生成所有有效排列。
    
    時間複雜度: O(N! × N) | 空間複雜度: O(N × N!)
    
    參數：
        n: 人數（1 ≤ N ≤ 15）
        avoid: 第 i 個人避免的位置集合（0-indexed）
    
    回傳：所有有效排列的列表（按字典序）
    """
    if n <= 0:
        return []
    
    names = [chr(ord('A') + i) for i in range(n)]
    perms = []
    
    def backtrack(pos: int, mask: int, perm: List[str]) -> None:
        """
        DFS 遞迴填充排列。位掩碼 O(1) 檢查已用狀態。
        
        位掩碼：mask 的第 i bit=1 表示人 i 已放置
        - 例如 mask=0b101=5 表示人 0 和人 2 已使用
        - 檢查：(mask & (1 << i)) 是否已用
        - 更新：(mask | (1 << i)) 標記為已用
        """
        if pos == n:
            # 終止：所有位置已填滿，保存排列（新建副本）
            perms.append(perm[:])
            return
        
        for i in range(n):
            # 剪枝 #1：已使用的人 O(1)
            if mask & (1 << i):
                continue
            
            # 剪枝 #2：該人避免的位置 O(1)
            if pos in avoid[i]:
                continue
            
            perm.append(names[i])  # 放置人 i
            backtrack(pos + 1, mask | (1 << i), perm)  # 遞迴
            perm.pop()  # 回溯
    
    backtrack(0, 0, [])
    perms.sort()  # 字典序排序
    return perms


def format_output(perms: List[List[str]]) -> str:
    """
    格式化輸出：只輸出與上次不同的部分。
    
    時間複雜度: O(K × N)，K = 排列數
    策略：找出相鄰排列的首個不同位置，只輸出之後的部分。
    """
    if not perms:
        return ""
    
    lines = []
    prev_perm: List[str] = []
    
    for perm in perms:
        # 使用 next() 找第一個不同位置（短路評估更高效）
        diff_idx = next((i for i in range(max(len(prev_perm), len(perm)))
                        if i >= len(prev_perm) or i >= len(perm) or perm[i] != prev_perm[i]),
                       len(perm))
        
        lines.append(' '.join(perm[diff_idx:]))
        prev_perm = perm
    
    return '\n'.join(lines)


def read_test_cases() -> List[Tuple[int, List[Set[int]]]]:
    """
    讀取多組測試案例（直到 N=0 或 EOF）。
    
    格式：
    - 第一行：N（人數，1≤N≤15）
    - 次 N 行：位置清單，0 結尾
    - N=0 終止
    """
    cases: List[Tuple[int, List[Set[int]]]] = []
    
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            
            n = int(line.strip())
            if n == 0:
                break
            
            avoid_list: List[Set[int]] = []
            for _ in range(n):
                pos_list = list(map(int, sys.stdin.readline().split()))
                # 轉 0-indexed，去除終止符 0
                avoid_set = {p - 1 for p in pos_list if p != 0}
                avoid_list.append(avoid_set)
            
            cases.append((n, avoid_list))
    
    except (EOFError, ValueError):
        # 靜默處理 EOF 或轉換錯誤
        pass
    
    return cases


def main() -> None:
    """主程式：多組測資輸入，去重排列輸出"""
    cases = read_test_cases()
    for n, avoid_list in cases:
        perms = generate_perms(n, avoid_list)
        output = format_output(perms)
        if output:
            print(output)


if __name__ == '__main__':
    main()
