"""
U01. 生成器基礎概念。

這份範例整理：
1. `yield` 如何讓函式變成生成器。
2. 生成器如何逐步產生值，而不是一次建立完整列表。
3. `yield from` 如何把子迭代結果接到目前生成器。
4. 生成器在樹狀資料與巢狀資料展開中的用法。
"""


def frange(start, stop, step):
    """
    產生浮點數範圍。

    Python 內建的 `range()` 只能處理整數。
    這裡用 `yield` 逐次產生浮點數，避免一次建立整份列表。
    """

    value = start
    while value < stop:
        yield value
        value += step


# 只有在需要把結果全部列出來時，才轉成 list。
result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(number):
    """
    從 number 倒數到 1。

    函式中只要出現 `yield`，呼叫它時就不會立刻執行內容，
    而是先回傳一個生成器物件。
    """

    print(f"Starting countdown from {number}")
    while number > 0:
        yield number
        number -= 1
    print("Done!")


print("\n--- 建立生成器 ---")
counter = countdown(3)
print(f"生成器物件: {counter}")


print("\n--- 逐步迭代 ---")

# `next()` 每呼叫一次，生成器就執行到下一個 yield。
print(f"next(c): {next(counter)}")
print(f"next(c): {next(counter)}")
print(f"next(c): {next(counter)}")

# 生成器沒有更多資料時，會拋出 StopIteration。
try:
    next(counter)
except StopIteration:
    print("StopIteration!")


def fibonacci():
    """
    無限產生 Fibonacci 數列。

    這個生成器沒有結束條件，所以使用時要由外部控制取幾個值。
    """

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()

# 只取前 10 個值，避免無限迴圈。
for _ in range(10):
    print(next(fib), end=" ")
print()


def chain_iter(*iterables):
    """
    串接多個可迭代物件。

    `yield from iterable` 會把 iterable 中的每個元素逐一 yield 出去，
    比手動再寫一層 for 迴圈更簡潔。
    """

    for iterable in iterables:
        yield from iterable


print("\n--- yield from 用法 ---")
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")


class Node:
    """簡單的樹狀節點。"""

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        """新增子節點。"""
        self.children.append(node)

    def __iter__(self):
        """讓 Node 可以直接被 for 迴圈走訪子節點。"""
        return iter(self.children)

    def depth_first(self):
        """
        以深度優先順序走訪整棵樹。

        先 yield 自己，再把每個子節點的 depth_first 結果接上來。
        """

        yield self
        for child in self:
            yield from child.depth_first()


print("\n--- 樹的深度優先遍歷 ---")
root = Node(0)
root.add_child(Node(1))
root.add_child(Node(2))
root.children[0].add_child(Node(3))
root.children[0].add_child(Node(4))

for node in root.depth_first():
    print(node.value, end=" ")
print()


def flatten(items):
    """
    展開巢狀序列。

    若元素本身可迭代，而且不是字串，就遞迴展開；
    否則直接把元素 yield 出去。
    """

    for item in items:
        if hasattr(item, "__iter__") and not isinstance(item, str):
            yield from flatten(item)
        else:
            yield item


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
