# U7. OrderedDict 的取捨：保序但更吃記憶體（1.7）

# OrderedDict 是在 Python 3.7 之前的替代方案。
# 現代 Python（3.7+）的內建 dict 已經預設保序，
# 所以 OrderedDict 在新版本中主要用於向下相容或特殊需求。
from collections import OrderedDict

# 建立一個 OrderedDict 實例。
d = OrderedDict()
# 加入鍵值對，順序會被記錄下來。
d['foo'] = 1
# 再添加另一筆。
d['bar'] = 2

# 為了維持插入順序，OrderedDict 內部需要額外結構（如雙向鏈結或記錄陣列），
# 因此記憶體佔用比一般 dict 更大。
#
# 記憶體 vs 功能的取捨：
# - OrderedDict 保證保序（即使在舊 Python 版本），但需額外開銷。
# - 現代 Python dict：預設保序，記憶體更經濟。
# - 若需要頻繁移動元素位置（如 move_to_end），OrderedDict 有專用方法。
#
# 實務建議：
# - Python 3.7+：優先用內建 dict。
# - 需要向下相容或特殊排序行為：才考慮 OrderedDict。
