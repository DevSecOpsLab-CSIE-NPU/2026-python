# Remember（記憶）- 迭代器基礎概念
# 本範例介紹 Python 中迭代器 (Iterator) 與可迭代物件 (Iterable) 的核心概念。

# ── 1. 迭代器協議的核心方法 ──────────────────────────────────
# 說明：Python 的迭代機制基於兩個內建函數：iter() 和 next()。
items = [1, 2, 3]

# iter() 函數會呼叫物件的 __iter__() 方法，將「可迭代物件」轉換為「迭代器」。
it = iter(items)
print(f"迭代器: {it}")

# next() 函數會呼叫迭代器的 __next__() 方法，逐一取出下一個元素。
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 當迭代器內已經沒有更多元素時，再次呼叫 next() 會擲出 StopIteration 例外，
# 這也是 for 迴圈判斷何時該停止的依據。
try:
    next(it)
except StopIteration:
    print("迭代結束!")

# ── 2. 常見可迭代物件 ────────────────────────────────────────
# 說明：Python 中許多內建的資料型態都是可迭代物件，可以使用 iter() 轉為迭代器。
print("\n--- 常見可迭代物件 ---")

# 列表 (List) 是一個可迭代物件
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串 (String) 也是一個可迭代物件，會逐字元迭代
print(f"字串 iter: {iter('abc')}")

# 字典 (Dictionary) 預設會迭代其鍵 (keys)
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案物件 (File object) 也是可迭代的，會逐行迭代
import io

f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")


# ── 3. 自訂可迭代物件 ────────────────────────────────────────
# 說明：要建立自訂的可迭代物件，需要實作 __iter__() 方法；
# 要建立自訂的迭代器，需要實作 __next__() 方法 (通常也包含 __iter__ 回傳自己)。

# CountDown 是一個「可迭代物件 (Iterable)」，因為它實作了 __iter__
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        # 必須回傳一個「迭代器」物件
        return CountDownIterator(self.start)


# CountDownIterator 是一個「迭代器 (Iterator)」，因為它實作了 __next__
class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        # 當條件滿足時停止迭代，擲出 StopIteration
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
# for 迴圈在背後會自動呼叫 iter(CountDown(3))，然後不斷呼叫 next() 直到 StopIteration
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1

# ── 4. 迭代器 vs 可迭代物件 ──────────────────────────────────
# 說明：釐清「可迭代物件 (Iterable)」與「迭代器 (Iterator)」的區別。
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表本身是「可迭代物件」(可以被 for 迴圈走訪)，但它不是「迭代器」(不能直接用 next() 呼叫)。
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 透過 iter() 轉換後，會產生一個專屬的「迭代器」物件來記錄當前走訪的狀態。
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 嚴格來說，正規的迭代器本身也應該實作 __iter__ (回傳自己)，所以它同時具備兩種身分。
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# ── 5. StopIteration 例外 ────────────────────────────────────
# 說明：示範如果不使用 for 迴圈，該如何手動安全地處理迭代過程。
print("\n--- StopIteration 用法 ---")


# 方法一：使用 try...except 手動捕獲 StopIteration (這正是 for 迴圈底層的運作方式)
def manual_iter(items):
    # 1. 取得迭代器
    it = iter(items)
    while True:
        try:
            # 2. 不斷取得下一個元素
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            # 3. 遇到 StopIteration 則結束迴圈
            break


manual_iter(["a", "b", "c"])


# 方法二：在 next() 中提供「預設值」，當迭代結束時會回傳預設值而不會擲出例外
def manual_iter_default(items):
    it = iter(items)
    while True:
        # 當迭代器耗盡時，回傳 None
        item = next(it, None)
        # 檢查是否達到結束條件
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
 