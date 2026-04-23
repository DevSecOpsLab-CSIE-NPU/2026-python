# 【Bloom 階段：R - 記憶與基本操作】
# R20. 合併多個映射到單一映射 (ChainMap)
# August 的惡意提醒：ChainMap 不會合併字典，而是「鏈接」它們。
# 它在處理優先級（如：局部設定 > 全局設定）時極其高效。
# 識破這點，你在開發 Week 13 的綜合專案時，配置系統會寫得比別人漂亮。

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 建立鏈接，查詢時會按順序從第一個字典開始找
c = ChainMap(a, b)

# 查詢行為
print(f"Value of x: {c['x']}") # 1 (from a)
print(f"Value of y: {c['y']}") # 2 (from b)
print(f"Value of z: {c['z']}") # 3 (from a，第一個找到的為準)

# 更新行為：只會影響「第一個」字典
c['z'] = 99
print(f"Updated a['z']: {a['z']}") # 99

# August 惡意筆記：這比使用 a.update(b) 更強，因為它能保持原始字典獨立，
# 且在原字典更新時，ChainMap 會同步反應（動態鏈接特性）。
