# ==========================================
# 迭代器基礎概念 (Iterator Basics)
# ==========================================

# 1. 迭代器協議的核心方法 (The Iterator Protocol)
# ------------------------------------------
# Python 的迭代器主要由兩個方法組成：__iter__() 和 __next__()
items = [1, 2, 3]

# 使用 iter() 函式取得迭代器物件，這會呼叫該物件內部的 __iter__() 方法
it = iter(items)
print(f"迭代器物件: {it}")

# 使用 next() 函式取得下一個元素，這會呼叫迭代器內部的 __next__() 方法
print(f"第一個元素: {next(it)}")  # 輸出 1
print(f"第二個元素: {next(it)}")  # 輸出 2
print(f"第三個元素: {next(it)}")  # 輸出 3

# 當沒有更多元素可以回傳時，next() 會擲出 StopIteration 例外
try:
    next(it)
except StopIteration:
    print("迭代結束！(已補捉到 StopIteration)")


# 2. 常見的可迭代物件 (Iterable Objects)
# ------------------------------------------
# 許多 Python 內建物件都是「可迭代的」(Iterable)，代表它們可以產生迭代器
print("\n--- 常見可迭代物件範例 ---")

# 列表 (List)
print(f"列表 iter 類型: {type(iter([1, 2, 3]))}")

# 字串 (String)
print(f"字串 iter 類型: {type(iter('abc'))}")

# 字典 (Dictionary) - 預設迭代其 Key (鍵)
print(f"字典 iter 類型: {type(iter({'a': 1, 'b': 2}))}")

# 檔案物件 (File Object) - 檔案本身也是一種迭代器，逐行讀取
import io
f = io.StringIO("line1\nline2\nline3")
print(f"檔案物件 iter 類型: {type(iter(f))}")


# 3. 自訂可迭代物件與迭代器 (Custom Iterator)
# ------------------------------------------

# 代表「可迭代物件」的類別：負責實作 __iter__ 並回傳一個迭代器
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 每次呼叫 iter() 都回傳一個全新的迭代器實體
        return CountDownIterator(self.start)

# 代表「迭代器」的類別：負責實作 __next__ 邏輯
class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current <= 0:
            raise StopIteration  # 終止條件
        self.current -= 1
        return self.current + 1

print("\n--- 自訂倒數計時迭代器 ---")
# 當我們使用 for 迴圈時，背後會先呼叫 iter(CountDown(3))
# 然後反覆呼叫 next() 直到遇到 StopIteration
for i in CountDown(3):
    print(i, end=" ")  # 輸出: 3 2 1 


# 4. 迭代器 (Iterator) vs 可迭代物件 (Iterable)
# ------------------------------------------
print("\n\n--- 觀念釐清：迭代器 vs 可迭代物件 ---")

# 列表 (List) 是「可迭代物件」，但它本身不是「迭代器」
# (因為 List 只有 __iter__ 方法，沒有紀錄狀態的 __next__ 方法)
my_list = [1, 2, 3]
print(f"列表本身: 是可迭代物件 ✓, 是迭代器 ✗")

# 呼叫 iter(列表) 後返回的物件才是「迭代器」
my_iter = iter(my_list)
print(f"iter(列表) 後: 是可迭代物件 ✗, 是迭代器 ✓")

# 關鍵：根據協議，迭代器本身也必須實作 __iter__，並回傳自己
# 所以「迭代器一定是可迭代的」，但「可迭代物件不一定是迭代器」


# 5. StopIteration 與手動遍歷
# ------------------------------------------
print("\n--- 手動遍歷的實作方式 ---")

# 模擬 for 迴圈背後的運作機制：手動處理 StopIteration
def manual_iter(items):
    it = iter(items)  # 取得迭代器
    while True:
        try:
            item = next(it)
            print(f"取得元素: {item}")
        except StopIteration:
            # 遇到結束訊號，跳出迴圈
            break

manual_iter(["a", "b", "c"])


# 進階技巧：使用 next() 的預設值避免例外
# ------------------------------------------
def manual_iter_default(items):
    it = iter(items)
    while True:
        # next(iterator, default)
        # 如果迭代結束，它會回傳 None 而不是擲出例外
        item = next(it, None)
        if item is None:
            break
        print(f"取得元素: {item}")

print("\n使用 next(it, None) 預設值版本:")
manual_iter_default(["X", "Y", "Z"])