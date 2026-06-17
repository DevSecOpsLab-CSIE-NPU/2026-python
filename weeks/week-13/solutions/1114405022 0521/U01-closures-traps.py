# U01. 陷阱！閉包與可變預設值
# 兩個「寫起來看似正確，但結果出乎意料」的 Python 坑
# 對應 Bloom's Taxonomy：理解（Understand）— 能解釋為什麼會出錯

# ── 陷阱 1：可變的預設值 ─────────────────────────────────
# 關鍵：函數的預設值只在「定義時」建立一次，之後每次呼叫都共用同一個物件

def add_to_cart(item, cart=[]):   # ← 這個 []（空列表）只建立一次！
    """
    有陷阱的購物車函數
    預設值 [] 在函數定義時就被建立，之後每次呼叫都共用同一個 list
    """
    cart.append(item)   # 在 cart 列表末端加入新項目
    return cart         # 回傳 cart 列表

print("=== 陷阱 1：可變預設值 ===")
print(add_to_cart("蘋果"))   # ['蘋果'] — 第一次呼叫，cart = []
print(add_to_cart("香蕉"))   # ['蘋果', '香蕉']  ← 驚！不是 ['香蕉']
print(add_to_cart("葡萄"))   # ['蘋果', '香蕉', '葡萄']
# 原因：cart=[] 這個 list 在 def 時就建好了，三次呼叫都用同一個
# 第一次加入蘋果後 cart = ['蘋果']
# 第二次加入香蕉時 cart 還是同一個，變成 ['蘋果', '香蕉']
# 第三次變成 ['蘋果', '香蕉', '葡萄']

print("\n--- 正確寫法：用 None 當預設值 ---")
def add_to_cart_safe(item, cart=None):
    """
    安全的購物車函數
    用 None 當預設值，在函數內部每次建立新的 list
    """
    if cart is None:       # 如果沒有傳入 cart
        cart = []   # ← 每次呼叫才建立新的 list（安全！）
    cart.append(item)      # 在 cart 列表末端加入新項目
    return cart            # 回傳 cart 列表

print(add_to_cart_safe("蘋果"))  # ['蘋果'] — 第一次建立新的 []
print(add_to_cart_safe("香蕉"))  # ['香蕉'] — 第二次又建立新的 []，各自獨立，正確！

# ── 陷阱 2：閉包的延遲綁定 ───────────────────────────────
# 關鍵：閉包記住的是「變數名稱」，不是「當下的值」
# 等迴圈跑完，i 已經是最後的值了

print("\n=== 陷阱 2：閉包延遲綁定 ===")
funcs = []                    # 用來存放 lambda 函數的列表
for i in range(5):            # 迴圈 i 從 0 到 4
    funcs.append(lambda: i)   # ← lambda 記住「i」這個名字，不是值

print("你以為：", [0, 1, 2, 3, 4])
# 實際上：全部都是 4！
# 原因：迴圈結束後 i=4，所有 lambda 去查變數 i 時都查到 4
print("實際上：", [f() for f in funcs])  # [4, 4, 4, 4, 4]

print("\n--- 正確寫法：用預設參數把值「複製」進來 ---")
funcs_ok = []                    # 用來存放修正後的 lambda
for i in range(5):               # 迴圈 i 從 0 到 4
    # i=i 的意思是：將當下 i 的值（例如 0）作為預設參數
    # 預設參數在 lambda 定義時就決定了，不會受到後續 i 變化的影響
    funcs_ok.append(lambda i=i: i)   # ← i=i 把當下的值複製成預設值

print("修正後：", [f() for f in funcs_ok])  # [0, 1, 2, 3, 4] ✓

# ── nonlocal：在閉包裡修改外層的變數 ─────────────────────
# 閉包預設只能「讀取」外層變數
# 要修改外層變數，必須用 nonlocal 宣告

print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """
    工廠函數：回傳一個計數器函數
    start：起始值（預設為 0）
    """
    count = start   # 外層函數的區域變數

    def counter():
        """
        內層函數（閉包）：每次呼叫加 1
        nonlocal count 表示「我要修改外層的 count 變數，不是在內層建立新的 count」
        """
        nonlocal count   # ← 宣告「我要修改外層的 count，不是建新的」
        count += 1       # 外層的 count 加 1
        return count     # 回傳加完後的值

    return counter   # 回傳內層函數（閉包）

c1 = make_counter()      # 建立一個從 0 開始計數的計數器
c2 = make_counter(10)    # 建立另一個從 10 開始計數的計數器
# c1 和 c2 各自獨立，因為每次呼叫 make_counter 都會建立新的 count 變數
print(c1(), c1(), c1())   # 輸出 1 2 3（連續呼叫三次，每次加 1）
print(c2(), c2())         # 輸出 11 12（從 10 起算，兩次各加 1）
print(c1())               # 輸出 4（c1 和 c2 是各自獨立的計數器）

# ── 實際應用：用閉包做「一次性」工具函數 ────────────────
# CPE 中偶爾需要「記住狀態」但又不想寫整個 class

print("\n=== 閉包應用：記住已走過的節點 ===")
def make_visit_tracker():
    """
    建立一個「已訪問節點」的追蹤器
    使用閉包來保存 visited 集合
    """
    visited = set()          # 外層的集合，記錄所有走過的節點

    def visit(node):
        """
        檢查節點是否已被訪問
        如果已走過回傳 False，第一次走到回傳 True
        """
        nonlocal visited      # 修改外層的 visited 集合
        if node in visited:    # 如果節點已在 visited 集合中
            return False       # 回傳 False：已走過
        visited.add(node)      # 否則將節點加入 visited
        return True            # 回傳 True：第一次走到

    return visit              # 回傳內層函數

visit = make_visit_tracker()   # 建立追蹤器
# 對列表 [1, 2, 1, 3, 2, 4] 依序訪問
results = [visit(n) for n in [1, 2, 1, 3, 2, 4]]
# 結果：1 第一次→True, 2 第一次→True, 1 第二次→False, 3 第一次→True, 2 第二次→False, 4 第一次→True
print(results)  # [True, True, False, True, False, True]

# 記憶重點 ──────────────────────────────────────────────────
# 可變預設值陷阱 → 預設值用 None，函數內再建 [] 或 {}
# 閉包延遲綁定  → 用 lambda x=x: x 把值固定下來
# nonlocal      → 要「修改」外層變數時才需要，只「讀取」不用
