# R02. JSON 基礎讀寫（6.2）
# json.loads / json.dumps / json.load / json.dump
#
# 這個範例主要示範 Python 內建 json 模組最常用的四個 API：
# 1. json.dumps：把 Python 物件轉成 JSON 字串。
# 2. json.loads：把 JSON 字串轉回 Python 物件。
# 3. json.dump：把 Python 物件直接寫入檔案。
# 4. json.load：從檔案讀入 JSON 內容並轉成 Python 物件。

import json

# ── 字串 ↔ Python 物件 ───────────────────────────────────
# JSON 和 Python 的資料型別很像，但仍然有固定對應關係。
# 這裡先準備一個 Python dict，後面會拿它做序列化與反序列化示範。
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）
# dumps 的意思是「dump 成字串」。
# 它會把 Python 物件轉成 JSON 格式的文字，適合要顯示、傳輸或暫存時使用。
s = json.dumps(data)
# type(s) 會是 str，代表結果已經變成 JSON 字串，而不是 Python dict。
print(type(s), s)

# 美化輸出
# indent 會讓 JSON 自動縮排，方便人類閱讀。
# sort_keys=True 會把 key 排序，輸出更穩定，也更容易比對差異。
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# 反序列化（JSON 字串 → Python）
# loads 的意思是「load from string」。
# 它會把 JSON 字串還原成 Python 物件，這裡會回到 dict。
obj = json.loads(s)
# 反序列化後就能像操作一般 Python dict 一樣取值。
print(type(obj), obj["name"])

# ── 檔案 I/O ─────────────────────────────────────────────
# 寫出到檔案
# 當資料需要長期保存，或要讓其他程式讀取時，通常會把 JSON 寫到檔案。
# json.dump 是直接把 Python 物件寫入檔案物件，而不是先回傳字串。
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    # ensure_ascii=False 可以保留原始 Unicode 字元，不把中文轉成 \uXXXX。
    # indent=2 則讓檔案內容更好讀。
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀入
# json.load 會直接從檔案物件讀取 JSON，並轉成對應的 Python 物件。
with open("/tmp/data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
# 讀回來後仍然是 dict，所以可以直接印出或做後續處理。
print(loaded)

# ── 型別對應 ──────────────────────────────────────────────
# 下面這段是在整理 Python 與 JSON 的基本型別對應。
# 了解這些對照很重要，因為 JSON 不是 Python 的原生格式，轉換時會有固定規則。
# Python dict   → JSON object  {}
# Python list   → JSON array   []
# Python str    → JSON string  ""
# Python int    → JSON number
# Python float  → JSON number
# Python True   → JSON true
# Python None   → JSON null

# 這裡把多種型別放在同一個 list 中，方便觀察 dumps 後的 JSON 結果。
print(json.dumps([1, True, None, "hello"]))
# [1, true, null, "hello"]

# ── 中文不跳脫 ───────────────────────────────────────────
# 預設情況下，json.dumps 會把非 ASCII 字元轉成跳脫序列。
# 如果資料中有中文、日文或其他 Unicode 字元，通常會希望保留原字元方便閱讀。
record = {"城市": "澎湖", "人口": 100000}
# ensure_ascii=False：保留中文原字，不做跳脫。
print(json.dumps(record, ensure_ascii=False))   # {"城市": "澎湖", "人口": 100000}
# ensure_ascii=True：預設行為，會把非 ASCII 字元轉成跳脫序列，適合機器處理，但人看起來較不直覺。
print(json.dumps(record, ensure_ascii=True))    # {"城市": "澎湖", ...}
