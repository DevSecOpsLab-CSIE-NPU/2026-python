# solution_10226_easy.py
# UVA 10226 簡單版本解決方案
# 使用遞歸生成有效排列，更容易記憶
# 繁體中文註解：這個版本用遞歸來生成排列，比 itertools 更直觀

import sys

def generate_perms(n, constraints, used, current, result):
    # 遞歸生成排列
    if len(current) == n:
        result.append(current[:])
        return
    for i in range(1, n+1):
        if not used[i] and i not in constraints[len(current)]:
            used[i] = True
            current.append(i)
            generate_perms(n, constraints, used, current, result)
            current.pop()
            used[i] = False

def generate_valid_permutations(n, constraints):
    # 初始化
    used = [False] * (n+1)
    result = []
    generate_perms(n, constraints, used, [], result)
    return result

def format_compressed_output(perms):
    # 同上
    if not perms:
        return ""
    output = []
    prev = None
    for perm in perms:
        perm_str = ''.join(map(str, perm))
        if prev is None:
            output.append(perm_str)
        else:
            for i in range(len(perm_str)):
                if i >= len(prev) or perm_str[i] != prev[i]:
                    output.append(perm_str[i:])
                    break
        prev = perm_str
    return '\n'.join(output) + '\n'

# 主程式
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