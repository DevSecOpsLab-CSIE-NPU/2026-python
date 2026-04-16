"""Remember（記憶）- 迭代器基礎概念。

本檔重點：
1. 了解 iter() / next() 與 StopIteration 的關係。
2. 分辨「可迭代物件」與「迭代器」差異。
3. 實作一個自訂迭代器並觀察 for 迴圈如何運作。
"""

# 1. 迭代器協議的核心方法
# 迭代器協議主要由 __iter__() 與 __next__() 兩個方法構成
items = [1, 2, 3]

# iter() 會呼叫可迭代物件的 __iter__()，取得一個迭代器
it = iter(items)
print(f"迭代器: {it}")

# next() 每呼叫一次，就會向迭代器要下一個元素
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 沒有更多元素時，迭代器會丟出 StopIteration 例外
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
# 常見內建型別大多可迭代：list / str / dict / file-like object
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
    # 可迭代物件：負責提供 __iter__，回傳對應迭代器
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountDownIterator(self.start)


class CountDownIterator:
    # 迭代器：負責保存狀態並逐步回傳值
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
# 這段示範 for 迴圈底層其實就是 while + next + StopIteration
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
