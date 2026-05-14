# R02. JSON 基礎讀寫（6.2）
# json.loads / json.dumps / json.load / json.dump

import json

# ── 字串 ↔ Python 物件 ───────────────────────────────────
# 建立一個 Python 字典 (dict) 作為範例資料
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）
# json.dumps() 將 Python 物件轉換成 JSON 格式的字串 (dump string)
s = json.dumps(data)
print(type(s), s)

# 美化輸出
# indent=4: 縮排 4 個空白，讓輸出的 JSON 更容易閱讀
# sort_keys=True: 將字典的 key 依照字母順序自動排序
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# 反序列化（JSON 字串 → Python）
# json.loads() 將 JSON 格式的字串轉換回 Python 物件 (load string)
obj = json.loads(s)
print(type(obj), obj["name"])

# ── 檔案 I/O ─────────────────────────────────────────────
# 寫出到檔案
# 使用 with open 確保檔案操作後自動關閉，並強制指定編碼為 utf-8
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    # json.dump() 直接將 Python 物件寫入檔案物件 f 中
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀入
# 同樣指定 utf-8 編碼來讀取檔案
with open("/tmp/data.json", "r", encoding="utf-8") as f:
    # json.load() 直接從檔案物件讀取 JSON 內容並轉換為 Python 物件
    loaded = json.load(f)
print(loaded)

# ── 型別對應 ──────────────────────────────────────────────
# Python dict   → JSON object  {}
# Python list   → JSON array   []
# Python str    → JSON string  ""
# Python int    → JSON number
# Python float  → JSON number
# Python True   → JSON true     (注意轉換後為小寫)
# Python None   → JSON null     (注意轉換後為小寫)

# 示範 Python 的 True 和 None 轉換成 JSON 後會變成 true 和 null
print(json.dumps([1, True, None, "hello"]))
# [1, true, null, "hello"]

# ── 中文不跳脫 ───────────────────────────────────────────
record = {"城市": "澎湖", "人口": 100000}
# ensure_ascii=False：讓非 ASCII 字元（如中文）正常顯示，不要轉成 \uXXXX 的格式
print(json.dumps(record, ensure_ascii=False))   # {"城市": "澎湖", "人口": 100000}
# ensure_ascii=True（預設）：中文會被轉義成 Unicode 編碼
print(json.dumps(record, ensure_ascii=True))    # {"城市": "澎湖", ...}
