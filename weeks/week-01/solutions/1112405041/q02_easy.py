# 主題 02：基本資料型別 - 簡易教學版

# Python 的基本資料型別
x = 7              # int：整數型別
y = 3.5            # float：浮點數（帶小數點）
name = 'ACME'      # str：字串型別
ok = True          # bool：布林值（True 或 False）

# 型別轉換（type conversion）
s = '12'           # 字串 '12'
num = int(s)       # 將字串轉換為整數 12
price = float('19.99')  # 將字串轉換為浮點數 19.99

# 也可以進行其他轉換
str_num = str(42)  # 將整數轉換為字串 '42'
bool_value = bool(1)  # 將整數轉換為布林值 True

# 列印各個變數及其型別
print(f"x = {x}, 型別: {type(x)}")
print(f"y = {y}, 型別: {type(y)}")
print(f"name = {name}, 型別: {type(name)}")
print(f"ok = {ok}, 型別: {type(ok)}")
print(f"轉換後的 num = {num}, 型別: {type(num)}")
print(f"轉換後的 price = {price}, 型別: {type(price)}")
