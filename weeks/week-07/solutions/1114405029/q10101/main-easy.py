import sys

# 詳細繁體中文註解說明：
# 1. 我們先列出 0 到 9 每個數字用了幾根木棒。
# 2. 我們也要知道，從一個數字變到另一個數字，是「多了」、「少了」還是「不變」。
# 3. 移動一根木棒只有三種可能：
#    (A) 某個數字自己內部移一下（總數不變，例如 6 變 9）。
#    (B) 把 A 數字的一根拿走，塞到 B 數字裡（A少1，B多1）。

def solve():
    # 每個數字在七段顯示器中的木棒數量
    sticks = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    
    # 七段顯示器的細節（用 1 表示有那根，0 表示沒有）
    # 順序為 a,b,c,d,e,f,g
    bits = [
        "1111110", "0110000", "1101101", "1111001", "0110011",
        "1011011", "1011111", "1110000", "1111111", "1111011"
    ]

    def get_changes(d1, d2):
        # 比較兩個數字的組成都底差在哪
        # add: 需要補幾根, rem: 需要拿走幾根
        b1, b2 = bits[d1], bits[d2]
        add = sum(1 for i in range(7) if b1[i] == '0' and b2[i] == '1')
        rem = sum(1 for i in range(7) if b1[i] == '1' and b2[i] == '0')
        return add, rem

    raw_input = sys.stdin.readline().strip()
    if not raw_input or raw_input == '#': return
    
    s_list = list(raw_input)
    num_pos = [i for i, c in enumerate(s_list) if c.isdigit()]

    # 檢查函數：把字串轉成數字運算看等號成不成立
    def is_ok(lst):
        temp_s = "".join(lst).replace('=', '==')
        try: return eval(temp_s)
        except: return False

    # 遍歷每一個數字位置
    for idx in num_pos:
        orig = int(s_list[idx])
        for target in range(10):
            if target == orig: continue
            add, rem = get_changes(orig, target)
            
            # 情況 A：同一個字內部移動一根 (拿走1根同時補回1根)
            if add == 1 and rem == 1:
                s_list[idx] = str(target)
                if is_ok(s_list):
                    print("".join(s_list))
                    return
                s_list[idx] = str(orig)
            
            # 情況 B：這個數字「拿走」1根 (rem=1, add=0)
            if rem == 1 and add == 0:
                s_list[idx] = str(target)
                # 既然拿走一根，就必須去別的地方「補上」一根
                for idx2 in num_pos:
                    if idx == idx2: continue
                    orig2 = int(s_list[idx2])
                    for target2 in range(10):
                        add2, rem2 = get_changes(orig2, target2)
                        if add2 == 1 and rem2 == 0:
                            s_list[idx2] = str(target2)
                            if is_ok(s_list):
                                print("".join(s_list))
                                return
                            s_list[idx2] = str(orig2)
                s_list[idx] = str(orig)

    print("No")

if __name__ == "__main__":
    solve()