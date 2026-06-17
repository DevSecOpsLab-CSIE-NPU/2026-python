# 7 函式與 lambda 範例

def double(x):
    return x * 2

values = [1, 2, 3]
result = [double(x) for x in values]

# lambda 做為 key
rows = [{'name': 'A', 'score': 90}, {'name': 'B', 'score': 75}]
rows_sorted = sorted(rows, key=lambda r: r['score'])
