import sys
import re

# 進階實作版：利用位元運算預處理數字變換
# 核心邏輯：枚舉所有「出」與「入」的木棒配對
def solve():
    # 七段顯示器編碼 (0-9)
    segs = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f]
    
    def get_diff(a, b):
        # 計算數字 a 變成數字 b 需要增加(+)或減少(-)幾根木棒
        # 返回 (增加數, 減少數)
        plus = bin(b & ~a).count('1')
        minus = bin(a & ~b).count('1')
        return plus, minus

    def check_expr(s):
        # 驗證等式字串是否成立
        try:
            left, right = s.split('=')
            # 處理可能出現的負號與運算
            return eval(left) == eval(right)
        except:
            return False

    line = sys.stdin.readline().strip()
    if not line or line == '#': return
    
    # 拆解出數字的位置與原本的字符
    chars = list(line)
    num_indices = [i for i, c in enumerate(chars) if c.isdigit()]
    
    # 嘗試方案一：同一個數字內部移動一根 (Type A: plus=1, minus=1)
    for i in num_indices:
        orig_digit = int(chars[i])
        for target in range(10):
            if target == orig_digit: continue
            p, m = get_diff(segs[orig_digit], segs[target])
            if p == 1 and m == 1:
                chars[i] = str(target)
                new_s = "".join(chars)
                if check_expr(new_s):
                    print(new_s)
                    return
                chars[i] = str(orig_digit) # 復原

    # 嘗試方案二：從一個數字拿走一根 (Type B: p=0, m=1)，補到另一個數字 (Type C: p=1, m=0)
    for i in num_indices:
        orig_i = int(chars[i])
        for target_i in range(10):
            p_i, m_i = get_diff(segs[orig_i], segs[target_i])
            if p_i == 0 and m_i == 1: # 貢獻出一根
                chars[i] = str(target_i)
                # 尋找接收者
                for j in num_indices:
                    if i == j: continue
                    orig_j = int(chars[j])
                    for target_j in range(10):
                        p_j, m_j = get_diff(segs[orig_j], segs[target_j])
                        if p_j == 1 and m_j == 0: # 接收一根
                            chars[j] = str(target_j)
                            new_s = "".join(chars)
                            if check_expr(new_s):
                                print(new_s)
                                return
                            chars[j] = str(orig_j)
                chars[i] = str(orig_i) # 復原

    print("No")

if __name__ == "__main__":
    solve()