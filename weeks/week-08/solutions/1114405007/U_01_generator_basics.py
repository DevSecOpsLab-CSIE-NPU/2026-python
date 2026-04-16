"""Week 05 in-class: 生成器基礎（標準版）

把教學腳本改為函式化設計，讓每個概念都可以被測試。
"""


def frange(start, stop, step):
    """浮點數版本的 range，逐步產生數值。"""
    if step <= 0:
        raise ValueError("step 必須大於 0")

    x = start
    while x < stop:
        yield x
        x += step


def countdown(n):
    """從 n 倒數到 1。"""
    while n > 0:
        yield n
        n -= 1


def fibonacci():
    """無限 Fibonacci 生成器。"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def chain_iter(*iterables):
    """把多個可迭代物件串接成一條序列。"""
    for it in iterables:
        yield from it


class Node:
    """簡單樹節點，支援深度優先走訪。"""

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        return iter(self.children)

    def depth_first(self):
        # 先回傳自己，再遞迴走訪所有子節點。
        yield self
        for child in self:
            yield from child.depth_first()


def flatten(items):
    """遞迴攤平巢狀序列（字串除外）。"""
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


def demo():
    """示範輸出，維持原始教材可讀性。"""
    print(f"frange(0, 2, 0.5): {list(frange(0, 2, 0.5))}")
    print(f"countdown(3): {list(countdown(3))}")

    fib = fibonacci()
    first_ten = [next(fib) for _ in range(10)]
    print(f"fibonacci 前 10 項: {first_ten}")

    print(f"chain_iter: {list(chain_iter([1, 2], [3, 4], [5, 6]))}")

    root = Node(0)
    root.add_child(Node(1))
    root.add_child(Node(2))
    root.children[0].add_child(Node(3))
    root.children[0].add_child(Node(4))
    print("depth_first:", [node.value for node in root.depth_first()])

    nested = [1, [2, [3, 4]], 5]
    print(f"flatten: {list(flatten(nested))}")


if __name__ == "__main__":
    demo()
