import sys

# 移動火柴棒小遊戲 - 大一入門版
# 題目要求：移動「一根」火柴棒，讓等式成立。
# 邏輯：
# 1. 把所有數字拆開，看成七段顯示器的組合。
# 2. 只有兩種情況：
#    (a) 在同一個數字內移動一根火柴（例如 6 變成 9）。
#    (b) 從一個數字拿走一根，放到另一個數字上（例如 8 拿走一根變 6，放給 5 變 6）。

# 七段顯示器的數字對應表（0-9 的火柴棒組成）
# 這裡用一個簡單的字典記錄每個數字增減火柴後可以變成誰
# 格式: (原始數字, 動作) -> [可變成的數字列表]
# 動作: 0 (原地移動), -1 (減少一根), 1 (增加一根)
TRANSITIONS = {
    ('0', 0): ['6', '9'], ('0', -1): [''], ('0', 1): ['8'],
    ('1', 0): [], ('1', -1): [], ('1', 1): ['7'],
    ('2', 0): ['3'], ('2', -1): [], ('2', 1): [],
    ('3', 0): ['2', '5'], ('3', -1): [], ('3', 1): ['9'],
    ('4', 0): [], ('4', -1): [], ('4', 1): [],
    ('5', 0): ['3'], ('5', -1): [], ('5', 1): ['6', '9'],
    ('6', 0): ['0', '9'], ('6', -1): ['5'], ('6', 1): ['8'],
    ('7', 0): [], ('7', -1): ['1'], ('7', 1): [],
    ('8', 0): [], ('8', -1): ['0', '6', '9'], ('8', 1): [],
    ('9', 0): ['0', '6'], ('9', -1): ['3', '5'], ('9', 1): ['8']
}

def check(s):
    # 檢查字串 s 代表的等式是否成立
    try:
        if '=' not in s: return False
        left, right = s.split('=')
        # 使用 eval 計算左邊和右邊是否相等
        return eval(left) == eval(right)
    except:
        return False

def main():
    line = sys.stdin.read().strip()
    if '#' not in line: return
    eq = line.split('#')[0]

    # 找尋所有數字的位置
    chars = list(eq)
    digit_indices = [i for i, c in enumerate(chars) if c.isdigit()]

    # 嘗試情況 (a): 原地移動
    for i in digit_indices:
        orig_char = chars[i]
        for next_char in TRANSITIONS.get((orig_char, 0), []):
            chars[i] = next_char
            new_eq = "".join(chars)
            if check(new_eq):
                print(new_eq + "#")
                return
            chars[i] = orig_char # 還原

    # 嘗試情況 (b): 跨數字移動
    for i in digit_indices:
        orig_i = chars[i]
        for rem_char in TRANSITIONS.get((orig_i, -1), []):
            if rem_char == '': continue # 不能變不見
            chars[i] = rem_char
            for j in digit_indices:
                if i == j: continue
                orig_j = chars[j]
                for add_char in TRANSITIONS.get((orig_j, 1), []):
                    chars[j] = add_char
                    new_eq = "".join(chars)
                    if check(new_eq):
                        print(new_eq + "#")
                        return
                    chars[j] = orig_j # 還原
            chars[i] = orig_i # 還原

    print("No")

if __name__ == "__main__":
    main()
