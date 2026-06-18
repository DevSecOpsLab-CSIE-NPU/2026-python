# =================================================================
# R02. JSON 基礎讀寫（Python 3 標準函式庫 6.2 節）
# =================================================================
# JSON (JavaScript Object Notation) 是一種輕量級的資料交換格式。
# 在 Python 中，我們主要使用內建的 `json` 模組來處理 JSON 資料。

import json
import os

# ── 1. 字串與 Python 物件之間的轉換 (loads / dumps) ──────────────────
# 這裡的 "s" 代表 String

data = {
    "name": "小明",
    "age": 20,
    "is_student": True,
    "scores": [95, 87, 92],
    "address": None
}

# 序列化 (Serialization)：將 Python 物件轉換為 JSON 字串
# 使用 indent 參數可以讓輸出的 JSON 縮排，方便人類閱讀
print("=== 1. 將 Python 物件轉為 JSON 字串 ===")
json_string = json.dumps(data, indent=4, ensure_ascii=False)
print(f"類型: {type(json_string)}")
print(json_string)

# 反序列化 (Deserialization)：將 JSON 字串轉回 Python 物件
print("\n=== 2. 將 JSON 字串轉回 Python 物件 ===")
python_obj = json.loads(json_string)
print(f"類型: {type(python_obj)}")
print(f"讀取姓名: {python_obj['name']}")


# ── 2. 檔案 I/O 操作 (load / dump) ────────────────────────────────
# 直接處理檔案物件，不需要先轉成字串。

file_path = "temp_data.json"

# 寫出到檔案 (dump)
print(f"\n=== 3. 將資料寫入檔案 {file_path} ===")
with open(file_path, "w", encoding="utf-8") as f:
    # ensure_ascii=False 確保中文字不會變成 \uXXXX 的格式
    json.dump(data, f, indent=4, ensure_ascii=False)

# 從檔案讀入 (load)
print(f"=== 4. 從檔案 {file_path} 讀取資料 ===")
if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    print(f"讀取到的資料: {loaded_data}")


# ── 3. 型別對應表 (Type Mapping) ───────────────────────────────────
# 在轉換過程中，Python 與 JSON 的型別會自動對應：
# Python dict   → JSON object  {}
# Python list   → JSON array   []
# Python str    → JSON string  ""
# Python int    → JSON number  123
# Python float  → JSON number  12.3
# Python True   → JSON true
# Python False  → JSON false
# Python None   → JSON null

print("\n=== 5. 示範型別對應 ===")
mixed_data = [1, "Hello", True, None, {"key": 10.5}]
print(f"原始資料: {mixed_data}")
print(f"轉換後: {json.dumps(mixed_data)}")


# ── 4. 進階技巧：美化與排序 ────────────────────────────────────────
# sort_keys=True 會讓字典的 Key 按照字母順序排列，方便比對資料差異。
print("\n=== 6. 排序後的 JSON ===")
print(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False))
