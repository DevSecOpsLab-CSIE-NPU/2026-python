import sys


def dfs(n, pos, used, cur, forb, prev, out):
    if pos == n:
        s = ''.join(cur)
        l = 0
        m = min(len(prev[0]), len(s))
        while l < m and prev[0][l] == s[l]:
            l += 1
        out.append(s[l:])
        prev[0] = s
        return
    for p in range(n):
        if not (used >> p) & 1 and (pos + 1) not in forb[p]:
            cur.append(chr(65 + p))
            dfs(n, pos + 1, used | (1 << p), cur, forb, prev, out)
            cur.pop()


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    out = []
    while True:
        try:
            n = int(next(it))
        except StopIteration:
            break
        forb = [set() for _ in range(n)]
        for i in range(n):
            while True:
                v = int(next(it))
                if v == 0:
                    break
                forb[i].add(v)
        prev = ['']
        dfs(n, 0, 0, [], forb, prev, out)
        out.append('')
    if out and out[-1] == '':
        out.pop()
    sys.stdout.write('\n'.join(out))


if __name__ == '__main__':
    main()
