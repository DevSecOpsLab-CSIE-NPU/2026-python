# Understand（理解）- 生成器概念
# 本檔案示範 Python 生成器的基本用法、延遲運算特性以及 yield 和 yield from 的應用。


def frange(start, stop, step):
    # 這是一個生成器函式，使用 yield 逐步產生浮點數序列
    x = start
    while x < stop:
        yield x
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    # 生成器可以在每次 yield 後暫停，保留函式內部狀態
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Done!")


print("\n--- 建立生成器 ---")
c = countdown(3)
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
# 呼叫 next() 會觸發生成器執行到下一個 yield
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    next(c)
except StopIteration:
    print("StopIteration!")


def fibonacci():
    # 無窮生成器，迴圈輸出費式數列
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()
for i in range(10):
    print(next(fib), end=" ")
print()


def chain_iter(*iterables):
    # yield from 會逐一取出內部可迭代物件的元素
    for it in iterables:
        yield from it


print("\n--- yield from 用法 ---")
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        # 讓 Node 物件可直接迭代子節點
        return iter(self.children)

    def depth_first(self):
        # 使用生成器遞迴輸出節點深度優先遍歷結果
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
    # 將巢狀序列遞迴攤平成一維序列
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
