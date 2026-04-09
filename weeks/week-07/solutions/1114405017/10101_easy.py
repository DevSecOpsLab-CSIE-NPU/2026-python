import sys

def solve():
    # 每個數字對應的木棒數量 (0-9)
    cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    # 同位移動：木棒數相同但形狀不同的數字對 (注意: 0, 6, 9 互換, 2, 3, 5 互換)
    # 這裡直接用 diff == 0 且 shape 不同來判定，簡化為預處理清單
    def can_swap(a, b): # 檢查 a 變 b 是否只需移動一根 (且總數不變)
        # 0,6,9 互換; 2,3,5 互換 需滿足特定形狀差異，此處為簡化邏輯，直接用題目定義
        shapes = ["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]
        s1, s2 = shapes[int(a)], shapes[int(b)]
        diff = sum(1 for i in range(7) if s1[i] != s2[i])
        return diff == 2 # 拔一根插一根，會造成兩個位置不同

    s_raw = sys.stdin.read().split('#')[0]
    chars = list(s_raw)
    digits = [i for i, c in enumerate(chars) if c.isdigit()]

    def check(cur_chars):
        expr = "".join(cur_chars).replace('=', '==')
        # 處理前導零：將數字字串轉為 int 再比較
        try:
            import re
            # 將所有數字匹配出來並轉為 int，避免 eval 的 0 開頭錯誤
            cleaned = re.sub(r'\d+', lambda m: str(int(m.group())), expr)
            return eval(cleaned)
        except: return False

    # 1. 嘗試同位移動 (變換一個數字)
    for i in digits:
        orig = chars[i]
        for target in "0123456789":
            if target != orig and can_swap(orig, target):
                chars[i] = target
                if check(chars): print(f"{''.join(chars)}#"); return
                chars[i] = orig

    # 2. 嘗試跨位移動 (從 i 拿一根給 j)
    for i in digits:
        for j in digits:
            if i == j: continue
            orig_i, orig_j = chars[i], chars[j]
            # 找到所有滿足 cnt-1 的 target_i 和 cnt+1 的 target_j
            for ti in "0123456789":
                if cnt[int(orig_i)] - cnt[int(ti)] == 1:
                    for tj in "0123456789":
                        if cnt[int(tj)] - cnt[int(orig_j)] == 1:
                            chars[i], chars[j] = ti, tj
                            if check(chars): print(f"{''.join(chars)}#"); return
                            chars[i], chars[j] = orig_i, orig_j

    print("No")

solve()
