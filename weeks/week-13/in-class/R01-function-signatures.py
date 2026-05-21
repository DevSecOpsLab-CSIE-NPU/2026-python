# R01. 函數彈性簽章（Function Signatures）
# 範例與說明（繁體中文）：
# 本檔說明 Python 中常見的函式參數簽章技巧，讓函數能更彈性地接收參數：
# - *args：接收任意數量的位置參數（在函式內部會變成 tuple）
# - **kwargs：接收任意數量的命名參數（在函式內部會變成 dict）
# - keyword-only（關鍵字專用參數）：使用 * 將後續參數強制為具名呼叫
# 此外也示範三種參數混用的典型範例與參數順序規範，便於記憶與設計 API。

# ── *args：不定個數的位置參數 ─────────────────────────────
# 問題：想加總任意幾個數字，不知道會有幾個

def add_all(*args):
        """
        將任意數量的數值相加。

        參數：
            *args: 任意數量的位置參數，函數內部會收到一個 tuple，例如 (1, 2, 3)

        回傳：
            傳入數值的總和（若沒有參數則回傳 0）

        注意：當使用 *args 時要確保傳入的內容都可由 sum() 相加，或在函式內處理異常類型。
        """
        return sum(args)

print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())                # 0（空的也沒問題）

# ── **kwargs：不定個數的關鍵字參數 ───────────────────────
# kwargs 在函數內是一個 dict

def make_student(**kwargs):
        """
        建立學生資料字典，欄位由呼叫端以關鍵字參數提供。

        參數：
            **kwargs: 任意數量的命名參數，例如 name="王小明", grade=85

        回傳：
            包含所有欄位的字典，方便後續存取或轉換成 JSON 等格式。

        適用情境：當欄位不固定或希望 API 接受可擴充的屬性時使用。
        """
        return kwargs

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
s = make_student(name="王小明", grade=85, seat=12)
print(s)   # {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制用名稱呼叫 ─────────────────────────
# * 後面的參數「一定要具名」，避免填錯順序

def send_score(student_id, *, subject, score):
        """
        範例示範 keyword-only 參數的語法：在 * 之後宣告的參數必須以名稱呼叫。

        參數：
            student_id: 學生識別字串（位置引數）
            subject (keyword-only): 科目名稱，呼叫時必須使用 subject=...
            score (keyword-only): 分數，呼叫時必須使用 score=...

        範例呼叫：send_score("411234001", subject="數學", score=90)
        這樣可以避免呼叫者因位置順序錯誤而把參數搞混。
        """
        print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)   # 正確
# send_score("411234001", "數學", 90)  # ← 這樣會 TypeError！

# ── 三種參數混合使用 ──────────────────────────────────────
def report(title, *scores, prefix="成績"):
        """
        混合範例：示範普通參數、*args（不定位置參數）、與帶預設值的命名參數一起使用。

        參數：
            title: 報告標題（位置引數）
            *scores: 任意多個分數（位置引數，會變成 tuple）
            prefix: 關鍵字參數，具有預設值，可透過 prefix="最終" 覆蓋

        行為：計算 scores 的平均值（若無 scores 則視為 0），並印出格式化結果。
        """
        avg = sum(scores) / len(scores) if scores else 0
        print(f"{prefix}報告－{title}：平均 {avg:.1f}")

print("\n=== 混合：普通 + *args + 預設值 ===")
report("期中考", 80, 90, 70)
report("期末考", 95, 85, 75, 100, prefix="最終")

# ── 記憶重點 ──────────────────────────────────────────────
# - *args   → 在函數內是一個 tuple，接受任意個位置引數
# - **kwargs → 在函數內是一個 dict，接受任意個命名引數（key=val）
# - 單獨的 *（star）→ 用來標示後面的參數必須以關鍵字（keyword）指定
# - 參數順序（常見）：普通參數 → *args → keyword-only → **kwargs
# - 設計 API 時建議：
#   - 使用 keyword-only 可以提高可讀性並避免位置參數錯位造成的 bug
#   - 透過 *args/**kwargs 可提供向後相容性（未來擴充參數而不破壞既有呼叫）
