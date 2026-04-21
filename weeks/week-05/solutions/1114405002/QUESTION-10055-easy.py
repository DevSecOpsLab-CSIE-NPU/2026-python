import sys


class FenwickXor:
    # Fenwick Tree (BIT) 這裡存的是「奇偶性」：
    # 0 代表偶數次翻轉，1 代表奇數次翻轉。
    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def flip(self, idx: int) -> None:
        # 單點反轉：把位置 idx 的狀態做 XOR 1。
        while idx <= self.n:
            self.bit[idx] ^= 1
            idx += idx & -idx

    def query_prefix(self, idx: int) -> int:
        # 回傳 [1..idx] 區間內反轉次數的奇偶性。
        x = 0
        while idx > 0:
            x ^= self.bit[idx]
            idx -= idx & -idx
        return x

    def query_range(self, left: int, right: int) -> int:
        # 區間奇偶性 = prefix(right) XOR prefix(left-1)
        return self.query_prefix(right) ^ self.query_prefix(left - 1)


def solve(data: bytes) -> str:
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    n, q = nums[0], nums[1]
    p = 2
    fw = FenwickXor(n)
    ans = []

    for _ in range(q):
        op = nums[p]
        p += 1

        if op == 1:
            i = nums[p]
            p += 1
            fw.flip(i)
        else:
            l = nums[p]
            r = nums[p + 1]
            p += 2

            # 若區間內「減函數」數量為奇數，複合後為減函數(輸出1)
            # 若為偶數，複合後為增函數(輸出0)
            ans.append(str(fw.query_range(l, r)))

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
