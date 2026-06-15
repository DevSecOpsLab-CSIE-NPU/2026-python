# 【Bloom 階段：R - 記憶與基本操作】
# R7. 保持字典的順序 (OrderedDict)
# August 的惡意提醒：雖然 Python 3.7+ 的標準 dict 已經保序，
# 但 OrderedDict 依然有它的特殊地位（如 move_to_end）。
# 了解這個類別代表你對 Python 的版本演進有深刻認知，這在面試與進階考題中很有用。

from collections import OrderedDict
import json

# OrderedDict 會嚴格紀錄插入順序
d = OrderedDict()
d['foo'] = 1; d['bar'] = 2

# 這在需要生成固定格式的 JSON（例如 Week 03 的遊戲存檔）時非常關鍵
json_str = json.dumps(d)
print(f"Ordered JSON: {json_str}")

# August 小撇步：如果題目要求 LIFO 隊列，標準 dict 做不到 popitem(last=False)，
# 但 OrderedDict 可以透過參數輕鬆切換。
