# U10. zip 為何只能用一次（1.8）
# 展示 zip 返回迭代器物件，迭代後就被消耗完的特性

# 股票名稱和價格的字典
prices = {'A': 2.0, 'B': 1.0}

# 建立 zip 迭代器：配對值和鍵
z = zip(prices.values(), prices.keys())
print("zip 物件:", z)
# 結果：zip 物件（惰性求值的迭代器，不是列表）

# 第一次使用：計算最小值
print("\n第一次使用 - min(z):")
min_result = min(z)  # 結果：(1.0, 'B')
print(f"  結果: {min_result}")
print("  此時迭代器已經被完全消耗（遍歷過所有元素）")

# ❌ 第二次使用：計算最大值
print("\n第二次使用 - max(z):")
try:
    max_result = max(z)  # 會失敗！
    print(f"  結果: {max_result}")
except ValueError as e:
    print(f"  失敗: {e}")
    print("  原因：迭代器中的元素已經被消耗，無法再次迭代")

# ✓ 解決方法：如果需要多次使用相同的資料，轉換為列表
print("\n解決方法 - 轉換為列表:")
z_list = list(zip(prices.values(), prices.keys()))
print(f"  z_list: {z_list}")
# 現在 z_list = [(2.0, 'A'), (1.0, 'B')]

print(f"  min(z_list): {min(z_list)}")
print(f"  max(z_list): {max(z_list)}")
print("  都能正常工作！")

# 記憶體考量：
print("\n記憶體考量:")
print("  - 使用迭代器（zip）：省記憶體，但只能用一次")
print("  - 轉換為列表（list(zip(...))：佔用記憶體，但可重複使用")
