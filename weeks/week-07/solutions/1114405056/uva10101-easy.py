import sys

# 七段顯示器每個數字對應到的亮燈區段。
SEG = {
    "0": frozenset("abcefg"),
    "1": frozenset("cf"),
    "2": frozenset("acdeg"),
    "3": frozenset("acdfg"),
    "4": frozenset("bcdf"),
    "5": frozenset("abdfg"),
    "6": frozenset("abdefg"),
    "7": frozenset("acf"),
    "8": frozenset("abcdefg"),
    "9": frozenset("abcdfg"),
}

SET_TO_DIGIT = {v: k for k, v in SEG.items()}


def build_transitions():
    # remove_one[d]：d 移除 1 根火柴可變成哪些數字
    # add_one[d]：d 增加 1 根火柴可變成哪些數字
    # move_inside[d]：d 在同一數字內搬 1 根（移除+新增）可變成哪些數字
    remove_one = {d: [] for d in SEG}
    add_one = {d: [] for d in SEG}
    move_inside = {d: [] for d in SEG}

    for d, ss in SEG.items():
        for t, tt in SEG.items():
            rm = len(ss - tt)
            ad = len(tt - ss)
            if rm == 1 and ad == 0:
                remove_one[d].append(t)
            if rm == 0 and ad == 1:
                add_one[d].append(t)
            if rm == 1 and ad == 1:
                move_inside[d].append(t)

    return remove_one, add_one, move_inside


REMOVE_ONE, ADD_ONE, MOVE_INSIDE = build_transitions()


def eval_expr(expr: str):
    # 僅處理 +、-（含一元正負號）的整數運算。
    i = 0
    n = len(expr)
    total = 0

    while i < n:
        sign = 1
        if expr[i] == "+":
            i += 1
        elif expr[i] == "-":
            sign = -1
            i += 1

        if i >= n or not expr[i].isdigit():
            return None

        j = i
        while j < n and expr[j].isdigit():
            j += 1

        total += sign * int(expr[i:j])
        i = j

    return total


def is_valid_equation(s: str) -> bool:
    if "=" not in s:
        return False
    left, right = s.split("=", 1)
    lv = eval_expr(left)
    rv = eval_expr(right)
    if lv is None or rv is None:
        return False
    return lv == rv


def solve(data: str) -> str:
    raw = data.strip("\n")
    if not raw:
        return "No"

    hash_pos = raw.find("#")
    if hash_pos == -1:
        expr = raw
        suffix = ""
    else:
        expr = raw[:hash_pos]
        suffix = "#"

    chars = list(expr)
    digit_pos = [i for i, ch in enumerate(chars) if ch.isdigit()]

    # 枚舉「移動一根火柴」的兩種方式：
    # 1) 同一個數字內部搬移
    # 2) 從數字 i 拿走一根，補到數字 j
    for p_i in digit_pos:
        d_i = chars[p_i]

        # 情況 1：在同一個數字內搬移。
        for nd in MOVE_INSIDE[d_i]:
            if nd == d_i:
                continue
            chars[p_i] = nd
            cand = "".join(chars)
            if is_valid_equation(cand):
                return cand + suffix
        chars[p_i] = d_i

        # 情況 2：把一根從 i 移到另一個數字 j。
        for d_i_after in REMOVE_ONE[d_i]:
            chars[p_i] = d_i_after

            for p_j in digit_pos:
                if p_j == p_i:
                    continue

                d_j = chars[p_j]
                # d_j here is current digit (original), safe because p_i != p_j.
                for d_j_after in ADD_ONE[d_j]:
                    if d_j_after == d_j:
                        continue
                    old_j = chars[p_j]
                    chars[p_j] = d_j_after

                    cand = "".join(chars)
                    if is_valid_equation(cand):
                        return cand + suffix

                    chars[p_j] = old_j

            chars[p_i] = d_i

    return "No"


def main() -> None:
    text = sys.stdin.read()
    print(solve(text))


if __name__ == "__main__":
    main()
