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
# *args   → tuple，接受任意個「值」
# **kwargs → dict，接受任意個「名稱=值」
# *（單獨）→ 後面的參數一定要具名
# 順序：普通參數 → *args → keyword-only → **kwargs
