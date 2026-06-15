# 主題 06：可迭代物件（Iterable）- 簡易教學版

# 可迭代物件（iterable）是可以遍歷的物件
# 常見的可迭代物件：list、tuple、dict、set、str、file 等

items = [1, 2, 3]

def consume(it):
    """消耗掉 iterable 中的所有元素"""
    for x in it:
        pass

# list 是 iterable
consume(items)
print("消耗 list 完成")

# 字串也是 iterable
consume('abc')
print("消耗字串完成")

# iterator 與 iterable 的差異
# iterator 只能走一次，之後就耗盡了
z = zip([1, 2], [3, 4])
first = list(z)          # 第一次轉為 list：[(1, 3), (2, 4)]
second = list(z)         # 第二次轉為 list：[] （已經耗盡）

print(f"第一次: {first}")
print(f"第二次: {second}")

# 其他 iterator：filter、map、groupby 等
filtered = filter(lambda x: x > 1, [1, 2, 3])
first_filter = list(filtered)
second_filter = list(filtered)  # 這也會是空的

print(f"第一次 filter: {first_filter}")
print(f"第二次 filter: {second_filter}")
