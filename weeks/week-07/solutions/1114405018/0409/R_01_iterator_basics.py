# Remember（記憶）- 迭代器基礎概念
# 這份檔案會用小範例說明：
# 1. 什麼是「可迭代物件（iterable）」與「迭代器（iterator）」。
# 2. iter() / next() 在底層其實呼叫哪些協議方法。
# 3. StopIteration 在手動遍歷時扮演的角色。

# 1. 迭代器協議的核心方法
items = [1, 2, 3]

# iter() 呼叫 __iter__()
# list 本身是可迭代物件；呼叫 iter(list) 會拿到一個「列表迭代器」。
it = iter(items)
print(f"迭代器: {it}")

# next() 呼叫 __next__()
# next() 每呼叫一次，就從迭代器取下一個值，並推進內部游標。
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 沒有更多元素時，擲出 StopIteration
# 這個例外不是錯誤狀態，而是 Python 用來表示「資料已取完」的正常訊號。
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
print("\n--- 常見可迭代物件 ---")

# 列表
# 列表可迭代，iter(列表) 會回傳 list_iterator。
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串
# 字串也是可迭代物件，會逐字元產生值。
print(f"字串 iter: {iter('abc')}")

# 字典
# 字典預設迭代的是 key，不是 value。
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案
import io

# 檔案物件也支援迭代，通常一次吐出一行文字。
f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# 3. 自訂可迭代物件
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 可迭代物件的責任：回傳一個迭代器。
        # 這裡把真正的遍歷狀態交給 CountDownIterator 管理。
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        # 迭代器通常會保存目前走到哪裡的狀態。
        self.current = start

    def __next__(self):
        # 當沒有下一個值時，必須拋出 StopIteration。
        if self.current <= 0:
            raise StopIteration
        # 先遞減再回傳，讓輸出序列為 start, start-1, ... , 1。
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
# for 迴圈內部會自動呼叫 iter() 與 next()，直到捕捉到 StopIteration 為止。
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1

# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表是可迭代物件，不是迭代器
# 也就是說它有 __iter__，但沒有直接提供 __next__。
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 列表的 iter() 返回迭代器
# 這個回傳物件才是可以被 next() 逐步消耗的對象。
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器本身就是可迭代物件
# 大多數迭代器的 __iter__ 會回傳自己，因此既是 iterable 也是 iterator。
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")


# 手動遍歷（章節 4.1 風格）
def manual_iter(items):
    # 這段等價於 for item in items: ... 的底層核心流程。
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
    # next(it, default) 不會拋例外，而是取完後回傳 default。
    # 這樣可以少寫 try/except，但要小心 default 不要和合法資料衝突。
    # 此範例資料是字串清單，用 None 當結束哨兵值是安全的。
    it = iter(items)
    while True:
        item = next(it, None)  # 預設值
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
