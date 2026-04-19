# U05. 日期時間的陷阱（3.12–3.15）
# timedelta 不支援月份 / strptime 效能問題

# 導入 timeit 模組，用於測量程式碼執行時間，比較不同實現的效能。
import timeit
# 導入 calendar 模組，提供許多與日曆相關的實用函數，例如計算某月有幾天。
import calendar
# 從 datetime 模組導入 datetime 類別 (日期和時間) 以及 timedelta 類別 (時間間隔)。
from datetime import datetime, timedelta

# ── timedelta 不支援月份（3.12）──────────────────────
# 說明：因為每個月的天數不固定（28 到 31 天），Python 標準函式庫的 timedelta 物件
# 不支援直接使用 `months` 或 `years` 作為參數進行加減。

# 建立一個基準日期：2012年9月23日
dt = datetime(2012, 9, 23)
try:
    # 嘗試使用 timedelta 加上一個月，這會引發 TypeError。
    # `type: ignore[call-arg]` 是給型別檢查工具 (如 mypy) 看的，忽略此處的引數錯誤。
    dt + timedelta(months=1)
except TypeError as e:
    # 捕獲並印出錯誤訊息，證明不能這樣操作。
    print(f"TypeError: {e}")  # 'months' is an invalid keyword argument


# 說明：若要精確地加減月份，正確做法是手動計算目標年份和月份，
# 並將可能超出範圍的天數限制 (clamp) 在該月的最後一天（例如 1/31 加一個月應該是 2/28 或 2/29）。
def add_one_month(dt: datetime) -> datetime:
    # 計算目標的年與月
    year = dt.year
    month = dt.month + 1
    # 如果月份加 1 後變成 13，代表跨年了，需要將年份加 1，月份重置為 1 月。
    if month == 13:
        year += 1
        month = 1

    # 取得目標月份的天數，並把日期限制在該月最後一天
    # calendar.monthrange(year, month) 會回傳一個 tuple：(該月第一天是星期幾, 該月總天數)
    # 我們只關心總天數，所以第一個回傳值用底線 `_` 忽略。
    _, days_in_target_month = calendar.monthrange(year, month)
    # 使用 min() 確保天數不會超過目標月份的最大天數。
    # 舉例：如果原本是 1/31，加上一個月變成 2 月，2 月最多只有 28 或 29 天，min(31, 29) 會得到 29。
    day = min(dt.day, days_in_target_month)

    # 使用 replace() 方法回傳一個更新了年、月、日的新 datetime 物件。
    return dt.replace(year=year, month=month, day=day)


# 測試：2012 是閏年，1/31 加一個月應該變成 2/29。
print(add_one_month(datetime(2012, 1, 31)))  # 輸出: 2012-02-29 00:00:00
# 測試：9/23 加一個月變成 10/23。
print(add_one_month(datetime(2012, 9, 23)))  # 輸出: 2012-10-23 00:00:00

# ── strptime 效能問題（3.15）─────────────────────────
# 說明：datetime.strptime() 在解析字串時，底層使用了純 Python 實作，並包含較為複雜的正則表達式處理。
# 因此，在需要大量解析「已知且格式固定」的日期字串時（例如處理幾百萬行的 CSV），
# 直接使用原生的字串切割 (split) 和整數轉換 (int) 效能會好非常多。

# 產生一個包含 2012 年每一天前 28 天的字串列表，用於效能測試。
dates = [f"2012-{m:02d}-{d:02d}" for m in range(1, 13) for d in range(1, 29)]

# 方法一：使用標準的 strptime() 函數解析。
def use_strptime(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%d")

# 方法二：使用手動字串切割與整數轉換解析。
def use_manual(s: str) -> datetime:
    y, m, d = s.split("-")
    return datetime(int(y), int(m), int(d))

# 確保兩種方法解析出來的結果是一模一樣的。
assert use_strptime("2012-09-20") == use_manual("2012-09-20")

# 使用 timeit 測量標準方法解析整個列表 100 次所需的時間。
t1 = timeit.timeit(lambda: [use_strptime(d) for d in dates], number=100)
# 使用 timeit 測量手動方法解析整個列表 100 次所需的時間。
t2 = timeit.timeit(lambda: [use_manual(d) for d in dates], number=100)
# 輸出比較結果，手動解析通常會比 strptime 至少快 5 到 7 倍。
print(f"strptime: {t1:.3f}s  手動解析: {t2:.3f}s（快 {t1 / t2:.1f} 倍）")
