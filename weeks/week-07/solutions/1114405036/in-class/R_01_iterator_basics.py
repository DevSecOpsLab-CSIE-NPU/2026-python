# Remember（記憶）- 迭代器基礎概念

# 1. 迭代器協議的核心方法
items = [1, 2, 3]

# iter() 呼叫 __iter__()
it = iter(items)
print(f"迭代器: {it}")

# next() 呼叫 __next__()
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 沒有更多元素時，擲出 StopIteration
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
print("\n--- 常見可迭代物件 ---")

# 列表
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串
print(f"字串 iter: {iter('abc')}")

# 字典
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案
import io

f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# 3. 自訂可迭代物件
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1

# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表是可迭代物件，不是迭代器
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 列表的 iter() 返回迭代器
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器本身就是可迭代物件
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")


# 手動遍歷（章節 4.1 風格）
def manual_iter(items):
    it = iter(items)
    while True:
        try:
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            break


manual_iter(["a", "b", "c"])


# 使用預設值的版本
def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)  # 預設值
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
