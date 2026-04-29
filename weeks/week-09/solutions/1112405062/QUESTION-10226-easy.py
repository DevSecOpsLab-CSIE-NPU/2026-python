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

from itertools import permutations
import sys

def solve():
    """
    主函式：讀取輸入、處理多筆測資、輸出結果
    
    輸入處理流程：
    1. 讀取所有非空白行
    2. 每筆測資第一行是 N
    3. 接下來 N 行讀取每個人的禁忌位置
    """
    # 讀取所有非空白行，去除首尾空白
    lines = [l.strip() for l in sys.stdin if l.strip()]
    if not lines:
        return

    idx = 0      # 目前讀取到的行索引（指標）
    first = True # 是否為第一筆測資（用於輸出空行分隔）

    # 不斷讀取直到資料結束
    while idx < len(lines):
        # --- 讀取 N（第幾個人）---
        N = int(lines[idx])
        idx += 1

        # --- 讀取每個人的禁忌位置 ---
        # forbidden[i] 儲存第 i 個人（A=0, B=1, ...）不想排的位置集合
        # 例如：forbidden[0] 儲存 A不想排的位置
        forbidden = []
        for _ in range(N):
            f = []
            # 讀取一行，可能有多個數字，以 0 表示結束
            # 例如："1 3 0" 表示不想排位置 1 和 3
            for x in map(int, lines[idx].split()):
                if x == 0:
                    break
                f.append(x)
            # 轉換為 set 以加快查詢速度
            forbidden.append(set(f))
            idx += 1

        # 測資之間用空行分隔（第一筆測資不輸出空行）
        if not first:
            print()
        first = False

        # --- 產生並輸出排列 ---
        gen_permutations(N, forbidden)

def gen_permutations(N, forbidden):
    """
    產生並輸出所有合法排列
    
    參數：
    - N: 人數（幾個人）
    - forbidden: 禁忌位置列表，forbidden[i] 為第 i 人不想排的位置集合
    
    演算法：
    1. 使用 itertools.permutations 生成所有排列（自動按字典順序）
    2. 檢查每個排列是否符合禁忌限制
    3. 輸出時只顯示與前一個排列不同的後綴
    """
    # 產生人員列表 ['A', 'B', 'C', ...] 長度為 N
    # chr(ord('A') + i) 將數字轉換為對應的英文字母
    persons = [chr(ord('A') + i) for i in range(N)]
    prev = ""  # 儲存上一個輸出的排列（用於比較差異）

    # 枚舉所有排列（itertools 自動按字典順序產生）
    # 例如：permutations(['A','B','C']) 會產生 ABC, ACB, BAC, BCA, CAB, CBA
    for p in permutations(persons):
        # --- 檢查該排列是否合法 ---
        ok = True
        for pos, person in enumerate(p):
            # position 是從 0 開始索引（位置 0 = 實際位置 1）
            # 需要 +1 轉換為 1-based（題目使用 1-based 位置）
            person_idx = ord(person) - ord('A')  # 取得人員索引（A=0, B=1, ...）
            
            # 如果該人不想排在此位置，則此排列無效
            if (pos + 1) in forbidden[person_idx]:
                ok = False
                break

        # 跳过不合法的排列
        if not ok:
            continue

        # --- 輸出（壓縮格式）---
        cur = ''.join(p)  # 將排列轉換為字串

        if not prev:
            # 第一個排列直接完整輸出
            print(cur)
        else:
            # 後續排列：找出與上一個排列的第一個不同位置
            # 只輸出從該位置開始的後綴（差異部分）
            for i in range(len(prev)):
                if i >= len(cur) or prev[i] != cur[i]:
                    print(cur[i:])
                    break

        prev = cur  # 更新 previous 排列

if __name__ == "__main__":
    solve()