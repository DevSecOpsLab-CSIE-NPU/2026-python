# R01. 函數彈性簽章（Function Signatures）
# 本檔示範 Python 常見的函數簽章技巧：
# - *args：接收任意數量的位置參數（形成 tuple）
# - **kwargs：接收任意數量的關鍵字參數（形成 dict）
# - keyword-only 參數：強制用名稱呼叫以避免參數順序錯誤
# 並說明這些寫法在實務上的用途與注意事項。


# ---------- 範例 1：*args（不定個數的位置參數） ----------
def add_all(*args):
    """
    加總任意個數的數字。

    - `*args` 在函數內會被視為一個 tuple，因此可直接對其使用 sum、len 等操作。
    - 適用情境：當呼叫方不知道會傳入多少個位置參數時，例如加總、多重欄位聚合等。
    - 注意：若傳入非數值型別，sum 會拋出 TypeError，必要時可在函式內做類型檢查或轉換。
    """
    return sum(args)


print("=== *args：不定個數的位置參數 ===")
print(add_all(1, 2))            # 3
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all())                # 0（空的 tuple 也沒問題）


# ---------- 範例 2：**kwargs（不定個數的關鍵字參數） ----------
def make_student(**kwargs):
    """
    建立學生資料（示範用）。

    - `**kwargs` 在函數內會是 dict，鍵為參數名稱，值為呼叫方傳入的值。
    - 適用情境：功能較通用的建構器或設定函式，例如把多個可選欄位打包回傳。
    """
    return kwargs


print("\n=== **kwargs：不定個數的關鍵字參數 ===")
s = make_student(name="王小明", grade=85, seat=12)
print(s)   # {'name': '王小明', 'grade': 85, 'seat': 12}


# ---------- 範例 3：keyword-only（強制具名參數） ----------
# 語法：在參數列表中放一個單獨的星號 *，之後的參數都必須使用關鍵字形式傳入
def send_score(student_id, *, subject, score):
    """
    傳送學生分數，示範 keyword-only 參數的作用。

    設計理由：當函式參數很多，或有相似型別參數（例如多個 int），
    強制使用具名參數可以避免傳入順序錯誤造成邏輯錯誤。
    """
    print(f"學號 {student_id}｜{subject}：{score} 分")


print("\n=== keyword-only：強制具名，避免填錯順序 ===")
send_score("411234001", subject="數學", score=90)   # 正確示範
# 若改成 positional 形式 send_score("411234001", "數學", 90) 會得到 TypeError


# ---------- 範例 4：混合使用位置、*args 與有預設值參數 ----------
def report(title, *scores, prefix="成績"):
    """
    示範多種類型參數混合的常見使用模式。

    - title：一般的必填位置參數
    - *scores：任意數量的位置參數，這裡代表一系列分數
    - prefix：有預設值的命名參數，可被覆寫
    """
    avg = sum(scores) / len(scores) if scores else 0
    print(f"{prefix}報告－{title}：平均 {avg:.1f}")


print("\n=== 混合：普通 + *args + 預設值 ===")
report("期中考", 80, 90, 70)
report("期末考", 95, 85, 75, 100, prefix="最終")


# ---------- 記憶重點（總結） ----------
# - *args   → 函數內為 tuple，接受任意個位置參數（值）
# - **kwargs → 函數內為 dict，接受任意個關鍵字參數（名稱=值）
# - 單獨的星號 * → 後面的參數為 keyword-only，呼叫時必須使用名稱指定
# - 參數順序（函式定義時）：普通參數 → *args → keyword-only → **kwargs
# - 實務建議：
#   * 在 API 設計時，對於可選但較多的參數，用 **kwargs 或者 keyword-only 可以提高可讀性
#   * 在需要明確語意的情況下，用 partial、dataclass 或明確的參數命名比濫用 **kwargs 更佳
