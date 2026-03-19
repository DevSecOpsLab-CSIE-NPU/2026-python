# U6. defaultdict 為何比手動初始化乾淨（1.6）
# 展示 defaultdict 如何減少字典初始化邏輯的冗長程式碼

# 導入 defaultdict 模組
from collections import defaultdict

# 鍵值對列表
pairs = [('a', 1), ('a', 2), ('b', 3)]

# ❌ 手動版本：需要檢查鍵是否存在
print("手動版本:")
d = {}
for k, v in pairs:
    # 冗長的條件判斷：每次都要檢查 key 是否存在
    if k not in d:
        d[k] = []  # 初始化為空列表
    d[k].append(v)  # 然後才能添加值
print(f"  結果：{dict(d)}\n")  # 結果：{'a': [1, 2], 'b': [3]}

# ✓ defaultdict 版本：自動初始化
# defaultdict(list) 表示：任何新鍵的預設值為 list()
print("defaultdict 版本:")
d2 = defaultdict(list)
for k, v in pairs:
    # 代碼更簡潔：直接存取鍵
    # 如果鍵不存在，defaultdict 會自動用 list() 初始化
    d2[k].append(v)
print(f"  結果：{dict(d2)}")  # 結果：defaultdict(<class 'list'>, {'a': [1, 2], 'b': [3]})

# 優點：
print("\n優點:")
print("  1. 代碼更乾淨，邏輯更清楚")
print("  2. 減少 if 判斷，提高可讀性")
print("  3. defaultdict 還支援其他工廠函數如 int, set, float 等")
