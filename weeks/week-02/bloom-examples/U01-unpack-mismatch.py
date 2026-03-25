# ============================================================================
# U1. 解包失敗的診斷：變數數量 ≠ 序列元素數量（1.1）
# ============================================================================
# 本題演示解包（unpacking）失敗的常見原因及如何診斷。
# 
# 解包規則：
# 等式左邊的變數數量 必須 等於 右邊序列的元素數量
# 否則拋出 ValueError
# ============================================================================

print("【解包失敗示範】")
print("=" * 50)
print()

print("【場景】")
p = (4, 5)
print(f"序列 p = {p}  # 包含 2 個元素")
print()

print("【嘗試 1】正確的解包 - 變數數量 = 元素數量")
print()
print("代碼：x, y = p")
x, y = p
print(f"結果：x = {x}, y = {y}  ✓ 成功")
print()

print("【嘗試 2】解包失敗 - 變數太多")
print()
print("代碼：x, y, z = p")
print("錯誤類型：ValueError")
print()

try:
    x, y, z = p
except ValueError as e:
    print(f"❌ 錯誤信息：{e}")
    print()
    print("說明：")
    print(f"  - 序列 p 只有 2 個元素")
    print(f"  - 但提供了 3 個變數 (x, y, z)")
    print(f"  - Python 無法將 2 個元素分配給 3 個變數")
    print()

print("【嘗試 3】解包失敗 - 變數太少")
print()
print("代碼：x = p")
print("結果：x = (4, 5)  ✓ 成功（但 x 成為元組，非分解）")
x = p
print(f"  x = {x}, 型別 = {type(x).__name__}")
print()

print("代碼：x, = p  # 注意右邊的逗號")
print("錯誤類型：ValueError")
print()

try:
    x, = p
except ValueError as e:
    print(f"❌ 錯誤信息：{e}")
    print()
    print("說明：")
    print(f"  - x, 表示期望 1 個元素")
    print(f"  - 但 p 有 2 個元素")
    print(f"  - 無法匹配")
    print()

print("\n" + "=" * 50)
print("【診斷方法】")
print("=" * 50)
print("""
遇到 ValueError 時的檢查清單：

1. 確認序列的元素數量：
   len(sequence) 或直接查看內容

2. 確認等式左邊的變數數量：
   數一下 = 左邊有幾個變數名

3. 兩個數字必須相等

4. 如果數量不確定，使用 * 解包（下一題）
""")

print("\n例子：")
data = [1, 2, 3]
print(f"序列：data = {data}  # 元素數量 = {len(data)}")
print(f"✓ x, y, z = data  # 3 個變數，可行")
print(f"✗ a, b = data     # 2 個變數，失敗")
print(f"✓ a, *b = data    # 使用 *，可變數量")
