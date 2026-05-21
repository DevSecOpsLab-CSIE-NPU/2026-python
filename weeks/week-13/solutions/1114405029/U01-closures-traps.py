# U01. 陷阱！閉包與可變預設值
# 兩個「寫起來看似正確，但結果出乎意料」的 Python 坑
# 對應 Bloom's Taxonomy：理解（Understand）— 能解釋為什麼會出錯
#
# 本題核心：
# 這份程式整理兩個 Python 初學者很容易遇到的陷阱：
#
# 1. 可變預設值陷阱
#    函數的預設參數只會在 def 被執行時建立一次。
#    如果預設值是 list、dict、set 這種可變物件，
#    多次呼叫函數時就會共用同一個物件，
#    造成資料被累積、互相影響。
#
# 2. 閉包的延遲綁定
#    閉包記住的是「變數名稱」或「變數參照」，
#    不是每次迴圈當下的值。
#    因此 lambda 或內部函數如果在之後才執行，
#    可能會讀到迴圈變數最後留下來的值。
#
# 另外也會補充：
# 3. nonlocal
#    當內部函數想修改外層函數的變數時，
#    需要使用 nonlocal 宣告。
#
# 4. 閉包實際應用
#    用閉包保存狀態，例如記錄哪些節點已經走過。

# ── 陷阱 1：可變的預設值 ─────────────────────────────────
# 關鍵：函數的預設值只在「定義時」建立一次，之後每次呼叫都共用同一個物件
#
# Python 的函數預設參數不是每次呼叫都重新建立。
#
# 例如：
# def add_to_cart(item, cart=[]):
#
# 這裡的 [] 不是每次呼叫 add_to_cart() 都建立新的空 list。
# 它是在 Python 執行到 def 這行、建立函數物件時，
# 就先建立好一次。
#
# 之後如果呼叫時沒有傳入 cart，
# 就會一直共用同一個預設 list。
#
# 因為 list 是可變物件，
# cart.append(item) 會直接修改同一個 list。
#
# 所以多次呼叫後，資料會一直累積在同一個 cart 裡。

def add_to_cart(item, cart=[]):   # ← 這個 [] 只建立一次！
    # item 是這次要加入購物車的品項。
    #
    # cart 是購物車 list。
    #
    # 這裡的問題在於：
    # cart 的預設值是 []，
    # 而 [] 是可變物件。
    #
    # 如果呼叫 add_to_cart() 時沒有傳入 cart，
    # Python 會使用同一個預設 list。
    cart.append(item)

    # 回傳目前的 cart。
    #
    # 因為每次都可能是同一個 list，
    # 所以結果會不斷累積。
    return cart

# 印出第一個陷阱的標題。
print("=== 陷阱 1：可變預設值 ===")

# 第一次呼叫 add_to_cart("蘋果")。
#
# 沒有傳入 cart，
# 所以使用預設的那個 list。
#
# 此時 cart 原本是 []，
# append "蘋果" 後變成 ['蘋果']。
print(add_to_cart("蘋果"))   # ['蘋果']

# 第二次呼叫 add_to_cart("香蕉")。
#
# 你可能以為會重新建立一個新的 []，
# 所以結果應該是 ['香蕉']。
#
# 但實際上 Python 仍然使用同一個預設 list。
#
# 那個 list 上一次已經有 ['蘋果']，
# 這次再 append "香蕉"，
# 所以變成 ['蘋果', '香蕉']。
print(add_to_cart("香蕉"))   # ['蘋果', '香蕉']  ← 驚！不是 ['香蕉']

# 第三次呼叫 add_to_cart("葡萄")。
#
# 一樣共用同一個預設 list。
#
# 所以會在前面的 ['蘋果', '香蕉'] 後面再加入 '葡萄'。
print(add_to_cart("葡萄"))   # ['蘋果', '香蕉', '葡萄']

# 原因：cart=[] 這個 list 在 def 時就建好了，三次呼叫都用同一個
#
# 這種 bug 很危險，因為程式看起來很合理，
# 但多次呼叫後結果會被前一次呼叫影響。

print("\n--- 正確寫法：用 None 當預設值 ---")

# 正確做法：
# 不要把 list、dict、set 這種可變物件直接當預設值。
#
# 通常改用 None 當預設值。
#
# 然後在函數內檢查：
# 如果 cart 是 None，
# 就建立新的空 list。
#
# 這樣每次沒有傳入 cart 時，
# 都會在函數執行當下建立新的 list。

def add_to_cart_safe(item, cart=None):
    # 如果呼叫者沒有傳入 cart，
    # cart 就會是 None。
    if cart is None:
        # 這裡才建立新的空 list。
        #
        # 因為這行是在函數呼叫時執行，
        # 所以每次呼叫都會建立不同的新 list。
        cart = []   # ← 每次呼叫才建立新的 list

    # 把 item 加入這次自己的 cart。
    cart.append(item)

    # 回傳這次的購物車內容。
    return cart

