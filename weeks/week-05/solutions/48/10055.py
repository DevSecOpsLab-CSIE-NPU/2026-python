import sys


class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def range_sum(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


def main():
    # 讀入全部 token，支援大量查詢
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    idx = 0
    n = data[idx]
    idx += 1
    q = data[idx]
    idx += 1

    # state[i]：0 代表增函數，1 代表減函數（是否反轉奇數次）
    state = [0] * (n + 1)
    ft = FenwickTree(n)
    answers = []

    for _ in range(q):
        v = data[idx]
        idx += 1

        if v == 1:
            i = data[idx]
            idx += 1

            # 反轉第 i 個函數的增減性
            if state[i] == 0:
                state[i] = 1
                ft.add(i, 1)
            else:
                state[i] = 0
                ft.add(i, -1)
        else:
            left = data[idx]
            idx += 1
            right = data[idx]
            idx += 1

            # 複合函數為減函數 <=> 區間內減函數數量為奇數
            cnt_dec = ft.range_sum(left, right)
            answers.append("1" if cnt_dec % 2 == 1 else "0")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    main()
