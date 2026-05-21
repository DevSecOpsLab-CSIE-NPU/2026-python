# U01. 陷阱！閉包與可變預設值
# 兩個「寫起來看似正確，但結果出乎意料」的 Python 坑
# 對應 Bloom's Taxonomy：理解（Understand）— 能解釋為什麼會出錯

# ── 陷阱 1：可變的預設值 ─────────────────────────────────
# 關鍵：函數的預設值只在「定義時」建立一次，之後每次呼叫都共用同一個物件

def add_to_cart(item, cart=[]):   # ← 這個 [] 只建立一次！
    # 每次呼叫若是沒給 cart，就會操作到同一個在記憶體裡的 list
    cart.append(item)
    return cart

print("=== 陷阱 1：可變預設值 ===")
print(add_to_cart("蘋果"))   # ['蘋果']
print(add_to_cart("香蕉"))   # ['蘋果', '香蕉']  ← 驚！不是 ['香蕉']
print(add_to_cart("葡萄"))   # ['蘋果', '香蕉', '葡萄']
# 原因：cart=[] 這個 list 在 def 時就建好了，三次呼叫都用同一個

print("\n--- 正確寫法：用 None 當預設值 ---")
def add_to_cart_safe(item, cart=None):
    # 檢查如果沒傳入 cart，就在函數內部建立一個全新的空 list，確保大家各自獨立
    if cart is None:
        cart = []   # ← 每次呼叫才建立新的 list
    cart.append(item)
    return cart

print(add_to_cart_safe("蘋果"))  # ['蘋果']
print(add_to_cart_safe("香蕉"))  # ['香蕉'] ← 各自獨立，正確！

# ── 陷阱 2：閉包的延遲綁定 ───────────────────────────────
# 關鍵：閉包記住的是「變數名稱」，不是「當下的值」
# 等迴圈跑完，i 已經是最後的值了

print("\n=== 陷阱 2：閉包延遲綁定 ===")
funcs = []
for i in range(5):
    # 這裡的 lambda 只記住「要回傳外層的變數 i」，但不會馬上把當下的數字存起來 (這叫延遲綁定)
    funcs.append(lambda: i)

print("你以為：", [0, 1, 2, 3, 4])
print("實際上：", [f() for f in funcs])  # [4, 4, 4, 4, 4]，全部都是 4！
# 原因：迴圈結束後 i=4，所有 lambda 去查 i，都查到 4

print("\n--- 正確寫法：用預設參數把值「複製」進來 ---")
funcs_ok = []
for i in range(5):
    # 透過預設參數 i=i，強制在每次迴圈時就把當下 i 的值「複製」並綁定給這個 lambda 的內部區域變數 i
    funcs_ok.append(lambda i=i: i)

print("修正後：", [f() for f in funcs_ok])  # [0, 1, 2, 3, 4] ✓

# ── nonlocal：在閉包裡修改外層的變數 ─────────────────────
# 閉包預設只能「讀取」外層變數
# 要修改外層變數，必須用 nonlocal 宣告

print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """回傳一個計數器函數，每次呼叫加 1"""
    count = start

    def counter():
        # 如果沒有這行 nonlocal，Python 看到 count += 1 (即 count = count + 1)
        # 會以為你要建立新的區域變數，導致找不到等號右邊的 count，引發 UnboundLocalError
        nonlocal count   # ← 宣告「我要修改外層的 count，不是建新的」
        count += 1
        return count

    return counter

c1 = make_counter()
c2 = make_counter(10)
print(c1(), c1(), c1())   # 1 2 3
print(c2(), c2())         # 11 12
print(c1())               # 4（c1 和 c2 是各自獨立的計數器）

# ── 實際應用：用閉包做「一次性」工具函數 ────────────────
# CPE 中偶爾需要「記住狀態」但又不想寫整個 class

print("\n=== 閉包應用：記住已走過的節點 ===")
def make_visit_tracker():
    # 狀態變數 visited 被封裝在閉包裡，外部無法直接竄改，達到了類似 class 的封裝效果
    visited = set()

    def visit(node):
        # 其實這裡對 set 做 .add() 是改變內部狀態，並未重新賦值 (visited = ...)，
        # 所以即使不寫 nonlocal 也完全合法。不過加上 nonlocal 可以更明確表達我們要存取外層變數。
        nonlocal visited
        if node in visited:
            return False    # 已走過
        visited.add(node)
        return True         # 第一次走到

    return visit

visit = make_visit_tracker()
results = [visit(n) for n in [1, 2, 1, 3, 2, 4]]
print(results)  # [True, True, False, True, False, True]

# 記憶重點 ──────────────────────────────────────────────────
# 可變預設值陷阱 → 預設值用 None，函數內再建 [] 或 {}
# 閉包延遲綁定  → 用 lambda x=x: x 把值固定下來
# nonlocal      → 要「修改」外層變數時才需要，只「讀取」不用
