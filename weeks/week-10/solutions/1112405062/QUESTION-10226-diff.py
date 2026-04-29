"""
UVA 10226 - 限制排列
==================

題目說明：
- 給定 N 個人，編號為 A, B, C, ... （第 i 個人編號為第 i 個英文字母）
- 每個人有不想排的位置（禁忌位置）
- 請輸出所有可能的排列（字典順序），僅輸出與上次不同的部分

輸入格式：
- 多筆測資，每筆第一行是 N（1 ≦ N ≦ 15）
- 接下來 N 行，第 i 行代表第 i 個人不想排的位置，0 表示結束

輸出格式：
- 所有合法排列依字典順序輸出
- 每個排列只輸出與上一個排列不同的部分（壓縮格式）
- 測資之間用空行分隔
"""

import sys

def solve():
    lines = [l.strip() for l in sys.stdin if l.strip()]
    if not lines:
        return

    idx = 0
    first = True

    while idx < len(lines):
        N = int(lines[idx])
        idx += 1

        forbidden = []
        for _ in range(N):
            f = []
            for x in map(int, lines[idx].split()):
                if x == 0:
                    break
                f.append(x)
            forbidden.append(set(f))
            idx += 1

        if not first:
            print()
        first = False

        gen_permutations(N, forbidden)

def gen_permutations(N, forbidden):
    persons = [chr(ord('A') + i) for i in range(N)]
    prev = ""

    def backtrack(pos, used, cur):
        nonlocal prev
        if pos == N:
            result = ''.join(cur)
            if not prev:
                print(result)
            else:
                for i in range(len(prev)):
                    if i >= len(result) or prev[i] != result[i]:
                        print(result[i:])
                        break
            prev = result
            return

        for i in range(N):
            if not used[i] and (pos + 1) not in forbidden[i]:
                used[i] = True
                cur.append(persons[i])
                backtrack(pos + 1, used, cur)
                cur.pop()
                used[i] = False

    backtrack(0, [False] * N, [])

if __name__ == "__main__":
    solve()
