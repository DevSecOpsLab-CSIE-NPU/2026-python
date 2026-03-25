"""
UVA 10057 簡單好記版（easy）

口訣：
1) 排序
2) 奇數取中位數；偶數取中間兩個 low/high
3) 輸出：最小 A、區間內元素數、A 的可能個數

詳細理解：
- 目標是讓 sum(|Xi - A|) 最小。
- 這種「絕對值總和最小化」問題，最佳解會落在中位數位置（或中位數區間）。
- n 為奇數：中位數唯一，A 只有一種。
- n 為偶數：中間兩個值 low, high 之間的所有整數都能達最小值。
"""

import sys


def solve(data: str) -> str:
    # 題目是 EOF 多組輸入，所以先把所有數字一次讀完。
    nums = list(map(int, data.split()))

    # i 是讀取指標，指向目前尚未處理的位置。
    i = 0

    # out 用來收集每組的答案，最後再換行輸出。
    out = []

    while i < len(nums):
        # 每組第一個數字是 n（這組資料有幾個整數）。
        n = nums[i]
        i += 1

        # 取出這組的 n 個數字。
        a = nums[i : i + n]
        i += n

        # 先排序，才能方便取得中位數與中位數區間。
        a.sort()

        if n % 2:
            # 奇數：中位數唯一，直接取中間值。
            m = a[n // 2]

            # 第二欄：資料中等於 m 的數量。
            # 第三欄：可能 A 的個數，奇數時一定是 1。
            out.append(f"{m} {a.count(m)} 1")
        else:
            # 偶數：中間兩個值形成可行區間 [low, high]。
            low, high = a[n // 2 - 1], a[n // 2]

            # 第二欄：有多少 Xi 落在可行區間內。
            cnt = sum(low <= x <= high for x in a)

            # 第三欄：可行 A 的整數個數。
            ways = high - low + 1

            # 第一欄要求輸出最小可行 A，因此輸出 low。
            out.append(f"{low} {cnt} {ways}")

    return "\n".join(out)


def main() -> None:
    ans = solve(sys.stdin.read())
    if ans:
        sys.stdout.write(ans)


if __name__ == "__main__":
    main()
