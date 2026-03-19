"""
R20: ChainMap

把多個字典串成一個查找視圖。
"""

from collections import ChainMap


a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}
c = ChainMap(a, b)

# 先找第一個字典，找不到才往後找。
c["x"]

# z 會先取到 a 裡的值，而不是 b 裡的值。
c["z"]
