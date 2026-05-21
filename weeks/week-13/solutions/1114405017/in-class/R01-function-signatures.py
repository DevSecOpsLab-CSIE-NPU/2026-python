# R01. 函數彈性簽章
# 讓函數可以接受「不固定數量」的參數
# 這是 Python 中非常強大的特性，允許開發者撰寫更具通用性的 API

# ── *args：不定個數的位置參數 ─────────────────────────────
# 當你不知道呼叫者會傳入多少個位置參數時，可以使用 *args。
# 在函數內部，args 會被包裝成一個 tuple。

def add_all(*args):
    """加總所有傳入的參數。"""
    # args 是一個 tuple，例如 (1, 2, 3)
    return sum(args)

print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())                # 0（空的也沒問題）

# ── **kwargs：不定個數的關鍵字參數 ───────────────────────
# 當你想接受任意數量的「具名參數」（key=value）時使用。
# 在函數內部，kwargs 會被包裝成一個 dictionary。

def make_student(**kwargs):
    """建立學生資料字典，允許動態增加屬性。"""
    # kwargs 是一個 dict，例如 {'name': '王小明', 'grade': 85}
    return kwargs

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
s = make_student(name="王小明", grade=85, seat=12)
print(s)   # {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制用名稱呼叫 ─────────────────────────
# 在參數列中使用單獨的 *，表示其後的所有參數都必須以「關鍵字參數」形式傳入。
# 這能提高代碼的可讀性，防止在參數過多時傳錯位置。

def send_score(student_id, *, subject, score):
    """
    發送成績通知。
    * 號後的 subject 和 score 強制要求具名呼叫。
    """
    print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)   # 正確
# send_score("411234001", "數學", 90)  # ← 這樣會 TypeError！

# ── 三種參數混合使用 ──────────────────────────────────────
# 定義順序必須是：一般參數 -> *args -> 具名必填參數 -> **kwargs
def report(title, *scores, prefix="成績"):
    """
    綜合報告函數。
    title: 一般參數，scores: 位置參數 tuple，prefix: 具名參數（有預設值）。
    """
    avg = sum(scores) / len(scores) if scores else 0
    print(f"{prefix}報告－{title}：平均 {avg:.1f}")

print("\n=== 混合：普通 + *args + 預設值 ===")
report("期中考", 80, 90, 70)
report("期末考", 95, 85, 75, 100, prefix="最終") # prefix 必須具名才能覆蓋預設值

# ── 記憶重點 ──────────────────────────────────────────────
# *args   → tuple，接受任意個「值」
# **kwargs → dict，接受任意個「名稱=值」
# *（單獨）→ 後面的參數一定要具名
# 順序：普通參數 → *args → keyword-only → **kwargs
