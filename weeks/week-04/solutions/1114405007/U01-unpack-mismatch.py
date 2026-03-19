# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）

# 這個 tuple 只有 2 個元素
p = (4, 5)

# 解包時左邊變數數量必須和右邊元素數量一致
try:
	x, y, z = p
except ValueError as error:
	print('解包失敗:', error)

print('原始資料:', p)
