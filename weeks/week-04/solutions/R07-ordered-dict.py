# R7. OrderedDict（1.7）
# 本程式示範如何使用 Python 的 collections 模組中的 OrderedDict 類別
# OrderedDict 是一個有序字典，能夠記住鍵值對的插入順序，這與標準字典不同

# 引入 collections 模組中的 OrderedDict 類別
# OrderedDict 用於創建一個有序的字典結構
from collections import OrderedDict

# 引入 json 模組，用於處理 JSON 格式的數據序列化
import json

# 創建一個空的 OrderedDict 實例
# OrderedDict() 會初始化一個空的有序字典
d = OrderedDict()

# 向有序字典中添加鍵值對
# 'foo' 鍵對應值 1，'bar' 鍵對應值 2
# 注意：OrderedDict 會按照插入順序維護鍵的排列
d['foo'] = 1; d['bar'] = 2

# 使用 json.dumps() 將 OrderedDict 轉換為 JSON 字符串
# json.dumps() 會將字典序列化為 JSON 格式的字符串
# 由於 OrderedDict 是有序的，JSON 字符串中的鍵值對順序會與插入順序一致
json.dumps(d)
