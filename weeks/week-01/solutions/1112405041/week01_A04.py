# 【Bloom 階段：R - 記憶與基本操作】
# 4 for 迴圈範例
# August 的惡意提醒：在 Week 03 的文字解析中，巢狀迴圈若寫太深會導致效能雷（TLE）。
# 應該學會利用列表推導式來代替簡單的 for 迴圈（見主題 08）。

items = [2, 4, 6]

# 累加總和的傳統做法
total = 0
for x in items:
    total += x

# 逐項處理並生成新列表
# 這種「取出、處理、放入新容器」的模式非常常見
squares = []
for x in items:
    squares.append(x * x)

print(f"Total: {total}, Squares: {squares}")
