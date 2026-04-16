"""Understand（理解）- 生成器概念

本檔案示範 Python 生成器（generator）的常見用法：
1. 用 yield 逐步產生資料（不一次建立完整列表）
2. 用 next() 手動推進生成器
3. 用 yield from 串接多個可迭代物件
4. 在樹狀結構中做深度優先遍歷（DFS）
5. 透過遞迴將巢狀序列攤平

重點觀念：
- 生成器會保留執行狀態，下一次迭代可從上次暫停位置繼續。
- 相比一次建立整包資料，生成器更省記憶體，特別適合大資料流。
"""


def frange(start, stop, step):
    """浮點版本的 range。

    與 range 不同，這裡允許 step 是浮點數，並透過 yield
    一次產生一個值。
    """
    x = start
    while x < stop:
        # 回傳目前值並暫停函式，等待下一次迭代再繼續
        yield x
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    """倒數生成器：從 n 倒數到 1。"""
    # 注意：這行會在第一次 next() 時才印出（惰性執行）
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    # 當 while 結束後，生成器自然結束
    print("Done!")


print("\n--- 建立生成器 ---")
# 這裡只建立生成器物件，尚未開始執行 countdown 內容
c = countdown(3)
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    # 再 next 一次會觸發生成器結束，拋出 StopIteration
    next(c)
except StopIteration:
    print("StopIteration!")


def fibonacci():
    """無限 Fibonacci 生成器。"""
    a, b = 0, 1
    while True:
        yield a
        # 一次更新兩個變數：下一輪 (a, b) 變成 (b, a+b)
        a, b = b, a + b


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()
# 雖然是無限生成器，但我們只取前 10 個值
for i in range(10):
    print(next(fib), end=" ")
print()


def chain_iter(*iterables):
    """把多個可迭代物件串成單一迭代序列。"""
    for it in iterables:
        # yield from 等價於：for x in it: yield x
        yield from it


print("\n--- yield from 用法 ---")
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")


class Node:
    """簡單樹節點：每個節點有 value 與 children。"""

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        # 讓 Node 可以被 for 迴圈直接迭代其子節點
        return iter(self.children)

    def depth_first(self):
        """深度優先遍歷（先拜訪自己，再遞迴拜訪子節點）。"""
        # 先輸出自己（前序遍歷）
        yield self
        for child in self:
            # 把每個子樹的遍歷結果接到目前序列後面
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
    """遞迴攤平巢狀可迭代結構（字串除外）。"""
    for x in items:
        # 若 x 是可迭代物件且不是字串，遞迴展開
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            # 基本元素直接輸出
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
