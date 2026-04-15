"""
R08：字典找最小/最大值

學習目標：
1. 會用 zip(values, keys) 同步比較價格並保留股票代號。
2. 會用 min / max / sorted 觀察結果型態。
3. 會用 min(dict, key=...) 直接取得對應 key。
"""


def main():
    print("=== R08 字典最值運算 ===")

    prices = {
        "ACME": 45.23,
        "AAPL": 612.78,
        "FB": 10.75,
        "HPQ": 37.2,
    }
    print("[原始資料] prices =", prices)

    min_pair = min(zip(prices.values(), prices.keys()))
    max_pair = max(zip(prices.values(), prices.keys()))

    print("[例1] 最小 (price, name) =", min_pair)
    print("[例2] 最大 (price, name) =", max_pair)
    print("[例3] 由小到大排序 =", sorted(zip(prices.values(), prices.keys())))

    min_key = min(prices, key=lambda k: prices[k])
    print("[例4] 只取最小值對應 key =", min_key)


if __name__ == "__main__":
    main()
