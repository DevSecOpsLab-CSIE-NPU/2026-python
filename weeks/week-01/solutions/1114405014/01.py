# 01.py - 變數賦值、元組拆包與函式返回多個值的範例
x = 10
name = '凃彥任'

# 使用元組拆包同時給兩個變數賦值
x, y = 9, 10


def get_point():
    # 函式返回一個坐標元組
    return 7, 1

# 呼叫 get_point 並將結果拆包到 px 和 py
px, py = get_point()

# 顯示各變數值
print(f"x={x}, y={y}, name={name}")
print(f"px={px}, py={py}")
print("get_point() returned", get_point())