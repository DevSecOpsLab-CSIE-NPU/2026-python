# R7. OrderedDict（Keeping Dictionaries in Order）—— Python Cookbook 1.7

from collections import OrderedDict
import json

# ── OrderedDict ───────────────────────────────────────────
# 普通的 dict 在 Python 3.7+ 雖然也保持插入順序，
# 但 OrderedDict 提供額外功能（如 move_to_end），
# 並且在「需要明確語意：此字典的順序具有意義」時更清楚。
#
# 主要用途：
#   1. 需要精確控制 JSON 序列化的欄位順序
#   2. 實作 LRU Cache（搭配 move_to_end）
d = OrderedDict()
d['foo'] = 1   # 插入順序：foo 先
d['bar'] = 2   # bar 後

# json.dumps 會依照插入順序序列化
# 輸出：'{"foo": 1, "bar": 2}'（foo 一定在 bar 之前）
json.dumps(d)
