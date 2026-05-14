"""
R02. JSON 基礎讀寫（6.2）

本模組展示 Python 內建 json 模組的四種主要用法：
    1. json.dumps - 將 Python 物件序列化為 JSON 字串
    2. json.loads - 將 JSON 字串反序列化為 Python 物件
    3. json.dump - 將 Python 物件序列化並寫入檔案
    4. json.load - 從檔案讀取 JSON 資料並反序列化為 Python 物件

JSON 是一種輕量級的資料交換格式，廣泛用於 Web API、設定檔等場景。
本模組同時演示如何正確處理中文字符和美化輸出。
"""

import json  # Python 內建的 JSON 讀寫模組

# ── 字串 ↔ Python 物件 ───────────────────────────────────
# 本段落演示 json.dumps() 和 json.loads() 的用法
# 這兩個函數用於在 Python 物件和 JSON 字串之間進行轉換

data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}  # 建立一個 Python 字典

# ● 序列化（Python 物件 → JSON 字串）
# json.dumps() 將 Python 物件轉換為 JSON 格式的字串
# 返回值是字串類型，可以傳輸、儲存或顯示
s = json.dumps(data)  # 將 data 字典轉換為 JSON 字串
print(type(s), s)  # 輸出類型和字串內容

# ● 美化輸出（提高可讀性）
# indent=4：使用 4 個空格進行縮進，使 JSON 結構更清晰
# sort_keys=True：按照鍵名進行字母排序，便於查看
s_pretty = json.dumps(data, indent=4, sort_keys=True)  # 生成美化後的 JSON 字串
print(s_pretty)  # 輸出美化後的結果

# ● 反序列化（JSON 字串 → Python 物件）
# json.loads() 將 JSON 字串解析回 Python 物件（通常是 dict 或 list）
# 名稱中的 's' 表示字串（string），'load' 表示從 dict/list 讀取
obj = json.loads(s)  # 將 JSON 字串反序列化為 Python 字典
print(type(obj), obj["name"])  # 驗證反序列化結果，並訪問 name 欄位

# ── 檔案 I/O ─────────────────────────────────────────────
# 本段落演示如何在檔案中讀寫 JSON 資料
# 使用 json.dump() 和 json.load() 直接操作檔案，不需要手動轉換字串

# ● 寫出到檔案
# json.dump() 直接將 Python 物件寫入檔案（相比 dumps 省去中間字串步驟）
# encoding="utf-8"：指定檔案編碼為 UTF-8，支援中文等多國字符
# indent=2：使用 2 個空格縮進，使檔案內容更易閱讀
# ensure_ascii=False：允許直接寫入非 ASCII 字符（如中文），而非轉義為 \uXXXX
with open("/tmp/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)  # 將資料寫入檔案

# ● 從檔案讀入
# json.load() 直接從檔案讀取 JSON 資料並反序列化為 Python 物件
# 與 json.loads() 的差異：load() 接收檔案物件，loads() 接收字串
with open("/tmp/data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)  # 從檔案讀取並反序列化
print(loaded)  # 輸出讀取的資料

# ── 型別對應 ──────────────────────────────────────────────
# JSON 是語言中立的資料格式，不同程式語言間型別有相應的對應關係
# 了解這些對應關係對於資料交換和解析至關重要：
#
# Python 型別          →  JSON 型別      →  JSON 字面量
# ─────────────────────────────────────────────────────────
# dict                 →  object        →  {key: value, ...}
# list / tuple         →  array         →  [item, ...]
# str                  →  string        →  "text"
# int                  →  number        →  123
# float                →  number        →  123.45
# True                 →  true          →  true（小寫）
# False                →  false         →  false（小寫）
# None                 →  null          →  null（小寫）
#
# 注意：JSON 的布林值和 null 都是小寫，與 Python 的大寫不同

print(json.dumps([1, True, None, "hello"]))  # 演示多種型別的序列化
# 輸出：[1, true, null, "hello"]  # 注意 True → true，None → null

# ── 中文字符處理 ─────────────────────────────────────────
# 預設情況下，json.dumps() 會將非 ASCII 字符（如中文）轉義為 \uXXXX 形式
# 這樣做的好處是確保 JSON 能在任何編碼的系統中傳輸，但可讀性下降
# 使用 ensure_ascii=False 可以直接保留中文字符，提高可讀性

record = {"城市": "澎湖", "人口": 100000}  # 建立包含中文的字典

# ● ensure_ascii=False：直接保留中文（推薦用於現代應用）
print(json.dumps(record, ensure_ascii=False))   
# 輸出：{"城市": "澎湖", "人口": 100000}  # 中文直接顯示，易於閱讀

# ● ensure_ascii=True（默認值）：將中文轉義為 Unicode 轉義序列
print(json.dumps(record, ensure_ascii=True))    
# 輸出：{"\u57ce\u5e02": "\u6ff8\u6e56", "\u4eba\u53e3": 100000}  # 中文被轉義

# 提示：在現代應用中，由於大多數系統都支援 UTF-8 編碼，
# 通常建議使用 ensure_ascii=False 和 encoding='utf-8'，
# 這樣既能保留中文可讀性，又能確保跨平台相容性
