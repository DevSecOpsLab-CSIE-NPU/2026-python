# ===================================================================
# R01. 函數彈性簽章
# 學生：賴俋勳 1114405041
# 日期：2026-05-21
# 主題：*args / **kwargs / keyword-only — 讓函數接受不固定數量的參數
# ===================================================================
# 【學習心得】
#   Python 的函數簽章非常靈活：
#   *args   → 接受任意個「位置參數」，在函數內是 tuple
#   **kwargs → 接受任意個「關鍵字參數」，在函數內是 dict
#   *（單獨）→ 強制後面的參數一定要具名，避免填錯順序
#   
#   記憶順序：普通參數 → *args → keyword-only → **kwargs
# ===================================================================

# ── *args：不定個數的位置參數 ─────────────────────────────
# 問題：想加總任意幾個數字，但事先不知道有幾個。
# *args 把多餘的位置參數打包成一個 tuple。
# 函數內用 sum(args) 或 for x in args 使用。

def add_all(*args):
    """
    接受任意個數字，回傳總和。
    呼叫時：add_all(1, 2, 3) → args = (1, 2, 3)，型別是 tuple
    """
    return sum(args)   # sum() 可直接對 tuple 求和

print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())                # 0（空的 tuple 也沒問題）

# ── **kwargs：不定個數的關鍵字參數 ──────────────────────
# **kwargs 把「名稱=值」的關鍵字參數打包成一個 dict。
# 適合需要「欄位名稱不固定」的情境，例如建立資料紀錄。

def make_student(**kwargs):
    """
    建立學生資料，欄位可以自由指定（不同學生可有不同欄位）。
    呼叫時：make_student(name="王小明", grade=85) 
            → kwargs = {'name': '王小明', 'grade': 85}
    """
    return kwargs

print("\n=== **kwargs：不定個數的關鍵字參數 ===")
s = make_student(name="王小明", grade=85, seat=12)
print(s)   # {'name': '王小明', 'grade': 85, 'seat': 12}

# ── keyword-only：強制用名稱呼叫 ─────────────────────────
# 在函數簽章中，* 後面的參數「一定要具名」才能呼叫。
# 好處：避免因為填錯順序而產生難以發現的 bug。
# 例如 subject 和 score 如果位置對調，不用名稱的話不會報錯，但邏輯錯了。

def send_score(student_id, *, subject, score):
    """
    送出學生成績。
    student_id 是普通參數（位置或具名都可）。
    subject, score 在 * 後面，一定要具名呼叫：
        send_score("411234001", subject="數學", score=90)  ← 正確
        send_score("411234001", "數學", 90)               ← TypeError！
    """
    print(f"學號 {student_id}｜{subject}：{score} 分")

print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)   # 正確寫法
# 下面這行會產生 TypeError，因為 subject 和 score 是 keyword-only
# send_score("411234001", "數學", 90)  # ← 不合法！

# ── 三種參數混合使用 ───────────────────────────────────────
# 一個函數可以同時用三種方式接受參數。
# 參數順序規定：普通參數 → *args → keyword-only → **kwargs

def report(title, *scores, prefix="成績"):
    """
    title  ：普通參數（第一個）
    *scores：接受任意個分數（tuple）
    prefix ：在 *scores 後面，所以是 keyword-only（有預設值）
    """
    avg = sum(scores) / len(scores) if scores else 0
    print(f"{prefix}報告－{title}：平均 {avg:.1f}")

print("\n=== 混合：普通 + *args + 預設值 ===")
report("期中考", 80, 90, 70)                       # prefix 用預設值
report("期末考", 95, 85, 75, 100, prefix="最終")   # 覆蓋 prefix

# ─── 記憶重點 ──────────────────────────────────────────────
# *args    → tuple，接受任意個「值」
# **kwargs → dict，接受任意個「名稱=值」
# *（單獨）→ 後面的參數一定要具名（keyword-only）
# 順序：普通參數 → *args → keyword-only → **kwargs
