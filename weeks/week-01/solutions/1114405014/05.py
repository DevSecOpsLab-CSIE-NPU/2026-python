# 05.py - 字串與列表切片範例
text = 'abcdefg'
first = text[0]               # 第一個字元
mid = text[2:5]               # 從索引2到(不含)5的子字串

nums = [10, 20, 30, 40, 50]
last_two = nums[-2:]          # 切出列表的最後兩個元素

print(f"text = {text}")
print(f"first = {first}")
print(f"mid = {mid}")
print(f"last_two = {last_two}")