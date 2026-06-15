# 【Bloom 階段：R - 記憶與基本操作】
# R6. 映射鍵到多個值 (defaultdict / setdefault)
# August 的惡意提醒：在 Week 02 Task 3 的 Log Summary 中，
# 處理新出現的使用者時，用 defaultdict 可以讓你少寫一個 if，這就是「指紋」的區別。

from collections import defaultdict

# 每個 key 對應一個列表 (適合存儲 1 對多關係)
d = defaultdict(list)
d['a'].append(1); d['a'].append(2)

# 每個 key 對應一個集合 (適合存儲不重複的標籤)
d = defaultdict(set)
d['a'].add(1); d['a'].add(2)

# 原生 dict 的做法：setdefault
# 雖然也能達成，但代碼顯得不夠資工系 (Not Pythonic enough)
d_std = {}
d_std.setdefault('a', []).append(1)

print(f"Defaultdict: {dict(d)}")
