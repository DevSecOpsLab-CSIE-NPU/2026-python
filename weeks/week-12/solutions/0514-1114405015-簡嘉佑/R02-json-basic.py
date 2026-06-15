# R02. JSON 基礎讀寫（6.2）
# json.loads / json.dumps / json.load / json.dump
#
# JSON（JavaScript Object Notation）是目前最流行的資料交換格式，
# 廣泛用於 REST API、設定檔、前後端溝通等場景。
# Python 的 json 標準庫提供四個核心函式：
#   dumps / loads → 字串層級的序列化 / 反序列化
#   dump  / load  → 直接對檔案物件操作

import json

# ── 字串 ↔ Python 物件 ───────────────────────────────────
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）
# json.dumps 回傳 str，適合存到變數或透過網路傳輸
s = json.dumps(data)
print(type(s), s)   # <class 'str'> {"name": "Alice", ...}

# 美化輸出：indent 設縮排空格數，sort_keys 讓鍵值字母排序
# 適合寫入設定檔、方便人工閱讀
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# 反序列化（JSON 字串 → Python）
# json.loads 的 s 代表「string」，輸入必須是 str 或 bytes
obj = json.loads(s)
print(type(obj), obj["name"])   # <class 'dict'> Alice

# ── 檔案 I/O ─────────────────────────────────────────────
# json.dump / json.load 直接對檔案物件操作，不需要中間字串變數
# ensure_ascii=False 讓中文直接輸出，而不是跳脫成 \uXXXX 編碼
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀回，得到與原始 data 等價的 Python 物件
with open("/tmp/data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)

# ── 型別對應 ──────────────────────────────────────────────
# Python dict   → JSON object  {}   （最外層也常是 object）
# Python list   → JSON array   []   （有序序列）
# Python str    → JSON string  ""   （必須雙引號）
# Python int    → JSON number       （無小數點）
# Python float  → JSON number       （有小數點）
# Python True   → JSON true         （小寫）
# Python None   → JSON null         （小寫）
# ⚠️ tuple 序列化後變成 array，反序列化回來是 list，不再是 tuple！

print(json.dumps([1, True, None, "hello"]))
# [1, true, null, "hello"]

# ── 中文不跳脫 ───────────────────────────────────────────
# 預設 ensure_ascii=True 會把所有非 ASCII 字元轉成 \uXXXX 跳脫序列，
# 雖然合法，但可讀性差；設 False 直接保留中文字。
record = {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=False))   # {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=True))    # {"\u57ce\u5e02": "\u6f8e\u6e56", ...}
