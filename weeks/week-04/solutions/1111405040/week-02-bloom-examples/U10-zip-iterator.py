"""
U10: zip 回傳的是 iterator

iterator 被消耗後，就不能再重複使用。
"""

prices = {"A": 2.0, "B": 1.0}
z = zip(prices.values(), prices.keys())

min(z)

# max(z)
# 這裡不會得到原本的資料，因為 z 已經被 min 消耗掉了。
