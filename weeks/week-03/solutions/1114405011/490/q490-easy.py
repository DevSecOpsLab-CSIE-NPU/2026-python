"""
UVA 490 / ZeroJudge c045 - Rotating Text 簡易版
================================================
【與 q490.py 的差異】
  q490.py      → 自己寫雙層 for 迴圈，逐欄收集字元，邏輯清晰
  q490-easy.py → 利用 Python 內建的 zip() 與切片，一行完成旋轉

【核心簡化想法：zip 旋轉技巧】

  Python 的 zip(*matrix) 可以「轉置」一個二維矩陣（列↔欄互換）。
  但我們要的是「順時針旋轉 90 度」，不是單純轉置。

  觀察：
    順時針旋轉 90 度  = 先「上下翻轉」再「轉置」
                      = 先把行的順序倒過來（[::-1]），再 zip

  驗證（HELLO / WORLD 範例）：
    原始：  ['HELLO', 'WORLD']
    倒轉：  ['WORLD', 'HELLO']    ← padded[::-1]
    zip：   zip('WORLD', 'HELLO')
            → ('W','H'), ('O','E'), ('R','L'), ('L','L'), ('D','O')
    join：  'WH', 'OE', 'RL', 'LL', 'DO'   ✓

  所以只需要：
    result = [''.join(col) for col in zip(*padded[::-1])]

  這樣就搞定了！不需要手動處理索引，完全交給 Python 內建工具。
"""

import sys


# ─────────────────────────────────────────────────────────────────────────────
def solve(input_text: str) -> str:
    """
    讀入完整輸入文字，輸出順時針旋轉 90 度後的結果。

    【做法拆解】

    步驟 1：splitlines()
        將輸入切成行列表，保留行內空格（不呼叫 strip）。
        例：'HELLO\\nWORLD' → ['HELLO', 'WORLD']

    步驟 2：找 max_w 並補空格（ljust）
        所有行補到相同長度，形成完整矩形，避免旋轉後錯位。
        例：['AB', 'CDE', 'F'] → ['AB ', 'CDE', 'F  ']

    步驟 3：[::-1] 上下翻轉
        把行的順序倒過來：最後一行變第一行。
        這一步讓 zip 取出的欄方向恰好是「由下往上」。
        例：['F  ', 'CDE', 'AB ']

    步驟 4：zip(*padded[::-1]) 同時取各行的同位置字元
        zip 的特性：zip('ACE', 'BDF') → ('A','B'), ('C','D'), ('E','F')
        加上 * 解包，相當於對每一欄（同一 j）同時取所有行的第 j 個字元。
        每個 tuple 就是旋轉後的一列。

    步驟 5：''.join(col) 把 tuple 變字串
        ('W','H') → 'WH'

    步驟 6：'\n'.join(result) 組成最終輸出

    參數：
        input_text (str): 完整輸入文字

    回傳：
        str: 旋轉後的完整輸出文字
    """
    lines = input_text.splitlines()   # 步驟 1：切行，保留空格

    if not lines:
        return ""

    max_w = max(len(line) for line in lines)       # 步驟 2a：找最長行

    padded = [line.ljust(max_w) for line in lines] # 步驟 2b：補空格成矩形

    # 步驟 3+4+5：倒轉 → zip 取欄 → join 成字串
    rotated = [''.join(col) for col in zip(*padded[::-1])]

    return '\n'.join(rotated)   # 步驟 6：組合輸出


# ── 直接執行時：從 stdin 讀入，輸出至 stdout ─────────────────────────────────
if __name__ == "__main__":
    print(solve(sys.stdin.read()))