# 第一次呼叫安全版本。
#
# cart 是 None，
# 函數內建立新的 []，
# 加入 "蘋果" 後回傳 ['蘋果']。
print(add_to_cart_safe("蘋果"))  # ['蘋果']

# 第二次呼叫安全版本。
#
# cart 一樣是 None，
# 函數內會重新建立另一個新的 []，
# 不會共用上次的 list。
#
# 所以結果是 ['香蕉']。
print(add_to_cart_safe("香蕉"))  # ['香蕉'] ← 各自獨立，正確！

# ── 陷阱 2：閉包的延遲綁定 ───────────────────────────────
# 關鍵：閉包記住的是「變數名稱」，不是「當下的值」
# 等迴圈跑完，i 已經是最後的值了
#
# 閉包 closure：
# 指的是內部函數記住外部作用域變數的能力。
#
# 例如 lambda: i 使用了外層的 i。
# 即使 lambda 被放進 list 裡，之後才執行，
# 它仍然能找到外層的 i。
#
# 但陷阱在於：
# 它記住的是 i 這個變數名稱，
# 不是建立 lambda 當下 i 的值。
#
# 因此當迴圈結束後，
# i 已經停在最後一個值 4。
#
# 之後所有 lambda 執行時，
# 都會去查同一個 i，
# 所以全部得到 4。

print("\n=== 陷阱 2：閉包延遲綁定 ===")

# 建立一個空 list，
# 用來存放等等產生的 lambda 函數。
funcs = []

# 迴圈 i 會依序是：
# 0, 1, 2, 3, 4
for i in range(5):
    # 每次迴圈都建立一個 lambda 函數，
    # 並把它加入 funcs。
    #
    # lambda: i 的意思是：
    # 建立一個不需要參數的匿名函數，
    # 執行時回傳 i。
    #
    # 但是這裡的 lambda 沒有把當下的 i 值存起來。
    # 它只是記住「之後要去找 i 這個變數」。
    funcs.append(lambda: i)   # ← lambda 記住「i」這個名字，不是值

# 你可能以為五個 lambda 分別記住：
# 0, 1, 2, 3, 4
print("你以為：", [0, 1, 2, 3, 4])

# 實際上，這裡才真正呼叫每個 lambda。
#
# 這時 for 迴圈早已結束，
# i 的最後值是 4。
#
# 所以每個 lambda 執行時去查 i，
# 都查到同一個最後值 4。
print("實際上：", [f() for f in funcs])  # [4, 4, 4, 4, 4]，全部都是 4！

# 原因：迴圈結束後 i=4，所有 lambda 去查 i，都查到 4
#
# 這叫做 late binding，也就是延遲綁定。
# 變數值不是在函數建立時固定，
# 而是在函數真正執行時才去查。

print("\n--- 正確寫法：用預設參數把值「複製」進來 ---")

# 修正方式：
# 用 lambda i=i: i
#
# 第一個 i：
# 是 lambda 的參數名稱。
#
# 第二個 i：
# 是當下外層迴圈的 i。
#
# 預設參數會在函數建立時就先計算並保存。
# 因此每次迴圈建立 lambda 時，
# 都會把當下的 i 值存成該 lambda 的預設值。
funcs_ok = []

# 再跑一次 0 到 4 的迴圈。
for i in range(5):
    # lambda i=i: i 的效果是：
    # 把當下的 i 固定成這個 lambda 的預設參數。
    #
    # 第一次迴圈：
    # i=0，所以建立 lambda i=0: i
    #
    # 第二次迴圈：
    # i=1，所以建立 lambda i=1: i
    #
    # 依此類推。
    funcs_ok.append(lambda i=i: i)   # ← i=i 把當下的值複製成預設值

# 呼叫修正後的 lambda。
#
# 因為每個 lambda 都有自己的預設參數值，
# 所以結果會是 0, 1, 2, 3, 4。
print("修正後：", [f() for f in funcs_ok])  # [0, 1, 2, 3, 4] ✓

# ── nonlocal：在閉包裡修改外層的變數 ─────────────────────
# 閉包預設只能「讀取」外層變數
# 要修改外層變數，必須用 nonlocal 宣告
#
# 在 Python 中，
# 如果內部函數只是讀取外層變數，通常可以直接讀。
#
# 但是如果內部函數想要「重新指定」外層變數，
# Python 會把它當成內部函數自己的區域變數。
#
# 例如：
# count += 1
#
# 這其實包含：
# count = count + 1
#
# 因為有賦值行為，
# Python 會認為 count 是內部函數的區域變數。
#
# 如果沒有 nonlocal，
# 就可能產生 UnboundLocalError。
#
# nonlocal count 的意思是：
# 這個 count 不是內部函數自己的變數，
# 而是外層 make_counter() 裡面的 count。
#
# 我要修改的是外層的 count。

print("\n=== nonlocal：修改外層變數 ===")

