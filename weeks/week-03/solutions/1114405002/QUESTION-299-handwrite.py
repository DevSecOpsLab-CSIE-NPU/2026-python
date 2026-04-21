import sys


def swap_need(arr):
    s = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                s += 1
    return s


def main():
    v = list(map(int, sys.stdin.buffer.read().split()))
    if not v:
        return

    t = v[0]
    p = 1
    out = []

    for _ in range(t):
        l = v[p]
        p += 1
        arr = v[p:p + l]
        p += l
        out.append(f'Optimal train swapping takes {swap_need(arr)} swaps.')

    sys.stdout.write('\n'.join(out) + ('\n' if out else ''))


if __name__ == '__main__':
    main()