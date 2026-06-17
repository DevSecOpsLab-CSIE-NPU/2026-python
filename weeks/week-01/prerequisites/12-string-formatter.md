# 12 Python 字串格式化（string formatter）

你必須已經「不需要解釋」就能看懂：

```python
name = 'ACME'
price = 91.1

# f-string（推薦）
text = f'{name} price = {price:.2f}'

# format 方法
text2 = '{} price = {:.2f}'.format(name, price)
```

用途：

- 輸出對齊
- 結果顯示
- 除錯訊息
