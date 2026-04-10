import sys

def solve():
    bits = [
        "1111110", "0110000", "1101101", "1111001", "0110011",
        "1011011", "1011111", "1110000", "1111111", "1111011"
    ]

    def get_changes(d1, d2):
        b1, b2 = bits[d1], bits[d2]
        add = sum(1 for i in range(7) if b1[i] == '0' and b2[i] == '1')
        rem = sum(1 for i in range(7) if b1[i] == '1' and b2[i] == '0')
        return add, rem

    raw_input = sys.stdin.readline().strip()
    if not raw_input or raw_input == '#': return
    
    s_list = list(raw_input)
    num_pos = [i for i, c in enumerate(s_list) if c.isdigit()]

    def is_ok(lst):
        temp_s = "".join(lst).replace('=', '==')
        try: return eval(temp_s)
        except: return False

    for idx in num_pos:
        orig = int(s_list[idx])
        for target in range(10):
            if target == orig: continue
            add, rem = get_changes(orig, target)
            if add == 1 and rem == 1:
                s_list[idx] = str(target)
                if is_ok(s_list):
                    print("".join(s_list))
                    return
                s_list[idx] = str(orig)
            if rem == 1 and add == 0:
                s_list[idx] = str(target)
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