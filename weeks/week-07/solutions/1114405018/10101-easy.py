import sys


# 七段顯示器定義（a,b,c,d,e,f,g 對應 bit 0..6）
SEG_MASK = {
    "0": 0b0111111,
    "1": 0b0000110,
    "2": 0b1011011,
    "3": 0b1001111,
    "4": 0b1100110,
    "5": 0b1101101,
    "6": 0b1111101,
    "7": 0b0000111,
    "8": 0b1111111,
    "9": 0b1101111,
}
DIGITS = "0123456789"


def build_transition_maps():
    """建立三種轉換表。

    三種轉換的意義：
    1. remove_map[a]: 把數字 a 拿掉一根木棒後，可以變成哪些數字。
    2. add_map[a]: 在數字 a 加上一根木棒後，可以變成哪些數字。
    3. move_map[a]: 在同一個數字內搬移一根木棒後，可以變成哪些數字。

    這三張表先預處理好，solve() 時就能直接查表，程式更直覺。
    """
    remove_map = {d: [] for d in DIGITS}
    add_map = {d: [] for d in DIGITS}
    move_map = {d: [] for d in DIGITS}

    for a in DIGITS:
        ma = SEG_MASK[a]
        ca = ma.bit_count()
        for b in DIGITS:
            if a == b:
                continue
            mb = SEG_MASK[b]
            cb = mb.bit_count()
            diff = (ma ^ mb).bit_count()

            # 只差一段：可能是拔一根或加一根
            if diff == 1:
                # a 的段數比 b 多 1：表示 a 可以拔掉一根變成 b
                if ca == cb + 1:
                    remove_map[a].append(b)
                # b 的段數比 a 多 1：表示 a 可以加上一根變成 b
                elif cb == ca + 1:
                    add_map[a].append(b)

            # 差兩段且總段數一樣：同一數字內搬一根
            elif diff == 2 and ca == cb:
                move_map[a].append(b)

    # 排序讓輸出固定（同樣輸入時，回傳結果穩定）
    for d in DIGITS:
        remove_map[d].sort()
        add_map[d].sort()
        move_map[d].sort()

    return remove_map, add_map, move_map


REMOVE_MAP, ADD_MAP, MOVE_MAP = build_transition_maps()


def eval_side(side):
    """計算一側算式值。

    支援格式：
    - 只有 +、- 與數字
    - 允許第一個數字帶負號（例如 -12+3）
    """
    i = 0
    n = len(side)
    sign = 1
    total = 0

    while i < n:
        ch = side[i]
        if ch == "+":
            sign = 1
            i += 1
            continue
        if ch == "-":
            sign = -1
            i += 1
            continue

        j = i
        while j < n and side[j].isdigit():
            j += 1
        if j == i:
            # 代表不是合法數字起點，視為非法算式
            return None

        total += sign * int(side[i:j])
        i = j

    return total


def is_true_equation(expr):
    """判斷 expr 是否為成立等式。"""
    if expr.count("=") != 1:
        return False

    left, right = expr.split("=")
    lv = eval_side(left)
    rv = eval_side(right)
    if lv is None or rv is None:
        return False
    return lv == rv


def solve(text):
    """easy 版主流程：直接枚舉所有「只移動一根木棒」的候選。"""

    # 題目規定輸入以 # 結尾，且 # 後面可能有垃圾字元，這裡只取 # 前內容
    sharp = text.find("#")
    expr = text[:sharp] if sharp != -1 else text.strip()
    if not expr:
        return "No"

    # 只有數字可以被動到，運算子與等號不能改
    positions = [i for i, ch in enumerate(expr) if ch.isdigit()]
    if not positions:
        return "No"

    # 先轉 list，方便改動某一個字元後快速組回字串
    chars = list(expr)

    # 情況 A：同一數字內搬移一根
    for i in positions:
        old_i = chars[i]
        for new_i in MOVE_MAP[old_i]:
            cand = chars[:]
            cand[i] = new_i
            s = "".join(cand)
            if is_true_equation(s):
                # 找到第一個可行答案就回傳
                return s + "#"

    # 情況 B：從某數字拔一根，放到另一數字
    for i in positions:
        old_i = chars[i]
        for mid_i in REMOVE_MAP[old_i]:
            for j in positions:
                if j == i:
                    continue
                old_j = chars[j]
                for new_j in ADD_MAP[old_j]:
                    cand = chars[:]
                    cand[i] = mid_i
                    cand[j] = new_j
                    s = "".join(cand)
                    if is_true_equation(s):
                        # 這裡正好對應「拿一根 + 放一根」共移動一根木棒
                        return s + "#"

    # 所有候選都試完仍無解
    return "No"


def main():
    """競賽入口：讀 stdin 並輸出答案。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
