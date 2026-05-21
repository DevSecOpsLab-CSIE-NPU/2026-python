# R01. 函數彈性簽章
# 本範例示範 Python 中函數簽章的彈性寫法，包含：
#  - `*args`：接收任意數量的位置參數，函數內視為 tuple
#  - `**kwargs`：接收任意數量的關鍵字參數，函數內視為 dict
#  - keyword-only 參數：使用 `*` 或已有 `*args` 後，強制某些參數必須具名
#
# 學習重點：掌握參數的位置與優先順序，能寫出既靈活又具可讀性的函式介面。

# ── *args：不定個數的位置參數 ─────────────────────────────
# 問題：想加總任意幾個數字，不知道會有幾個

def add_all(*args):
        """將傳入的所有數值相加並回傳總和。

        參數：
            *args -- 任意數量的位置參數（數值），在函數內以 tuple 表示。

        回傳：
            所有傳入數值的和（若未傳入任何值，回傳 0）。

        範例：add_all(1,2,3) -> 6
        """
        return sum(args)

print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())                # 0（空的也沒問題）

# ── **kwargs：不定個數的關鍵字參數 ───────────────────────
# kwargs 在函數內是一個 dict

def make_student(**kwargs):
        """建立並回傳一個學生資料的字典，欄位可由呼叫端自由指定。

        參數：
            **kwargs -- 任意數量的關鍵字參數，例如 name="王小明", grade=85

        回傳：
            一個包含所傳欄位的 dict（直接回傳 kwargs）。
        """
        return kwargs

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
s = make_student(name="王小明", grade=85, seat=12)
print(s)   # {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制用名稱呼叫 ─────────────────────────
# * 後面的參數「一定要具名」，避免填錯順序

def send_score(student_id, *, subject, score):
        """示範 keyword-only 參數的用法。

        說明：`*` 之後列出的參數（此處為 subject, score）必須以關鍵字形式傳入，
        可避免呼叫時因參數順序錯誤而造成的混淆。

        參數：
            student_id -- 學生學號（位置參數）
            subject -- 科目名稱（keyword-only）
            score -- 分數（keyword-only）
        """
        print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)   # 正確
# send_score("411234001", "數學", 90)  # ← 這樣會 TypeError！

# ── 三種參數混合使用 ──────────────────────────────────────
def report(title, *scores, prefix="成績"):
        """混合使用普通參數、*args 與具預設值的命名參數。

        參數：
            title -- 報告標題（位置參數）
            *scores -- 任意數量的分數（位置參數，會被收成 tuple）
            prefix -- 可選的文字前綴，預設為 "成績"

        行為：計算 scores 的平均值並列印格式化報告；若未提供任何分數，平均視為 0。
        """
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
