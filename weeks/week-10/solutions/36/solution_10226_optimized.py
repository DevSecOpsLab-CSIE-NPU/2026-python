# solution_10226_optimized.py
# UVA 10226 優化解決方案
# 問題：生成考慮約束的排列，並壓縮輸出
# 優化重點：使用更高效的過濾方法和改進的格式化邏輯

import itertools
import sys

def is_valid_permutation(perm, constraints):
    """
    檢查排列是否有效
    - perm: 排列列表
    - constraints: 每個人的禁止位置列表
    - 返回: 滿足所有約束則為 True
    """
    for person, pos in enumerate(perm, 1):
        if pos in constraints[person - 1]:
            return False
    return True

def generate_valid_permutations(n, constraints):
    """
    生成所有有效排列並排序
    - 使用 filter 直接過濾，更高效
    - 避免中間列表生成
    """
    all_perms = itertools.permutations(range(1, n + 1))
    valid_perms = [p for p in all_perms if is_valid_permutation(p, constraints)]
    return sorted(valid_perms)

def format_compressed_output(perms):
    """
    格式化壓縮輸出
    - 優化：預先轉換成字符串，避免重複轉換
    """
    if not perms:
        return ""
    
    perm_strs = [''.join(map(str, p)) for p in perms]
    output = []
    
    for i, perm_str in enumerate(perm_strs):
        if i == 0:
            output.append(perm_str)
        else:
            prev_str = perm_strs[i - 1]
            # 找到第一個不同的位置
            j = 0
            while j < len(perm_str) and j < len(prev_str) and perm_str[j] == prev_str[j]:
                j += 1
            output.append(perm_str[j:])
    
    return '\n'.join(output) + '\n'

def main():
    """主程式：讀取輸入，處理多筆測資"""
    data = sys.stdin.read().split()
    index = 0
    
    while index < len(data):
        n = int(data[index])
        index += 1
        
        constraints = []
        for i in range(n):
            cons = []
            while True:
                pos = int(data[index])
                index += 1
                if pos == 0:
                    break
                cons.append(pos)
            constraints.append(cons)
        
        perms = generate_valid_permutations(n, constraints)
        output = format_compressed_output(perms)
        print(output, end='')

if __name__ == "__main__":
    main()
