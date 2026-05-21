# U01. 陷阱！閉包與可變預設值 (Closures & Mutable Defaults)
# 兩個「寫起來看似正確，但結果出乎意料」的 Python 經典陷阱。
# 對應 Bloom's Taxonomy：理解 (Understand) — 能解釋為什麼會出錯，並知道如何修正。

# ── 陷阱 1：可變的預設值 (Mutable Default Arguments) ─────────────────────────
# 關鍵：在 Python 中，函數的預設值只在「定義 (def) 時」建立一次。
# 之後每次呼叫該函數時，如果沒傳入對應參數，都會共用同一個物件。

def add_to_cart(item, cart=[]):   # ⚠️ 注意：這個 [] 只會建立一次！
    cart.append(item)
    return cart

print("=== 陷阱 1：可變預設值 ===")
print(f"第一次呼叫：{add_to_cart('蘋果')}")   # ['蘋果']
print(f"第二次呼叫：{add_to_cart('香蕉')}")   # ['蘋果', '香蕉']  ← 💡 驚！不是 ['香蕉']
print(f"第三次呼叫：{add_to_cart('葡萄')}")   # ['蘋果', '香蕉', '葡萄']
# 原因：cart=[] 這個 list 在定義時就生成了，後續所有呼叫都持續修改同一個 list。

print("\n--- 正確寫法：使用 None 作為預設值 ---")
def add_to_cart_safe(item, cart=None):
    """如果沒傳入 cart，就在函數內部建立一個新的空 list"""
    if cart is None:
        cart = []   # ✅ 每次呼叫時才動態建立新的 list
    cart.append(item)
    return cart

print(f"第一次 (安全)：{add_to_cart_safe('蘋果')}")  # ['蘋果']
print(f"第二次 (安全)：{add_to_cart_safe('香蕉')}")  # ['香蕉'] ← 各自獨立，正確！

# ── 陷阱 2：閉包的延遲綁定 (Late Binding in Closures) ─────────────────────────
# 關鍵：閉包（如 lambda）捕捉的是「變數名稱」本身，而不是「變數當下的值」。
# 當迴圈跑完後再執行函數，變數的值早已變成最後一次迭代的結果。

print("\n=== 陷阱 2：閉包延遲綁定 ===")
funcs = []
for i in range(5):
    # 這裡的 lambda 會記住「i」這個名字
    funcs.append(lambda: i)   

print("預期結果：[0, 1, 2, 3, 4]")
print(f"實際執行：{[f() for f in funcs]}")  # [4, 4, 4, 4, 4]，全部都是 4！
# 原因：當迴圈結束後 i = 4。當我們執行 f() 時，它才去查看 i 是多少，結果全部查到 4。

print("\n--- 正確寫法：使用預設參數將值「立即綁定」 ---")
funcs_ok = []
for i in range(5):
    # 透過 i=i，將當下的 i 值存入該 lambda 的預設參數中（定義時即固定）
    funcs_ok.append(lambda i=i: i)   

print(f"修正執行：{[f() for f in funcs_ok]}")  # [0, 1, 2, 3, 4] ✓

# ── nonlocal：在閉包內部修改外層變數 ─────────────────────
# 在巢狀函數中，內部函數預設只能「讀取」外層變數，不能直接「修改」。
# 若要修改外層變數，必須明確使用 nonlocal 關鍵字宣告。

print("\n=== nonlocal：修改外層作用域變數 ===")

def make_counter(start=0):
    """回傳一個計數器函數，展現狀態保存的功能"""
    count = start

    def counter():
        nonlocal count   # ✅ 告訴 Python：我要修改的是外層的 count，不是建立新局部變數
        count += 1
        return count

    return counter

c1 = make_counter()      # 從 0 開始的計數器
c2 = make_counter(10)    # 從 10 開始的計數器
print(f"c1 呼叫：{c1()}, {c1()}, {c1()}")   # 1 2 3
print(f"c2 呼叫：{c2()}, {c2()}")         # 11 12
print(f"c1 再次：{c1()}")                  # 4（證明 c1 與 c2 狀態完全隔離）

# ── 實際應用：使用閉包實作「一次性」狀態工具 ────────────────
# 在 CPE 競程中，有時需要記住已訪問過的節點，但又不想動用類別 (class) 時非常方便。

print("\n=== 實務應用：路徑訪問追蹤器 ===")
def make_visit_tracker():
    """建立一個可以記住哪些節點已被造訪過的函數"""
    visited = set()

    def visit(node):
        nonlocal visited
        if node in visited:
            return False    # 此節點已走過
        visited.add(node)
        return True         # 這是第一次造訪

    return visit

checker = make_visit_tracker()
nodes = [1, 2, 1, 3, 2, 4]
results = [checker(n) for n in nodes]
print(f"造訪節點序列：{nodes}")
print(f"是否為首次造訪：{results}")  # [True, True, False, True, False, True]

# 記憶重點 ──────────────────────────────────────────────────
# 1. 可變預設值陷阱：永遠使用 None 當預設值，再於內部建立 list/dict。
# 2. 閉包延遲綁定：在迴圈建立 lambda 時，使用預設參數 `var=var` 來捕捉當下數值。
# 3. nonlocal：當你需要在內部函數「重新賦值 (+=, =)」給外層變數時才需要。
# 4. 閉包優勢：封裝狀態，提供比類別更輕量化的解決方案。
