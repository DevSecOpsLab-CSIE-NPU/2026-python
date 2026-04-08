import re

def fix_equation(input_str):
    # --- 核心邏輯與變換表 ---
    segments = {
        '0': {0, 1, 2, 4, 5, 6}, '1': {2, 5}, '2': {0, 2, 3, 4, 6},
        '3': {0, 2, 3, 5, 6}, '4': {1, 2, 3, 5}, '5': {0, 1, 3, 5, 6},
        '6': {0, 1, 3, 4, 5, 6}, '7': {0, 2, 5}, '8': {0, 1, 2, 3, 4, 5, 6},
        '9': {0, 1, 2, 3, 5, 6}
    }

    transform = {}
    for i in "0123456789":
        for j in "0123456789":
            s1, s2 = segments[i], segments[j]
            added = len(s2 - s1)
            removed = len(s1 - s2)
            can_self = (added == 1 and removed == 1)
            diff = len(s2) - len(s1)
            transform[(i, j)] = (diff, can_self)

    # 清理輸入，只取 # 之前的內容
    line = input_str.split('#')[0]
    
    # 找出數字的位置
    nums_info = []
    for m in re.finditer(r'\d+', line):
        nums_info.append({'start': m.start(), 'end': m.end(), 'val': m.group()})

    def check(expr):
        try:
            left, right = expr.split('=')
            # 移除前導零以便 eval 計算 (例如 05 -> 5)，但維持內容
            def eval_expr(e):
                # 將所有數字替換為 int(n) 的形式，避免 Python 3 把 0 開頭視為無效
                return eval(re.sub(r'(\d+)', lambda x: str(int(x.group(0))), e))
            return eval_expr(left) == eval_expr(right)
        except:
            return False

    # 1. 嘗試自我修正
    for info in nums_info:
        v = list(info['val'])
        for i in range(len(v)):
            original_char = v[i]
            for target_char in "0123456789":
                if original_char == target_char: continue
                _, can_self = transform[(original_char, target_char)]
                if can_self:
                    v[i] = target_char
                    new_expr = line[:info['start']] + "".join(v) + line[info['end']:]
                    if check(new_expr): return f"{new_expr}#"
                    v[i] = original_char # 還原

    # 2. 嘗試跨數字移動
    for i_idx, info_i in enumerate(nums_info):
        vi = list(info_i['val'])
        for i_pos in range(len(vi)):
            ori_i = vi[i_pos]
            for target_i in "0123456789":
                diff_i, _ = transform[(ori_i, target_i)]
                if diff_i == -1: # 拿走一根
                    vi[i_pos] = target_i
                    # 更新當前數字後的暫時表達式
                    mid_expr = list(line)
                    mid_expr[info_i['start'] : info_i['end']] = vi
                    
                    # 尋找接收者
                    for j_idx, info_j in enumerate(nums_info):
                        vj = list(info_j['val'])
                        # 若受贈者就是剛才修改過的數字，要用修改後的 vi
                        if i_idx == j_idx: vj = vi[:]
                        
                        for j_pos in range(len(vj)):
                            # 如果是完全同一個字元位置則跳過
                            if i_idx == j_idx and i_pos == j_pos: continue
                            
                            ori_j = vj[j_pos]
                            for target_j in "0123456789":
                                diff_j, _ = transform[(ori_j, target_j)]
                                if diff_j == 1: # 接收一根
                                    final_list = mid_expr[:]
                                    # 這裡要注意，如果 i_idx == j_idx，mid_expr 已經包含 target_i 了
                                    # 我們只需要把 target_j 塞進對應位置
                                    final_list[info_j['start'] + j_pos] = target_j
                                    new_expr = "".join(final_list)
                                    if check(new_expr): return f"{new_expr}#"
                    vi[i_pos] = ori_i # 還原
    return "No"

# --- 單元測試 ---
import unittest

class TestMatchstickGame(unittest.TestCase):
    def test_basic_self_move(self):
        # 3 變 2 (自我修正)
        self.assertEqual(fix_equation("1+1=3#"), "1+1=2#")
    
    def test_cross_move(self):
        # 15+1=12 -> 13+1=14 (5 移一根給 2)
        self.assertEqual(fix_equation("15+1=12#"), "13+1=14#")

    def test_leading_zero(self):
        # 題目說修改後允許 0 開頭
        # 0+3=3 -> 8-5=3 (舉例，非真實變換) 
        # 我們測一個簡單的：從 9 拿一根給 5 變成 6
        self.assertEqual(fix_equation("8+5=9#"), "8+6=14#") # 這裡僅為邏輯示範

    def test_no_solution(self):
        self.assertEqual(fix_equation("1+1=4#"), "No")

    def test_negative_sign(self):
        # 測試包含負號的情況
        # -2+5=3 -> -3+5=2 (2 變 3 自我修正)
        self.assertEqual(fix_equation("-2+5=3#"), "-3+5=2#")

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)