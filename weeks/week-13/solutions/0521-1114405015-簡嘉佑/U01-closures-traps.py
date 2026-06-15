# U01. 陷阱！閉包與可變預設值
# 兩個「寫起來看似正確，但結果出乎意料」的 Python 坑
# 對應 Bloom's Taxonomy：理解（Understand）— 能解釋為什麼會出錯
#
# 本檔整理兩個 Python 新手最常踩到的陷阱：
# 1) 可變物件（list/dict）當函數預設值 → 所有呼叫共用同一個物件
# 2) 閉包的「延遲綁定」→ lambda 記住的是變數名稱，不是當下的值

# ── 陷阱 1：可變的預設值 ─────────────────────────────────
# 關鍵：函數的預設值只在「定義時」建立一次，之後每次呼叫都共用同一個物件

def add_to_cart(item, cart=[]):   # ← 這個 [] 只建立一次！
    # 陷阱：cart=[] 在 def 時就建好了，之後每次呼叫都用同一個 list
    # Python 不會每次呼叫時重新建立預設值
    cart.append(item)
    return cart

print("=== 陷阱 1：可變預設值 ===")
print(add_to_cart("蘋果"))   # ['蘋果']
print(add_to_cart("香蕉"))   # ['蘋果', '香蕉']  ← 驚！不是 ['香蕉']
print(add_to_cart("葡萄"))   # ['蘋果', '香蕉', '葡萄']
# 原因：cart=[] 這個 list 在 def 時就建好了，三次呼叫都用同一個

print("\n--- 正確寫法：用 None 當預設值 ---")
def add_to_cart_safe(item, cart=None):
    # 正確做法：用 None 當哨兵值，每次呼叫才建立新的 list
    # None 是不可變物件，沒有「共用同一個物件」的問題
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
    # 閉包「捕捉」的是變數 i 的參考，而非當下的數值
    # 迴圈結束後 i=4，所有 lambda 去查 i，都查到 4
for i in range(5):
    funcs.append(lambda: i)   # ← lambda 記住「i」這個名字，不是值

print("你以為：", [0, 1, 2, 3, 4])
print("實際上：", [f() for f in funcs])  # [4, 4, 4, 4, 4]，全部都是 4！
# 原因：迴圈結束後 i=4，所有 lambda 去查 i，都查到 4

print("\n--- 正確寫法：用預設參數把值「複製」進來 ---")
funcs_ok = []
    # 每次迴圈時，預設值 i=i 會立刻把當前的 i 的值儲存下來
    # 這樣每個 lambda 都有自己獨立的「當下值」
for i in range(5):
    funcs_ok.append(lambda i=i: i)   # ← i=i 把當下的值複製成預設值

print("修正後：", [f() for f in funcs_ok])  # [0, 1, 2, 3, 4] ✓

# ── nonlocal：在閉包裡修改外層的變數 ─────────────────────
# 閉包預設只能「讀取」外層變數
# 要修改外層變數，必須用 nonlocal 宣告

print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """回傳一個計數器函數，每次呼叫加 1"""
    count = start

    def # 沒有 nonlocal：Python 會在本地找 count，找不到就報 UnboundLocalError
        # 加了 nonlocal：Python 知道要修改外層作用域的 count
        counter():
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
# CPE 中偶爾需要「記住狀態」但又   # 閉包內的狀態，每次建立追蹤器都是獨立的 set

    def visit(node):
        nonlocal visited   # 只是讀取 + 呼叫 .add，其實不需要 nonlocal
        # （set.add 是原地修改，不是重新賦值，不需要 nonlocal）:
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
