# R20 ChainMap 合併多層對映
# 重點：讀取時會依序查找多個 dict，不會真的複製資料。

from collections import ChainMap

a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}

# 查找順序：先 a 再 b。
c = ChainMap(a, b)

c["x"]

# z 在兩層都存在時，會先取到 a 的 z。
c["z"]
