# 主題 01：變數與指定（Assignment）- 簡易教學版
# 繁體中文詳細註解版本

# 基本變數指定（assignment）
x = 10           # 將整數 10 指定給變數 x
name = 'ACME'    # 將字串 'ACME' 指定給變數 name

# 多重指定（multiple assignment）
# 同時將多個值指定給多個變數
x, y = 3, 5

# 解包函式回傳值
# 函式 get_point() 回傳兩個值（tuple），我們把它們解包到 px 和 py
def get_point():
    """回傳一個座標點 (4, 9)"""
    return 4, 9

px, py = get_point()

# 列印結果來驗證
print(f"x = {x}, name = {name}")
print(f"x, y = {x}, {y}")
print(f"座標點: ({px}, {py})")
