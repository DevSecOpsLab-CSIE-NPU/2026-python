# Understand（理解）- 生成器概念

# frange 範例：模擬 float 範圍產生器
# 這個生成器會依照 step 返回連續數值

def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


# countdown 生成器：每次 yield 一個倒數值
# next() 呼叫時才會繼續執行

def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Done!")


print("\n--- 建立生成器 ---")
c = countdown(3)
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    next(c)
except StopIteration:
    # 生成器耗盡後會丟出 StopIteration
    print("StopIteration!")


# Fibonacci 生成器：無限產生 Fibonacci 數列

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()
for i in range(10):
    print(next(fib), end=" ")
print()


# chain_iter 範例：串接多個可疊代物件
# yield from 會一次吐出子序列中的每個元素

def chain_iter(*iterables):
    for it in iterables:
        yield from it


print("\n--- yield from 用法 ---")
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")


# 節點類別，實作可疊代迭代子節點
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        return iter(self.children)

    def depth_first(self):
        # 深度優先遍歷，先 yield 自己，再遞迴子節點
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


# flatten 生成器：遞迴展開巢狀可疊代物件
# 遇字串時視為原子元素，不再展開

def flatten(items):
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
