# R02. JSON 基礎讀寫（6.2）
# json.loads / json.dumps / json.load / json.dump

# 匯入json模組，用於處理JSON資料的序列化和反序列化
import json

# ── 字串 ↔ Python 物件 ───────────────────────────────────
# 定義一個Python字典作為範例資料，包含姓名、年齡和分數列表
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python物件 → JSON字串）
# json.dumps()將Python物件轉換為JSON格式的字串
s = json.dumps(data)
print(type(s), s)  # 輸出類型和JSON字串

# 美化輸出：使用indent參數縮排，使JSON更易讀；sort_keys=True按鍵排序
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# 反序列化（JSON字串 → Python物件）
# json.loads()將JSON字串轉換回Python物件
obj = json.loads(s)
print(type(obj), obj["name"])  # 輸出類型和特定欄位的值

# ── 檔案 I/O ─────────────────────────────────────────────
# 將JSON資料寫入檔案
# 使用with語句確保檔案正確關閉
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    # json.dump()將Python物件序列化並寫入檔案
    # indent=2：縮排2個空格；ensure_ascii=False：保留非ASCII字元（如中文）
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀取JSON資料
with open("/tmp/data.json", "r", encoding="utf-8") as f:
    # json.load()從檔案讀取並反序列化為Python物件
    loaded = json.load(f)
print(loaded)  # 輸出讀取的資料

# ── 型別對應 ──────────────────────────────────────────────
# JSON與Python型別的對應關係：
# Python dict   → JSON object  {}     （物件）
# Python list   → JSON array   []     （陣列）
# Python str    → JSON string  ""     （字串）
# Python int    → JSON number         （數字）
# Python float  → JSON number         （浮點數）
# Python True   → JSON true           （布林值真）
# Python None   → JSON null           （空值）

# 範例：序列化包含不同型別的列表
print(json.dumps([1, True, None, "hello"]))
# 輸出：[1, true, null, "hello"]  （注意Python的True變成true，None變成null）

# ── 中文不跳脫 ───────────────────────────────────────────
# 定義包含中文的字典
record = {"城市": "澎湖", "人口": 100000}

# ensure_ascii=False：保留Unicode字元，不進行ASCII跳脫
print(json.dumps(record, ensure_ascii=False))   # {"城市": "澎湖", "人口": 100000}

# ensure_ascii=True：將非ASCII字元跳脫為\u編碼（預設行為）
print(json.dumps(record, ensure_ascii=True))    # {"城市": "\u6f8e\u6e56", "人口": 100000}
