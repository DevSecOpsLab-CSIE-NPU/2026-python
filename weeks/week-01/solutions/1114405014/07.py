# 07.py - 函式、列表解析與使用 key 排序

def double(x):
    return x * 2

values = [1, 2, 3]
result = [double(x) for x in values]   # 對列表中的每個元素套用函式

rows = [{'name': 'A', 'score': 90}, {'name': 'B', 'score': 75}]
rows_sorted = sorted(rows, key=lambda r: r['score'])  # 依 score 欄位排序

# 輸出並解釋
print(f"values = {values}")
print(f"result = {result}")

print(f"rows = {rows}")
print(f"rows_sorted = {rows_sorted}")