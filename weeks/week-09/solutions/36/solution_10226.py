# solution_10226.py
# UVA 10226 解決方案
# 問題：生成考慮約束的排列，並壓縮輸出
# 繁體中文註解：這個程式解決 UVA 10226 問題，生成有效排列並以壓縮格式輸出

import itertools
import sys

def is_valid_permutation(perm, constraints):
    # 檢查排列是否有效：確保沒有人排在他們不想的位置
    # perm 是 1-based 位置列表，constraints[i] 是第 i+1 個人不想的位置列表
    for person, pos in enumerate(perm, 1):
        if pos in constraints[person-1]:
            return False
    return True

def generate_valid_permutations(n, constraints):
    # 生成所有有效排列，按字典順序排序
    # 使用 itertools.permutations 生成所有可能，過濾有效
    all_perms = list(itertools.permutations(range(1, n+1)))
    valid = [list(p) for p in all_perms if is_valid_permutation(p, constraints)]
    return sorted(valid)

def format_compressed_output(perms):
    # 格式化壓縮輸出：如果新排列與前一個有相同前綴，只輸出不同部分
    if not perms:
        return ""
    output = []
    prev = None
    for perm in perms:
        perm_str = ''.join(map(str, perm))
        if prev is None:
            output.append(perm_str)
        else:
            # 找到第一個不同的位置
            for i in range(len(perm_str)):
                if i >= len(prev) or perm_str[i] != prev[i]:
                    output.append(perm_str[i:])
                    break
        prev = perm_str
    return '\n'.join(output) + '\n'

# 主程式：讀取輸入，處理多筆測資
if __name__ == "__main__":
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