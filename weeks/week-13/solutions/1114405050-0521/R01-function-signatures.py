# R01. 函數彈性簽章
# 讓函數可以接受「不固定數量」的參數
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出語法

# ── *args：不定個數的位置參數 ─────────────────────────────
# 問題：想加總任意幾個數字，不知道會有幾個

def add_all(*args):
    """args 在函數內會變成一個 tuple (元組)，它會自動把所有傳入的位置參數打包起來"""
    return sum(args)

print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())                # 0（空的也沒問題）

# ── **kwargs：不定個數的關鍵字參數 ───────────────────────
# kwargs 在函數內是一個 dict

def make_student(**kwargs):
    """kwargs 在函數內會變成一個 dict (字典)，它會收集所有傳入的「名稱=值」關鍵字參數"""
    return kwargs

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
s = make_student(name="王小明", grade=85, seat=12)
print(s)   # {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制用名稱呼叫 ─────────────────────────
# * 後面的參數「一定要具名」，避免填錯順序

def send_score(student_id, *, subject, score):
    """單獨的星號 (*) 是個分水嶺，它表示之後的參數 (subject 與 score) 呼叫時都必須明確寫出名稱"""
    print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)   # 正確
# send_score("411234001", "數學", 90)  # ← 這樣會 TypeError！

# ── 三種參數混合使用 ──────────────────────────────────────
def report(title, *scores, prefix="成績"):
    """title 負責接第一個參數，*scores 把剩下的位置參數全包了，而 prefix 只能透過具名傳遞（且自帶預設值）"""
    # 如果 scores 裡面有成績，就計算平均數；若無，預設平均給 0
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
