# R10. 去重且保序（1.10）
#
# 這份程式示範「去重（deduplicate）」但保留原始出現順序的技巧。
# 核心想法：
# - 用 set 記錄看過的值（查找速度快）
# - 逐項掃描資料，只在第一次出現時輸出


def dedupe(items):
    # seen 用來存「已出現過」的元素
    seen = set()

    # 依原始順序走訪 items
    for item in items:
        # 第一次出現才輸出
        if item not in seen:
            # yield 代表這是一個生成器（generator）：
            # 不是一次回傳整包結果，而是逐個產生元素
            yield item

            # 標記已看過，後面重複值就會被略過
            seen.add(item)


def dedupe2(items, key=None):
    # 進階版：可自訂「如何判定重複」
    # seen 存的是比較用的 key 值，不一定是 item 本體
    seen = set()

    for item in items:
        # 若沒提供 key，就直接用 item 本身比對
        # 若有提供 key，就先轉成可比較/可雜湊的 val
        # 例如 item 是 dict 時，可用 key=lambda d: (d['x'], d['y'])
        val = item if key is None else key(item)

        # val 第一次出現才輸出原 item
        if val not in seen:
            yield item
            seen.add(val)


# 讀懂這份程式的步驟：
# 1. 先抓主軸：for 迴圈逐項掃描 + seen 記錄是否看過。
# 2. 看到 yield 就知道是「惰性產生」：常搭配 list(dedupe(...)) 才會得到清單。
# 3. dedupe 與 dedupe2 差別在比較基準：
#    - dedupe：直接比 item
#    - dedupe2：可用 key(item) 決定重複規則
# 4. 這種寫法能同時做到「去重」與「保留第一次出現順序」。
