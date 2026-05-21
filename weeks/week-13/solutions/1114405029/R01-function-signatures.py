# R01. 函數彈性簽章
# 讓函數可以接受「不固定數量」的參數
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出語法
#
# 本題核心：
# Python 函數的參數不一定只能固定一個、兩個或三個。
# 有時候我們會希望函數可以接受「任意數量」的參數。
#
# 例如：
# 1. 想加總很多數字，但不知道會傳幾個
# 2. 想建立學生資料，但欄位名稱不固定
# 3. 想強制某些參數一定要用名稱指定，避免填錯順序
#
# 這份程式會練習三個重要語法：
#
# 1. *args
#    用來接收不固定數量的「位置參數」。
#    在函數內，args 會變成 tuple。
#
# 2. **kwargs
#    用來接收不固定數量的「關鍵字參數」。
#    在函數內，kwargs 會變成 dict。
#
# 3. keyword-only
#    使用單獨的 *，強制 * 後面的參數一定要用「名稱=值」來呼叫。
#
# 這些語法常用在：
# 函數設計、工具函數、資料處理、框架 API、測試輔助函數中。

# ── *args：不定個數的位置參數 ─────────────────────────────
# 問題：想加總任意幾個數字，不知道會有幾個
#
# 位置參數：
# 指的是呼叫函數時，直接依照順序傳入的值。
#
# 例如：
# add_all(1, 2, 3)
#
# 這裡的 1、2、3 都是位置參數。
#
# *args 的意思是：
# 把多出來、不固定數量的位置參數全部收集起來。
#
# 在函數內部，args 會是一個 tuple。
#
# 例如：
# add_all(1, 2, 3)
# 則 args 會是：
# (1, 2, 3)

def add_all(*args):
    """args 在函數內是一個 tuple"""

    # sum(args) 會把 args 這個 tuple 裡面的所有數字加總。
    #
    # 例如：
    # args = (1, 2)
    # sum(args) = 3
    #
    # args = (1, 2, 3, 4, 5)
    # sum(args) = 15
    #
    # 如果 args 是空 tuple，也就是沒有傳任何數字：
    # args = ()
    # sum(args) 會得到 0。
    return sum(args)

# 印出區塊標題，方便觀察 *args 的示範輸出。
print("=== *args：不定個數的位置參數 ===")

# 傳入兩個位置參數 1 和 2。
#
# 在 add_all() 裡面：
# args = (1, 2)
#
# 回傳：
# 1 + 2 = 3
print(add_all(1, 2))            # 3

# 傳入五個位置參數。
#
# 在 add_all() 裡面：
# args = (1, 2, 3, 4, 5)
#
# 回傳：
# 1 + 2 + 3 + 4 + 5 = 15
print(add_all(1, 2, 3, 4, 5))  # 15

# 沒有傳入任何參數。
#
# 在 add_all() 裡面：
# args = ()
#
# 空的 tuple 也可以被 sum() 處理，
# 結果會是 0。
print(add_all())                # 0（空的也沒問題）

# ── **kwargs：不定個數的關鍵字參數 ───────────────────────
# kwargs 在函數內是一個 dict
#
# 關鍵字參數：
# 指的是呼叫函數時，用「名稱=值」的方式傳入。
#
# 例如：
# make_student(name="王小明", grade=85, seat=12)
#
# 這裡的：
# name="王小明"
# grade=85
# seat=12
#
# 都是關鍵字參數。
#
# **kwargs 的意思是：
# 把不固定數量的關鍵字參數全部收集起來。
#
# 在函數內部，kwargs 會是一個 dictionary。
#
# 例如：
# kwargs = {
#     "name": "王小明",
#     "grade": 85,
#     "seat": 12
# }

def make_student(**kwargs):
    """建立學生資料，欄位可以自由指定"""

    # 這個函數直接回傳 kwargs。
    #
    # 因為 kwargs 本身就是一個 dict，
    # 所以可以用來表示一筆學生資料。
    #
    # 好處是欄位可以自由指定，
    # 不一定只能固定 name、grade 或 seat。
    return kwargs

# 印出區塊標題，方便觀察 **kwargs 的示範輸出。
print("\n=== **kwargs：不定個數的關鍵字參數 ===")

# 呼叫 make_student() 時，
# 使用 name、grade、seat 三個關鍵字參數。
#
# 在 make_student() 裡面：
# kwargs 會變成：
# {
#     "name": "王小明",
#     "grade": 85,
#     "seat": 12
# }
s = make_student(name="王小明", grade=85, seat=12)

