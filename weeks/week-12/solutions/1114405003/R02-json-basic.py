# R02. JSON 基礎讀寫（6.2）
# 主題：`json.loads` / `json.dumps` / `json.load` / `json.dump`
# 說明語言：繁體中文（臺灣 zh-TW），並補充每個步驟的目的、型別轉換與常見注意事項

import json
import tempfile
from pathlib import Path

# ── 字串 ↔ Python 物件 ───────────────────────────────────
# JSON 最常見的用途，是在「Python 物件」與「JSON 字串」之間做轉換。
# 這段範例先建立一個 Python 的 `dict`，裡面同時包含字串、整數與串列，
# 用來示範 JSON 可以如何表示巢狀資料。
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）
# `json.dumps()` 會把 Python 物件轉成 JSON 格式的字串。
# 這裡回傳的是「字串」，不是檔案，也不是 dict；因此可以直接印出、傳給 API，
# 或者進一步寫入檔案。
s = json.dumps(data)
print(type(s), s)

# 美化輸出
# `indent=4` 會讓輸出的 JSON 具有縮排，方便閱讀與除錯。
# `sort_keys=True` 則會把 key 依字母順序排序，讓結果更穩定，適合比較輸出內容。
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# 反序列化（JSON 字串 → Python）
# `json.loads()` 則是反過來，把 JSON 字串還原成 Python 物件。
# 轉回來之後，`obj` 會是 `dict`，因此可以像一般字典一樣用 key 存取資料。
obj = json.loads(s)
print(type(obj), obj["name"])

# ── 檔案 I/O ─────────────────────────────────────────────
# 實務上 JSON 常常不是單純存在變數，而是要寫進檔案或從檔案讀回來。
# `json.dump()` / `json.load()` 就是專門處理檔案物件的版本。

# 寫出到檔案
# 這裡不直接寫死 `/tmp/data.json`，而是先取得系統暫存目錄，
# 這樣在 Windows、macOS、Linux 上都能正常運作。
tmp_path = Path(tempfile.gettempdir()) / "data.json"

# `open(..., "w", encoding="utf-8")`：
# - `"w"` 表示寫入模式，如果檔案不存在會建立新檔。
# - `encoding="utf-8"` 可避免中文變成亂碼，尤其在跨平台時很重要。
# `ensure_ascii=False` 代表中文會以原樣輸出，而不是被轉成 `\uXXXX` 形式。
with open(tmp_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀入
# `json.load()` 會直接從檔案物件讀取內容並轉成 Python 物件。
# 這裡使用 `"r"` 讀取模式，表示要把前面寫出的 JSON 再讀回來。
with open(tmp_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)

# ── 型別對應 ──────────────────────────────────────────────
# JSON 與 Python 的型別不是完全一樣，所以使用時要知道對應關係：
# - Python dict   → JSON object  {}
# - Python list   → JSON array   []
# - Python str    → JSON string  ""
# - Python int    → JSON number
# - Python float  → JSON number
# - Python True   → JSON true
# - Python None   → JSON null
# 注意：JSON 沒有 `tuple`、`set` 這種型別，若直接序列化可能需要先轉成 list。

# 這行示範混合型別的序列化結果。
# 輸出時 Python 的 `True` 和 `None` 會自動對應成 JSON 的 `true` 和 `null`。
print(json.dumps([1, True, None, "hello"]))
# [1, true, null, "hello"]

# ── 中文不跳脫 ───────────────────────────────────────────
# JSON 預設會把非 ASCII 字元轉成跳脫序列，例如中文可能變成 `\u6f22\u5b57`。
# 如果你希望保留原本中文內容，請把 `ensure_ascii=False`。
record = {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=False))   # {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=True))    # 中文會被轉成跳脫字元形式

# ── 常見提醒 ─────────────────────────────────────────────
# - `json.dumps()` / `json.loads()` 處理的是「字串」。
# - `json.dump()` / `json.load()` 處理的是「檔案物件」。
# - 若物件中含有日期、集合、類別實例等特殊型別，預設無法直接 JSON 化，需要自訂轉換方式。
# - 寫入檔案時建議固定使用 UTF-8，讀回來時也要一致，避免跨系統出現編碼問題。