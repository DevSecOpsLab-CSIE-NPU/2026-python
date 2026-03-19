# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）
#
# Python 的序列解包（unpacking）會把右側的序列（tuple/list 等）
# 一個一個對應到左側的變數。
#
# 例如：
#   x, y = (4, 5)
# 會把 4 指派給 x、把 5 指派給 y。
#
# 如果左邊變數數量和右邊元素數量不一致，就會發生 ValueError：
#   "not enough values to unpack" 或 "too many values to unpack"
#
# 若要處理可變長度，可以使用星號語法（*rest）來接收多餘元素。

p = (4, 5)
# x, y, z = p  # ValueError：元素只有 2 個但變數要 3 個
