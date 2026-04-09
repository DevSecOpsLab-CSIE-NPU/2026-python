import sys

def solve():
    cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    def can_swap(a, b):
        shapes = ["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]
        s1, s2 = shapes[int(a)], shapes[int(b)]
        diff = sum(1 for i in range(7) if s1[i] != s2[i])
        return diff == 2 
    s_raw = sys.stdin.read().split('#')[0]
    chars = list(s_raw)
    digits = [i for i, c in enumerate(chars) if c.isdigit()]
    def check(cur_chars):
        expr = "".join(cur_chars).replace('=', '==')
        try:
            import re
            cleaned = re.sub(r'\d+', lambda m: str(int(m.group())), expr)
            return eval(cleaned)
        except: return False
    for i in digits:
        orig = chars[i]
        for target in "0123456789":
            if target != orig and can_swap(orig, target):
                chars[i] = target
                if check(chars): print(f"{''.join(chars)}#"); return
                chars[i] = orig
    for i in digits:
        for j in digits:
            if i == j: continue
            orig_i, orig_j = chars[i], chars[j]
            for ti in "0123456789":
                if cnt[int(orig_i)] - cnt[int(ti)] == 1:
                    for tj in "0123456789":
                        if cnt[int(tj)] - cnt[int(orig_j)] == 1:
                            chars[i], chars[j] = ti, tj
                            if check(chars): print(f"{''.join(chars)}#"); return
                            chars[i], chars[j] = orig_i, orig_j
    print("No")
solve()
