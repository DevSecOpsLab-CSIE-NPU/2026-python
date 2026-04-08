import sys

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


def build_transitions():
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

    for p_i in digit_pos:
        d_i = chars[p_i]

        for nd in MOVE_INSIDE[d_i]:
            if nd == d_i:
                continue
            chars[p_i] = nd
            cand = "".join(chars)
            if is_valid_equation(cand):
                return cand + suffix
        chars[p_i] = d_i

        for d_i_after in REMOVE_ONE[d_i]:
            chars[p_i] = d_i_after

            for p_j in digit_pos:
                if p_j == p_i:
                    continue

                d_j = chars[p_j]
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
