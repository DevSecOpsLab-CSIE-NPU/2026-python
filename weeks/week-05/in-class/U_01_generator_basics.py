# Understand（理解）- 生成器概念
#
# 中文詳解：
# 1) 什麼是生成器（generator）？
#    - 透過函式中的 yield 產生「可逐步產出資料」的物件。
#    - 和一次建立完整 list 不同，生成器是「需要時才算下一個值」。
#
# 2) 生成器的優點
#    - 省記憶體：不必一次把所有結果放進記憶體。
#    - 可處理大型或無限序列：例如無限 Fibonacci。
#
# 3) 執行特性
#    - 每次 next() 會執行到下一個 yield 並暫停。
#    - 區域變數狀態會被保留，下一次 next() 可從暫停點繼續。
#    - 沒有更多值時會拋出 StopIteration。


def frange(start, stop, step):
    # 類似 range，但可處理浮點步進
    x = start
    while x < stop:
        yield x
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    # 示範：生成器建立時不會立刻執行，直到第一次 next() 才開始
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
    # 值已取完時會進入這裡
    print("StopIteration!")


def fibonacci():
    # 無限序列生成器：只在被 next() 時才產生下一項
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
    # yield from 會把子可迭代物件的值直接轉交出去
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
        # 深度優先（DFS）遞迴走訪
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
    # 遞迴攤平巢狀序列；字串視為單一值，不再往下拆字元
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")


# 小提醒：生成器通常只能走訪一次；若已耗盡，需重新建立新的生成器物件。