def make_counter(start=0):
    """回傳一個計數器函數，每次呼叫加 1"""

    # count 是 make_counter() 的區域變數。
    #
    # start 是起始值。
    # 如果沒有傳入 start，
    # 預設從 0 開始。
    count = start

    def counter():
        # counter() 是內部函數。
        #
        # 它會形成閉包，
        # 記住外層 make_counter() 的 count。
        #
        # 因為下面要執行 count += 1，
        # 這是修改外層變數，
        # 所以必須使用 nonlocal。
        nonlocal count   # ← 宣告「我要修改外層的 count，不是建新的」

        # 將外層的 count 加 1。
        count += 1

        # 回傳更新後的 count。
        return count

    # 回傳 counter 函數本身。
    #
    # 注意：
    # 這裡不是 return counter()
    # 因為 return counter() 會立刻執行 counter。
    #
    # return counter 是把函數物件回傳出去，
    # 之後可以用 c1()、c2() 的方式多次呼叫。
    return counter

# 建立第一個計數器。
#
# 沒有傳入 start，
# 所以 start=0。
#
# c1 會記住自己的 count。
c1 = make_counter()

# 建立第二個計數器。
#
# 傳入 start=10。
#
# c2 會有另一份獨立的 count，
# 不會和 c1 共用。
c2 = make_counter(10)

# 呼叫 c1 三次。
#
# c1 的 count 從 0 開始：
# 第一次：1
# 第二次：2
# 第三次：3
print(c1(), c1(), c1())   # 1 2 3

# 呼叫 c2 兩次。
#
# c2 的 count 從 10 開始：
# 第一次：11
# 第二次：12
print(c2(), c2())         # 11 12

# 再呼叫 c1 一次。
#
# c1 和 c2 是不同閉包，
# 所以 c1 的 count 仍然接續自己的狀態。
#
# 前面 c1 已經到 3，
# 這次會變成 4。
print(c1())               # 4（c1 和 c2 是各自獨立的計數器）

# ── 實際應用：用閉包做「一次性」工具函數 ────────────────
# CPE 中偶爾需要「記住狀態」但又不想寫整個 class
#
# 閉包可以在不寫 class 的情況下記住狀態。
#
# 例如：
# 我們想建立一個 visit(node) 函數，
# 它可以記住哪些 node 已經走過。
#
# 如果某個 node 第一次出現：
# 回傳 True
#
# 如果某個 node 已經出現過：
# 回傳 False
#
# 這種情況可以用閉包保存 visited 集合。

print("\n=== 閉包應用：記住已走過的節點 ===")

def make_visit_tracker():
    # visited 是一個 set。
    #
    # set 的特色是：
    # 1. 不會有重複元素
    # 2. 查詢某個元素是否存在通常很快
    #
    # 這裡用來記錄已經拜訪過的節點。
    visited = set()

    def visit(node):
        # visit() 是內部函數。
        #
        # 它會使用外層的 visited。
        #
        # 因為下面會呼叫 visited.add(node)，
        # 這是修改 set 物件的內容。
        #
        # 這段程式原本保留 nonlocal visited。
        # 雖然對 set.add() 這種「修改物件內容」來說，
        # 不一定需要 nonlocal，
        # 但保留它可以明確表達這個內部函數會使用外層 visited。
        nonlocal visited

        # 如果 node 已經在 visited 裡，
        # 代表之前走過。
        if node in visited:
            return False    # 已走過

        # 如果 node 還沒有出現過，
        # 就把它加入 visited。
        visited.add(node)

        # 回傳 True 表示這是第一次走到。
        return True         # 第一次走到

    # 回傳 visit 函數。
    #
    # 呼叫 make_visit_tracker() 後，
    # 會得到一個能記住 visited 狀態的函數。
    return visit

# 建立一個 visit 函數。
#
# 它內部記住自己的 visited set。
visit = make_visit_tracker()

# 依序拜訪節點：
# 1, 2, 1, 3, 2, 4
#
# 第一次看到 1 → True
# 第一次看到 2 → True
# 第二次看到 1 → False
# 第一次看到 3 → True
# 第二次看到 2 → False
# 第一次看到 4 → True
results = [visit(n) for n in [1, 2, 1, 3, 2, 4]]

# 印出每次拜訪是否為第一次。
print(results)  # [True, True, False, True, False, True]

# 記憶重點 ──────────────────────────────────────────────────
# 可變預設值陷阱 → 預設值用 None，函數內再建 [] 或 {}
# 閉包延遲綁定  → 用 lambda x=x: x 把值固定下來
# nonlocal      → 要「修改」外層變數時才需要，只「讀取」不用
#
# 補充整理：
#
# 1. 不要把 []、{}、set() 這種可變物件直接當預設參數。
#    安全寫法通常是先用 None，再在函數內建立新物件。
#
# 2. 函數預設參數是在 def 執行時建立，
#    不是每次呼叫函數時建立。
#
# 3. 閉包會記住外層變數，
#    但延遲綁定會讓 lambda 在真正執行時才查變數值。
#
# 4. 迴圈中建立 lambda 時，
#    如果要固定當下的值，
#    可以使用 lambda i=i: i。
#
# 5. nonlocal 用於內部函數想重新指定外層函數變數的情況。
#
# 6. 閉包可以用來記住狀態，
#    例如計數器、拜訪紀錄、快取等。