# 題目 10101: 移動一根木棒使等式成立 - 簡單版本
# 同主要版本，暴力嘗試。

# 同上程式
segments = [
    "1111110",  # 0
    "0110000",  # 1
    "1101101",  # 2
    "1111001",  # 3
    "0110011",  # 4
    "1011011",  # 5
    "1011111",  # 6
    "1110000",  # 7
    "1111111",  # 8
    "1111011",  # 9
]

num_to_seg = {str(i): segments[i] for i in range(10)}
seg_to_num = {v: str(i) for i, v in enumerate(segments)}

def get_possible_nums(original):
    possibles = []
    for pos in range(len(original)):
        new_seg = list(original)
        new_seg[pos] = '1' if new_seg[pos] == '0' else '0'
        new_str = ''.join(new_seg)
        if new_str in seg_to_num:
            possibles.append(seg_to_num[new_str])
    return possibles

def parse_expression(expr):
    parts = []
    current = ""
    for c in expr:
        if c in "+-=":
            if current:
                parts.append(int(current))
                current = ""
            parts.append(c)
        else:
            current += c
    if current:
        parts.append(int(current))
    return parts

def evaluate(parts):
    result = parts[0]
    i = 1
    while i < len(parts):
        op = parts[i]
        num = parts[i+1]
        if op == '+':
            result += num
        elif op == '-':
            result -= num
        i += 2
    return result

def solve_equation_easy(expr):
    expr = expr.rstrip('#')
    parts = parse_expression(expr)
    eq_pos = None
    for i, p in enumerate(parts):
        if p == '=':
            eq_pos = i
            break
    left_parts = parts[:eq_pos]
    right_parts = parts[eq_pos+1:]
    left_val = evaluate(left_parts)
    right_val = evaluate(right_parts)
    if left_val == right_val:
        return expr + '#'

    str_parts = []
    for p in parts:
        if isinstance(p, int):
            str_parts.append(str(p))
        else:
            str_parts.append(p)

    for idx, s in enumerate(str_parts):
        if s not in "+-=":
            seg = num_to_seg[s]
            possibles = get_possible_nums(seg)
            for new_num in possibles:
                new_str_parts = str_parts[:]
                new_str_parts[idx] = new_num
                new_expr = ''.join(new_str_parts)
                try:
                    new_parts = parse_expression(new_expr)
                    new_left = new_parts[:eq_pos]
                    new_right = new_parts[eq_pos+1:]
                    new_left_val = evaluate(new_left)
                    new_right_val = evaluate(new_right)
                    if new_left_val == new_right_val:
                        return new_expr + '#'
                except:
                    continue
    return "No"

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    expr = input.strip()
    result = solve_equation_easy(expr)
    print(result)