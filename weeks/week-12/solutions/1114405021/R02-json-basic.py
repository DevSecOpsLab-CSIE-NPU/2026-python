# R02. JSON 基礎讀寫（6.2）
# 本範例示範 json 模組的四個核心操作：
# 1. json.dumps：把 Python 物件轉成 JSON 字串
# 2. json.loads：把 JSON 字串轉回 Python 物件
# 3. json.dump：把 Python 物件直接寫入 JSON 檔案
# 4. json.load：從 JSON 檔案讀回 Python 物件

import json
import os
import tempfile

# -----------------------------------------------------------------------------
# 一、字串 ↔ Python 物件
# -----------------------------------------------------------------------------
# 先建立一個 Python 字典，裡面包含字串、數字與串列。
# JSON 最常處理的就是這類巢狀資料結構。
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# json.dumps() 會把 Python 物件「序列化」成 JSON 字串。
# 這裡的結果仍然是字串型別，只是內容格式符合 JSON。
s = json.dumps(data)
print(type(s), s)

# indent=4 代表縮排 4 個空白，讓輸出更容易閱讀。
# sort_keys=True 會將 key 排序，方便比對與除錯。
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)

# json.loads() 則是反過來，把 JSON 字串「反序列化」成 Python 物件。
# 轉回來之後，原本的 JSON object 會變成 Python dict。
obj = json.loads(s)
print(type(obj), obj["name"])

# -----------------------------------------------------------------------------
# 二、檔案 I/O
# -----------------------------------------------------------------------------
# 實務上 JSON 很常拿來當設定檔、交換格式或暫存資料。
# 這裡示範如何把資料寫到檔案，再從檔案讀回來。
#
# 原始範例使用 /tmp/data.json，但那是偏向 Unix/Linux 的路徑。
# 為了讓這份獨立版本在 Windows 上也能執行，改用系統暫存目錄。
temp_dir = tempfile.gettempdir()
file_path = os.path.join(temp_dir, "data.json")

# json.dump() 會直接把 Python 物件寫入檔案。
# indent=2 讓檔案內容排版整齊。
# ensure_ascii=False 讓中文保留原樣，不會被轉成 \uXXXX。
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# json.load() 會直接從檔案讀取 JSON，並轉回 Python 物件。
with open(file_path, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)

# -----------------------------------------------------------------------------
# 三、型別對應
# -----------------------------------------------------------------------------
# JSON 與 Python 的型別並不是完全一樣，但有明確對應關係：
# - Python dict   → JSON object  {}
# - Python list   → JSON array   []
# - Python str    → JSON string  ""
# - Python int    → JSON number
# - Python float  → JSON number
# - Python True   → JSON true
# - Python None   → JSON null
#
# 下面這行會輸出對應後的 JSON 字串，方便觀察型別如何轉換。
print(json.dumps([1, True, None, "hello"]))
# 輸出結果會是：
# [1, true, null, "hello"]

# -----------------------------------------------------------------------------
# 四、中文不跳脫
# -----------------------------------------------------------------------------
# JSON 預設會把非 ASCII 字元轉成跳脫序列，例如中文會變成 \uXXXX。
# 如果你想直接看到中文內容，可以設定 ensure_ascii=False。
record = {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=False))   # 中文會直接顯示
print(json.dumps(record, ensure_ascii=True))    # 中文會被跳脫成 Unicode 表示法

# -----------------------------------------------------------------------------
# 補充說明
# -----------------------------------------------------------------------------
# json.dumps / json.dump：輸出資料
# json.loads / json.load：讀入資料
#
# 差別可簡單記成：
# - s = string，處理字串
# - load = 從檔案讀入
# - dump = 寫入檔案
#
# 當你要在不同程式、不同語言、或網路 API 間傳遞資料時，
# JSON 是最常見也最方便的格式之一。
