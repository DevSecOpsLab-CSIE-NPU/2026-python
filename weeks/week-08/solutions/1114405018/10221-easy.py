import math
import sys


def solve(text):
    """把題目輸入轉成答案字串。"""

    out = []

    # 題目是多筆測資，每一行一筆，直接逐行處理最簡單
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue

        s, angle, unit = line.split()
        s = int(s)
        angle = float(angle)

        # 地球半徑固定 6440 公里
        radius = 6440 + s

        # deg 代表角度，min 代表角分，先都轉成弧度
        if unit == "deg":
            theta = math.radians(angle)
        else:
            theta = math.radians(angle / 60.0)

        # 弧長 = 半徑 × 圓心角
        arc = radius * theta

        # 弦長 = 2 × 半徑 × sin(圓心角 / 2)
        chord = 2 * radius * math.sin(theta / 2.0)

        out.append(f"{arc:.6f} {chord:.6f}")

    return "\n".join(out)


def main():
    """競賽模式入口：讀標準輸入，印出答案。"""

    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()