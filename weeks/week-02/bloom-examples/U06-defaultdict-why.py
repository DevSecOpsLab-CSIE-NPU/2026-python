# U6. defaultdict 為何比手動初始化乾淨（1.6）

# defaultdict 是一個特殊的字典，會在存取不存在的鍵時自動產生默認值。
# 適合處理「需要先初始化才能操作」的情境，例如：
# - 彙集相同鍵多個值時（需要先準備容器）
# - 計數時（需要先初始化為 0）

from collections import defaultdict

# 測試資料：多對鍵值，相同的鍵可能重複出現。
pairs = [('a', 1), ('a', 2), ('b', 3)]

# 方式 1：手動版（傳統做法）
# 每次都要判斷鍵是否已存在，不存在就先初始化為空列表。
# 程式碼冗長且容易遺漏或出錯。
d = {}
for k, v in pairs:
    if k not in d:        # 檢查鍵是否存在
        d[k] = []         # 不存在就初始化為空列表
    d[k].append(v)        # 然後才能附加值

# 結果：{'a': [1, 2], 'b': [3]}

# 方式 2：defaultdict（乾淨做法）
# 它會自動在訪問不存在的鍵時呼叫 default_factory 產生默認值。
# default_factory=list 表示：每個不存在的鍵自動產生一個空列表 []。
# 不需要手動判斷與初始化，程式碼更簡潔。
d2 = defaultdict(list)
for k, v in pairs:
    # 若 d2[k] 不存在，defaultdict 會自動執行 list() 產生 []
    # 若已存在，就直接取用
    d2[k].append(v)       # 可直接操作，無需先檢查鍵

# 結果同樣是：defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})

# 常見的 default_factory 用法：
# - defaultdict(list)：預設為空列表，適合彙集
# - defaultdict(int)：預設為 0，適合計數
# - defaultdict(set)：預設為空集合
# - defaultdict(lambda: 0)：用 lambda 自訂默認值邏輯
