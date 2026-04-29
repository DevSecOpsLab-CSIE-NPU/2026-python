# UVA 10242 - Fourth Point!!
import sys


def solve_standard():
    """
    Standard: 使用集合快速尋找重複點 (公共頂點)，然後運用向量加法求第四點。
    """
    for line in sys.stdin:
        if not line.strip():
            continue
        coords = list(map(float, line.split()))
        p1, p2, p3, p4 = coords[0:2], coords[2:4], coords[4:6], coords[6:8]

        points = [tuple(p1), tuple(p2), tuple(p3), tuple(p4)]

        # 尋找重複的點
        for i in range(len(points)):
            if points.count(points[i]) == 2:
                common = points[i]
                break

        # 剩下的兩個非公共點
        unique_points = [p for p in set(points) if p != common]

        if len(unique_points) == 2:
            x4 = unique_points[0][0] + unique_points[1][0] - common[0]
            y4 = unique_points[0][1] + unique_points[1][1] - common[1]
            print(f"{x4:.3f} {y4:.3f}")


def solve_easy():
    """
    Easy: 直觀比對座標找出交點，用簡單算術求未知點。
    """
    while True:
        try:
            line = input()
            if not line:
                break
            data = list(map(float, line.split()))
            x1, y1 = data[0], data[1]
            x2, y2 = data[2], data[3]
            x3, y3 = data[4], data[5]
            x4, y4 = data[6], data[7]

            # 判斷交點
            if (x1, y1) == (x3, y3):
                cx, cy = x1, y1
                p1, p2 = (x2, y2), (x4, y4)
            elif (x1, y1) == (x4, y4):
                cx, cy = x1, y1
                p1, p2 = (x2, y2), (x3, y3)
            elif (x2, y2) == (x3, y3):
                cx, cy = x2, y2
                p1, p2 = (x1, y1), (x4, y4)
            else:
                cx, cy = x2, y2
                p1, p2 = (x1, y1), (x3, y3)

            ans_x = p1[0] + p2[0] - cx
            ans_y = p1[1] + p2[1] - cy
            print(f"{ans_x:.3f} {ans_y:.3f}")
        except EOFError:
            break


def solve_manual():
    """
    Manual: 避免使用 tuple 或複雜資料結構，完全用手動迴圈和條件判斷，確保基礎記憶。
    """
    while True:
        try:
            line = input()
            if not line:
                break

            # 手動解析浮點數
            parts = []
            word = ""
            for char in line + " ":
                if char == " " or char == "\t":
                    if word:
                        parts.append(float(word))
                        word = ""
                else:
                    word += char

            x1, y1 = parts[0], parts[1]
            x2, y2 = parts[2], parts[3]
            x3, y3 = parts[4], parts[5]
            x4, y4 = parts[6], parts[7]

            if x1 == x3 and y1 == y3:
                ans_x = x2 + x4 - x1
                ans_y = y2 + y4 - y1
            elif x1 == x4 and y1 == y4:
                ans_x = x2 + x3 - x1
                ans_y = y2 + y3 - y1
            elif x2 == x3 and y2 == y3:
                ans_x = x1 + x4 - x2
                ans_y = y1 + y4 - y2
            else:
                ans_x = x1 + x3 - x2
                ans_y = y1 + y3 - y2

            print(f"{ans_x:.3f} {ans_y:.3f}")
        except EOFError:
            break


if __name__ == "__main__":
    solve_standard()
