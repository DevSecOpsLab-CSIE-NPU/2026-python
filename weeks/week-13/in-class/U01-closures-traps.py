# U01. 陷阱！閉包與可變預設值（Closures & Mutable Default Traps）
# 範例與說明（繁體中文、詳盡註解）：
# 本檔示範兩個容易讓初學者踩到的坑，並解釋底層原因與常見修正策略：
# 1) 可變預設值（mutable default）會被所有呼叫共用，因為預設值在函式定義時建立一次
# 2) 閉包（closure）中變數的延遲綁定（late binding）行為：閉包記住的是名稱（reference），
#    呼叫時才去查該名稱目前的值，而不是在定義時就把值快照下來。
# 提供的修正：對於可變預設值改用 `None` 並在函式內建立新物件；對於閉包延遲綁定可用
# 將當下值綁到預設參數（例如 `lambda i=i: i`）或建立工廠函式來捕捉當下值。

# ── 陷阱 1：可變的預設值 ─────────────────────────────────
# 關鍵：函數的預設值只在「定義時」建立一次，之後每次呼叫都共用同一個物件

def add_to_cart(item, cart=[]):   # ← 這個 [] 只建立一次！
    # 問題示範：此寫法會在函式定義時建立一次空 list，之後每次呼叫都共用同一個物件。
    # 這會造成函式有「隱性狀態」，通常不是我們想要的行為。
    # 注意：如果你希望回傳的 list 是獨立的，應改用下方的安全寫法。
    cart.append(item)
    return cart

print("=== 陷阱 1：可變預設值 ===")
print(add_to_cart("蘋果"))   # ['蘋果']
print(add_to_cart("香蕉"))   # ['蘋果', '香蕉']  ← 驚！不是 ['香蕉']
print(add_to_cart("葡萄"))   # ['蘋果', '香蕉', '葡萄']
# 原因：cart=[] 這個 list 在 def 時就建好了，三次呼叫都用同一個

# 補充說明：
# - 這種行為是 Python 語言定義的一部分（預設參數在函式定義時求值），
#   不是某個實作的 bug。當預設值是不可變物件（如 None、數字、字串）時通常不會注意到。
# - 若你刻意想要累積狀態（例如實作 cache 或單例列表），則可利用此特性；但應該
#   明確註明並考慮執行緒安全性（thread-safety）問題。

print("\n--- 正確寫法：用 None 當預設值 ---")
def add_to_cart_safe(item, cart=None):
    # 正確做法：以 None 作為預設值，函數內再建立新的 list，確保每次呼叫互相獨立
    if cart is None:
        cart = []   # ← 每次呼叫才建立新的 list
    cart.append(item)
    return cart

print(add_to_cart_safe("蘋果"))  # ['蘋果']
print(add_to_cart_safe("香蕉"))  # ['香蕉'] ← 各自獨立，正確！

# ── 陷阱 2：閉包的延遲綁定（closure late binding） ─────────────────
# 關鍵：閉包會記住外層變數的參考（名字），呼叫時會去讀取當下的值，而不是定義時的快照
# 因此在迴圈中建立多個 lambda，如果直接使用迴圈變數，最後會發現全部 lambda 都回傳迴圈結束後的值

print("\n=== 陷阱 2：閉包延遲綁定 ===")
funcs = []
for i in range(5):
    # 錯誤示範：此 lambda 捕捉的是名字 i，呼叫時才去查 i 的值
    funcs.append(lambda: i)   # ← lambda 記住「i」這個名字，不是值

print("你以為：", [0, 1, 2, 3, 4])
print("實際上：", [f() for f in funcs])  # [4, 4, 4, 4, 4]，全部都是 4！
# 原因：迴圈結束後 i=4，所有 lambda 去查 i，都查到 4

# 補充說明：
# - 閉包內的 free variables（自由變數）是以詞彙作用域（lexical scope）解析名稱，
#   但 name binding（名稱綁定）並非自動複製當時的值；這就是所謂「late binding」。
# - 若要在定義時捕捉值，常見技巧為把值放到預設參數，因為預設參數在函式定義時
#   就會被求值並存入函數物件內部；因此 `lambda i=i: i` 會把當下的 i 值固定住。

print("\n--- 正確寫法：用預設參數把值「複製」進來 ---")
funcs_ok = []
for i in range(5):
    # 修正技巧：利用函數預設值的「建立時即求值」特性，把當下的 i 綁定成 lambda 的預設參數
    funcs_ok.append(lambda i=i: i)   # ← i=i 把當下的值複製成預設值

print("修正後：", [f() for f in funcs_ok])  # [0, 1, 2, 3, 4] ✓

# ── nonlocal：在閉包裡修改外層的變數 ─────────────────────
# 閉包可以讀取外層變數，但若要在內層修改外層變數（而非建立新的區域變數），
# 必須使用 nonlocal（若要修改全域變數則使用 global）。 nonlocal 告知直譯器該名稱來自外層封閉範圍。

print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """回傳一個計數器函數，每次呼叫加 1。

    說明：count 在 make_counter 的區域被建立，counter 閉包可以讀取並藉由 nonlocal 修改它，
    使得每次呼叫 counter() 時能保有並累積狀態。
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

# ── 實際應用：用閉包做「一次性」工具函數（stateful helper）──────────────
# 閉包是實作輕量狀態儲存的好工具，當你不需要完整類別的複雜性時，可用閉包包裝狀態與操作

print("\n=== 閉包應用：記住已走過的節點 ===")
def make_visit_tracker():
    visited = set()

    def visit(node):
        # nonlocal visited  # 不需要 nonlocal，因為我們不改變 visited 本身（只呼叫其方法）
        # 注意：只有在要重新賦值 visited 時才需要 nonlocal；呼叫 visited.add() 並不改變變數綁定
        if node in visited:
            return False    # 已走過
        visited.add(node)
        return True         # 第一次走到

    return visit

visit = make_visit_tracker()
results = [visit(n) for n in [1, 2, 1, 3, 2, 4]]
print(results)  # [True, True, False, True, False, True]

# 記憶重點 ──────────────────────────────────────────────────
# - 可變預設值陷阱 → 若預設值為可變物件（list/dict），應改用 None 並在函數內建立新物件
# - 閉包延遲綁定（late binding）→ 閉包會在呼叫時解析外層變數，使用 lambda i=i 的技巧可把當下值綁定
# - nonlocal → 只有在要重新指派外層變數（例如 count = count + 1）時才需要；呼叫外層可變物件的方法通常不需 nonlocal
# - 設計建議：對於需要明確狀態管理的情境，若邏輯變複雜，考慮使用 class（較易讀與測試）
