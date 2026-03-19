# R20. ChainMap 合併映射（1.20）
# 展示如何使用 ChainMap 合併多個字典，實現優先順序搜尋

# 從 collections 模組導入 ChainMap
from collections import ChainMap

# 建立兩個字典
a = {'x': 1, 'z': 3}  # 第一個字典
b = {'y': 2, 'z': 4}  # 第二個字典

# 建立 ChainMap：優先搜尋順序是 a，然後 b
# ChainMap 不會複製字典，只是建立搜尋链
c = ChainMap(a, b)

# 存取只在 a 中的鍵
print("c['x']:", c['x'])  # 結果：1（來自 a）

# 存取在兩個字典中都存在的鍵
print("c['z']:", c['z'])  # 結果：3（來自 a，因為 a 優先級更高）
print("c['y']:", c['y'])  # 結果：2（來自 b）
# 如果改為 c = ChainMap(b, a)，則 c['z'] 會得到 4（來自 b）
