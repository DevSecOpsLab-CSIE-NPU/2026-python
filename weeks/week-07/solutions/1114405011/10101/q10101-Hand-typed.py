from __future__ import annotations
import sys
from collections import defaultdict

SEG = {0: 0b1111110, 1: 0b0110000, 2: 0b1101101, 3: 0b1111001, 4: 0b0110011, 5: 0b1011011, 6: 0b1011111, 7: 0b1110000, 8: 0b1111111, 9: 0b1111011}


def build():
    rm = defaultdict(list)
    ad = defaultdict(list)
    mv = defaultdict(list)
    for a in range(10):
        ma = SEG[a]
        for b in range(10):
            if a == b:
                continue
            mb = SEG[b]
            d = (ma ^ mb).bit_count()
            if ma.bit_count() - mb.bit_count() == 1 and (mb & ma) == mb and d == 1:
                rm[a].append(b)
            if mb.bit_count() - ma.bit_count() == 1 and (ma & mb) == ma and d == 1:
                ad[a].append(b)
            if ma.bit_count() == mb.bit_count() and d == 2:
                mv[a].append(b)
    return rm, ad, mv


REMOVE, ADD, MOVE = build()


def parse_side(s: str, off: int, side_sign: int):
    i = 0
    n = len(s)
    sign = 1
    if i < n and s[i] == "-":
        sign = -1
        i += 1
    v = 0
    cf = {}
    while i < n:
        j = i
        while j < n and s[j].isdigit():
            j += 1
        token = s[i:j]
        num = int(token)
        v += sign * num
        p = 1
        for k in range(j - 1, i - 1, -1):
            cf[off + k] = side_sign * sign * p
            p *= 10
        if j < n:
            sign = 1 if s[j] == "+" else -1
        i = j + 1
    return v, cf


def coef(expr: str):
    e = expr.index("=")
    lv, lc = parse_side(expr[:e], 0, 1)
    rv, rc = parse_side(expr[e + 1 :], e + 1, -1)
    c = {}
    c.update(lc)
    c.update(rc)
    return lv - rv, c


def try_fix(expr: str):
    ch = list(expr)
    pos = [i for i, x in enumerate(ch) if x.isdigit()]
    if not pos:
        return None
    d, c = coef(expr)
    for i in pos:
        od = ord(ch[i]) - 48
        for nd in MOVE[od]:
            if d + c[i] * (nd - od) == 0:
                nc = ch[:]
                nc[i] = str(nd)
                return "".join(nc)
    bucket = defaultdict(list)
    for j in pos:
        od = ord(ch[j]) - 48
        for nd in ADD[od]:
            bucket[c[j] * (nd - od)].append((j, nd))
    t = -d
    for i in pos:
        od = ord(ch[i]) - 48
        for nd in REMOVE[od]:
            di = c[i] * (nd - od)
            need = t - di
            for j, ndj in bucket.get(need, []):
                if i == j:
                    continue
                nc = ch[:]
                nc[i] = str(nd)
                nc[j] = str(ndj)
                return "".join(nc)
    return None


def solve(data: str) -> str:
    if "#" not in data:
        return "No"
    expr = data[: data.index("#")]
    ans = try_fix(expr)
    if ans is None:
        return "No"
    return ans + "#"


if __name__ == "__main__":
    sys.stdout.write(solve(sys.stdin.read()))
