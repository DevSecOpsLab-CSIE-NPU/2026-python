from typing import List, Tuple


def convert_pixel(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
    """將單一像素由 RGB 轉成 XYZ。"""
    r, g, b = rgb
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z


def solve(lines: List[str]) -> List[str]:
    """解析輸入並輸出所有像素的 XYZ 與平均亮度。"""
    data = [int(value) for line in lines for value in line.split()]
    if not data:
        return []

    n = data[0]
    values = data[1:]
    expected = n * n * 3
    if len(values) != expected:
        raise ValueError("像素資料長度不正確")

    output: List[str] = []
    total_y = 0.0
    pixel_index = 0
    for _ in range(n * n):
        r = values[pixel_index]
        g = values[pixel_index + 1]
        b = values[pixel_index + 2]
        pixel_index += 3
        x, y, z = convert_pixel((r, g, b))
        total_y += y
        output.append(f"{x:.4f} {y:.4f} {z:.4f}")

    average_y = total_y / (n * n)
    output.append(f"The average of Y is {average_y:.4f}")
    return output


def main() -> None:
    import sys
    lines = [line.rstrip("\n") for line in sys.stdin]
    print("\n".join(solve(lines)))


if __name__ == "__main__":
    main()
