import sys
import re

def solve(input_text):
    """
    處理 UVA 11349 Symmetric Matrix 的主邏輯（簡單易記版）
    """
    # 提取所有數字，避開 'N =' 帶來字串處理的麻煩
    tokens = re.findall(r'-?\d+', input_text)
    if not tokens:
        return ""
    
    T = int(tokens[0])
    idx = 1
    output = []
    
    for t in range(1, T + 1):
        if idx >= len(tokens):
            break
            
        n = int(tokens[idx])
        idx += 1
        
        # 直接連續讀取 n*n 個元素為「一維陣列 (1D Array)」
        elements = [int(x) for x in tokens[idx : idx + n*n]]
        idx += n * n
        
        # 簡單判斷法 (Easy Way) 💡
        # 1. all(x >= 0 for x in elements): 確定陣列裡面所有的數字都 >= 0（沒有負數）。
        # 2. elements == elements[::-1]: 使用 Python 切片 [::-1] 取得反轉陣列。
        #    如果陣列正著看和反著看一模一樣，那就代表它滿足了「中心對稱」的條件！
        # 這種寫法完全避開了複雜的二維雙重迴圈，不僅行數極少，且邏輯十分清晰。
        if all(x >= 0 for x in elements) and elements == elements[::-1]:
            output.append(f"Test #{t}: Symmetric.")
        else:
            output.append(f"Test #{t}: Non-symmetric.")
            
    return '\n'.join(output) + '\n'

if __name__ == '__main__':
    print(solve(sys.stdin.read()), end='')
