"""
R01. 迭代器基礎概念。

這份範例整理：
1. 什麼是可迭代物件。
2. `iter()` 與 `next()` 各自扮演什麼角色。
3. 如何自訂一個能被 `for` 迴圈使用的迭代器。
4. `StopIteration` 在手動遍歷中的用途。
"""

import io


# ── 1. 迭代器協議的核心：iter() 與 next() ─────────────────
items = [1, 2, 3]

# `iter(items)` 會取得一個迭代器物件。
iterator = iter(items)
print(f"迭代器: {iterator}")

# `next(iterator)` 每呼叫一次，就往前取一個元素。
print(f"第一個: {next(iterator)}")
print(f"第二個: {next(iterator)}")
print(f"第三個: {next(iterator)}")

# 當沒有資料可取時，會丟出 StopIteration。
try:
    next(iterator)
except StopIteration:
    print("迭代結束!")


# ── 2. 常見的可迭代物件 ───────────────────────────────────
print("\n--- 常見可迭代物件 ---")

# 列表、字串、字典、檔案物件都可以被 iter() 包起來。
print(f"列表 iter: {iter([1, 2, 3])}")
print(f"字串 iter: {iter('abc')}")
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

fake_file = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(fake_file)}")


# ── 3. 自訂可迭代物件與迭代器 ─────────────────────────────
class CountDown:
    """可迭代物件：負責提供 iterator。"""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountDownIterator(self.start)


class CountDownIterator:
    """真正逐步產生值的迭代器。"""

    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current <= 0:
            raise StopIteration

        self.current -= 1
        return self.current + 1


print("\n--- 自訂迭代器 ---")
for value in CountDown(3):
    print(value, end=" ")


# ── 4. 迭代器與可迭代物件不是完全同一件事 ─────────────────
print("\n\n--- 迭代器 vs 可迭代物件 ---")

my_list = [1, 2, 3]
print("列表: 可迭代物件 ✓, 迭代器 ✗")

my_iter = iter(my_list)
print("iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器通常也能再次被 iter() 包，因為它本身就代表「目前遍歷到哪裡」。
print("迭代器: 可迭代物件 ✓, 迭代器 ✓")


# ── 5. 手動處理 StopIteration ────────────────────────────
def manual_iter(items):
    """最直接的手動遍歷寫法。"""

    iterator = iter(items)
    while True:
        try:
            item = next(iterator)
            print(f"取得: {item}")
        except StopIteration:
            break


manual_iter(["a", "b", "c"])


def manual_iter_default(items):
    """
    使用 `next(iterator, default)` 的寫法。

    這種寫法可以避免手動 try/except，
    但要自己決定一個不會和正常資料衝突的預設值。
    """

    iterator = iter(items)
    while True:
        item = next(iterator, None)
        if item is None:
            break
        print(f"取得: {item}")


print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
