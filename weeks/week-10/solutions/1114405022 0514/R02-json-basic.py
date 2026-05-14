# R02. JSON 基礎讀寫（6.2）
# 本示例展示了 JSON (JavaScript Object Notation) 的檔案處理方式：
# 1. json.loads()：將 JSON 字串轉換成 Python 物件（反序列化）
# 2. json.dumps()：將 Python 物件轉換成 JSON 字串（序列化）
# 3. json.load()：從檔案讀入 JSON 並轉換成 Python 物件
# 4. json.dump()：將 Python 物件寫成 JSON 檔案

import json  # 標準庫：JSON 檔案處理

# ── 字串 ↔ Python 物件 ───────────────────────────────────
# 此段展示序列化和反序列化的核心概念
# 序列化：Python 資料結構 → JSON 字串（適合存檔或網路傳輸）
# 反序列化：JSON 字串 → Python 資料結構（適合程式讀取）
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）
# json.dumps() 轉換 Python 物件成可開啟打印的 JSON 字串
# 轉換對應：dict → {}; list → []; str → ""; int/float → 數字; True → true; None → null
s = json.dumps(data)  # 預期：'{"name": "Alice", "age": 30, "scores": [95, 87, 92]}'
print(type(s), s)  # 預期輸出：<class 'str'> {...}

# 美化輸出 ⚠ 主要參數：
# indent=4：每級縮排 4 個空格（易於閱讀視覺層級）
# sort_keys=True：按字母順序排列欄位（解決 dict 順序不確定問題）
s_pretty = json.dumps(data, indent=4, sort_keys=True)  # 例子輸出格式化結果
# 預期輸出：
# {
#     "age": 30,
#     "name": "Alice",
#     "scores": [95, 87, 92]
# }
print(s_pretty)

# 反序列化（JSON 字串 → Python 物件）
# json.loads() 對應 json.dumps()：接受字串並轉換回 Python 物件
# 注意：與 csv.DictReader 不同，json.loads() 對字串要求嚴格
obj = json.loads(s)  # 字串 s 轉換回 dict
print(type(obj), obj["name"])  # 預期輸出：<class 'dict'> Alice

# ── 檔案 I/O ─────────────────────────────────────────────
# 寫出到檔案：json.dump() 直接將 Python 物件寫入檔案（對應 json.dumps()）
# encoding="utf-8" 確保中文正確儲存；ensure_ascii=False 不轉換中文為 Unicode 序列
with open("/tmp/data.json", "w", encoding="utf-8") as f:  # 以寫入模式開啟
    json.dump(data, f, indent=2, ensure_ascii=False)  # 預期輸出：\n{\n  "name": "Alice",\n  ...}

# 從檔案讀入：json.load() 直接從檔案記憶體中讀取並轉換成 Python 物件
# 不需要分開用 loads()：json.load() 內部會呼叫 loads()
with open("/tmp/data.json", "r", encoding="utf-8") as f:  # 以讀取模式開啟
    loaded = json.load(f)  # 直接轉換為 dict
print(loaded)  # 預期輸出：{'name': 'Alice', 'age': 30, 'scores': [95, 87, 92]}

# ── 型別對應 ──────────────────────────────────────────────
# 這是 Python 及 JSON 之間的數據型別映射表（非常重要）：
# Python dict      → JSON object  {}
# Python list      → JSON array   []
# Python str       → JSON string  ""
# Python int       → JSON number  (粘連數值)
# Python float     → JSON number  (粘連數值)
# Python True      → JSON true    (注意第一個大寫 T)
# Python False     → JSON false   
# Python None      → JSON null    (反之不存在對應)
#
# 重要提示：Python tuple 在 JSON 中沒有對應型別，轉換時只會變成 list
print(json.dumps([1, True, None, "hello"]))  # 預期輸出：[1, true, null, "hello"]
# 留意：true、null 都是小寫英文

# ── 中文不逃脫 ───────────────────────────────────────────
# ensure_ascii 參數控制是否將中文轉換為 Unicode 序列
# True 時：中文會轉換為 \u... 形式（可讀性差但跨平台相容）
# False 時：中文直接保存（可讀性好但需確保編碼正確）
record = {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=False))   # 預期：{"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=True))    # 預期：{"\u57ce\u5e02": "\u6f8e\u6e56", "\u4eba\u53e3": 100000}