# 印出學生資料 dictionary。
print(s)   # {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制用名稱呼叫 ─────────────────────────
# * 後面的參數「一定要具名」，避免填錯順序
#
# keyword-only 的意思是：
# 某些參數不能只靠位置傳入，
# 必須明確寫出參數名稱。
#
# 這樣可以避免參數順序混淆。
#
# 例如：
# send_score("411234001", subject="數學", score=90)
#
# 這樣看起來很清楚：
# student_id 是 "411234001"
# subject 是 "數學"
# score 是 90
#
# 如果允許全部用位置傳入：
# send_score("411234001", "數學", 90)
#
# 當參數變多時就容易搞錯順序。
#
# 在函數定義中，單獨的 * 代表：
# 從這個 * 後面的參數開始，
# 呼叫時都必須使用「參數名稱=值」。

def send_score(student_id, *, subject, score):
    """* 之後的參數必須具名，避免搞混"""

    # student_id 是普通位置參數，
    # 可以直接用順序傳入。
    #
    # subject 和 score 位在 * 後面，
    # 所以是 keyword-only 參數。
    #
    # 呼叫時必須寫成：
    # subject="數學"
    # score=90
    #
    # 這樣可以讓輸出成績時比較不容易把科目和分數填反。
    print(f"學號 {student_id}｜{subject}：{score} 分")

# 印出區塊標題，方便觀察 keyword-only 的示範輸出。
print("\n=== keyword-only：強制具名，避免填錯順序 ===")

# 正確呼叫方式：
#
# 第一個參數 student_id 可以用位置參數傳入。
# subject 和 score 必須用名稱指定。
send_score("411234001", subject="數學", score=90)   # 正確

# 下面這行被註解掉，表示它不會執行。
#
# 如果取消註解，會發生 TypeError。
#
# 原因：
# subject 和 score 是 keyword-only 參數，
# 不能直接用位置傳入。
# send_score("411234001", "數學", 90)  # ← 這樣會 TypeError！

# ── 三種參數混合使用 ──────────────────────────────────────
#
# 這段示範普通參數、*args、以及有預設值的 keyword-only 參數混合使用。
#
# 函數參數順序很重要：
#
# 1. 普通參數
#    例如 title
#
# 2. *args
#    收集不固定數量的位置參數
#    例如 *scores
#
# 3. keyword-only 參數
#    例如 prefix="成績"
#
# 在 def report(title, *scores, prefix="成績") 中：
#
# title：
# 必填的普通參數。
#
# *scores：
# 接收任意數量的成績。
#
# prefix：
# 因為它出現在 *scores 後面，
# 所以它必須用名稱指定，
# 例如 prefix="最終"。
#
# 如果沒有指定 prefix，
# 就會使用預設值 "成績"。

def report(title, *scores, prefix="成績"):
    """title 普通參數，scores 不定個數，prefix 有預設值"""

    # scores 是由 *scores 收集到的 tuple。
    #
    # 例如：
    # report("期中考", 80, 90, 70)
    #
    # 在函數內：
    # title = "期中考"
    # scores = (80, 90, 70)
    # prefix = "成績"
    #
    # 這行用條件運算式避免 scores 為空時除以 0。
    #
    # 如果 scores 不是空的：
    # avg = sum(scores) / len(scores)
    #
    # 如果 scores 是空的：
    # avg = 0
    avg = sum(scores) / len(scores) if scores else 0

    # 印出報告結果。
    #
    # {avg:.1f} 代表平均值顯示到小數點後 1 位。
    print(f"{prefix}報告－{title}：平均 {avg:.1f}")

# 印出混合參數示範區塊標題。
print("\n=== 混合：普通 + *args + 預設值 ===")

# 呼叫 report()：
#
# title = "期中考"
# scores = (80, 90, 70)
# prefix 使用預設值 "成績"
#
# 平均：
# (80 + 90 + 70) / 3 = 80.0
report("期中考", 80, 90, 70)

# 呼叫 report()：
#
# title = "期末考"
# scores = (95, 85, 75, 100)
# prefix = "最終"
#
# 注意：
# prefix 位在 *scores 後面，
# 所以必須用 prefix="最終" 的方式傳入。
#
# 平均：
# (95 + 85 + 75 + 100) / 4 = 88.75
# 顯示到小數點後 1 位會變成 88.8。
report("期末考", 95, 85, 75, 100, prefix="最終")

# ── 記憶重點 ──────────────────────────────────────────────
# *args   → tuple，接受任意個「值」
# **kwargs → dict，接受任意個「名稱=值」
# *（單獨）→ 後面的參數一定要具名
# 順序：普通參數 → *args → keyword-only → **kwargs
#
# 補充整理：
#
# 1. *args
#    適合用在不知道會傳幾個值的情況。
#    例如加總、平均、批次處理資料。
#
# 2. **kwargs
#    適合用在欄位或設定項目不固定的情況。
#    例如建立資料、設定參數、傳遞選項。
#
# 3. keyword-only
#    適合用在希望呼叫者明確寫出參數名稱的情況。
#    可以增加可讀性，也可以降低填錯順序的風險。
#
# 4. 混合使用時要注意順序：
#    普通參數 → *args → keyword-only → **kwargs
#
# 5. 真正寫大型程式時，
#    參數設計會影響函數是否好讀、好用、好維護。