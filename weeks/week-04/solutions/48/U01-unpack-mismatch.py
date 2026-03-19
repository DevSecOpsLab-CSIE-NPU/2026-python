# U1. 解包失敗的原因：變數數量 ≠ 元素數量（1.1）
# 展示解包操作中常見的錯誤情況

# 建立包含 2 個元素的元組
p = (4, 5)
print("元組:", p)

# 正確的解包方式
x, y = p
print(f"解包成功: x={x}, y={y}")

# 嘗試解包到 3 個變數會失敗
# 取消下面註解以查看錯誤
try:
    x, y, z = p  # ValueError: not enough values to unpack (expected 3, got 2)
except ValueError as e:
    print(f"解包失敗錯誤: {e}")
