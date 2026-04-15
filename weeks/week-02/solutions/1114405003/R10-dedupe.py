"""
R10：去重且保留原順序

學習目標：
1. 用 seen 集合紀錄「出現過」的元素。
2. 用生成器 yield 達成逐步輸出（節省記憶體）。
3. 透過 key 參數支援不可雜湊資料的去重規則。
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            # 第一次看到 item，才輸出
            yield item
            seen.add(item)


def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def main():
    print("=== R10 去重且保序 ===")

    nums = [1, 5, 2, 1, 9, 1, 5, 10]
    print("[例1] 原始 nums =", nums)
    print("[例1] 基本去重結果 =", list(dedupe(nums)))

    rows = [
        {"x": 1, "y": 2},
        {"x": 1, "y": 3},
        {"x": 1, "y": 2},
        {"x": 2, "y": 4},
    ]
    print("[例2] 原始 rows =", rows)
    print("[例2] 依 (x, y) 去重 =", list(dedupe2(rows, key=lambda d: (d["x"], d["y"]))))


if __name__ == "__main__":
    main()
