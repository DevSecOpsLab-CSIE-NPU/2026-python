# Remember（記憶）- 迭代器基礎概念
# 本檔案示範 Python 中可迭代物件、迭代器與迭代協議的運作方式。
# 透過 iter()、next() 和自訂類別示範迭代流程。

# 1. 迭代器協議的核心方法
items = [1, 2, 3]

# iter() 呼叫可迭代物件的 __iter__()，取得一個迭代器物件
it = iter(items)
print(f"迭代器: {it}")

# next() 呼叫迭代器的 __next__()，取得下一個元素
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 當迭代器沒有更多元素時，__next__() 會擲出 StopIteration
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
print("\n--- 常見可迭代物件 ---")

# 列表是一種可迭代物件，iter() 會回傳一個迭代器
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串也是可迭代物件，會逐字元產生元素
print(f"字串 iter: {iter('abc')}")

# 字典迭代時預設對 key 進行迭代
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案物件同樣是可迭代的，會逐行讀取
import io

f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# 3. 自訂可迭代物件
# CountDown 是可迭代物件，__iter__() 返回 CountDownIterator
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 每次迭代都會建立一個新的迭代器物件
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        # 當 current 變成 0 或更小時，結束迭代
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
for i in CountDown(3):
    # CountDown 會從 3 倒數到 1
    print(i, end=" ")  # 3 2 1

# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表本身是可迭代物件，但不是迭代器
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 使用 iter() 後，會得到真正的迭代器物件
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器本身同樣具備可迭代物件的特性（有 __iter__() 和 __next__()）
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")


# 手動遍歷：使用 while 迴圈搭配 next() 和 StopIteration
# 這與 for 迴圈內部的行為一致
def manual_iter(items):
    it = iter(items)
    while True:
        try:
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            break


manual_iter(["a", "b", "c"])


# 使用 next() 的預設值，避免透過 try/except 捕捉例外
def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)  # 如果沒有元素則回傳 None
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
