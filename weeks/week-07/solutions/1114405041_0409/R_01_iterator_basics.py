# Remember（記憶）- 迭代器基礎概念
# 本檔是 iterator 的入門示範，重點在理解：
# 1. 什麼是「可迭代物件」
# 2. 什麼是「迭代器」
# 3. iter() 與 next() 背後實際做了什麼
# 4. StopIteration 在手動遍歷中的角色

# 1. 迭代器協議的核心方法
items = [1, 2, 3]

# iter() 會向物件要求「請給我一個可以逐一取值的迭代器」。
# 對 list 來說，Python 會在背後呼叫它的 __iter__()。
it = iter(items)
print(f"迭代器: {it}")

# next() 則是向迭代器要求「請給我下一個元素」。
# 背後對應的是 __next__()。
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 當元素取完後，迭代器不會回傳 None，
# 而是丟出 StopIteration 來明確表示「資料已經結束」。
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# 2. 常見可迭代物件
print("\n--- 常見可迭代物件 ---")

# 只要能被 for 迴圈逐一取值的物件，通常就是可迭代物件。
# 常見例子包括 list、str、dict、file 物件等。

# 列表：每次取出一個元素
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串：每次取出一個字元
print(f"字串 iter: {iter('abc')}")

# 字典：預設逐一取出 key
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案：每次取出一行，是非常常見的 iterator 使用情境
import io

f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# 3. 自訂可迭代物件
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # CountDown 本身是「可迭代物件」，
        # 真正負責逐步吐值的是另一個迭代器物件 CountDownIterator。
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        # 當 current <= 0 時，代表倒數已經結束，
        # 必須丟出 StopIteration 通知迴圈停止。
        if self.current <= 0:
            raise StopIteration

        # 先把目前值記住，再往下減一。
        # 這裡用 current + 1 回傳，是因為前一行已經先做了遞減。
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
# for 迴圈看到 CountDown(3) 時，會先呼叫 iter()，
# 之後反覆呼叫 next() 直到收到 StopIteration。
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1

# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表本身可以被 iter() 建立出 iterator，
# 但 list 自己沒有 __next__()，所以它不是 iterator。
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 對列表呼叫 iter() 之後，得到的物件才是真正的 iterator。
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器通常同時具備：
# 1. __iter__()，因此它自己也能被 for 使用
# 2. __next__()，因此它能持續產生下一個值
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")


# 手動遍歷（章節 4.1 風格）
# 這段程式等於把 for 迴圈背後在做的事情手動攤開來寫。
def manual_iter(items):
    it = iter(items)
    while True:
        try:
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            # 一旦收到 StopIteration，就代表資料已取完，跳出迴圈。
            break


manual_iter(["a", "b", "c"])


# 使用預設值的版本
# next(iterator, 預設值) 可以避免自己寫 try/except。
# 若 iterator 已耗盡，就直接回傳預設值，而不是拋出 StopIteration。
def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)  # 預設值
        if item is None:
            # 這裡用 None 當停止訊號。
            # 但要注意：若資料本身可能真的出現 None，
            # 就不適合用 None 當預設值，應改用其他專用標記。
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
