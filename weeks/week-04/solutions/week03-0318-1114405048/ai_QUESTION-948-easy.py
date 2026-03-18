import sys


def check(coin, heavy, ws):
    # heavy=True 表示假幣較重，False 表示較輕
    for L, R, sign in ws:
        inL = coin in L
        inR = coin in R

        if sign == '=':
            # 平衡：假幣不能在秤盤上
            if inL or inR:
                return False
            continue

        # 不平衡：假幣一定在秤盤上
        if not inL and not inR:
            return False

        # 預期結果
        if inL:
            expect = '>' if heavy else '<'
        else:
            expect = '<' if heavy else '>'

        if expect != sign:
            return False

    return True


def main():
    tok = sys.stdin.read().split()
    p = 0

    m = int(tok[p])
    p += 1

    out = []

    for _ in range(m):
        n = int(tok[p])
        k = int(tok[p + 1])
        p += 2

        ws = []
        for _ in range(k):
            cnt = int(tok[p])
            p += 1

            L = set(map(int, tok[p:p + cnt]))
            p += cnt

            R = set(map(int, tok[p:p + cnt]))
            p += cnt

            sign = tok[p]
            p += 1

            ws.append((L, R, sign))

        cand = []
        for coin in range(1, n + 1):
            if check(coin, True, ws) or check(coin, False, ws):
                cand.append(coin)

        if len(cand) == 1:
            out.append(str(cand[0]))
        else:
            out.append('0')

    print("\n\n".join(out))


if __name__ == "__main__":
    main()