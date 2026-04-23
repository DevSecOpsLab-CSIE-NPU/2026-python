import sys
import re

# 根據 QUESTION-10101.md (真正的聖經)：這題不是數字格式化！
# 是「移動火柴棒」遊戲：移動一根木棒使等式成立。

# 七段顯示器的位元遮罩
segments = [
    0b1111110, # 0
    0b0110000, # 1
    0b1101101, # 2
    0b1111001, # 3
    0b0110011, # 4
    0b1011011, # 5
    0b1011111, # 6
    0b1110000, # 7
    0b1111111, # 8
    0b1111011  # 9
]

def count_sticks(mask):
    return bin(mask).count('1')

def solve():
    raw = sys.stdin.read().strip()
    if '#' not in raw: return
    equation = raw.split('#')[0]

    tokens = re.findall(r'\d+|[+\-=]', equation)
    digit_pos = []
    for i, t in enumerate(tokens):
        if t.isdigit():
            for j in range(len(t)):
                digit_pos.append((i, j))

    def check(parts):
        try:
            s = "".join(parts)
            l, r = s.split('=')
            return eval(l) == eval(r)
        except: return False

    # 1. 原地移動
    for t_idx, c_idx in digit_pos:
        orig_v = int(tokens[t_idx][c_idx])
        orig_m = segments[orig_v]
        for v in range(10):
            if v == orig_v: continue
            if count_sticks(orig_m) == count_sticks(segments[v]):
                if bin(orig_m ^ segments[v]).count('1') == 2:
                    new_tokens = list(tokens)
                    s = list(new_tokens[t_idx]); s[c_idx] = str(v); new_tokens[t_idx] = "".join(s)
                    if check(new_tokens):
                        print("".join(new_tokens) + "#")
                        return

    # 2. 跨數字移動
    for idx1, (t1, c1) in enumerate(digit_pos):
        v1 = int(tokens[t1][c1])
        for v1_new in range(10):
            if count_sticks(segments[v1_new]) == count_sticks(segments[v1]) - 1:
                if (segments[v1] & segments[v1_new]) == segments[v1_new]:
                    for idx2, (t2, c2) in enumerate(digit_pos):
                        if idx1 == idx2: continue
                        v2 = int(tokens[t2][c2])
                        for v2_new in range(10):
                            if count_sticks(segments[v2_new]) == count_sticks(segments[v2]) + 1:
                                if (segments[v2_new] & segments[v2]) == segments[v2]:
                                    new_t = list(tokens)
                                    s1 = list(new_t[t1]); s1[c1] = str(v1_new); new_t[t1] = "".join(s1)
                                    s2 = list(new_t[t2]); s2[c2] = str(v2_new); new_t[t2] = "".join(s2)
                                    if check(new_t):
                                        print("".join(new_t) + "#")
                                        return
    print("No")

if __name__ == "__main__":
    solve()
