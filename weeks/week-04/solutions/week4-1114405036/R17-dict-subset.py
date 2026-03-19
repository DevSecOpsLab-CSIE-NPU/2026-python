# R17. 字典子集 (Dictionary Comprehension)（1.17）
# 說明：從現有的字典中快速篩選出符合條件的子集。

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 1. 篩選價格大於 200 的股票
p1 = {k: v for k, v in prices.items() if v > 200}
# 結果：{'AAPL': 612.78, 'IBM': 205.55}

# 2. 篩選特定的股票名稱
tech_names = {'AAPL', 'IBM', 'HPQ'}
p2 = {k: v for k, v in prices.items() if k in tech_names}
# 結果：{'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20}