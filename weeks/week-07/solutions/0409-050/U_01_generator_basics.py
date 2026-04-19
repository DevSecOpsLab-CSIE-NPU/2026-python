# Understand（理解）- 生成器概念

# 核心概念：生成器函式 (Generator Function)
# 生成器函式是一種特殊的函式，它使用 `yield` 關鍵字來回傳一個「生成器 (Generator)」物件。
# 與普通函式不同，生成器函式在每次 `yield` 後會暫停執行，並保留其內部狀態，直到下次被要求產生值時才從上次暫停的地方繼續執行。
# 『語法』：
#   `def 函式名稱(參數):`
#       `...`
#       `yield 值` 
#       `...`
# 『用途』：
#   1. 建立一個可以「惰性求值 (Lazy Evaluation)」的序列，也就是「要一個才算一個」，而不是一次性產生所有結果並儲存在記憶體中。
#   2. 處理大量資料或無限序列時，可以大幅節省記憶體。
#   3. 實作協程 (coroutine) 等進階非同步操作。
# 『結果』：
#   呼叫生成器函式不會立即執行函式內的程式碼，而是回傳一個「生成器物件」。當你對這個生成器物件進行迭代（例如使用 `for` 迴圈或 `next()` 函式），函式內的程式碼才會開始執行，直到遇到 `yield` 語句。
#   這個 `frange` 函式模擬了 `range()` 函式，但可以處理浮點數步長。
def frange(start, stop, step):
    # 初始化變數 x 為起始值。
    x = start
    # 迴圈條件：當 x 小於停止值時繼續執行。
    while x < stop:
        # `yield x`：這是生成器函式的核心。它會暫停函式的執行，並回傳 x 的值。
        # 下次呼叫 `next()` 時，函式會從這裡繼續執行。
        yield x
        # 將 x 增加步長。
        x += step

# 呼叫 `frange` 函式，它會回傳一個生成器物件。
# `list()` 函式會迭代這個生成器物件，將其產生所有值收集成一個串列。
result = list(frange(0, 2, 0.5))
# 印出結果。
print(f"frange(0, 2, 0.5): {result}")

# 核心概念：生成器生命週期與 `next()` 函式
# 這個 `countdown` 函式展示了生成器從啟動、產生值到結束的整個過程，以及 `next()` 函式如何驅動生成器。
def countdown(n):
    # 函式開始執行時，會先印出這行。
    print(f"Starting countdown from {n}")
    # 迴圈條件：當 n 大於 0 時繼續產生值。
    while n > 0:
        # 產生當前的 n 值。
        yield n
        # 將 n 減 1。
        n -= 1
    # 當迴圈結束（n 不再大於 0）時，印出這行。
    print("Done!")

print("\n--- 建立生成器 ---")
# 呼叫 `countdown(3)`，這會建立一個生成器物件 `c`，但函式內部的程式碼（包括第一個 `print`）還不會執行。
c = countdown(3)
# 印出生成器物件本身，可以看到它的記憶體位址。
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
# 第一次呼叫 `next(c)`：
#   - `countdown` 函式開始執行。
#   - 印出 "Starting countdown from 3"。
#   - 進入 `while` 迴圈，`n` 是 3。
#   - `yield 3`，函式暫停，回傳 3。
print(f"next(c): {next(c)}")
# 第二次呼叫 `next(c)`：
#   - 函式從上次暫停的地方（`yield n` 之後）繼續執行。
#   - `n -= 1`，`n` 變成 2。
#   - 再次進入 `while` 迴圈，`n` 是 2。
#   - `yield 2`，函式暫停，回傳 2。
print(f"next(c): {next(c)}")
# 第三次呼叫 `next(c)`：
#   - 函式從上次暫停的地方繼續執行。
#   - `n -= 1`，`n` 變成 1。
#   - 再次進入 `while` 迴圈，`n` 是 1。
#   - `yield 1`，函式暫停，回傳 1。
print(f"next(c): {next(c)}")

# 核心概念：StopIteration 例外
# 當生成器已經沒有更多值可以產生時，再次呼叫 `next()` 會觸發 `StopIteration` 例外。
# `for` 迴圈在內部就是透過捕獲這個例外來判斷何時停止迭代的。
try:
    # 第四次呼叫 `next(c)`：
    #   - 函式從上次暫停的地方繼續執行。
    #   - `n -= 1`，`n` 變成 0。
    #   - `while n > 0` 條件不成立，迴圈結束。
    #   - 印出 "Done!"。
    #   - 函式執行完畢，沒有更多的 `yield` 語句，所以會觸發 `StopIteration` 例外。
    next(c)
except StopIteration:
    # 捕獲到 `StopIteration` 例外，印出訊息。
    print("StopIteration!")

# 核心概念：無限序列生成器
# 生成器可以設計成產生無限序列，因為它們是惰性求值的，不會一次性佔用所有記憶體。
# 這個 `fibonacci` 函式會產生費波那契數列。
def fibonacci():
    # 初始化費波那契數列的兩個起始值。
    a, b = 0, 1
    # 無限迴圈，表示這個生成器可以無限地產生費波那契數。
    while True:
        # 產生當前的 a 值。
        yield a
        # 更新 a 和 b 的值，計算下一個費波那契數。
        a, b = b, a + b

