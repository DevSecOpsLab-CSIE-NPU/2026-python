# R02. JSON 基礎讀寫（6.2）
# json.loads / json.dumps / json.load / json.dump

import json

# ── 字串 ↔ Python 物件 ───────────────────────────────────
# 【詳解】
# JSON 是現代 Web 最通用的資料交換格式。
# json.dumps(obj) → 將 Python 物件序列化成 JSON 字串。
# json.loads(str) → 將 JSON 字串反序列化回 Python 物件。
# 這兩個是「記憶體操作」，若要寫入/讀取檔案用 dump/load。
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）
s = json.dumps(data)
print(type(s), s)

# 美化輸出
# indent=4 → 縮排 4 格，讓輸出易讀（但檔案略大）
# sort_keys=True → 按鍵名字母順序排列，讓輸出穩定（利於版本管控）
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# 反序列化（JSON 字串 → Python）
obj = json.loads(s)
print(type(obj), obj["name"])

# ── 檔案 I/O ─────────────────────────────────────────────
# 【詳解】
# json.dump(obj, file) → 寫入檔案（無 s，直接操作 file object）
# json.load(file) → 從檔案讀入（無 s，直接操作 file object）
# ensure_ascii=False → 保留中文等非 ASCII 字元（不轉成 \uXXXX）
# 寫檔時用 encoding="utf-8" 避免 BOM、encoding="utf-8-sig" 相容 Excel
# 寫出到檔案
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀入
with open("/tmp/data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)

# ── 型別對應 ──────────────────────────────────────────────
# 【詳解】
# 需要記住 Python 與 JSON 的型別對應。
# Python 的 tuple 會變成 JSON array，反序列化時無法復原為 tuple。
# 若需要保留 tuple，需自訂 default 與 object_hook 參數。
# Python dict   → JSON object  {}
# Python list   → JSON array   []
# Python str    → JSON string  ""
# Python int    → JSON number
# Python float  → JSON number
# Python True   → JSON true
# Python None   → JSON null

print(json.dumps([1, True, None, "hello"]))
# [1, true, null, "hello"]

# ── 中文不跳脫 ───────────────────────────────────────────
# 【詳解】
# ensure_ascii=False 是 Python 處理中文 JSON 的關鍵。
# 預設（ensure_ascii=True）會把中文轉成 \uXXXX，檔案龐大、難讀。
# 改用 ensure_ascii=False，中文直接存入，檔案更小、更易查看。
record = {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=False))   # {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=True))    # {"城市": "澎湖", ...}
