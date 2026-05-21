"""
R01. 函數彈性簽章（Function Signatures）範例

說明：展示 Python 常見的函數簽章技巧，包括 `*args`、`**kwargs`、
keyword-only 參數與混合使用情境。每個函式皆附上繁體中文 docstring，
說明參數用途、型別預期與回傳值，方便教學與作業使用。
"""

# ── *args：不定個數的位置參數（variadic positional arguments） ────────
# 範例情境：想加總任意個數的數字，但呼叫時不確定會傳入多少個值

def add_all(*args):
    """將任意數量的位置參數相加並回傳總和。

    參數：
    - *args: 任意個位置參數，預期為可相加的數值（如 int 或 float）。

    回傳：傳入值的總和（若未提供任何參數，回傳 0）。
    """
    return sum(args)

print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())                # 0（空的也沒問題）

# ── **kwargs：不定個數的關鍵字參數 ───────────────────────
# kwargs 在函數內是一個 dict

def make_student(**kwargs):
    """建立學生資料並以字典回傳。

    參數：
    - **kwargs: 任意數量的關鍵字參數，會被收集成一個 dict，key 為欄位名稱。

    回傳：包含所有傳入欄位的字典（例如 name、grade、seat 等）。
    """
    return kwargs

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
s = make_student(name="王小明", grade=85, seat=12)
print(s)   # {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制用名稱呼叫 ─────────────────────────
# * 後面的參數「一定要具名」，避免填錯順序

def send_score(student_id, *, subject, score):
    """示範 keyword-only 參數：強制以參名呼叫以避免位置參數順序錯誤。

    參數：
    - student_id: 學生編號（位置參數）
    - subject: 科目名稱（必須具名）
    - score: 分數（必須具名）

    此函式僅示範輸出格式，不回傳值。
    """
    print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)   # 正確
# send_score("411234001", "數學", 90)  # ← 這樣會 TypeError！

# ── 三種參數混合使用 ──────────────────────────────────────
def report(title, *scores, prefix="成績"):
    """綜合範例：混合普通參數、可變位置參數與預設參數。

    參數：
    - title: 報告標題（字串）
    - *scores: 任意個數的分數（位置參數），可省略
    - prefix: 報表前綴（具預設值），可用具名參數修改

    行為：計算分數平均（若無分數則平均視為 0），並印出格式化報表。
    """
    avg = sum(scores) / len(scores) if scores else 0
    print(f"{prefix}報告－{title}：平均 {avg:.1f}")

print("\n=== 混合：普通 + *args + 預設值 ===")
report("期中考", 80, 90, 70)
report("期末考", 95, 85, 75, 100, prefix="最終")

# ── 記憶重點 ──────────────────────────────────────────────
# - `*args`   → 會在函數內變成 tuple，適合接收任意數量的位置參數
# - `**kwargs`→ 會在函數內變成 dict，適合接收任意數量的關鍵字參數
# - 單獨的 `*`：將其後的參數定為 keyword-only，呼叫時需以參名傳入
# - 參數順序：普通參數 → *args → keyword-only → **kwargs
