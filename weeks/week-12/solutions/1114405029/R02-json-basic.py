# R02. JSON 基礎讀寫（6.2）
# json.loads / json.dumps / json.load / json.dump

# 匯入 Python 內建的 json 模組
# json 模組可以用來處理 JSON 格式資料
# JSON 是目前非常常見的資料交換格式
# 常用於：
# 1. Web API
# 2. 前後端資料傳輸
# 3. 設定檔
# 4. 資料儲存
import json

# ── 字串 ↔ Python 物件 ───────────────────────────────────

# 建立一個 Python dictionary
# data 是 Python 物件，不是 JSON 字串
# 其中：
# name 對應字串
# age 對應整數
# scores 對應 list
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}

# 序列化（Python → JSON 字串）

# json.dumps()：
# 將 Python 物件轉換成 JSON 格式字串
# dumps 的 s 代表 string
# 回傳值型態是 str
s = json.dumps(data)

# 印出 s 的型態與內容
# type(s) 會是 <class 'str'>
# 因為 JSON 本質上是一種文字格式
print(type(s), s)

# 美化輸出

# indent=4：
# 代表縮排 4 個空白
# 讓 JSON 更容易閱讀

# sort_keys=True：
# 將 key 依照字母順序排序輸出
# 方便閱讀與比較資料差異

# 這裡產生的是格式化後的 JSON 字串
s_pretty = json.dumps(data, indent=4, sort_keys=True)

# 印出美化後 JSON
print(s_pretty)

# 反序列化（JSON 字串 → Python）

# json.loads()：
# 將 JSON 字串轉回 Python 物件
# loads 的 s 代表 string

# 回傳後 obj 會是 Python dict
obj = json.loads(s)

# 印出 obj 的型態與 name 欄位
# type(obj) 會是 <class 'dict'>
# obj["name"] 可以取得 name 欄位值
print(type(obj), obj["name"])

# ── 檔案 I/O ─────────────────────────────────────────────

# 寫出到檔案

# open(..., "w")：
# 以寫入模式開啟檔案
# 如果檔案不存在會自動建立
# 如果已存在則會覆蓋原本內容

# encoding="utf-8"：
# 指定 UTF-8 編碼
# 避免中文亂碼

# with open(...) as f：
# 使用 with 可以自動關閉檔案
with open("/tmp/data.json", "w", encoding="utf-8") as f:

    # json.dump()：
    # 將 Python 物件直接寫入檔案

    # dump 與 dumps 差異：
    # dump  → 寫入檔案
    # dumps → 回傳字串

    # indent=2：
    # JSON 格式縮排 2 個空白

    # ensure_ascii=False：
    # 不強制轉成 ASCII
    # 中文會直接顯示，不會變成 \uXXXX
    json.dump(data, f, indent=2, ensure_ascii=False)

# 從檔案讀入

# "r" 代表讀取模式
with open("/tmp/data.json", "r", encoding="utf-8") as f:

    # json.load()：
    # 從檔案讀取 JSON
    # 並轉回 Python 物件

    # load 與 loads 差異：
    # load  → 從檔案讀
    # loads → 從字串讀
    loaded = json.load(f)

# 印出讀取後的 Python 物件
print(loaded)

# ── 型別對應 ──────────────────────────────────────────────

# Python 與 JSON 的常見型別對應關係：

# Python dict   → JSON object  {}
# Python list   → JSON array   []
# Python str    → JSON string  ""
# Python int    → JSON number
# Python float  → JSON number
# Python True   → JSON true
# Python None   → JSON null

# 建立包含多種型別的 list
# 並轉成 JSON 字串
print(json.dumps([1, True, None, "hello"]))

# JSON 輸出結果：
# [1, true, null, "hello"]

# 注意：
# Python 的 True 會變成 JSON 的 true
# Python 的 None 會變成 JSON 的 null

# ── 中文不跳脫 ───────────────────────────────────────────

# 建立包含中文的 dictionary
record = {"城市": "澎湖", "人口": 100000}

# ensure_ascii=False：
# 中文直接顯示
# 適合人類閱讀
print(json.dumps(record, ensure_ascii=False))   # {"城市": "澎湖", "人口": 100000}

# ensure_ascii=True：
# 中文轉成 Unicode 跳脫字元
# 例如 \u57ce\u5e02
# 這是 json.dumps() 的預設行為
print(json.dumps(record, ensure_ascii=True))    # {"城市": "澎湖", ...}