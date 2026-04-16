# Understand（理解）- 生成器概念
#
# 生成器（generator）是一種「延遲產生資料」的迭代器：
# - 不會一次把所有結果放進記憶體
# - 每次迭代才產生下一個值
# - 特別適合大資料流、無限序列、或串接多步處理流程


def frange(start, stop, step):
    # frange: 浮點版本的 range。
    # 每次 yield 當前值，呼叫端要下一個值時再往下執行。
    x = start
    while x < stop:
        yield x
        x += step


result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    # 這裡可觀察生成器的執行時機：
    # print 只有在真正迭代到該段程式時才會發生。
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Done!")


print("\n--- 建立生成器 ---")
c = countdown(3)
# 目前只是建立生成器物件，還沒真正執行 countdown 內部邏輯。
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
# 每次 next(c) 都會讓生成器從上次停住的位置繼續。
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    # 內容耗盡後會丟出 StopIteration，這是迭代結束的標準訊號。
    next(c)
except StopIteration:
    print("StopIteration!")


def fibonacci():
    # 無限生成器：理論上不會自己結束，需由外部控制取值次數。
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
    # yield from 可把子迭代器的元素「直接轉送」出去，
    # 省去手動巢狀 for 迴圈。
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
        # 讓 Node 可被 for 直接迭代其 children。
        return iter(self.children)

    def depth_first(self):
        # 深度優先（DFS）遞迴生成器：
        # 先回傳自己，再依序走訪每個子節點。
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
    # 遞迴攤平：如果元素本身可迭代（且不是字串），就繼續展開。
    # 字串雖然可迭代，但通常不希望被拆成單一字元，因此排除 str。
    for x in items:
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
