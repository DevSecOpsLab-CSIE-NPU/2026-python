# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）
# 說明：在解包 (Unpacking) 時，左邊的變數數量必須精確等於右邊的序列長度。

p = (4, 5)
# 這樣會噴錯：ValueError: not enough values to unpack (expected 3, got 2)
# x, y, z = p 

# 正確解法：變數數量要對齊，或是使用星號 (*)
x, y = p