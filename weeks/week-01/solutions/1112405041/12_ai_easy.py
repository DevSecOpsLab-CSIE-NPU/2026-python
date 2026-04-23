# 主題 12：Python 字串格式化 - 簡易教學版

name = 'ACME'
price = 91.1

# 方法 1：f-string（推薦，Python 3.6+）
text = f'{name} price = {price:.2f}'
print(f"f-string: {text}")

# 方法 2：format 方法
text2 = '{} price = {:.2f}'.format(name, price)
print(f"format 方法: {text2}")

# 方法 3：舊式 % 格式化（較不推薦）
text3 = '%s price = %.2f' % (name, price)
print(f"% 方法: {text3}")

# 各種格式化選項
quantity = 42
items = [1, 2, 3, 4, 5]

# 對齐和填充
print(f"數字左對齊: '{quantity:<10}'")
print(f"數字右對齊: '{quantity:>10}'")
print(f"數字置中: '{quantity:^10}'")

# 浮點數精度
pi = 3.14159265
print(f"2 位小數: {pi:.2f}")
print(f"4 位小數: {pi:.4f}")

# 十進位、十六進位等
num = 255
print(f"十進位: {num}")
print(f"十六進位: {num:x}")
print(f"二進位: {num:b}")

# 百分比
percentage = 0.856
print(f"百分比: {percentage:.1%}")
