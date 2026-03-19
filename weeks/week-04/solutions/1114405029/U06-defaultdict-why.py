# U6. defaultdict 為何比手動初始化乾淨（1.6）

# 從 collections 模組匯入 defaultdict
# defaultdict 是 dict（字典）的子類別
# 它的特色是：當存取不存在的 key 時，會自動建立預設值
from collections import defaultdict

# 建立一個串列 pairs
# 每個元素都是一個 tuple，包含 key 和 value
# 這裡的目的是要把相同 key 的 value 收集到同一個串列中
pairs = [('a', 1), ('a', 2), ('b', 3)]

# 手動版：一直判斷 key 是否存在
# 建立一個普通字典 d
d = {}

# 逐一讀取 pairs 中的每一組 (k, v)
for k, v in pairs:
    # 如果目前的 key 還不在字典 d 中
    # 就先建立一個空串列，準備用來存放這個 key 對應的多個值
    if k not in d:
        d[k] = []

    # 將目前的 value 加入對應 key 的串列中
    d[k].append(v)

# defaultdict：省掉初始化分支
# 建立一個 defaultdict 物件 d2
# 這裡指定 list 作為預設工廠函式
# 代表：當遇到不存在的 key 時，會自動建立一個空串列 []
d2 = defaultdict(list)

# 同樣逐一讀取 pairs 中的每一組 (k, v)
for k, v in pairs:
    # 因為 d2 是 defaultdict(list)
    # 若 k 不存在，會自動建立 d2[k] = []
    # 所以可以直接 append，不需要先手動判斷 key 是否存在
    d2[k].append(v)

# 印出原始資料 pairs
print("原始資料 pairs：", pairs)

print()  # 空一行，讓輸出結果更清楚

# 印出手動初始化做出來的結果
print("使用普通 dict 手動初始化後的結果 d：")
print(d)

print()  # 空一行，讓輸出結果更清楚

# 印出 defaultdict 做出來的結果
print("使用 defaultdict(list) 後的結果 d2：")
print(d2)

print()  # 空一行，讓輸出結果更清楚

# 為了方便比較內容，也把 defaultdict 轉成一般 dict 印出
print("將 d2 轉成一般 dict 後的內容：")
print(dict(d2))

print()  # 空一行，讓輸出結果更清楚

# 說明兩者差異
print("說明：")
print("普通 dict 需要先判斷 key 是否存在，若不存在就要手動建立空串列。")
print("defaultdict(list) 會在 key 不存在時自動建立空串列，因此程式更簡潔、更乾淨。")