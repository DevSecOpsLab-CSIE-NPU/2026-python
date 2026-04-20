# R7. OrderedDict（1.7）

# 從 collections 模組導入 OrderedDict 類別。
from collections import OrderedDict
# 導入 json 模組，用於將 Python 物件序列化為 JSON 格式的字串。
import json

print("--- 使用 OrderedDict ---")
# 創建一個 OrderedDict 物件 d。
d = OrderedDict()
# 顯示初始化後的 OrderedDict。
print(f"初始化 OrderedDict d: {d}")

# 向 OrderedDict 中加入鍵值對 'foo': 1。
d['foo'] = 1
# 顯示加入 'foo' 後的狀態。
print(f"加入 'foo': 1 後: {d}")

# 向 OrderedDict 中加入鍵值對 'bar': 2。
d['bar'] = 2
# 顯示加入 'bar' 後的狀態。
print(f"加入 'bar': 2 後: {d}")

# 使用 json.dumps() 將 OrderedDict 序列化 (轉換) 為 JSON 格式的字串。
# OrderedDict 能夠確保轉換成 JSON 字串後，鍵的排列順序與我們插入時完全一致。
json_output = json.dumps(d)
# 顯示轉換後的 JSON 字串結果。
print(f"轉換為 JSON 字串: {json_output}")
