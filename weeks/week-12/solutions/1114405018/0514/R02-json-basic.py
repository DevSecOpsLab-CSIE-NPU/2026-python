"""R02. JSON 基礎讀寫（6.2）

說明（繁體中文詳細註解）：
- JSON（JavaScript Object Notation）為輕量級資料交換格式，通用於網路傳輸與儲存。
- Python 內建 `json` 模組提供序列化/反序列化（dumps/loads）以及檔案 I/O（dump/load）。

常見使用情境：
- 將 Python 物件轉成 JSON 字串以便傳送到 API（`json.dumps`）。
- 從 JSON 字串或檔案載入為 Python 物件以供處理（`json.loads` / `json.load`）。

注意事項：
- 預設 `json.dumps` 會把非 ASCII 字元轉成 \uXXXX；若要保留中文請使用 `ensure_ascii=False`。
- 若要可讀性好的輸出可用 `indent` 參數；若要固定欄位順序可用 `sort_keys=True`（但排序可能影響原始資料意義）。
"""

import json


# 範例資料：Python 物件 → JSON 字串
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）
s = json.dumps(data)
print(type(s), s)

# 美化輸出：方便人工閱讀與除錯
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# 反序列化（JSON 字串 → Python 物件）
obj = json.loads(s)
print(type(obj), obj["name"])  # dict


# 檔案 I/O：寫入與讀取 JSON 檔案（示意用 /tmp 路徑）
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    # ensure_ascii=False 可保留中文不被轉為 \uXXXX
    json.dump(data, f, indent=2, ensure_ascii=False)

with open("/tmp/data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)


# 型別對應參考（JSON ↔ Python）：
# - JSON object {}  -> Python dict
# - JSON array  []  -> Python list
# - JSON string "" -> Python str
# - JSON number     -> Python int/float
# - JSON true/false -> Python True/False
# - JSON null       -> Python None

print(json.dumps([1, True, None, "hello"]))


# 中文示例：ensure_ascii=True/False 的差異
record = {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=False))   # 中文正常顯示
print(json.dumps(record, ensure_ascii=True))    # 中文會被 escape
