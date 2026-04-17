import sys


def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n, q = data[0], data[1]
    idx = 2

    # 0 代表增函數，1 代表減函數
    state = [0] * (n + 1)
    out = []

    for _ in range(q):
        op = data[idx]
        idx += 1

        if op == 1:
            i = data[idx]
            idx += 1
            state[i] ^= 1
        else:
            l = data[idx]
            r = data[idx + 1]
            idx += 2

            parity = 0
            for j in range(l, r + 1):
                parity ^= state[j]
            out.append(str(parity))

    print("\n".join(out))


if __name__ == "__main__":
    main()
