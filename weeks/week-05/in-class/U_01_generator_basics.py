# Understand（理解）- 生成器概念
#
# 這份範例示範：
# 1. 什麼是生成器（generator）
# 2. yield 如何一個一個產生資料
# 3. next() 如何逐步取值
# 4. yield from 如何委派給其他可迭代物件
# 5. 生成器在樹狀走訪與巢狀資料展平中的實際應用


def frange(start, stop, step):
    """像 range() 一樣逐步產生數字，但支援浮點數。"""
    x = start
    while x < stop:
        # 把目前的 x 交出去，函式狀態會暫停在這一行
        yield x
        # 下一次有人再取值時，會從這裡繼續執行
        x += step


# list(...) 會把生成器裡的所有值全部取出，轉成串列方便觀察
result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


def countdown(n):
    """從 n 開始倒數到 1。"""
    # 這行只有在真正開始迭代生成器時才會被執行
    print(f"Starting countdown from {n}")
    while n > 0:
        # 每次產生目前的倒數值
        yield n
        n -= 1
    # 當 while 結束時，代表生成器沒有更多資料了
    print("Done!")


print("\n--- 建立生成器 ---")
# 呼叫 countdown(3) 不會立刻跑完整個函式，
# 只會得到一個生成器物件
c = countdown(3)
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
# 每呼叫一次 next(c)，生成器就往前執行到下一個 yield
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    # 當資料取完後，再 next() 就會丟出 StopIteration
    next(c)
except StopIteration:
    print("StopIteration!")


def fibonacci():
    """無限產生 Fibonacci（費波那契）數列。"""
    a, b = 0, 1
    while True:
        # 先回傳目前值 a
        yield a
        # 再更新成下一組 Fibonacci 狀態
        a, b = b, a + b


print("\n--- Fibonacci 生成器 ---")
# 因為是無限生成器，所以通常搭配 for、next()、islice() 等方式限制取值數量
fib = fibonacci()
for i in range(10):
    print(next(fib), end=" ")
print()


def chain_iter(*iterables):
    """把多個可迭代物件串接成單一序列。"""
    for it in iterables:
        # yield from 會把 it 裡面的元素逐一交出去
        # 等同於：for x in it: yield x
        yield from it


print("\n--- yield from 用法 ---")
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")


class Node:
    """簡單的樹節點類別，用來示範生成器走訪樹狀結構。"""

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        """加入子節點。"""
        self.children.append(node)

    def __iter__(self):
        """讓 Node 可以直接被 for 迴圈迭代其 children。"""
        return iter(self.children)

    def depth_first(self):
        """使用深度優先搜尋（DFS）依序產生所有節點。"""
        # 先產生自己
        yield self
        # 再遞迴產生所有子孫節點
        for child in self:
            yield from child.depth_first()


print("\n--- 樹的深度優先遍歷 ---")
# 建立一棵簡單的樹：
#       0
#      / \
#     1   2
#    / \
#   3   4
root = Node(0)
root.add_child(Node(1))
root.add_child(Node(2))
root.children[0].add_child(Node(3))
root.children[0].add_child(Node(4))

# 走訪結果會是：0 1 3 4 2
for node in root.depth_first():
    print(node.value, end=" ")
print()


def flatten(items):
    """遞迴展開巢狀可迭代物件，字串除外。"""
    for x in items:
        # 如果 x 也是可迭代物件，而且不是字串，
        # 就繼續往下展開
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            # 如果是一般元素，就直接產生
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
