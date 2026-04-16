# Understand（理解）- 生成器概念


def frange(start, stop, step):
    # 以 yield 實作浮點版本 range：每次產生一個值，不一次建立完整清單
    x = start
    while x < stop:
        yield x
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    # 觀察生成器執行時機：只有在 next() 時才會往下跑
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Done!")


print("\n--- 建立生成器 ---")
# 呼叫函式時只會得到生成器物件，函式本體尚未完整執行
c = countdown(3)
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
# 每次 next(c) 只推進到下一個 yield
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    # 資料耗盡後會拋出 StopIteration
    next(c)
except StopIteration:
    print("StopIteration!")


def fibonacci():
    # 無窮生成器：每次只算下一個 Fibonacci 值
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
    # yield from 可把子迭代器內容直接往外轉送
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
        # 讓 Node 可直接被 for 迭代其子節點
        return iter(self.children)

    def depth_first(self):
        # 深度優先：先回傳自己，再遞迴回傳每個子樹
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
    # 遞迴攤平巢狀可迭代物件，但字串視為原子值不再拆解
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
