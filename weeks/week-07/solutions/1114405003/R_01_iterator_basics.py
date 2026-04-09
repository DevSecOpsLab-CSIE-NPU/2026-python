# Remember（記憶）- 迭代器基礎概念
#
# 本檔案示範 Python 迭代器最重要的觀念與實作方式：
# 1. 迭代器協議（iterator protocol）由 __iter__ 與 __next__ 組成。
# 2. 可迭代物件（iterable）與迭代器（iterator）是不同概念。
# 3. 當資料取完時，next() 會觸發 StopIteration，表示迭代結束。
# 4. 可以自己實作 __iter__/__next__，建立自訂迭代邏輯。

# 1. 迭代器協議的核心方法
items = [1, 2, 3]

# iter() 會向物件索取「迭代器」。
# 對 list 來說，iter(items) 會回傳一個 list_iterator 物件。
# 之後就可透過 next(it) 一個一個取值。
it = iter(items)
print(f"迭代器: {it}")

# next() 會呼叫迭代器的 __next__() 方法，
# 每呼叫一次就往前取一個元素。
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 當元素取完後，__next__() 必須拋出 StopIteration，
# Python 用這個例外作為「沒有下一筆資料」的結束訊號。
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
print("\n--- 常見可迭代物件 ---")

# 列表（list）是可迭代物件。
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串（str）也是可迭代物件，會逐字元迭代。
print(f"字串 iter: {iter('abc')}")

# 字典（dict）預設迭代的是 key。
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案物件也是可迭代物件，常見用途是逐行讀取。
import io

f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# 3. 自訂可迭代物件
class CountDown:
    # CountDown 本身代表「可迭代物件」：
    # 它透過 __iter__ 回傳真正負責取值的迭代器。
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 每次開始新的迴圈，都建立一個新的迭代器實例，
        # 這樣不同迴圈不會互相干擾狀態。
        return CountDownIterator(self.start)


class CountDownIterator:
    # CountDownIterator 才是「迭代器」：
    # 內部維護 current 狀態，並在 __next__ 中更新。
    def __init__(self, start):
        self.current = start

    def __next__(self):
        # 當 current <= 0 表示倒數完成，必須拋出 StopIteration。
        if self.current <= 0:
            raise StopIteration
        # 先遞減再回傳，讓輸出序列為 start, start-1, ... , 1。
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1

# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表有 __iter__，所以是可迭代物件；
# 但它沒有 __next__，所以不是迭代器。
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 對列表呼叫 iter() 後，會得到真正的迭代器物件。
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 多數迭代器同時也是可迭代物件（它們的 __iter__ 通常回傳自己）。
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")


# 手動遍歷（章節 4.1 風格）
def manual_iter(items):
    # 這段程式手動重現 for 迴圈背後做的事：
    # 1) 先 iter() 取得迭代器
    # 2) 持續 next()
    # 3) 捕捉 StopIteration 後結束
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
    # next(it, default) 是另一種寫法：
    # 若迭代結束，不拋例外而是回傳 default。
    # 這可避免 try/except，但要小心 default 不要與真實資料衝突。
    it = iter(items)
    while True:
        item = next(it, None)  # 預設值
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
