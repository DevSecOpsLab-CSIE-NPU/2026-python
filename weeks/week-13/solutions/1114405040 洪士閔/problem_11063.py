"""
Problem 11063 - RGB to XYZ 轉換（包含 process() 方便 unit test）

此檔提供：
- `rgb_to_xyz(r,g,b)`: 將單一像素由 RGB 轉為 XYZ（浮點數）。
- `process(input_str)`: 解析整個輸入字串並回傳符合題目輸出的字串。

所有函式均加入繁體中文註解，方便教學與測試。
"""

from typing import List, Tuple


def rgb_to_xyz(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """將單一像素 (r,g,b) 轉換為 (X,Y,Z)。

    使用題目中給定的線性組合係數：
    X = 0.5149*R + 0.3244*G + 0.1607*B
    Y = 0.2654*R + 0.6704*G + 0.0642*B
    Z = 0.0248*R + 0.1248*G + 0.8504*B

    回傳三個浮點數 (x,y,z)。
    """
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z


def process(input_str: str) -> str:
    """解析整個輸入並回傳題目要求的輸出字串。

    輸入格式：第一行為整數 n，接著有 n 行，每行包含 n 個像素（每個像素由三個整數 R G B 表示）。
    輸出：對每一個像素（由上至下、由左至右）輸出一行 "X Y Z"，小數點後四位；最後一行輸出 "The average of Y is v"。
    """
    tokens = input_str.strip().split()
    if not tokens:
        return ""
    p = 0
    n = int(tokens[p]); p += 1
    total = n * n
    out_lines: List[str] = []
    sum_y = 0.0

    for i in range(total):
        # 依序讀取 R G B
        r = int(tokens[p]); g = int(tokens[p+1]); b = int(tokens[p+2]); p += 3
        x, y, z = rgb_to_xyz(r, g, b)
        sum_y += y
        # 依題目要求四捨五入到小數點後四位
        out_lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    avg_y = sum_y / total if total > 0 else 0.0
    out_lines.append(f"The average of Y is {avg_y:.4f}")
    return "\n".join(out_lines)


def main():
    import sys
    data = sys.stdin.read()
    print(process(data))


if __name__ == '__main__':
    main()
