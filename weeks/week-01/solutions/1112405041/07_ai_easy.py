# 主題 07：函式與 Lambda - 簡易教學版

# 定義函式（function）
def double(x):
    """將輸入值乘以 2"""
    return x * 2

# 使用函式
values = [1, 2, 3]
result = [double(x) for x in values]
print(f"雙倍值: {result}")

# Lambda 函式是匿名函式，用於簡單的操作
# 語法：lambda 參數: 運算式
double_lambda = lambda x: x * 2
result_lambda = double_lambda(5)
print(f"Lambda 雙倍: {result_lambda}")

# Lambda 搭配 sorted，根據 score 排序
rows = [{'name': 'A', 'score': 90}, {'name': 'B', 'score': 75}]
rows_sorted = sorted(rows, key=lambda r: r['score'])
print(f"按 score 排序: {rows_sorted}")

# 其他使用 lambda 的地方
from operator import itemgetter
rows_sorted2 = sorted(rows, key=itemgetter('score'))
print(f"用 itemgetter 排序: {rows_sorted2}")

# Lambda 搭配 map、filter
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Map 結果: {doubled}")
print(f"Filter 結果: {evens}")
