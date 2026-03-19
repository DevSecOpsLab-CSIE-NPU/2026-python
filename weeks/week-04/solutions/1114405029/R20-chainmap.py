# R20. ChainMap 合併映射（1.20）

# 從 collections 模組匯入 ChainMap
# ChainMap 的功能是把多個字典「串接」起來，
# 看起來像是一個整體的字典，但實際上並沒有真的把資料複製合併
from collections import ChainMap

# 建立第一個字典 a
# 其中包含鍵 x 與 z
a = {'x': 1, 'z': 3}

# 建立第二個字典 b
# 其中包含鍵 y 與 z
b = {'y': 2, 'z': 4}

# 使用 ChainMap 將 a 與 b 合併成一個新的映射物件 c
# 查找資料時，會依照傳入順序由左到右搜尋
# 也就是先找 a，找不到再找 b
c = ChainMap(a, b)

# 取出 c 中鍵為 'x' 的值
# 因為 a 中有 x，所以會直接取到 a['x']，也就是 1
x_value = c['x']

# 取出 c 中鍵為 'z' 的值
# 雖然 a 和 b 都有 z，
# 但是 ChainMap 會優先使用前面字典中的值
# 因此這裡會取到 a['z']，也就是 3，而不是 b['z'] 的 4
z_value = c['z']  # 取到 a 的 z

# 印出原始字典 a
print("原始字典 a：", a)

# 印出原始字典 b
print("原始字典 b：", b)

print()  # 空一行，讓輸出結果更清楚

# 印出 ChainMap 物件 c
print("ChainMap 合併後的映射 c：")
print(c)

print()  # 空一行，讓輸出結果更清楚

# 印出 c['x'] 的結果
print("c['x'] 的值：", x_value)

# 印出 c['z'] 的結果
print("c['z'] 的值：", z_value)

print()  # 空一行，讓輸出結果更清楚

# 額外說明 a 和 b 中各自的 z 值，方便比較
print("a['z'] 的值：", a['z'])
print("b['z'] 的值：", b['z'])

print()

# 說明為什麼 c['z'] 會取到 a 的 z
print("因為 ChainMap 會依照順序先找前面的字典，所以 c['z'] 會先取到 a 中的 z。")