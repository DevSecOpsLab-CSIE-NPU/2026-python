"""
UVA 10226 - 排列生成問題 (DFS + 去重)

題目說明：
給定 N 個人（A, B, ..., Z），每個人都有一個列表表示不想排的位置。
生成所有可能的排列，按字典順序輸出，並且只輸出與上次排列不同的部分。
"""

import sys
from typing import List, Set


def generate_permutations(n: int, restrictions: List[Set[int]]) -> List[List[str]]:
    """
    生成所有可能的排列。
    
    參數：
        n: 人數
        restrictions: 每個人不想排的位置集合（0-indexed）
    
    回傳：
        所有有效排列的列表
    """
    people = [chr(ord('A') + i) for i in range(n)]
    result = []
    
    def dfs(position: int, used: int, current: List[str]) -> None:
        """
        DFS 遞迴生成排列。
        
        核心思想：針對每個位置，逐一嘗試放置未使用的人。
        - 使用位掩碼 `used` 追蹤已使用的人
        - 位掩碼的第 i 個 bit 表示第 i 個人是否已被放置
        - 快速檢查重複：O(1) 時間複雜度
        
        參數：
            position: 當前正在填充的位置（0 到 n-1）
            used: 位掩碼，表示已使用的人（整數，第 i bit = 1 表示第 i 人已用）
            current: 當前排列的列表
        """
        if position == n:
            # 我們成功填滿所有位置，找到了一個完整的排列
            result.append(current[:])
            return
        
        for i in range(n):
            # 位掩碼檢查：如果第 i 個人已使用，跳過
            if used & (1 << i):
                continue
            
            # 限制條件檢查：第 i 個人是否不想在位置 position
            if position in restrictions[i]:
                continue
            
            # 嘗試將第 i 個人放在位置 position
            # 將其人加入當前排列
            current.append(people[i])
            # 遞迴進入下一位置，更新位掩碼：位上 (1 << i) 設為 1
            dfs(position + 1, used | (1 << i), current)
            # 回溯：移除該人，準備嘗試其他人
            current.pop()
    
    dfs(0, 0, [])
    result.sort()  # 確保按字典序排列
    return result


def read_input() -> List[tuple]:
    """
    讀取輸入數據，返回多個測試案例。
    
    輸入格式：
    第一行：測試案例數
    每個案例：
        第一行：N（人數）
        接下來 N 行：每行為該人不想排的位置列表（0 代表結束）
    """
    test_cases = []
    
    try:
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            
            n = int(line.strip())
            if n == 0:
                break
            
            restrictions = []
            for _ in range(n):
                positions = list(map(int, sys.stdin.readline().split()))
                # 移除末尾的 0，轉為 0-indexed
                position_set = {pos - 1 for pos in positions if pos != 0}
                restrictions.append(position_set)
            
            test_cases.append((n, restrictions))
    except EOFError:
        pass
    
    return test_cases


def format_output(permutations: List[List[str]]) -> str:
    """
    格式化輸出，只輸出與上次排列不同的部分。
    """
    if not permutations:
        return ""
    
    lines = []
    prev = None
    
    for perm in permutations:
        if prev is None:
            # 第一個排列完全輸出
            lines.append(' '.join(perm))
        else:
            # 找出不同的部分
            diff_pos = 0
            for i in range(len(perm)):
                if i >= len(prev) or perm[i] != prev[i]:
                    diff_pos = i
                    break
            
            # 輸出從 diff_pos 開始的部分
            lines.append(' '.join(perm[diff_pos:]))
        
        prev = perm
    
    return '\n'.join(lines)


def main():
    """主程式：讀取輸入、生成排列、輸出結果"""
    test_cases = read_input()
    
    for n, restrictions in test_cases:
        permutations = generate_permutations(n, restrictions)
        output = format_output(permutations)
        if output:
            print(output)


if __name__ == '__main__':
    main()
