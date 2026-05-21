# U01. 陷阱！閉包與可變預設值（詳細說明）
# 說明：
# 本檔示範兩個常見但易出錯的 Python 寫法與其修正方式：
# 1) 可變預設值（mutable default arguments）陷阱
# 2) 閉包（closure）中變數的延遲綁定問題
# 並介紹 nonlocal 關鍵字在閉包中修改外層變數的用途。


# ---------- 陷阱 1：可變的預設值（mutable default） ----------
# 原因：Python 在定義函數時只會評估一次預設引數的表達式，
#          如果預設值是可變物件（如 list、dict），則所有呼叫會共用同一個物件，
#          導致資料意外累積或相互影響。

def add_to_cart(item, cart=[]):   # ← 這個 [] 只建立一次（在函式定義時）！
    # 這個函式看起來合理，但會有副作用：多次呼叫會共用同一個 cart
    cart.append(item)
    return cart

print("=== 陷阱 1：可變預設值 ===")
print(add_to_cart("蘋果"))   # ['蘋果']
print(add_to_cart("香蕉"))   # ['蘋果', '香蕉']  ← 出乎意料，並非隔離的呼叫
print(add_to_cart("葡萄"))   # ['蘋果', '香蕉', '葡萄']

# 正確做法：用 None 作為預設值，並在函數內建立新的容器
print("\n--- 正確寫法：用 None 當預設值 ---")
def add_to_cart_safe(item, cart=None):
    """
    安全版本：若未提供 cart，則在每次呼叫時建立新的 list，避免共用狀態。

    參數：
    - item: 要加入購物車的項目
    - cart: 可選的 list，若為 None 則在函式內建立新的 list
    """
    if cart is None:
        cart = []   # 每次呼叫建立新的 list，避免副作用
    cart.append(item)
    return cart

print(add_to_cart_safe("蘋果"))  # ['蘋果']
print(add_to_cart_safe("香蕉"))  # ['香蕉'] （互相獨立）



# ---------- 陷阱 2：閉包的延遲綁定（late binding） ----------
# 關鍵概念：閉包（closure）會捕捉變數名稱，而非當下的值；
# 當外層變數在迴圈中改變時，內部的 lambda/函式會在實際呼叫時才去查該變數，
# 因此若不特別處理，常見情況會導致所有閉包都回傳最後一次迭代的值。

print("\n=== 陷阱 2：閉包延遲綁定 ===")
funcs = []
for i in range(5):
    # 這裡的 lambda 並不會把當下的 i 值複製起來，
    # 它只是記住「有一個名為 i 的變數」，呼叫時才會去查它的值
    funcs.append(lambda: i)

print("你以為：", [0, 1, 2, 3, 4])
print("實際上：", [f() for f in funcs])  # [4, 4, 4, 4, 4]

# 修正方法 1：使用預設參數把當下的值複製到函式物件裡（常見且直覺）
print("\n--- 正確寫法：用預設參數把值「複製」進來 ---")
funcs_ok = []
for i in range(5):
    # 將當前的 i 賦給 lambda 的預設參數，這個預設值在定義時就會被計算並固定
    funcs_ok.append(lambda i=i: i)

print("修正後：", [f() for f in funcs_ok])  # [0, 1, 2, 3, 4] ✓

# 修正方法 2：用函數封裝（factory function）把值綁定在新作用域
def make_lambda(x):
    def inner():
        return x
    return inner

funcs_ok2 = [make_lambda(i) for i in range(5)]
print("封裝修正：", [f() for f in funcs_ok2])  # [0,1,2,3,4]



# ---------- nonlocal：在閉包裡修改外層變數 ----------
# 在閉包中讀取外層變數不需要宣告，但若要修改外層變數，必須用 nonlocal 指明，
# 否則賦值會建立新的區域變數（shadowing），而非修改外層變數。

print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """
    回傳一個計數器函數，每次呼叫會在內部狀態上加 1 並回傳新的值。

    範例用途：當需要一個簡潔的可呼叫物件維持狀態時，可用閉包代替完整的 class。
    """
    count = start

    def counter():
        nonlocal count   # 宣告我們要修改外層的 count
        count += 1
        return count

    return counter


c1 = make_counter()
c2 = make_counter(10)
print(c1(), c1(), c1())   # 1 2 3（c1 的內部狀態會累加）
print(c2(), c2())         # 11 12（不同起始值，互不干擾）
print(c1())               # 4（c1 和 c2 各自維護自己的 count）



# ---------- 實際應用示例：用閉包做一次性工具函數 ----------
# 在競賽或小型程式中，有時只需要一個小工具來記錄狀態（例如已走訪節點），
# 用閉包比寫完整 class 較簡潔清楚。

print("\n=== 閉包應用：記住已走過的節點 ===")
def make_visit_tracker():
    visited = set()

    def visit(node):
        # 這裡不需要 nonlocal，因為我們並沒有重新指派 visited 變數，
        # 而是呼叫 visited 的方法（add），這屬於可變物件的內容修改。
        if node in visited:
            return False    # 已走過
        visited.add(node)
        return True         # 第一次走到

    return visit


visit = make_visit_tracker()
results = [visit(n) for n in [1, 2, 1, 3, 2, 4]]
print(results)  # [True, True, False, True, False, True]



# ---------- 總結與最佳實務（建議） ----------
# - 可變預設值陷阱：若預設值是可變容器，請改用 None 作為預設，並在函式內建立新容器。
# - 閉包延遲綁定：當閉包需要捕捉迭代變數的當下值時，使用預設參數（lambda i=i: i）或
#                   用 factory function 把值固定下來。
# - nonlocal：僅在你確實要在閉包中重新指派外層變數時使用；若只是修改可變物件的內容
#             （例如 set.add 或 list.append），通常不需要 nonlocal。
# - 若程式邏輯變複雜，考慮改用 class（可讀性與可測試性較好）。
