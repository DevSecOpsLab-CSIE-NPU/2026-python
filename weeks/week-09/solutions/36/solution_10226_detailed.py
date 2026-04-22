# solution_10226_detailed.py
# UVA 10226 詳細註解版本解決方案
# 這個版本包含詳細的繁體中文註解，解釋每個部分

import itertools  # 用於生成所有可能的排列
import sys  # 用於讀取標準輸入

def is_valid_permutation(perm, constraints):
    """
    檢查一個排列是否有效。
    參數：
    - perm: 一個列表，表示排列，例如 [1, 2, 3]
    - constraints: 一個列表的列表，constraints[i] 是第 i+1 個人不想排的位置列表
    返回：True 如果有效，False 否則
    """
    for person, pos in enumerate(perm, 1):  # person 從 1 開始，pos 是位置
        if pos in constraints[person-1]:  # 如果這個位置在該人的約束中
            return False  # 無效
    return True  # 所有人都滿足約束

def generate_valid_permutations(n, constraints):
    """
    生成所有有效的排列，按字典順序排序。
    參數：
    - n: 人數和位置數
    - constraints: 約束列表
    返回：有效排列的列表，每個排列是列表
    """
    # 生成所有可能的排列：從 1 到 n 的所有排列
    all_perms = list(itertools.permutations(range(1, n+1)))
    # 過濾出有效的排列
    valid = [list(p) for p in all_perms if is_valid_permutation(p, constraints)]
    # 排序以確保字典順序
    return sorted(valid)

def format_compressed_output(perms):
    """
    將排列列表格式化為壓縮輸出。
    如果新排列與前一個有相同前綴，只輸出不同部分。
    參數：
    - perms: 排列列表
    返回：壓縮輸出的字符串
    """
    if not perms:  # 如果沒有排列
        return ""  # 返回空字符串
    output = []  # 輸出列表
    prev = None  # 前一個排列的字符串
    for perm in perms:
        perm_str = ''.join(map(str, perm))  # 將排列轉為字符串，如 '123'
        if prev is None:  # 第一個排列
            output.append(perm_str)  # 輸出完整
        else:
            # 找到第一個不同的位置
            for i in range(len(perm_str)):
                if i >= len(prev) or perm_str[i] != prev[i]:
                    output.append(perm_str[i:])  # 輸出從不同處開始的部分
                    break
        prev = perm_str  # 更新前一個
    return '\n'.join(output) + '\n'  # 用換行連接，並加最後換行

# 主程式：處理多筆測資
if __name__ == "__main__":
    # 讀取所有輸入
    data = sys.stdin.read().split()
    index = 0  # 數據索引
    while index < len(data):
        n = int(data[index])  # 讀取 N
        index += 1
        constraints = []  # 約束列表
        for i in range(n):  # 對每個個人
            cons = []  # 該人的約束
            while True:
                pos = int(data[index])  # 讀取位置
                index += 1
                if pos == 0:  # 0 表示結束
                    break
                cons.append(pos)  # 添加約束
            constraints.append(cons)  # 添加到總約束
        # 生成有效排列
        perms = generate_valid_permutations(n, constraints)
        # 格式化輸出
        output = format_compressed_output(perms)
        # 打印輸出，不加額外換行
        print(output, end='')