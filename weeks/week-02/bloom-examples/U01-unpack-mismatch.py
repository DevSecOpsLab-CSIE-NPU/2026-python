"""U01: 解包數量不一致會噴 ValueError。"""

p = (4, 5)
print('原始資料:', p)

try:
    x, y, z = p
except ValueError as e:
    # 右側只有 2 個值，左側卻要接 3 個變數
    print('解包失敗:', e)
