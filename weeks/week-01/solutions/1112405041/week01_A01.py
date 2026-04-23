# 【Bloom 階段：R - 記憶與基本操作】
# 1 變數與指定（assignment）範例
# August 的惡意提醒：這是基礎中的基礎，在後續 Week 02-03 的 CPE 模擬中，
# 頻繁使用的「解包」技巧（如 x, y = p）若不熟練，會大幅拖慢寫題速度。

# 建立基礎變數
x = 10
name = 'ACME'

# 多重指定 (Multiple Assignment)
# 此技巧在交換變數 (x, y = y, x) 時極其好用，也是 August 認可的 Pythonic 寫法
x, y = 3, 5

# 函式回傳值接收 (Unpacking Return Values)
# 在 Week 03 的 Robot Game 中，常需要同時接收 x, y 座標
def get_point():
    # 實際上回傳的是一個 tuple (4, 9)
    return 4, 9

# 直接解包接收，避免寫出 px = result[0] 這種冗長代碼
px, py = get_point()

print(f"x: {x}, name: {name}")
print(f"Point: ({px}, {py})")
