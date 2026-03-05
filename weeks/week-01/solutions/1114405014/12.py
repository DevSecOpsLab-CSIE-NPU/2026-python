# 12.py - 使用 f-string 和 format() 進行格式化字串
name = 'ACME'
price = 91.1

text = f'{name} price = {price:.2f}'            # f-string 格式，保留兩位小數

text2 = '{} price = {:.2f}'.format(name, price)  # 使用 format 方法

print(text)
print(text2)