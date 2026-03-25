import sys 

def main() -> None:
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        return

    n, q = nums[0], nums[1]
    i = 2

    state = [0] * (n + 1)  # state[idx]：目前是增(0)或減(1)
    out = []

    for _ in range(q):
        v = nums[i]
        i += 1

        if v == 1:
            idx = nums[i]
            i += 1
            state[idx] ^= 1  # 直接翻轉
        else:
            l = nums[i]
            r = nums[i + 1]
            i += 2

            # 區間內減函數數量的奇偶，就是複合函數的增減性
            parity = sum(state[l:r + 1]) % 2
            out.append(str(parity))

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
    