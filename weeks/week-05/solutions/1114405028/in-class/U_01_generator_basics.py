# Understand（理解）- 生成器概念
# 生成器是一種特殊的迭代器，可以用來產生序列，而不需要一次將所有值存儲在記憶體中

def frange(start, stop, step):
    # 自定義的浮點數範圍生成器，類似 range() 但支援浮點數
    x = start
    while x < stop:
        yield x  # yield 關鍵字使函數成為生成器，每次執行到這裡會暫停並返回值
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    # 倒數生成器，示範生成器的執行流程
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n  # 返回當前值，下次調用時從這裡繼續
        n -= 1
    print("Done!")  # 當生成器結束時執行


print("\n--- 建立生成器 ---")
c = countdown(3)
print(f"生成器物件: {c}")  # 這只會建立生成器物件，還沒有開始執行

print("\n--- 逐步迭代 ---")
print(f"next(c): {next(c)}")  # 開始執行生成器，直到第一個 yield
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    next(c)  # 嘗試獲取下一個值，但生成器已經結束
except StopIteration:
    print("StopIteration!")  # 會拋出 StopIteration 異常


def fibonacci():
    # 費波那契數列生成器，可以產生無限序列
    a, b = 0, 1
    while True:
        yield a  # 返回當前費波那契數
        a, b = b, a + b  # 更新下一個數


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()
for i in range(10):
    print(next(fib), end=" ")  # 打印前 10 個費波那契數
print()


def chain_iter(*iterables):
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
        return iter(self.children)

    def depth_first(self):
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
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
