# ============================================================
# Understand（理解）- 生成器概念
# ============================================================
# 生成器（Generator）是一種特殊的迭代器，使用 yield 語句實現延遲計算。
# 核心特性：
#   1. 可以暫停執行並保存狀態（yield 語句）
#   2. 節省記憶體：不需一次性生成所有值
#   3. 支援無限序列
#   4. 透過 yield 語句定義
#
# 與普通函數的區別：
#   - 普通函數：呼叫時執行完整，用 return 返回單個值
#   - 生成器函數：呼叫時返回生成器物件，每次呼叫 next() 時執行到 yield 暫停

# ============================================================
# 1. 基本生成器：frange()
# ============================================================
# 這是一個範浮點數的生成器（Python range() 只支援整數）
def frange(start, stop, step):
    """生成浮點數數列的生成器。每次呼叫 next() 時產生下一個值。"""
    x = start
    while x < stop:
        # yield 將值返回給呼叫者，並暫停執行
        # 下次呼叫 next() 時將從這裡恢復，x 保持上一次的值
        yield x
        x += step
    # 函數結束時自動拋出 StopIteration


# frange() 返回一個生成器物件，不是列表
result = list(frange(0, 2, 0.5))  # 轉換為列表以查看所有值
print(f"frange(0, 2, 0.5): {result}")


# ============================================================
# 2. 生成器的狀態和控制流
# ============================================================
# 這個例子展示生成器如何暫停和恢復執行
def countdown(n):
    """倒數計時的生成器，展示執行流程。"""
    print(f"Starting countdown from {n}")  # 第一次呼叫 next() 時執行
    while n > 0:
        yield n  # 返回值，暫停執行
        # next() 恢復時從這裡開始
        n -= 1
    print("Done!")  # 最後一次 yield 後執行
    # 函數結束，下一次 next() 呼叫會拋出 StopIteration


print("\n--- 建立生成器 ---")
# countdown(3) 不會立即執行函數，而是返回一個生成器物件
c = countdown(3)
print(f"生成器物件: {c}")  # 此時函數還沒開始執行

print("\n--- 逐步迭代 ---")
# 每次呼叫 next() 都會使函數執行到下一個 yield
print(f"next(c): {next(c)}")  # 執行到第一個 yield，返回 3
print(f"next(c): {next(c)}")  # 恢復執行，n 遞減為 2，返回 2
print(f"next(c): {next(c)}")  # 恢復執行，n 遞減為 1，返回 1

try:
    # 現在 n = 0，迴圈條件不滿足，函數執行 print("Done!")
    # 然後結束，拋出 StopIteration
    next(c)
except StopIteration:
    print("StopIteration!")  # 生成器已耗盡



# ============================================================
# 3. 無限生成器：Fibonacci 數列
# ============================================================
# 這個例子展示生成器如何處理無限序列
def fibonacci():
    """斐波那契數列生成器，可以無限產生值。"""
    a, b = 0, 1  # 初始值
    while True:  # 無限迴圈
        yield a  # 返回當前值
        # 計算下一個值
        a, b = b, a + b  # 同時更新 a 和 b


print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()  # 建立無限生成器
# 即使生成器可以產生無限值，我們仍可以控制取得多少個
for i in range(10):
    print(next(fib), end=" ")  # 只取前 10 個值
print()


# ============================================================
# 4. yield from - 委派給子生成器
# ============================================================
# yield from 用於從另一個可迭代物件產生所有值
# 它是以下程式碼的簡寫：
#   for item in iterable:
#       yield item

def chain_iter(*iterables):
    """將多個可迭代物件連接，逐個產生所有元素。"""
    for it in iterables:
        # yield from it 等同於：
        # for item in it:
        #     yield item
        # 但 yield from 更簡潔且效率更高
        yield from it


print("\n--- yield from 用法 ---")
# chain_iter 接收多個列表並將它們合併為一個序列
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")  # 輸出：[1, 2, 3, 4, 5, 6]


# ============================================================
# 5. 生成器與遞迴：樹的深度優先遍歷
# ============================================================
# 生成器在處理遞迴時特別有用，因為能避免一次性建立整個列表

class Node:
    """樹節點類別。"""
    def __init__(self, value):
        self.value = value  # 節點值
        self.children = []  # 子節點列表

    def add_child(self, node):
        """加入子節點。"""
        self.children.append(node)

    def __iter__(self):
        """使節點可迭代，迭代其所有子節點。"""
        return iter(self.children)

    def depth_first(self):
        """深度優先遍歷生成器。
        
        使用遞迴和 yield from 實現深度優先搜尋（DFS）。
        優點：不需建立完整的樹結構列表，邊遍歷邊產生結果。
        """
        # 首先產生自己 this node
        yield self
        # 然後遞迴地產生所有子節點的內容
        for child in self:
            # 委派給子節點的 depth_first() 生成器
            # yield from 會逐一產生所有子孫節點
            yield from child.depth_first()


print("\n--- 樹的深度優先遍歷 ---")
# 建立一棵樹：
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

# 使用生成器遍歷（DFS 順序：0, 1, 3, 4, 2）
for node in root.depth_first():
    print(node.value, end=" ")
print()


# ============================================================
# 6. 遞迴生成器：巢狀序列攤平
# ============================================================
# 使用生成器和遞迴來展平嵌套列表

def flatten(items):
    """遞迴地攤平巢狀序列，生成所有非集合元素。"""
    for x in items:
        # 檢查 x 是否為可迭代物件（但字串除外）
        # 字串雖然可迭代，但通常視為原子值而非集合
        if hasattr(x, "__iter__") and not isinstance(x, str):
            # 如果 x 是列表/元組等，遞迴展平
            # yield from 會產生所有遞迴結果
            yield from flatten(x)
        else:
            # 如果 x 是標量值，直接產生
            yield x


print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]  # 嵌套列表
print(f"展開: {list(flatten(nested))}")  # 輸出：[1, 2, 3, 4, 5]
