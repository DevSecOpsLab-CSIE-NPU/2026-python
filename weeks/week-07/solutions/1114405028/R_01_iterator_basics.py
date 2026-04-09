# Remember（記憶）- 迭代器基礎概念
# 本程式示範 Python 迭代器協議的核心概念，包括：
# 1. iter() 和 next() 函數的使用
# 2. 常見可迭代物件的迭代器
# 3. 自訂可迭代物件和迭代器的實現
# 4. 迭代器與可迭代物件的區別
# 5. StopIteration 例外的處理

# 1. 迭代器協議的核心方法
# 迭代器協議是 Python 中實現迭代的核心機制
# 任何物件只要實現了 __iter__() 和 __next__() 方法，就是可迭代的
items = [1, 2, 3]

# iter() 函數呼叫物件的 __iter__() 方法，返回一個迭代器
it = iter(items)
print(f"迭代器: {it}")

# next() 函數呼叫迭代器的 __next__() 方法，取得下一個元素
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 當沒有更多元素時，__next__() 會擲出 StopIteration 例外
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
# Python 中許多內建型別都是可迭代的，包括列表、字串、字典、檔案等
print("\n--- 常見可迭代物件 ---")

# 列表 - 最常見的可迭代物件
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串 - 逐個字元迭代
print(f"字串 iter: {iter('abc')}")

# 字典 - 預設迭代鍵
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案物件 - 逐行迭代
import io

f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# 3. 自訂可迭代物件
# 要建立自訂的可迭代物件，需要實現 __iter__() 方法
# __iter__() 應該返回一個迭代器物件
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 返回一個新的迭代器實例
        # 這樣每次迭代都會從頭開始
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        # 迭代器的狀態：當前計數值
        self.current = start

    def __next__(self):
        # 如果計數到 0 或以下，停止迭代
        if self.current <= 0:
            raise StopIteration
        # 返回當前值，然後減 1
        self.current -= 1
        return self.current + 1

    def __iter__(self):
        # 迭代器本身也是可迭代的，返回自己
        return self


print("\n--- 自訂迭代器 ---")
# 使用 for 迴圈遍歷自訂的可迭代物件
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1
print()

# 4. 迭代器 vs 可迭代物件
# 重要概念區分：
# - 可迭代物件：有 __iter__() 方法，可以被 iter() 呼叫
# - 迭代器：有 __iter__() 和 __next__() 方法，可以被 next() 呼叫
print("\n--- 迭代器 vs 可迭代物件 ---")

# 列表是可迭代物件，但不是迭代器
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 列表的 iter() 返回迭代器
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器本身就是可迭代物件（因為有 __iter__ 方法）
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
# StopIteration 是 Python 用來表示迭代結束的訊號
print("\n--- StopIteration 用法 ---")


# 手動遍歷（類似於 for 迴圈的內部實現）
def manual_iter(items):
    # 取得迭代器
    it = iter(items)
    while True:
        try:
            # 嘗試取得下一個元素
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            # 迭代結束，跳出迴圈
            break


manual_iter(["a", "b", "c"])


# 使用預設值的版本
# next() 的第二個參數是預設值，當迭代結束時返回而不是擲出例外
def manual_iter_default(items):
    it = iter(items)
    while True:
        # 使用 None 作為預設值
        item = next(it, None)  # 預設值
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
