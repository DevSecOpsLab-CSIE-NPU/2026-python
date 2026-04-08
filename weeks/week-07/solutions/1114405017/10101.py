import sys
import re

def solve():
    # 定義標準七段顯示器中，每個數字所使用的木棒位置 (0-6)
    #      0
    #    1   2
    #      3
    #    4   5
    #      6
    segments = {
        '0': {0, 1, 2, 4, 5, 6},
        '1': {2, 5},
        '2': {0, 2, 3, 4, 6},
        '3': {0, 2, 3, 5, 6},
        '4': {1, 2, 3, 5},
        '5': {0, 1, 3, 5, 6},
        '6': {0, 1, 3, 4, 5, 6},
        '7': {0, 2, 5},
        '8': {0, 1, 2, 3, 4, 5, 6},
        '9': {0, 1, 2, 3, 5, 6}
    }

    # 預先計算數字 A 變成數字 B 的變化關係
    # transform[(A, B)] = (木棒數量差, 是否可以透過移動單一數字內的一根木棒達成)
    transform = {}
    for i in "0123456789":
        for j in "0123456789":
            s1, s2 = segments[i], segments[j]
            added = len(s2 - s1)    # 變成 j 需要增加幾根
            removed = len(s1 - s2)  # 變成 j 需要移除幾根
            
            # 自我修正定義：拿走一根並插回同一個數字的其他位置 (移除1根且增加1根)
            can_self_move = (added == 1 and removed == 1)
            # 數量差：用於跨數字移動 (例如 -1 代表提供一根給別人)
            diff = len(s2) - len(s1)
            transform[(i, j)] = (diff, can_self_move)

    # 讀取輸入，只處理到 '#' 符號之前的內容
    input_data = sys.stdin.read().split('#')[0]
    if not input_data:
        return

    # 將原始字串轉為串列，方便根據索引修改字元
    original_chars = list(input_data)
    
    # 找出所有數字字元在字串中的索引位置
    digit_indices = [i for i, char in enumerate(original_chars) if char.isdigit()]

    def is_valid_equation(char_list):
        """ 驗證目前的字元串列是否構成成立的等式 """
        expr = "".join(char_list)
        try:
            if '=' not in expr: return False
            left, right = expr.split('=')
            
            # 輔助函式：處理 Python eval 不支援開頭為 0 的整數問題 (例如 05 -> 5)
            def parse_side(side_str):
                # 使用正則表達式尋找所有數字，並將其轉為 int 後重新組合
                # 這樣 '05+007' 會變成 '5+7'
                tokens = re.split('([-+])', side_str)
                processed = []
                for t in tokens:
                    if t.isdigit():
                        processed.append(str(int(t)))
                    else:
                        processed.append(t)
                return eval("".join(processed))

            return parse_side(left) == parse_side(right)
        except:
            return False

    # 策略 1：嘗試「自我修正」 (只改動一個數字，且該數字木棒總數不變)
    for idx in digit_indices:
        original_digit = original_chars[idx]
        for target_digit in "0123456789":
            if original_digit == target_digit: continue
            
            _, can_self = transform[(original_digit, target_digit)]
            if can_self:
                original_chars[idx] = target_digit
                if is_valid_equation(original_chars):
                    print(f"{''.join(original_chars)}#")
                    return
                original_chars[idx] = original_digit # 復原，嘗試下一個

    # 策略 2：嘗試「跨數字移動」 (從位置 A 拿走一根，補到位置 B)
    # 遍歷所有數字對 (idx_from, idx_to)
    for i in range(len(digit_indices)):
        for j in range(len(digit_indices)):
            if i == j: continue # 跨數字移動必須是不同的位置
            
            idx_from = digit_indices[i]
            idx_to = digit_indices[j]
            
            digit_from = original_chars[idx_from]
            digit_to = original_chars[idx_to]

            # 尋找所有可能的變換：digit_from 減少一根，digit_to 增加一根
            for target_from in "0123456789":
                diff_from, _ = transform[(digit_from, target_from)]
                if diff_from == -1: # 成功減少一根
                    
                    for target_to in "0123456789":
                        diff_to, _ = transform[(digit_to, target_to)]
                        if diff_to == 1: # 成功增加一根
                            
                            # 進行替換並驗證
                            original_chars[idx_from] = target_from
                            original_chars[idx_to] = target_to
                            
                            if is_valid_equation(original_chars):
                                print(f"{''.join(original_chars)}#")
                                return
                            
                            # 復原
                            original_chars[idx_from] = digit_from
                            original_chars[idx_to] = digit_to

    # 若所有組合都嘗試過仍無解
    print("No")

if __name__ == "__main__":
    solve()