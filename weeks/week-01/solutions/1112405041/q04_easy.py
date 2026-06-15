# 主題 04：for 迴圈 - 簡易教學版

# 基本 for 迴圈：遍歷（iterate）list 中的每個元素
items = [2, 4, 6]

# 方法 1：計算總和
total = 0
for x in items:              # 逐一取出 items 中的每個元素給變數 x
    total += x               # 將 x 累加到 total

print(f"總和: {total}")

# 方法 2：產生平方值
squares = []
for x in items:              # 遍歷 items
    squares.append(x * x)    # 計算 x 的平方，並加入 squares list

print(f"平方: {squares}")

# 也可以遍歷字串
word = 'hello'
for char in word:
    print(f"字元: {char}")

# 使用 range() 產生數字序列
for i in range(3):           # range(3) 產生 0, 1, 2
    print(f"計數: {i}")
