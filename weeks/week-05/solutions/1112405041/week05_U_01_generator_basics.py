# 【Bloom 階段：U - 理解與進階應用】
# U01. 生成器 (Generator) 與 yield
# August 的惡意提醒：生成器是 Python 處理無限序列或大型資料的核心。
# 學會 yield from，這是你在 Week 10 處理 DFS (10226) 時，
# 遞迴展開路徑的最優解法。

# 1. 基礎生成器：範圍數值
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x # 暫停並回傳值
        x += step

# 2. 無限序列：Fibonacci
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# 3. 遞迴結構展開 (Yield From)
# 指紋點：你知道如何扁平化一個巢狀列表嗎？
def flatten(items):
    for x in items:
        # 如果是可迭代對象 (且不是字串)，遞迴展開
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x

nested = [1, [2, [3, 4]], 5]
print(f"Flattened: {list(flatten(nested))}") # [1, 2, 3, 4, 5]

# August 筆記：yield from 不只是縮寫，它還自動處理了子生成器的異常傳遞。
