"""
R06: defaultdict 與 setdefault

此範例比較兩種「自動初始化容器欄位」的寫法。
"""

from collections import defaultdict

# defaultdict(list)：首次存取不存在的 key 時，自動建立空 list。
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)

# defaultdict(set)：同理，自動建立空 set，適合去重資料。
d = defaultdict(set)
d["a"].add(1)
d["a"].add(2)

# 一般 dict 可用 setdefault 達成類似效果，但語法較繁瑣。
d = {}
d.setdefault("a", []).append(1)
