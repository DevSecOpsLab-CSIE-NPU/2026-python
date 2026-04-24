# 理解（理解）- 生成器概念
# 這個檔案示範了 Python 中生成器的基本概念和用法。
# 生成器是一種特殊的迭代器，可以通過 yield 關鍵字暫停和恢復函數執行。

def frange(start, stop, step):
    # frange 函數：類似 range() 但支援浮點數
    # 生成器函數，使用 yield 返回值而不是 return
    x = start  # 起始值
    while x < stop:  # 當前值小於停止值時繼續
        yield x  # 暫停函數並返回當前值，下次呼叫時從這裡繼續
        x += step  # 增加步長

# 將生成器轉換為列表來查看所有值
result = list(frange(0, 2, 0.5))  # 生成 [0, 0.5, 1.0, 1.5]
print(f"frange(0, 2, 0.5): {result}")

def countdown(n):
    # countdown 生成器：倒數計時器
    print(f"Starting countdown from {n}")  # 印出開始訊息
    while n > 0:  # 當 n 大於 0 時繼續
        yield n  # 返回當前值
        n -= 1  # 減 1
    print("Done!")  # 迴圈結束後印出完成訊息

print("\n--- 建立生成器 ---")
c = countdown(3)  # 呼叫生成器函數，返回生成器物件（還沒有執行）
print(f"生成器物件: {c}")  # 印出生成器物件

print("\n--- 逐步迭代 ---")
# 使用 next() 逐步執行生成器
print(f"next(c): {next(c)}")  # 開始執行，印出 "Starting countdown from 3"，返回 3
print(f"next(c): {next(c)}")  # 繼續執行，返回 2
print(f"next(c): {next(c)}")  # 繼續執行，返回 1

try:
    next(c)  # 繼續執行，n 變為 0，迴圈結束，印出 "Done!"，然後擲出 StopIteration
except StopIteration:
    print("StopIteration!")  # 捕捉例外

def fibonacci():
    # Fibonacci 數列生成器：無限生成 Fibonacci 數列
    a, b = 0, 1  # 初始化前兩個數
    while True:  # 無限迴圈
        yield a  # 返回當前值
        a, b = b, a + b  # 更新為下一個數

print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()  # 創建 Fibonacci 生成器
for i in range(10):  # 取前 10 個數
    print(next(fib), end=" ")  # 印出數列
print()

def chain_iter(*iterables):
    # chain_iter 生成器：將多個可迭代物件鏈接起來
    for it in iterables:  # 遍歷每個可迭代物件
        yield from it  # 將子迭代器的所有值 yield 出來

print("\n--- yield from 用法 ---")
# yield from 用於委派給子生成器或可迭代物件
result = list(chain_iter([1, 2], [3, 4], [5, 6]))  # 鏈接三個列表
print(f"chain_iter: {result}")

class Node:
    # Node 類：樹節點
    def __init__(self, value):
        self.value = value  # 節點值
        self.children = []  # 子節點列表

    def add_child(self, node):
        self.children.append(node)  # 添加子節點

    def __iter__(self):
        return iter(self.children)  # 使節點可迭代，返回子節點的迭代器

    def depth_first(self):
        # 深度優先遍歷生成器
        yield self  # 返回當前節點
        for child in self:  # 遍歷子節點
            yield from child.depth_first()  # 遞歸遍歷子樹

print("\n--- 樹的深度優先遍歷 ---")
root = Node(0)  # 創建根節點
root.add_child(Node(1))  # 添加子節點 1
root.add_child(Node(2))  # 添加子節點 2
root.children[0].add_child(Node(3))  # 給節點 1 添加子節點 3
root.children[0].add_child(Node(4))  # 給節點 1 添加子節點 4

for node in root.depth_first():  # 深度優先遍歷
    print(node.value, end=" ")  # 印出節點值
print()

def flatten(items):
    # flatten 生成器：將巢狀序列攤平
    for x in items:  # 遍歷每個元素
        if hasattr(x, "__iter__") and not isinstance(x, str):  # 如果是可迭代物件且不是字串
            yield from flatten(x)  # 遞歸攤平子序列
        else:
            yield x  # 返回元素本身

print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]  # 巢狀列表
print(f"展開: {list(flatten(nested))}")  # 攤平為 [1, 2, 3, 4, 5]