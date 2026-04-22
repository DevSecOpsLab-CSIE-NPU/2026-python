# R20. ChainMap 合併映射（1.20）
# ChainMap 可把多個 dict 疊成一個「查詢視圖」，不會真的複製資料。

from collections import ChainMap

a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}
c = ChainMap(a, b)

print("a:", a)
print("b:", b)
print("ChainMap keys:", list(c.keys()))

# 查詢順序由左到右：先找 a，再找 b。
print("c['x'] =", c["x"])  # 來自 a
print("c['y'] =", c["y"])  # 來自 b
print("c['z'] =", c["z"])  # a 與 b 都有，優先取 a

# 寫入會寫到第一層 mapping（這裡是 a）。
c["w"] = 40
print("寫入 c['w']=40 後，a:", a)
print("b 不受影響:", b)
