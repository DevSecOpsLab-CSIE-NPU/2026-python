"""10101 easy-hand：手打版。"""

import sys


SEG = {
    '0': frozenset('abcefd'),
    '1': frozenset('bc'),
    '2': frozenset('abdeg'),
    '3': frozenset('abcdg'),
    '4': frozenset('bcfg'),
    '5': frozenset('acdfg'),
    '6': frozenset('acdefg'),
    '7': frozenset('abc'),
    '8': frozenset('abcdefg'),
    '9': frozenset('abcdfg'),
}


def parse_side(side):
    i = 0
    n = len(side)
    sign = 1
    total = 0

    if i < n and side[i] in '+-':
        sign = 1 if side[i] == '+' else -1
        i += 1

    while i < n:
        j = i
        while j < n and side[j].isdigit():
            j += 1
        if j == i:
            return None

        total += sign * int(side[i:j])
        if j == n:
            return total

        op = side[j]
        if op not in '+-':
            return None
        sign = 1 if op == '+' else -1
        i = j + 1

    return total


def ok_equation(expr):
    if expr.count('=') != 1:
        return False
    left, right = expr.split('=', 1)
    lv = parse_side(left)
    rv = parse_side(right)
    return lv is not None and rv is not None and lv == rv


def transitions(d):
    s = SEG[d]
    rem, add, mov = [], [], []
    for e, t in SEG.items():
        if e == d:
            continue
        if len(s) == len(t) + 1 and t.issubset(s):
            rem.append(e)
        if len(s) + 1 == len(t) and s.issubset(t):
            add.append(e)
        if len(s) == len(t) and len(s ^ t) == 2:
            mov.append(e)
    return rem, add, mov


def solve(raw):
    p = raw.find('#')
    expr = raw[:p] if p != -1 else raw.strip()
    chars = list(expr)

    dpos = [i for i, ch in enumerate(chars) if ch.isdigit()]
    trans = {d: transitions(d) for d in SEG}

    # A. 同一個數字內搬動一根。
    for i in dpos:
        d = chars[i]
        _rem, _add, mov = trans[d]
        for nd in mov:
            cand = chars[:]
            cand[i] = nd
            cexpr = ''.join(cand)
            if ok_equation(cexpr):
                return cexpr + '#'

    # B. 從一個數字拿一根，補到另一個數字。
    for i in dpos:
        d1 = chars[i]
        rem1, _a1, _m1 = trans[d1]
        for nd1 in rem1:
            for j in dpos:
                if i == j:
                    continue
                d2 = chars[j]
                _r2, add2, _m2 = trans[d2]
                for nd2 in add2:
                    cand = chars[:]
                    cand[i] = nd1
                    cand[j] = nd2
                    cexpr = ''.join(cand)
                    if ok_equation(cexpr):
                        return cexpr + '#'

    return 'No'


def main():
    raw = sys.stdin.buffer.read().decode(errors='ignore')
    if not raw:
        return
    print(solve(raw))


if __name__ == '__main__':
    main()
