# R06 defaultdict
# 目標：示範多值字典收集模式（list / set）與 setdefault 對照。

from collections import defaultdict

# 每個 key 對應 list，第一次訪問會自動建立空 list
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)

# 每個 key 對應 set，自動去重
d = defaultdict(set)
d["a"].add(1)
d["a"].add(2)

# 傳統 dict 也能做到，但語法較冗長
d = {}
d.setdefault("a", []).append(1)
