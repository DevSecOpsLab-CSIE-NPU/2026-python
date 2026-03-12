# R6: defaultdict 與 setdefault
# 觀念：處理「key 可能不存在」時，避免手動寫很多 if 判斷。

from collections import defaultdict

# defaultdict(list): 第一次存取不存在的 key 時，自動建立空 list
# 適合用在「一個 key 對應多個值」的情境

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)

# defaultdict(set): 自動建立空 set，可天然去重

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)

# 一般 dict 也可用 setdefault：若 key 不存在就放入預設值後回傳
# 常見寫法：聚合資料時一行完成初始化 + append

d = {}
d.setdefault('a', []).append(1)
