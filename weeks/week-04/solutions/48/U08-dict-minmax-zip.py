# U8. 字典最值為何常用 zip(values, keys)（1.8）
# 展示如何使用 zip 同時獲取字典的最小/最大值及其對應鍵

# 股票名稱和價格的字典
prices = {'A': 2.0, 'B': 1.0}

# ❌ 方法 1：直接在字典上使用 min()
min(prices)  # 結果：'A'（按字母序比較鍵，不是值）
# 問題：得到的是鍵的最小值，而不是最小的價格

# ❌ 方法 2：只看值
min(prices.values())  # 結果：1.0（最小價格）
# 問題：得到最小值，但不知道它對應哪個股票名稱

# ✓ 方法 3：使用 zip() 配對值和鍵
print("\n方法 3 - 使用 zip():")
min_result = min(zip(prices.values(), prices.keys()))
print(f"  min(zip(...)) = {min_result}")
# 結果：(1.0, 'B')
# 好處：
# 1. zip(values, keys) 建立 (值, 鍵) 的元組對
# 2. min() 會先比較第一個元素（值），得到最小值
# 3. 同時返回對應的鍵，一次拿到兩個資訊
#
# 說明：
# - zip(prices.values(), prices.keys()) 產生 [(2.0, 'A'), (1.0, 'B')]
# - min() 比較時先看第一元素，所以 (1.0, 'B') 被選中
# - 最後回傳的元組 (1.0, 'B') 表示最小價格是 1.0，對應股票是 'B'
#
# 這個技巧對 max() 也適用：max(zip(prices.values(), prices.keys()))
max_result = max(zip(prices.values(), prices.keys()))
print(f"  max(zip(...)) = {max_result}")
print("  會得到 (2.0, 'A')，表示最高價格")

# 注意：tuple 比較遵循字典序（lexicographic order），
# 先比較第一個元素，相等時才比較第二個元素
