# R02. JSON 基礎讀寫（6.2）
# json.loads / json.dumps / json.load / json.dump

import json

# ── 字串 ↔ Python 物件 ───────────────────────────────────
# 先準備一個 Python 的資料結構，後面拿來示範序列化與反序列化。
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）
s = json.dumps(data)
# dumps 會把 Python 物件轉成 JSON 字串。
print(type(s), s)

# 美化輸出
s_pretty = json.dumps(data, indent=4, sort_keys=True)
# indent 讓 JSON 更好讀，sort_keys 讓欄位排序固定。
print(s_pretty)

# 反序列化（JSON 字串 → Python）
obj = json.loads(s)
# loads 會把 JSON 字串還原成 Python 物件。
print(type(obj), obj["name"])

# ── 檔案 I/O ─────────────────────────────────────────────
# 寫出到檔案
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    # dump 直接寫入檔案，不需要先手動存成字串。
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀入
with open("/tmp/data.json", "r", encoding="utf-8") as f:
    # load 直接從檔案讀回 Python 物件。
    loaded = json.load(f)
print(loaded)

# ── 型別對應 ──────────────────────────────────────────────
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
# ensure_ascii=False 才會保留中文原樣輸出。
record = {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=False))   # {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=True))    # {"城市": "澎湖", ...}
