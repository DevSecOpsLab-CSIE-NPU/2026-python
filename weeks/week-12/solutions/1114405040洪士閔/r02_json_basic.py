"""R02. JSON 基礎讀寫。

這份版本示範 JSON 與 Python 物件的雙向轉換，
並順便展示如何把 JSON 寫入和讀回檔案。
"""

import json
import tempfile
from pathlib import Path


# Python 的 dict、list 等物件可以透過 json.dumps() 轉成 JSON 字串。
data = {"name": "Alice", "age": 30, "scores": [95, 87, 92]}


# 序列化：Python → JSON 字串。
s = json.dumps(data)
print(type(s), s)


# indent 可以讓 JSON 輸出更容易閱讀，sort_keys 則是把 key 排序。
s_pretty = json.dumps(data, indent=4, sort_keys=True)
print(s_pretty)


# 反序列化：JSON 字串 → Python 物件。
obj = json.loads(s)
print(type(obj), obj["name"])


# 檔案 I/O：實際專案通常是把 JSON 存成檔案再讀回來。
# 這裡使用暫存資料夾，避免在不同作業系統上寫死 /tmp。
with tempfile.TemporaryDirectory() as temp_dir:
    json_path = Path(temp_dir) / "data.json"

    # json.dump()：直接把 Python 物件寫到檔案。
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # json.load()：從檔案讀回 Python 物件。
    with json_path.open("r", encoding="utf-8") as f:
        loaded = json.load(f)
    print(loaded)


# 型別對應關係：Python 與 JSON 的基本對照。
# dict   → object
# list   → array
# str    → string
# int    → number
# float  → number
# True   → true
# None   → null
print(json.dumps([1, True, None, "hello"]))


# ensure_ascii=False 可以保留中文，不會全部轉成跳脫序列。
record = {"城市": "澎湖", "人口": 100000}
print(json.dumps(record, ensure_ascii=False))
print(json.dumps(record, ensure_ascii=True))
