# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）

# 定義一個包含 2 個元素的元組 (Tuple)
p = (4, 5)

# 錯誤示範：
# x, y, z = p  
# 會導致 ValueError：not enough values to unpack (expected 3, got 2)
# 原因是等號右側的 p 只有 2 個元素（4 和 5），但左側卻準備了 3 個變數（x, y, z）來接收。

# 正確的做法應該是：
# x, y = p  # 變數數量與元素數量一致