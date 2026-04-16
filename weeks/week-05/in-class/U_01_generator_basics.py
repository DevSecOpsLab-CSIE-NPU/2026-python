# Understand（理解）- 生成器概念
# 生成器是一種延遲生成值的可迭代物件，適合處理大量資料或無限序列


def frange(start, stop, step):
    # 自定義浮點數範圍生成器，類似 range() 但可支援浮點數步進
    x = start
    while x < stop:
        yield x  # 每次產生一個值並暫停函數執行
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    # 倒數生成器：每次返回目前的計數值，直到 0 為止
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n  # 暫停並傳回 n，下一次從此處繼續
        n -= 1
    print("Done!")  # 生成器結束後會執行此處


print("\n--- 建立生成器 ---")
c = countdown(3)
print(f"生成器物件: {c}")  # 尚未執行，只建立生成器物件

print("\n--- 逐步迭代 ---")
print(f"next(c): {next(c)}")  # 取得第一個 yield 值
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    next(c)  # 生成器已執行完畢，會拋出 StopIteration
except StopIteration:
    print("StopIteration!")


def fibonacci():
    # 無限 Fibonacci 數列生成器
    a, b = 0, 1
    while True:
        yield a  # 依序輸出 Fibonacci 數
        a, b = b, a + b  # 更新下一個數值


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()
for i in range(10):
    print(next(fib), end=" ")  # 取出前 10 個 Fibonacci 值
print()


def chain_iter(*iterables):
    # yield from 會將子可迭代物件中的元素逐一產出
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
        # 讓 Node 物件變成可迭代，迭代其子節點
        return iter(self.children)

    def depth_first(self):
        # 深度優先遍歷生成器：先產生自己，再遞迴產生子節點
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
    # 遞迴攤平巢狀可迭代物件，排除字串
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
