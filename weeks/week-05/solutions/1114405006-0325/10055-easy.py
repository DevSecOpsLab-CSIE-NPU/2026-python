"""
UVA 10055 簡單好記版（easy）

口訣：
1) 每個位置只看「是不是減函數」：0 或 1
2) 查詢區間只看 1 的奇偶：偶數輸出 0，奇數輸出 1
3) 用 Fenwick Tree 做 XOR，反轉就是在該點 XOR 1

詳細理解：
- 複合函數最後是增或減，只看「減函數個數的奇偶」。
- 偶數個減函數互相抵消後會回到增函數（輸出 0）。
- 奇數個減函數則會留下減函數效果（輸出 1）。
- 因為我們只在乎奇偶，所以用 XOR（異或）最自然：
    0^0=0、0^1=1、1^1=0，剛好對應奇偶切換。
"""

import sys


class FenwickXor:
    """用 XOR 版本的 Fenwick Tree，支援單點更新與區間奇偶查詢。"""

    def __init__(self, n: int) -> None:
        self.n = n
        # bit[0] 不使用，與 Fenwick Tree 慣例一致。
        self.bit = [0] * (n + 1)

    def add_xor(self, i: int, v: int) -> None:
        # 在索引 i 做 XOR 更新（這裡 v 只會是 1）。
        while i <= self.n:
            self.bit[i] ^= v
            i += i & -i

    def prefix_xor(self, i: int) -> int:
        # 回傳區間 [1, i] 的 XOR 值。
        s = 0
        while i > 0:
            s ^= self.bit[i]
            i -= i & -i
        return s

    def range_xor(self, l: int, r: int) -> int:
        # 區間 [l, r] XOR = prefix(r) XOR prefix(l-1)
        return self.prefix_xor(r) ^ self.prefix_xor(l - 1)


def main() -> None:
    # 一次讀入全部數字，方便用索引 i 逐步取值。
    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        # 若沒有輸入，直接結束。
        return

    # 第一行有 N（函數數量）與 Q（操作數量）。
    n, q = nums[0], nums[1]

    # i 指向下一個尚未讀取的數字位置。
    i = 2

    tree = FenwickXor(n)

    # 收集所有查詢結果，最後一次輸出。
    out = []

    for _ in range(q):
        # op=1 代表反轉；op=2 代表查詢區間。
        op = nums[i]
        i += 1

        if op == 1:
            idx = nums[i]
            i += 1
            # 反轉：0<->1 等同 XOR 1
            tree.add_xor(idx, 1)
        else:
            l, r = nums[i], nums[i + 1]
            i += 2
            # 區間 XOR 結果就是減函數個數的奇偶（0:偶, 1:奇）
            out.append(str(tree.range_xor(l, r)))

    # 每次查詢輸出一行，符合題目格式。
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
