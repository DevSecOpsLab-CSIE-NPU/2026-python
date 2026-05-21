# R01. 函數彈性簽章 (Function Signatures)
# 讓函數可以接受「不固定數量」或「特定呼叫方式」的參數。
# 對應 Bloom's Taxonomy：記憶 (Remember) — 能背得出語法並正確辨識其用途。

# ── *args：不定個數的位置參數 (Positional Arguments) ─────────────────────────
# 問題場景：當你想寫一個可以加總「任意數量」數字的函數，但事先不知道使用者會傳入幾個。

def add_all(*args):
    """
    args 在函數內部會被包裝成一個元組 (tuple)。
    這讓我們可以使用 sum()、len() 或進行迴圈遍歷。
    """
    return sum(args)

print("=== *args：不定個數的位置參數 ===")
print(f"兩個參數：{add_all(1, 2)}")               # 傳入 (1, 2)
print(f"五個參數：{add_all(1, 2, 3, 4, 5)}")     # 傳入 (1, 2, 3, 4, 5)
print(f"零個參數：{add_all()}")                  # 傳入 ()，結果為 0，非常彈性

# ── **kwargs：不定個數的關鍵字參數 (Keyword Arguments) ──────────────────────
# kwargs 在函數內部會被包裝成一個字典 (dict)。
# 這適合用於「欄位名稱」不固定，或需要彈性擴充標籤的情境。

def make_student(**kwargs):
    """
    建立學生資料，使用者可以自由指定參數名稱與數值。
    """
    return kwargs

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
# 這裡的 name, grade, seat 會變成 dict 的 key
s = make_student(name="王小明", grade=85, seat=12)
print(f"產生的學生字典：{s}")   # {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制使用名稱呼叫 ─────────────────────────
# 在參數列中使用一個單獨的 `*`，代表之後的所有參數「一定要具名」。
# 優點：避免在參數很多時，因為填錯順序而產生邏輯錯誤。

def send_score(student_id, *, subject, score):
    """
    * 號之後的 subject 與 score 必須明確寫出名稱才能呼叫。
    """
    print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名呼叫 ===")
# ✅ 正確呼叫方式
send_score("411234001", subject="數學", score=90)

# ❌ 錯誤呼叫方式：send_score("411234001", "數學", 90) 
# 會噴出 TypeError: send_score() takes 1 positional argument but 3 were given

# ── 三種參數混合使用 ──────────────────────────────────────
# 定義順序建議：普通參數 -> *args -> 預設參數 (keyword-only) -> **kwargs

def report(title, *scores, prefix="[成績報告]"):
    """
    title: 普通位置參數 (必填)
    *scores: 不定數量的成績 (tuple)
    prefix: 具名預設參數
    """
    count = len(scores)
    avg = sum(scores) / count if count > 0 else 0
    print(f"{prefix} {title}：共 {count} 筆成績，平均 {avg:.1f} 分")

print("\n=== 混合應用示範 ===")
report("期中考", 80, 90, 70)                          # 使用預設 prefix
report("期末考", 95, 85, 75, 100, prefix="[最終結果]") # 覆寫預設值

# 記憶重點 ──────────────────────────────────────────────
# 1. *args    → 包裝成 tuple，收集所有剩餘的「值」。
# 2. **kwargs → 包裝成 dict，收集所有剩餘的「名稱=值」。
# 3. * (單獨) → 強制後方參數必須使用關鍵字 (Key=Value) 形式呼叫。
# 4. 參數排列順序：(positional, *args, keyword_only, **kwargs)。
