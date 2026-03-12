# R10: 去重（保留原順序）
# 觀念：用 seen 記錄已看過元素，第一次出現就產生（yield）。


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            # yield 讓函式成為生成器，逐筆輸出，不需一次建完整結果
            yield item
            seen.add(item)


# 支援不可雜湊（或需要自訂比較邏輯）資料：透過 key 提取可比較值
# 例如 item 是 dict 時，可用 key=lambda d: (d['x'], d['y'])
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
