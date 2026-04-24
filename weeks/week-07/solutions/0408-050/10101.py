# -*- coding: utf-8 -*-
import sys
import re

# --- 預先計算 ---
# 描述：預先計算所有數字之間透過移動、新增、移除一根火柴棒可以互相轉換的關係。
# 方法：使用位元遮罩代表七段顯示器的七個段，透過位元運算來判斷轉換關係。

# 使用標準七段顯示器映射 (a=top, b=tr, c=br, d=bot, e=bl, f=tl, g=mid)
# 位元遮罩: (g, f, e, d, c, b, a)
SEGMENTS = {
    '0': 0b0111111, '1': 0b0000110, '2': 0b1011011, '3': 0b1001111,
    '4': 0b1100110, '5': 0b1101101, '6': 0b1111101, '7': 0b0000111,
    '8': 0b1111111, '9': 0b1101111,
}

def popcount(n):
    """計算位元為 1 的數量"""
    return bin(n).count('1')

# 建立轉換表
ADD_MAP = {d: [] for d in SEGMENTS}
REMOVE_MAP = {d: [] for d in SEGMENTS}
MOVE_MAP = {d: [] for d in SEGMENTS}

for d1_str in SEGMENTS:
    for d2_str in SEGMENTS:
        if d1_str == d2_str:
            continue
        
        mask1, mask2 = SEGMENTS[d1_str], SEGMENTS[d2_str]
        segs1, segs2 = popcount(mask1), popcount(mask2)
        
        # 新增一根火柴 (段數+1，且只有一個位元不同)
        if segs2 == segs1 + 1 and popcount(mask1 ^ mask2) == 1:
            ADD_MAP[d1_str].append(d2_str)
        # 移除一根火柴 (段數-1，且只有一個位元不同)
        if segs2 == segs1 - 1 and popcount(mask1 ^ mask2) == 1:
            REMOVE_MAP[d1_str].append(d2_str)
        # 移動一根火柴 (段數不變，且有兩個位元不同)
        if segs1 == segs2 and popcount(mask1 ^ mask2) == 2:
            MOVE_MAP[d1_str].append(d2_str)

def evaluate(s_expr):
    """安全地評估表達式字串，返回其數值結果"""
    try:
        return eval(s_expr)
    except:
        return 0 # 處理中間可能產生的無效表達式

def calculate_delta(parts, num_idx, digit_idx, d_new):
    """計算單一數字變動對 (LHS - RHS) 總值的影響"""
    num_str = parts[num_idx]
    d_old = num_str[digit_idx]
    
    power_of_10 = 10 ** (len(num_str) - 1 - digit_idx)
    val_change = (int(d_new) - int(d_old)) * power_of_10
    
    # 判斷該數值的正負號
    sign = -1 if num_idx > 0 and parts[num_idx - 1] == '-' else 1
    
    eq_idx = parts.index('=')
    is_lhs = num_idx < eq_idx
    
    # 如果在等號左邊，直接回傳貢獻；如果在右邊，貢獻為負
    return val_change * sign if is_lhs else -val_change * sign

def solve(equation):
    """解決火柴棒問題的主函式"""
    clean_eq = equation.split('#')[0] if '#' in equation else equation
    parts = [p for p in re.split(r'([+\-=])', clean_eq) if p]
    
    if '=' not in parts:
        return "No"
        
    eq_idx = parts.index('=')
    initial_error = evaluate("".join(parts[:eq_idx])) - evaluate("".join(parts[eq_idx+1:]))

    num_indices = [i for i, p in enumerate(parts) if p.isdigit()]

    # 情況 1: 在同一個數字內移動火柴
    for num_idx in num_indices:
        for digit_idx, d_old in enumerate(parts[num_idx]):
            for d_new in MOVE_MAP[d_old]:
                if calculate_delta(parts, num_idx, digit_idx, d_new) == -initial_error:
                    new_parts = list(parts); old_num = new_parts[num_idx]
                    new_parts[num_idx] = old_num[:digit_idx] + d_new + old_num[digit_idx+1:]
                    return "".join(new_parts) + "#"

    # 情況 2: 在不同數字間移動火柴 (一增一減)
    removals = {calculate_delta(parts, n_idx, d_idx, d_n): (n_idx, d_idx, d_n) for n_idx in num_indices for d_idx, d_o in enumerate(parts[n_idx]) for d_n in REMOVE_MAP[d_o]}
    additions = {calculate_delta(parts, n_idx, d_idx, d_n): (n_idx, d_idx, d_n) for n_idx in num_indices for d_idx, d_o in enumerate(parts[n_idx]) for d_n in ADD_MAP[d_o]}

    for delta_rm, (n_idx_rm, d_idx_rm, d_new_rm) in removals.items():
        needed_delta = -initial_error - delta_rm
        if needed_delta in additions:
            n_idx_add, d_idx_add, d_new_add = additions[needed_delta]
            if n_idx_rm != n_idx_add or d_idx_rm != d_idx_add:
                new_parts = list(parts)
                old_rm, old_add = new_parts[n_idx_rm], new_parts[n_idx_add]
                new_parts[n_idx_rm] = old_rm[:d_idx_rm] + d_new_rm + old_rm[d_idx_rm+1:]
                new_parts[n_idx_add] = old_add[:d_idx_add] + d_new_add + old_add[d_idx_add+1:]
                return "".join(new_parts) + "#"

    return "No"

if __name__ == '__main__':
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        print(solve(line))