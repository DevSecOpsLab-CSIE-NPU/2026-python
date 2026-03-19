# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）
#
# 觀念重點：序列解包時，左邊變數個數必須與右邊元素個數一致。

p = (4, 5)

# p 只有 2 個元素，若用 3 個變數接，就會丟 ValueError。
# x, y, z = p  # ValueError：not enough values to unpack

# 正確寫法之一（剛好 2 個變數）：
# x, y = p
