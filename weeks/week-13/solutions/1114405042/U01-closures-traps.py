"""
U01. 陷阱！閉包與可變預設值

說明：本模組示範兩個容易出錯的情境：
1) 可變的預設值（mutable default arguments）會被共用；
2) 閉包（closure）的延遲綁定（late binding）使得 lambda/closure
   在迴圈內捕捉到的不是當下值而是變數名稱。

檔內範例保留原程式行為，同時加入繁體中文 docstring 與更詳盡註解，
方便教學與作業使用。
"""


# ── 陷阱 1：可變的預設值（mutable default）──────────────────
# 關鍵觀念：函數的預設值只會在定義時建立一次，因此若預設值是
# 可變物件（如 list, dict），後續每次呼叫都會共用同一個物件，容易導致
# 意外的狀態累積。

def add_to_cart(item, cart=[]):   # ← 這個 [] 只在函數定義時建立一次！
    """錯誤示範：將 item 加入預設的 cart 列表（不可取）。

    目的：示範為何不應將可變物件當作預設值。
    """
    cart.append(item)
    return cart

print("=== 陷阱 1：可變預設值 ===")
print(add_to_cart("蘋果"))   # ['蘋果']
print(add_to_cart("香蕉"))   # ['蘋果', '香蕉']  ← 因為共用同一個 list
print(add_to_cart("葡萄"))   # ['蘋果', '香蕉', '葡萄']


print("\n--- 正確寫法：用 None 當預設值 ---")
def add_to_cart_safe(item, cart=None):
    """正確寫法：以 None 為預設值，函數內再建立新的 list，避免共用狀態。"""
    if cart is None:
        cart = []   # 每次呼叫才建立新的 list
    cart.append(item)
    return cart

print(add_to_cart_safe("蘋果"))  # ['蘋果']
print(add_to_cart_safe("香蕉"))  # ['香蕉'] ← 各自獨立，正確！


# ── 陷阱 2：閉包的延遲綁定（closure late binding）────────────
# 關鍵觀念：閉包會捕捉變數的「名稱」，而非當下的值；若在迴圈中產生
# 多個 lambda/closure，迴圈結束後變數會是最後的值，因此所有 closure
# 讀到的會是同一個最終值。

print("\n=== 陷阱 2：閉包延遲綁定 ===")
funcs = []
for i in range(5):
    funcs.append(lambda: i)   # ← lambda 記住「i」這個名稱，而不是當下值

print("你以為：", [0, 1, 2, 3, 4])
print("實際上：", [f() for f in funcs])  # [4, 4, 4, 4, 4]，因為 i 最終為 4


print("\n--- 正確寫法：用預設參數把當下的值複製進來 ---")
funcs_ok = []
for i in range(5):
    funcs_ok.append(lambda i=i: i)   # ← 透過預設參數 i=i 固定當下的值

print("修正後：", [f() for f in funcs_ok])  # [0, 1, 2, 3, 4] ✓


# ── nonlocal：在閉包裡修改外層變數（需注意作用域）──────────
# 閉包預設可以讀取外層變數，但若要在閉包中重新指派（修改）外層變數，
# 必須使用 `nonlocal` 宣告，否則賦值會建立新的區域變數。

print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """回傳一個計數器函數（closure），每次呼叫會在內部計數並回傳。

    透過 `nonlocal` 對外層的 count 變數進行遞增，而不是建立新的區域變數。
    """
    count = start

    def counter():
        nonlocal count   # 宣告我們要修改外層的 count
        count += 1
        return count

    return counter

c1 = make_counter()
c2 = make_counter(10)
print(c1(), c1(), c1())   # 1 2 3
print(c2(), c2())         # 11 12
print(c1())               # 4（c1 和 c2 各自獨立）


# ── 實際應用：用閉包做記錄或狀態追蹤的工具函數 ─────────────
# 這在競程或簡短腳本中很方便：想要記住某些狀態但又不想建立完整類別時
# 可考慮使用閉包。

print("\n=== 閉包應用：記住已走過的節點 ===")
def make_visit_tracker():
    """回傳一個 visit 函數，用來追蹤已拜訪的節點（節點可雜湊）。

    每次呼叫 visit(node) 時，若 node 尚未被拜訪，加入集合並回傳 True，
    否則回傳 False 表示已拜訪過。
    """
    visited = set()

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


# 記憶重點 ──────────────────────────────────────────────────
# - 可變預設值陷阱：不要把 list/dict 當預設值，應用 None 並在函數內建立
# - 閉包延遲綁定：若要在迴圈建立 closure 時捕捉當下值，使用 `lambda x=x: x` 或類似手法
# - nonlocal：只有在要修改外層變數時才需要，否則單純讀取不需宣告
