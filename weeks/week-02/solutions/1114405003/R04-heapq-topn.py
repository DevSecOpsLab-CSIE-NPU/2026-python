"""
R04：heapq 取得 Top-N

學習目標：
1. 會用 nlargest / nsmallest 取得前 N 筆。
2. 會用 key 參數在複合資料（如字典）上比較。
3. 了解 heapify 與 heappop 的基本行為。
"""

import heapq


def main():
    print("=== R04 heapq Top-N ===")

    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print("[例1] 原始數列 =", nums)
    print("[例1] 最大 3 筆 =", heapq.nlargest(3, nums))
    print("[例1] 最小 3 筆 =", heapq.nsmallest(3, nums))

    portfolio = [
        {"name": "IBM", "shares": 100, "price": 91.1},
        {"name": "AAPL", "shares": 50, "price": 543.22},
        {"name": "FB", "shares": 200, "price": 21.09},
    ]
    cheapest = heapq.nsmallest(1, portfolio, key=lambda s: s["price"])
    print("[例2] 股票清單 =", portfolio)
    print("[例2] 依 price 取最便宜 1 筆 =", cheapest)

    heap = list(nums)
    heapq.heapify(heap)
    print("[例3] heapify 後（最小堆內部結構）=", heap)
    print("[例3] heappop 取出最小值 =", heapq.heappop(heap))
    print("[例3] pop 後剩餘堆 =", heap)


if __name__ == "__main__":
    main()
