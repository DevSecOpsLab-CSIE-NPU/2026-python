# U01. 陷阱！閉包與可變預設值
#
# 本檔示範兩個常見且容易誤解的 Python 行為：
#  1) 可變的預設參數（mutable default arguments）會被所有呼叫共用，
#     因為預設值只在函式定義時評估一次；
#  2) 閉包（closure）會記住「變數名稱」而非當下的值，導致延遲綁定（late binding）問題。
#
# 這些行為常在初學者或在實作簡潔函式時造成 bug。示範同時也提供正確做法與適用情境：
#  - 若預設值需要每次呼叫都為新物件，請用 None 作為預設並在函式內建立新物件；
#  - 若要在閉包中固定當前迴圈的值，可把值放到預設參數（如 lambda i=i）。

# ── 陷阱 1：可變的預設值 ─────────────────────────────────
# 關鍵：函數的預設值只在「定義時」建立一次，之後每次呼叫都共用同一個物件

def add_to_cart(item, cart=[]):   # ← 這個 [] 只建立一次！
    """錯誤示範：使用可變物件當預設參數。

    問題：`cart=[]` 這個 list 只會在函式定義時建立一次，之後每次呼叫都會共用同一個 list，
    因此多次呼叫會把元素累積到同一個 cart 中。
    """
    cart.append(item)
    return cart

print("=== 陷阱 1：可變預設值 ===")
print(add_to_cart("蘋果"))   # ['蘋果']
print(add_to_cart("香蕉"))   # ['蘋果', '香蕉']  ← 驚！不是 ['香蕉']
print(add_to_cart("葡萄"))   # ['蘋果', '香蕉', '葡萄']
# 原因：cart=[] 這個 list 在 def 時就建好了，三次呼叫都用同一個

print("\n--- 正確寫法：用 None 當預設值 ---")
def add_to_cart_safe(item, cart=None):
    """正確寫法：將預設值設為 None，並在函式內視需要建立新的容器。

    這樣每次呼叫若不傳入 cart，會建立新的 list，避免跨呼叫狀態污染。
    """
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
    # 錯誤示範：lambda 在此記住的是變數名稱 i，非當下數值；等迴圈結束再呼叫時，i 會是最後的值
    funcs.append(lambda: i)   # ← lambda 記住「i」這個名字，不是值

print("你以為：", [0, 1, 2, 3, 4])
print("實際上：", [f() for f in funcs])  # [4, 4, 4, 4, 4]，全部都是 4！
# 原因：迴圈結束後 i=4，所有 lambda 去查 i，都查到 4

print("\n--- 正確寫法：用預設參數把值「複製」進來 ---")
funcs_ok = []
for i in range(5):
    # 正確寫法：把當下的 i 複製為 lambda 的預設參數（預設參數在定義時就會被計算）
    funcs_ok.append(lambda i=i: i)   # ← i=i 把當下的值複製成預設值

print("修正後：", [f() for f in funcs_ok])  # [0, 1, 2, 3, 4] ✓

# ── nonlocal：在閉包裡修改外層的變數 ─────────────────────
# 閉包預設只能「讀取」外層變數
# 要修改外層變數，必須用 nonlocal 宣告

print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """建立一個閉包計數器：每次呼叫回傳遞增的計數值。

    說明：
      - `count` 在外層函式中定義，內層的 `counter` 閉包要修改它，因此使用 `nonlocal count`。
      - `nonlocal` 告訴 Python 在外層作用域尋找該變數並修改它，而非建立新的區域變數。
    """
    count = start

    def counter():
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
    """示範閉包在實務上的用法：建立一個簡單的訪問追蹤器（visited set）。

    用途：在某些演算法或測試中，想要記住哪些節點已被訪問，但又不想建立整個 class，
    閉包提供一種輕量的替代方案。
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
# 可變預設值陷阱 → 預設值用 None，函數內再建 [] 或 {}
# 閉包延遲綁定  → 用 lambda x=x: x 把值固定下來
# nonlocal      → 要「修改」外層變數時才需要，只「讀取」不用
