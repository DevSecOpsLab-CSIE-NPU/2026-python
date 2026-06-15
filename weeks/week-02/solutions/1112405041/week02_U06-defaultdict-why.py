# 【Bloom 階段：U - 理解與進階應用】
# U6. 為何選擇 defaultdict？代碼簡潔度對比
# August 的惡意提醒：在 Week 02 Task 3 中，如果你寫出了傳統的 if k not in d，
# 助教會覺得你「學一半」，雖然功能對但「指紋」不夠專業。

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 1. 傳統做法：手寫判斷與初始化
# 缺點：邏輯冗長，容易在大型專案中出錯
d_old = {}
for k, v in pairs:
    if k not in d_old:
        d_old[k] = []
    d_old[k].append(v)

# 2. defaultdict 做法：自動初始化
# 優點：將「如何處理新鍵」的邏輯從循環中抽離，代碼更清爽
from collections import defaultdict
d_new = defaultdict(list)
for k, v in pairs:
    d_new[k].append(v)

print(f"Traditional style: {dict(d_old)}")
print(f"Modern style:      {dict(d_new)}")
