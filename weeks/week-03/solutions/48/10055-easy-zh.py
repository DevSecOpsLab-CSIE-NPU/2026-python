import sys


# UVA 10055（此作業版本題意為函數增減性查詢）
# 規則：
# - 增函數記為 0，減函數記為 1
# - 區間 [L, R] 的複合函數為減函數，等價於該區間 1 的個數為奇數
# 這裡用直觀解法：每次查詢都直接掃描區間，適合學習理解。
def main() -> None:
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return

    n, q = data[0], data[1]
    idx = 2

    # state[i]：第 i 個函數狀態（0 增、1 減）
    state = [0] * (n + 1)
    out = []

    for _ in range(q):
        op = data[idx]
        idx += 1

        if op == 1:
            # 翻轉第 i 個函數狀態
            i = data[idx]
            idx += 1
            state[i] ^= 1
        else:
            # 查詢區間 [l, r] 的奇偶（XOR）
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
