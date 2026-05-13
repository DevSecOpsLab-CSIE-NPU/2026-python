"""
10931-easy — 更簡單且詳細註解的版本

說明（繁體中文詳細註解）:
- 對每個輸入整數 I（直到遇到 0 為止），輸出其二進位表示以及其中 1 的個數。
- 使用 Python 內建的 `bin()` 或 `format(n, 'b')` 可直接取得不含前導零的二進位字串。
- 計算 1 的個數可用字串方法 `.count('1')`。

此檔案的重點是直觀且容易記住的步驟。
"""
import sys

def solve(lines=None):
    if lines is None:
        tokens = sys.stdin.read().strip().split()
    else:
        tokens = [t for t in lines if t.strip()]
    out = []
    for tok in tokens:
        n = int(tok)
        if n == 0:
            break
        b = format(n, 'b')  # 取得二進位字串，不含前導零
        ones = b.count('1')
        out.append(f"The parity of {b} is {ones} (mod 2).")
    return out

if __name__ == '__main__':
    for line in solve():
        print(line)
