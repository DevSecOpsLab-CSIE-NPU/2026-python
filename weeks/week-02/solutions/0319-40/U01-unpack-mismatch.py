# U1. 解包失敗的原因：變數數量 != 元素數量（1.1）

p = (4, 5)

# 正確解包（2 個變數接 2 個元素）
x, y = p
print("正確解包:", x, y)

# 示範錯誤解包，並捕捉錯誤訊息
try:
    x, y, z = p
except ValueError as err:
    print("錯誤解包觸發 ValueError:", err)
