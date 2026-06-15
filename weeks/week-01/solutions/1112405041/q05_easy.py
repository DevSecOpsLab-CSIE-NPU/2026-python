# 主題 05：索引與切片 - 簡易教學版

# 索引（indexing）：取得特定位置的元素
text = 'abcdefg'
first = text[0]              # 第一個字元 'a'
last = text[-1]              # 最後一個字元 'g'（負號表示從末尾計數）

print(f"字串: {text}")
print(f"第一個: {first}")
print(f"最後一個: {last}")

# 切片（slicing）：取得連續的元素範圍
mid = text[2:5]              # 從索引 2 到 4（不包含 5）-> 'cde'
print(f"中間部分 [2:5]: {mid}")

# 數字 list 的索引與切片
nums = [10, 20, 30, 40, 50]
first_num = nums[0]          # 第一個 10
last_two = nums[-2:]         # 最後兩個 [40, 50]
first_three = nums[:3]       # 前三個 [10, 20, 30]
every_other = nums[::2]      # 每隔一個 [10, 30, 50]

print(f"列表: {nums}")
print(f"第一個: {first_num}")
print(f"最後兩個: {last_two}")
print(f"前三個: {first_three}")
print(f"每隔一個: {every_other}")
