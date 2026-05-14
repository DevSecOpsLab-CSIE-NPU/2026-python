# R02. JSON 基礎讀寫（6.2）
# json.loads / json.dumps / json.load / json.dump

import json

# 這份示範主要在說明：
# 1) Python 物件如何轉成 JSON
# 2) JSON 字串如何轉回 Python 物件
# 3) 如何直接對檔案做讀寫
# 4) 中文內容為什麼有時候會被跳脫成 \uXXXX

# ── 字串 ↔ Python 物件 ───────────────────────────────────
# 先準備一個 Python dict，之後會拿它示範序列化與反序列化。
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）
# dumps 的 d 代表 data，意思是把 Python 物件轉成 JSON 字串。
# 轉換後得到的是 str，不是 dict。
s = json.dumps(data)
print(type(s), s)

# 美化輸出
# indent 會加入縮排，讓 JSON 比較容易閱讀。
# sort_keys=True 會依 key 名稱排序，方便比對或除錯。
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# 反序列化（JSON 字串 → Python）
# loads 的 l 代表 string（字串），把 JSON 文字解析回 Python 物件。
# 解析後通常會回到 dict / list / str / int 等 Python 型別。
obj = json.loads(s)
print(type(obj), obj["name"])

# ── 檔案 I/O ─────────────────────────────────────────────
# 寫出到檔案
# dump 是把 Python 物件直接寫到檔案。
# encoding="utf-8" 可確保中文正確編碼。
# ensure_ascii=False 表示中文不要被轉成 \uXXXX，輸出會比較直觀。
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀入
# load 是直接從檔案物件讀 JSON，並轉回 Python 物件。
with open("/tmp/data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)

# ── 型別對應 ──────────────────────────────────────────────
# JSON 與 Python 的常見對應關係如下：
# Python dict   → JSON object  {}
# Python list   → JSON array   []
# Python str    → JSON string  ""
# Python int    → JSON number
# Python float  → JSON number
# Python True   → JSON true
# Python None   → JSON null

# 這行示範混合型別資料在 JSON 中的呈現方式：
# True 會變成 true，None 會變成 null。
print(json.dumps([1, True, None, "hello"]))
# [1, true, null, "hello"]

# ── 中文不跳脫 ───────────────────────────────────────────
# JSON 預設會把非 ASCII 字元轉成跳脫字元，這樣在某些系統中比較安全，
# 但可讀性會下降。
record = {"城市": "澎湖", "人口": 100000}
# ensure_ascii=False：保留中文原樣輸出
print(json.dumps(record, ensure_ascii=False))   # {"城市": "澎湖", "人口": 100000}
# ensure_ascii=True：中文會被轉成 \u 開頭的 Unicode 跳脫序列
print(json.dumps(record, ensure_ascii=True))    # {"城市": "澎湖", ...}
