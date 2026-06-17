# 12 Python 字串格式化（string formatter）範例

name = 'ACME'
price = 91.1

# f-string（推薦）
text = f'{name} price = {price:.2f}'

# format 方法
text2 = '{} price = {:.2f}'.format(name, price)
