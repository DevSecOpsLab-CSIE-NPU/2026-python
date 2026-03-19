"""R17: 用字典推導式建立子集合。"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

# 價格高於 200 的股票
expensive = {k: v for k, v in prices.items() if v > 200}
print('高價股:', expensive)

# 只保留指定公司
tech_names = {'AAPL', 'IBM', 'MSFT'}
selected = {k: v for k, v in prices.items() if k in tech_names}
print('指定公司:', selected)
