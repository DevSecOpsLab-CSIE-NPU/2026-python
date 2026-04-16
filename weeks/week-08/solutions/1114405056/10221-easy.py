import math

# 弧長與弦長：根據衛星高度和角度計算弧長和弦長

while True:
    try:
        line = input().split()
    except EOFError:
        break

    s = int(line[0])   # 衛星高度（公里）
    a_val = int(line[1])  # 角度數值
    unit = line[2]     # 單位：deg（度）或 min（角分）

    # 將角度換算成弧度
    if unit == 'deg':
        angle = math.radians(a_val)
    else:
        # 角分：1 度 = 60 角分
        angle = math.radians(a_val / 60.0)

    r = 6440 + s  # 地球半徑 6440 公里加上衛星高度

    # 弧長 = 半徑 × 角度（弧度）
    arc = r * angle

    # 弦長 = 2 × 半徑 × sin(角度 / 2)
    chord = 2 * r * math.sin(angle / 2)

    print(f"{arc:.6f} {chord:.6f}")
