# ===================================================================
# U01. 陷阱！閉包與可變預設值
# 學生：賴俋勳 1114405041
# 日期：2026-05-21
# 主題：可變預設值陷阱、閉包延遲綁定陷阱、nonlocal
# ===================================================================
# 【學習心得】
#   這兩個陷阱是 Python 初學者最容易犯的錯誤之一。
#   陷阱1（可變預設值）：list/dict 預設值只建立一次，多次呼叫共用！
#     → 解法：預設值用 None，函數內再建立新的 [] 或 {}
#   陷阱2（閉包延遲綁定）：lambda 記住的是「變數名字」不是「值」！
#     → 解法：用 lambda i=i: i 把當下的值「複製」進預設值
#   nonlocal：在閉包裡「修改」外層變數時才需要（只讀不用）
# ===================================================================

# ── 陷阱 1：可變的預設值 ──────────────────────────────────
# 問題根源：函數的預設值在「def 執行時」只建立一次。
# 之後每次呼叫這個函數，都共用同一個預設值物件。
# 如果預設值是「可變的」（list, dict, set），就會被累積修改。

def add_to_cart(item, cart=[]):   # ← 這個 [] 只在 def 時建立一次！
    cart.append(item)
    return cart

print("=== 陷阱 1：可變預設值 ===")
print(add_to_cart("蘋果"))   # ['蘋果'] ← 看起來正確
print(add_to_cart("香蕉"))   # ['蘋果', '香蕉'] ← 驚！不是 ['香蕉']！
print(add_to_cart("葡萄"))   # ['蘋果', '香蕉', '葡萄'] ← 一直累積！
# 原因：cart=[] 這個 list 三次呼叫都用同一個物件，不斷被 append。

print("\n--- 正確寫法：用 None 當預設值 ---")
def add_to_cart_safe(item, cart=None):
    # None 是不可變的，每次呼叫若沒給 cart，就建立一個新的 []
    if cart is None:
        cart = []   # ← 每次呼叫才建立新的 list，互不影響
    cart.append(item)
    return cart

print(add_to_cart_safe("蘋果"))  # ['蘋果'] ← 新的 list
print(add_to_cart_safe("香蕉"))  # ['香蕉'] ← 又是新的 list，正確！

# ── 陷阱 2：閉包的延遲綁定 ────────────────────────────────
# 問題根源：lambda（和一般函數）的閉包記住的是「變數名稱」，
# 不是「建立當下的值」。等實際呼叫 lambda 時才去查變數的值。
# 迴圈結束後 i 的值是最後一個（這裡是 4），所有 lambda 都查到 4。

print("\n=== 陷阱 2：閉包延遲綁定 ===")
funcs = []
for i in range(5):
    funcs.append(lambda: i)   # ← lambda 記住「i」這個名字，不是當下的值

print("你以為：", [0, 1, 2, 3, 4])
print("實際上：", [f() for f in funcs])  # [4, 4, 4, 4, 4]，全部都是 4！
# 原因：呼叫 f() 時，i 已經是 4（迴圈跑完），所有 lambda 都查到 4。

print("\n--- 正確寫法：用預設參數把值「固定」下來 ---")
funcs_ok = []
for i in range(5):
    # lambda i=i: i → 利用「預設值在定義時求值」的特性
    # i=i：左邊是預設參數名字，右邊是當下 i 的值
    # 這樣每個 lambda 的預設值各自獨立（0, 1, 2, 3, 4）
    funcs_ok.append(lambda i=i: i)

print("修正後：", [f() for f in funcs_ok])  # [0, 1, 2, 3, 4] ✓

# ── nonlocal：在閉包裡修改外層的變數 ─────────────────────
# 閉包預設只能「讀取」外層變數。
# 如果要「修改」外層變數（例如 count += 1），
# 不加 nonlocal 會報 UnboundLocalError（Python 以為你在建立新的局部變數）。
# 加上 nonlocal count 告訴 Python：「我要修改的是外層那個 count」。

print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """
    工廠函數：每次呼叫回傳一個獨立的計數器函數。
    count 是外層的變數，counter() 閉包需要修改它，
    所以必須用 nonlocal 宣告。
    """
    count = start   # 外層變數，每個 make_counter() 呼叫都有自己的 count

    def counter():
        nonlocal count   # ← 告訴 Python：count 是外層的變數，不是新建的
        count += 1       # 修改外層的 count
        return count

    return counter   # 回傳函數物件（不是呼叫它）

c1 = make_counter()      # 從 0 開始
c2 = make_counter(10)    # 從 10 開始
print(c1(), c1(), c1())  # 1 2 3（c1 自己的 count）
print(c2(), c2())        # 11 12（c2 自己的 count，與 c1 獨立）
print(c1())              # 4（c1 繼續從上次的狀態）

# ── 實際應用：用閉包做「記住狀態」的工具函數 ─────────────
# CPE 中偶爾需要「記住已走過的節點」但又不想寫整個 class。

print("\n=== 閉包應用：記住已走過的節點 ===")
def make_visit_tracker():
    visited = set()   # 外層變數：記錄走過的節點集合

    def visit(node):
        nonlocal visited
        if node in visited:
            return False    # 已走過
        visited.add(node)
        return True         # 第一次走到

    return visit

visit = make_visit_tracker()
results = [visit(n) for n in [1, 2, 1, 3, 2, 4]]
print(results)  # [True, True, False, True, False, True]

# ─── 記憶重點 ──────────────────────────────────────────────
# 可變預設值陷阱 → 預設值用 None，函數內再建 [] 或 {}
# 閉包延遲綁定  → 用 lambda x=x: x 把值固定下來（利用預設值當快照）
# nonlocal      → 要「修改」外層變數時才需要，只「讀取」不用
