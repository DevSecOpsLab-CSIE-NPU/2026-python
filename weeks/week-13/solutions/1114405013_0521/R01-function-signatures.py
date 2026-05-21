# R01. 函數彈性簽章
# 讓函數可以接受「不固定數量」的參數
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出語法

# ── *args：不定個數的位置參數 ─────────────────────────────
# 問題：想加總任意幾個數字，不知道會有幾個

def add_all(*args):
    """args 在函數內是一個 tuple"""
    return sum(args)

print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())                # 0（空的也沒問題）

# ── **kwargs：不定個數的關鍵字參數 ───────────────────────
# kwargs 在函數內是一個 dict

def make_student(**kwargs):
    """建立學生資料，欄位可以自由指定"""
    return kwargs

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
s = make_student(name="王小明", grade=85, seat=12)
print(s)   # {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制用名稱呼叫 ─────────────────────────
# * 後面的參數「一定要具名」，避免填錯順序

def send_score(student_id, *, subject, score):
    """* 之後的參數必須具名，避免搞混"""
    print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)   # 正確
# send_score("411234001", "數學", 90)  # ← 這樣會 TypeError！

# ── 三種參數混合使用 ──────────────────────────────────────
def report(title, *scores, prefix="成績"):
    """title 普通參數，scores 不定個數，prefix 有預設值"""
    avg = sum(scores) / len(scores) if scores else 0
    print(f"{prefix}報告－{title}：平均 {avg:.1f}")

print("\n=== 混合：普通 + *args + 預設值 ===")
report("期中考", 80, 90, 70)
report("期末考", 95, 85, 75, 100, prefix="最終")

# ── 記憶重點 ──────────────────────────────────────────────
# ── 進階補充與常見應用範例 ─────────────────────────────────
# 呼叫時展開（unpacking）
# - 如果你有一個 list/tuple，可以用 * 展開傳給接受 *args 的參數
nums = [1, 2, 3, 4]
print('\n=== 呼叫時展開（unpack） ===')
print('add_all(*nums) =>', add_all(*nums))

# - 同理，dict 可以用 ** 展開成關鍵字參數
print('make_student(**{...}) =>', make_student(**{"name": "陳小英", "grade": 92}))

# 參數轉發（forwarding）：把任意參數轉給另一個函數
def wrapper_and_sum(*args, **kwargs):
    """範例：包一層後把收到的所有參數轉發給 add_all

    注意：add_all 只會使用位置參數，在這裡 kwargs 會被忽略
    但示範如何接收並傳遞 *args 和 **kwargs
    """
    print('wrapper 收到 kwargs:', kwargs)
    return add_all(*args)

print('\n=== 參數轉發範例 ===')
print('wrapper_and_sum(5,6,7) =>', wrapper_and_sum(5, 6, 7))

# 合併字典與覆寫預設值的技巧
def make_student_with_defaults(name, **kwargs):
    """示範把預設欄位與使用者提供的欄位合併

    用法：提供的欄位會覆寫預設值
    """
    defaults = {"grade": 0, "seat": None}
    # 先取 defaults，再用 kwargs 覆寫相同 key
    merged = {**defaults, **kwargs}
    merged['name'] = name
    return merged

print('\n=== 合併字典與覆寫範例 ===')
print(make_student_with_defaults('林小芳', grade=88))

# positional-only 與 keyword-only 的完整順序說明
# - Python 3.8+ 支援 positional-only 參數，用法在參數後加 '/'
#   def func(a, b, /, c, *, d): -> a,b 必須以位置引數提供；d 必須具名
# - 一般順序：位置參數 -> *args -> keyword-only -> **kwargs

# ── 記憶重點（詳細版）──────────────────────────────────
# *args    : 在函數內為 tuple，接受任意個位置參數
# **kwargs : 在函數內為 dict，接受任意個名稱=值
# *（單獨）: 在參數表中單獨的星號會強制後面的參數必須具名
# positional-only ('/') : 強制前面的參數只能以位置方式指定（Python 3.8+）
# 常見應用：
# - 用 * / ** 在呼叫時做 unpack（把 list/tuple 或 dict 轉成引數）
# - 用 ** 合併 dict（例如覆寫預設值）
# - 用 *args/**kwargs 做參數轉發，讓 wrapper 能接受任意參數
# 順序：普通位置參數 -> *args -> keyword-only -> **kwargs
