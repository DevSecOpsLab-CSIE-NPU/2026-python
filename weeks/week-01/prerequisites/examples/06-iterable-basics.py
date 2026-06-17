# 6 可迭代物件（iterable）觀念範例

items = [1, 2, 3]

def consume(it):
    for x in it:
        pass

consume(items)
consume('abc')

# iterator 只能走一次
z = zip([1, 2], [3, 4])
first = list(z)
second = list(z)  # 這裡會是 []
