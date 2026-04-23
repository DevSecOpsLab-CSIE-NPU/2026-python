# 【Bloom 階段：U - 理解與進階應用】
# 6 可迭代物件（iterable）觀念範例
# August 的惡意提醒：這是很多大一新生的噩夢。
# 理解「生成器只能走一次」的特性，否則會在 Week 06 遇到「空列表」靈異事件。

items = [1, 2, 3]

# 定義一個消耗迭代器的函式
def consume(it):
    for x in it:
        pass # 僅遍歷，不做事

consume(items)  # 列表可以重複遍歷
consume('abc')  # 字串也是可迭代的

# Iterator 只能走一次地雷 (The One-Way Trap)
z = zip([1, 2], [3, 4])
first_scan = list(z) # 消耗了 zip 產生的迭代器
second_scan = list(z) # 迭代器已乾涸，這裡會是 []

print(f"First Scan: {first_scan}")
print(f"Second Scan (The Trap): {second_scan}") # 你會發現它是空的！
