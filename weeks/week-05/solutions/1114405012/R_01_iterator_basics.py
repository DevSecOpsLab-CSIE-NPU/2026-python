# Remember（記憶）- 迭代器基礎概念

# 1. 迭代器協議的核心方法
# Python 的 for 迴圈底層其實就是：
# 1) 先呼叫 iter(obj) 取得迭代器
# 2) 持續呼叫 next(it) 取下一個值
# 3) 收到 StopIteration 就結束
items = [1, 2, 3]

# iter() 呼叫 __iter__()
it = iter(items)
print(f"原始資料: {items}")
print(f"透過 iter() 取得的迭代器物件: {it}")

# next() 呼叫 __next__()
print(f"第一次 next(it): {next(it)}")  # 1
print(f"第二次 next(it): {next(it)}")  # 2
print(f"第三次 next(it): {next(it)}")  # 3

# 沒有更多元素時，擲出 StopIteration
try:
    next(it)
except StopIteration:
    print("沒有更多元素，觸發 StopIteration，迭代結束")

# 2. 常見可迭代物件
print("\n--- 常見可迭代物件 ---")

# 列表
print(f"列表可被 iter() 轉成迭代器: {iter([1, 2, 3])}")

# 字串
print(f"字串可被 iter() 轉成迭代器: {iter('abc')}")

# 字典
print(f"字典可被 iter() 轉成迭代器: {iter({'a': 1, 'b': 2})}")

# 檔案
import io

f = io.StringIO("line1\nline2\nline3")
print(f"檔案物件也可迭代（逐行讀取）: {iter(f)}")


# 3. 自訂可迭代物件
# CountDown 只負責回傳迭代器（__iter__）。
# 真正的走訪邏輯放在 CountDownIterator 的 __next__。
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountDownIterator(self.start)


class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        # current 小於等於 0 代表沒有可回傳的值，必須拋出 StopIteration。
        if self.current <= 0:
            raise StopIteration
        # 先遞減再回傳，讓輸出變成 start, start-1, ... , 1
        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
print("CountDown(3) 逐次取值結果:", end=" ")
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1

# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表是可迭代物件，不是迭代器
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")
print(f"  是否有 __iter__? {'__iter__' in dir(my_list)}")
print(f"  是否有 __next__? {'__next__' in dir(my_list)}")

# 列表的 iter() 返回迭代器
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")
print(f"  是否有 __iter__? {'__iter__' in dir(my_iter)}")
print(f"  是否有 __next__? {'__next__' in dir(my_iter)}")

# 迭代器本身就是可迭代物件
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")

# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")


# 手動遍歷（章節 4.1 風格）
def manual_iter(items):
    print("手動迭代示範（try/except StopIteration）")
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
    print("手動迭代示範（next(it, 預設值)）")
    it = iter(items)
    while True:
        item = next(it, None)  # 預設值
        if item is None:
            print("已取得預設值 None，代表迭代完成")
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
