import math
import sys


def main():
    # 一行一筆測資，直到 EOF
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        # 每筆資料包含高度、角度與單位
        s, angle, unit = line.split()
        s = float(s)
        angle = float(angle)

        # 先把角度轉成弧度
        if unit == 'min':
            # 分要先換成度，再交給 math.radians 轉弧度
            angle = angle / 60.0
        radians = math.radians(angle)

        radius = 6440.0 + s
        # 弧長與弦長都直接套公式即可
        arc_length = radius * radians
        chord_length = 2.0 * radius * math.sin(radians / 2.0)

        print(f'{arc_length:.6f} {chord_length:.6f}')


if __name__ == '__main__':
    main()
