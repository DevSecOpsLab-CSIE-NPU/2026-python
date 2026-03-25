import sys


class Fenwick:
    """Fenwick Tree（BIT），這裡只需要處理奇偶，因此用 XOR 邏輯。"""

    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: int) -> None:
        while index <= self.size:
            self.tree[index] ^= (value & 1)
            index += index & -index

    def prefix_xor(self, index: int) -> int:
        result = 0
        while index > 0:
            result ^= self.tree[index]
            index -= index & -index
        return result

    def range_xor(self, left: int, right: int) -> int:
        return self.prefix_xor(right) ^ self.prefix_xor(left - 1)


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    n, q = nums[0], nums[1]
    idx = 2

    # 初始全部為增函數（0），若某位置翻轉次數為奇數則為減函數（1）
    bit = Fenwick(n)
    outputs = []

    for _ in range(q):
        op = nums[idx]
        idx += 1

        if op == 1:
            func_index = nums[idx]
            idx += 1
            # 翻轉一次等同 XOR 1
            bit.add(func_index, 1)
        else:
            left = nums[idx]
            right = nums[idx + 1]
            idx += 2

            # 區間內減函數個數奇數 -> 合成後為減函數（輸出 1）
            # 偶數 -> 增函數（輸出 0）
            outputs.append(str(bit.range_xor(left, right)))

    return "\n".join(outputs)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))
