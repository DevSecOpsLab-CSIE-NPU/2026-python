import sys
import datetime

def solve(input_text):
    """
    計算 UVA 12019 - Doom's Day Algorithm (簡單易記版)
    利用 Python 內建的 datetime 模組，完全不需背誦演算法與日期表。
    """
    lines = input_text.strip().split('\n')
    if not lines or not lines[0]:
        return ""
        
    T = int(lines[0].strip())
    output = []
    
    line_idx = 1
    for _ in range(T):
        if line_idx >= len(lines):
            break
            
        parts = lines[line_idx].split()
        if len(parts) >= 2:
            m = int(parts[0])
            d = int(parts[1])
            
            # 簡單判斷法 (Easy Way) 💡
            # 1. 既然題目是固定年份 (UVA12019 原題為 2011)，我們就直接產生一個 2011 年 m 月 d 日的 date 物件。
            # 2. Python 的 datetime 物件提供了一個無敵神技：`.strftime("%A")`。
            #    其中 "%A" 就代表「回傳星期的英文全名 (例如 Monday)」。
            # 這樣寫完全不用背誦任何月份的 Doomsday 日期，也不用計算餘數與偏移量，無腦秒殺！
            ans = datetime.date(2011, m, d).strftime("%A")
            output.append(ans)
            
        line_idx += 1
        
    return '\n'.join(output) + '\n'

if __name__ == '__main__':
    sys.stdout.write(solve(sys.stdin.read()))
