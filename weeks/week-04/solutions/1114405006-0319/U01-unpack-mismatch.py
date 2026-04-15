# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）

# p 是一個 tuple，裡面只有 2 個元素。
p = (4, 5)

# 下列這行若取消註解會拋出 ValueError：
# 因為左邊有 3 個變數（x, y, z），
# 但右邊 tuple 只有 2 個值，兩邊數量不一致。
#
# Python 解包（unpacking）原則：
# - 一般解包時，左側變數個數必須與右側元素個數完全相同。
# - 不相同就會發生「too many values to unpack」或
#   「not enough values to unpack」這類錯誤。
#
# x, y, z = p  # ValueError：元素只有 2 個但變數要 3 個

# 正確示例（說明用）：
# x, y = p
#
# 若資料長度可能不固定，可用星號解包（說明用）：
# x, *rest = p
# 其中 rest 會接住剩餘元素（型別是 list）。
