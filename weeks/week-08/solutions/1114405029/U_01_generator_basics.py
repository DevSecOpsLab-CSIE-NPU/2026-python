# Understand（理解）- 生成器概念


# =========================
# 1. 基本生成器（模擬 range，但支援浮點數）
# =========================
def frange(start, stop, step):
    # 初始化目前值
    x = start

    # 當 x 小於 stop 時持續產生
    while x < stop:
        # yield：
        # 1. 回傳 x 給呼叫者
        # 2. 函式「暫停」，保留目前狀態（x 的值）
        yield x

        # 下一次恢復執行時，從這行繼續
        x += step


# 將生成器轉成 list（會一次把所有值取出）
result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")


# =========================
# 2. 觀察生成器執行流程
# =========================
def countdown(n):
    # 注意：這行在「第一次 next()」時才會執行
    print(f"Starting countdown from {n}")

    while n > 0:
        # 每次 yield 一個值，並暫停
        yield n
        n -= 1

    # 當迴圈結束（n <= 0）後才會執行
    print("Done!")


print("\n--- 建立生成器 ---")

# 呼叫函式「不會執行內容」，只會回傳生成器物件
c = countdown(3)
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")

# 第一次 next()：
# -> 執行到第一個 yield，並印出 Starting...
print(f"next(c): {next(c)}")

# 第二次 next()：
# -> 從 yield 後繼續執行
print(f"next(c): {next(c)}")

# 第三次 next()：
print(f"next(c): {next(c)}")

# 第四次 next()：
# -> 進入 while 結束後，執行 print("Done!")
# -> 然後拋出 StopIteration
try:
    next(c)
except StopIteration:
    print("StopIteration!")


# =========================
# 3. 無限生成器（Fibonacci）
# =========================
def fibonacci():
    # 初始化前兩項
    a, b = 0, 1

    # 無限迴圈（生成器常見用法）
    while True:
        yield a

        # 同時更新 a, b（tuple unpacking）
        # a = b
        # b = a + b（舊的 a）
        a, b = b, a + b


print("\n--- Fibonacci 生成器 ---")

# 建立生成器
fib = fibonacci()

# 只取前 10 個（否則會無限跑）
for i in range(10):
    print(next(fib), end=" ")
print()


# =========================
# 4. yield from（委派生成器）
# =========================
def chain_iter(*iterables):
    # *iterables：可接收多個可迭代物件（tuple 形式）

    for it in iterables:
        # yield from：
        # 將「子迭代器」的元素逐一 yield 出來
        # 等價於：
        # for x in it:
        #     yield x
        yield from it


print("\n--- yield from 用法 ---")

# 將多個序列串接
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")


# =========================
# 5. 樹狀結構 + 深度優先搜尋（DFS）
# =========================
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []  # 存子節點

    def add_child(self, node):
        # 加入子節點
        self.children.append(node)

    def __iter__(self):
        # 讓 Node 物件可以被 for 迴圈使用
        # 回傳 children 的迭代器
        return iter(self.children)

    def depth_first(self):
        # 先回傳自己（前序走訪）
        yield self

        # 對每個子節點做遞迴
        for child in self:
            # yield from 遞迴呼叫
            # 將 child.depth_first() 的所有結果展開
            yield from child.depth_first()


print("\n--- 樹的深度優先遍歷 ---")

# 建立樹結構
root = Node(0)
root.add_child(Node(1))
root.add_child(Node(2))
root.children[0].add_child(Node(3))
root.children[0].add_child(Node(4))

# DFS 走訪
for node in root.depth_first():
    print(node.value, end=" ")
print()


# =========================
# 6. 巢狀序列攤平（遞迴生成器）
# =========================
def flatten(items):
    for x in items:
        # hasattr(x, "__iter__")：
        # 判斷 x 是否為可迭代物件（list、tuple 等）

        # not isinstance(x, str)：
        # 排除字串（因為字串也是 iterable，但我們不想拆成字元）
        if hasattr(x, "__iter__") and not isinstance(x, str):
            # 如果是可迭代物件 → 遞迴展開
            yield from flatten(x)
        else:
            # 否則直接回傳元素
            yield x


print("\n--- 巢狀序列攤平 ---")

nested = [1, [2, [3, 4]], 5]

# 將巢狀結構轉成一維列表
print(f"展開: {list(flatten(nested))}")