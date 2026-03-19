# U6. defaultdict 為何比手動初始化乾淨（1.6）
"""
本範例說明 collections.defaultdict 相較於一般 dict 的優勢：
不需要手動檢查 key 是否存在並做初始化，程式碼更簡潔、意圖更明確。

defaultdict 會在 key 不存在時，自動建立一個預設值（由 factory 決定），
並將該預設值放入 dict 中，以便立即使用。

常見用途：
- 將資料歸類到多個群組（grouping）
- 統計計數（例如計算詞頻、物件出現次數）
"""

from collections import defaultdict

# 範例資料：一組 (key, value) 對
pairs = [('a', 1), ('a', 2), ('b', 3)]

# 1) 手動版：需要先檢查 key 是否存在，若不存在就初始化容器
#    這樣的程式碼容易重複且不夠乾淨
#    如果忘記初始化，就會得到 KeyError。
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []
    d[k].append(v)

# 2) defaultdict 版：只要指定 factory（這裡是 list），
#    當 key 不存在時會自動建立 d2[key] = list()（也就是 []）
#    讓我們可以直接使用 append()，省略條件分支。
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)

# defaultdict 的預設值可以是任何可呼叫的工廠函式，例如 int()、set() 等
# 常見用途包括計數（defaultdict(int)）和去重集合（defaultdict(set)）。
