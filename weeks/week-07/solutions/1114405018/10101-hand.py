import sys

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

            if diff == 1:
                 
                if ca == cb + 1:
                    remove_map[a].append(b)
                
                elif cb == ca + 1:
                    add_map[a].append(b)

            
            elif diff == 2 and ca == cb:
                move_map[a].append(b)

    for d in DIGITS:
        remove_map[d].sort()
        add_map[d].sort()
        move_map[d].sort()

    return remove_map, add_map, move_map

REMOVE_MAP, ADD_MAP, MOVE_MAP = build_transition_maps()

def eval_side(side):
    i=0
    n=len(side)
    Sign=1
    total=0
  
    while i<n:
        ch = side[i]
        if ch == '-':
            Sign = -1
            i+=1
            continue

        j=i
        while j<n and side[j] not in '+-':
            j+=1
        if j==i:
            return None
        
        total += Sign * int(side[i:j])
        i=j
    return total

def is_trun_eqation(expr):
    
    if expr.count('=') != 1:
        return False
    
    left, right = expr.split('=')
    lv = eval_side(left)
    rv = eval_side(right)
    if lv is None or rv is None:
        return False    
    return lv == rv

def solve(text):

    sharp = text.find('#')
    expr = text[:sharp]if sharp != -1 else text
    if not expr:
        return lv == rv
    
    positions = [i for i, ch in enumerate(expr) if ch.isdigit()]
    if not positions:
        return "No"
    
    chars = list(expr)

    for i in positions:
        old_i = chars[i]
        for new_i in MOVE_MAP[old_i]:
            cand = chars[:]
            cand[i] = new_i
            s = "".join(cand)
            if is_true_equation(s):
                return s + "#"
            
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

    return "No"

def main():
    """競賽入口：讀 stdin 並輸出答案。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