print("\n--- Fibonacci 生成器 ---")
# 建立費波那契生成器物件。
fib = fibonacci()
# 使用 `for` 迴圈迭代生成器，這裡只取前 10 個數。
for i in range(10):
    # 每次呼叫 `next(fib)` 取得下一個費波那契數並印出。
    print(next(fib), end=" ")
# 印出換行。
print()

# 核心概念：`yield from` 語法
# `yield from` 語法用於將生成器的控制權委託給另一個生成器或可迭代物件。
# 它可以簡化生成器函式中處理子生成器或迭代器的邏輯，讓程式碼更簡潔。
# 『語法』：`yield from 可迭代物件`
# 『用途』：
#   1. 簡化生成器鏈接 (chaining generators) 的程式碼。
#   2. 處理遞迴生成器。
#   3. 在協程 (coroutine) 中實現委託。
# 『結果』：
#   當 `yield from` 被執行時，它會直接將子生成器或可迭代物件產生所有值傳遞給呼叫者，直到子生成器耗盡或完成。
def chain_iter(*iterables):
    # 遍歷傳入的所有可迭代物件。
    for it in iterables:
        # `yield from it` 會將 `it` 這個可迭代物件中的所有元素一個接一個地產生出來。
        # 相當於 `for item in it: yield item`。
        yield from it

print("\n--- yield from 用法 ---")
# 呼叫 `chain_iter` 函式，傳入三個串列。
# `list()` 會收集 `chain_iter` 生成器產生所有值。
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
# 印出結果。
print(f"chain_iter: {result}")

# 核心概念：生成器與物件導向 (Generator with Object-Oriented Programming)
# 生成器可以作為類別的方法，用於實現複雜資料結構（如樹）的遍歷。
# 這個 `Node` 類別代表樹狀結構中的一個節點，並實作了深度優先遍歷的生成器方法。
class Node:
    # 節點的初始化方法。
    def __init__(self, value):
        # 節點的值。
        self.value = value
        # 儲存子節點的串列。
        self.children = []

    # 新增子節點的方法。
    def add_child(self, node):
        self.children.append(node)

    # 實作 `__iter__` 方法，讓 `Node` 物件本身成為一個可迭代物件，
    # 迭代時會遍歷其子節點。
    def __iter__(self):
        return iter(self.children)

    # 核心概念：深度優先遍歷生成器 (Depth-First Traversal Generator)
    # 這個方法是一個生成器，用於以深度優先的方式遍歷樹中的所有節點。
    def depth_first(self):
        # 首先產生當前節點本身。
        yield self
        # 遍歷當前節點的所有子節點。
        for child in self:
            # 遞迴呼叫子節點的 `depth_first` 方法，並使用 `yield from` 將子生成器產生所有值委託給當前生成器。
            # 這確保了深度優先的順序：先遍歷完一個子樹，再遍歷下一個子樹。
            yield from child.depth_first()

print("\n--- 樹的深度優先遍歷 ---")
# 建立根節點。
root = Node(0)
# 新增子節點。
root.add_child(Node(1))
root.add_child(Node(2))
# 為第一個子節點新增子節點，建立更深的層次。
root.children[0].add_child(Node(3))
root.children[0].add_child(Node(4))

# 使用 `for` 迴圈遍歷 `root` 節點的深度優先生成器。
for node in root.depth_first():
    # 印出每個遍歷到的節點的值。
    print(node.value, end=" ")
# 印出換行。
print()

# 核心概念：巢狀序列攤平生成器 (Flattening Nested Sequences Generator)
# 這個 `flatten` 函式是一個生成器，用於將任意層次的巢狀序列（例如串列中包含串列）攤平為一個單一的序列。
def flatten(items):
    # 遍歷傳入的序列中的每個元素。
    for x in items:
        # 檢查元素 `x` 是否是可迭代物件，並且不是字串。
        # `hasattr(x, "__iter__")` 檢查 `x` 是否有 `__iter__` 方法，表示它是可迭代的。
        # `not isinstance(x, str)` 是為了避免將字串（例如 'abc'）也當作可迭代物件而逐字元攤平。
        if hasattr(x, "__iter__") and not isinstance(x, str):
            # 如果是巢狀的可迭代物件（且不是字串），則遞迴呼叫 `flatten`，並使用 `yield from` 將其產生所有值委託給當前生成器。
            yield from flatten(x)
        else:
            # 如果不是巢狀的可迭代物件（或者它是字串），則直接產生這個元素。
            yield x

print("\n--- 巢狀序列攤平 ---")
# 範例巢狀串列。
nested = [1, [2, [3, 4]], 5]
# 呼叫 `flatten` 函式，並使用 `list()` 將其產生所有值收集成一個串列。
print(f"展開: {list(flatten(nested))}")
