# Remember（記憶）- 迭代器基礎概念

# 1. 迭代器協議 (Iterator Protocol) 的核心方法
items = [1, 2, 3]

# iter() 會呼叫物件的 __iter__() 方法，回傳一個迭代器物件
it = iter(items)
print(f"迭代器: {it}")

# next() 會呼叫迭代器的 __next__() 方法取得下一個元素
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 當沒有更多元素時，必須擲出 StopIteration 異常來告知遍歷結束
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件 (Iterables)
print("\n--- 常見可迭代物件 ---")
print(f"列表 iter: {iter([1, 2, 3])}")
print(f"字串 iter: {iter('abc')}")
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

import io
f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}") # 檔案物件本身就是一種迭代器

# 3. 自訂可迭代物件：區分「容器」與「游標（迭代器）」
class CountDown: # 這是「可迭代物件」
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        return CountDownIterator(self.start) # 每次呼叫 iter() 都回傳新的游標

class CountDownIterator: # 這是真正的「迭代器」
    def __init__(self, start):
        self.current = start
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

print("\n--- 自訂迭代器 ---")
for i in CountDown(3): # for 迴圈內部會自動呼叫 iter() 與 next()
    print(i, end=" ")  # 3 2 1

# 4. 迭代器 vs 可迭代物件 的差異
# 可迭代物件 (Iterable)：有 __iter__，可以產出迭代器（如 List、Set）
# 迭代器 (Iterator)：同時有 __iter__ 與 __next__，記錄目前存取的位置

# 5. 手動遍歷的技巧
print("\n--- StopIteration 用法 ---")

def manual_iter(items):
    it = iter(items)
    while True:
        try:
            item = next(it)
            print(f"取得: {item}")
        except StopIteration: # 捕獲結束信號，優雅跳出
            break

manual_iter(["a", "b", "c"])

# 使用 next() 的預設值版本（不擲出異常，而是回傳預設值）
def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)  # 若結束則回傳 None
        if item is None:
            break
        print(f"取得: {item}")

print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])