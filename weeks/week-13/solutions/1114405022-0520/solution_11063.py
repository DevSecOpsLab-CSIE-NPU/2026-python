import sys

def rgb_to_xyz(r, g, b):
    """將 RGB 色彩轉換為 XYZ 表色系統"""
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z

def solve(data=None):
    """主程式：讀入 n、像素資料，計算並輸出 XYZ 與平均亮度"""
    if data is None:
        data = sys.stdin.read()
    lines = data.strip().splitlines()
    n = int(lines[0])
    pixels = []
    for line in lines[1:1+n]:
        nums = list(map(int, line.split()))
        # 每三個數字為一組像素 (R, G, B)
        for i in range(0, len(nums), 3):
            pixels.append((nums[i], nums[i+1], nums[i+2]))
    out_lines = []
    total_y = 0.0
    for r, g, b in pixels:
        x, y, z = rgb_to_xyz(r, g, b)
        out_lines.append(f"{x:.4f} {y:.4f} {z:.4f}")
        total_y += y
    avg_y = total_y / len(pixels)
    out_lines.append(f"The average of Y is {avg_y:.4f}")
    return "\n".join(out_lines) + "\n"

if __name__ == "__main__":
    sys.stdout.write(solve())
