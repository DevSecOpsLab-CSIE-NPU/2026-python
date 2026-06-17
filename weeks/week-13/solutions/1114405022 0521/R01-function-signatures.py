# R01. 函數彈性簽章
# 讓函數可以接受「不固定數量」的參數
# 對應 Bloom's Taxonomy：記憶（Remember）— 背得出語法

# ── *args：不定個數的位置參數 ─────────────────────────────
# 問題：想加總任意幾個數字，不知道會有幾個

def add_all(*args):
    """
    接受任意數量的位置參數
    *args 的 * 表示「把剩下的位置參數全部收集成一個 tuple」
    """
    return sum(args)  # args 在函數內是一個 tuple，可以直接傳給 sum()

print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))            # 傳入 2 個參數，args = (1, 2)，回傳 3
print(add_all(1, 2, 3, 4, 5))  # 傳入 5 個參數，args = (1,2,3,4,5)，回傳 15
print(add_all())                # 不傳任何參數，args = ()，回傳 0（空的也沒問題）

# ── **kwargs：不定個數的關鍵字參數 ───────────────────────
# kwargs 在函數內是一個 dict

def make_student(**kwargs):
    """
    接受任意數量的關鍵字參數
    **kwargs 的 ** 表示「把剩下的關鍵字參數全部收集成一個 dict」
    """
    return kwargs  # 直接把收集到的 dict 回傳

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
# 傳入三個關鍵字參數，kwargs = {"name": "王小明", "grade": 85, "seat": 12}
s = make_student(name="王小明", grade=85, seat=12)
print(s)   # 輸出 {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制用名稱呼叫 ─────────────────────────
# * 後面的參數「一定要具名」，避免填錯順序

def send_score(student_id, *, subject, score):
    """
    * 是「分隔符號」
    在 * 之前的參數（student_id）可以位置傳入
    在 * 之後的參數（subject, score）必須具名（強制使用 keyword argument）
    """
    print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)   # 正確：subject 和 score 都具名
# send_score("411234001", "數學", 90)  # ← 這樣會 TypeError！因為 * 後的參數必須具名

# ── 三種參數混合使用 ──────────────────────────────────────
def report(title, *scores, prefix="成績"):
    """
    混合三種參數的範例
    title   ：一般位置參數（必填）
    *scores ：收集所有額外的位置參數成 tuple
    prefix  ：keyword-only 參數（因在 *scores 之後），有預設值
    """
    # 如果有 scores 則計算平均，否則為 0
    avg = sum(scores) / len(scores) if scores else 0
    print(f"{prefix}報告－{title}：平均 {avg:.1f}")

print("\n=== 混合：普通 + *args + 預設值 ===")
report("期中考", 80, 90, 70)      # title="期中考", scores=(80,90,70), prefix 用預設
report("期末考", 95, 85, 75, 100, prefix="最終")  # 指定 prefix="最終"

# ── 記憶重點 ──────────────────────────────────────────────
# *args   → tuple，接受任意個「值」
# **kwargs → dict，接受任意個「名稱=值」
# *（單獨）→ 後面的參數一定要具名
# 順序：普通參數 → *args → keyword-only → **kwargs
