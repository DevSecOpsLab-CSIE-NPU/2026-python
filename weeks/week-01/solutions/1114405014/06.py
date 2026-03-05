# 06.py - 消耗可迭代物件與 zip 的行為
items = [1, 2, 3]

def consume(it):
    # 遍歷可迭代物件但不做任何處理
    for x in it:
        pass

consume(items)   # 消耗列表
consume('abc')   # 消耗字串（遍歷字符）

# zip 回傳一個迭代器，消耗後不可重用
z = zip([1, 2], [3, 4])
first = list(z)
second = list(z)   # second 為空，因為 z 已被消耗

print(f"items = {items}")
print(f"first = {first}")
print(f"second = {second}")