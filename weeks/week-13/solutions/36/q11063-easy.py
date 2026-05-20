from typing import List, Tuple


def convert_pixel(rgb: Tuple[int, int, int]) -> Tuple[float, float, float]:
    """更淺顯地寫出 RGB 轉 XYZ 的公式。"""
    r, g, b = rgb
    X = 0.5149 * r + 0.3244 * g + 0.1607 * b
    Y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    Z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return X, Y, Z


def solve(lines: List[str]) -> List[str]:
    """用最容易理解的方式讀取每個像素並輸出結果。"""
    items: List[int] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        for token in line.split():
            items.append(int(token))
    if not items:
        return []

    n = items[0]
    pixels = items[1:]
    output: List[str] = []
    total_y = 0.0
    pixel_count = n * n
    index = 0

    for _ in range(pixel_count):
        r = pixels[index]
        g = pixels[index + 1]
        b = pixels[index + 2]
        index += 3
        x, y, z = convert_pixel((r, g, b))
        total_y += y
        output.append(f"{x:.4f} {y:.4f} {z:.4f}")

    average_y = total_y / pixel_count
    output.append(f"The average of Y is {average_y:.4f}")
    return output


def main() -> None:
    import sys
    lines = [line.rstrip("\n") for line in sys.stdin]
    result = solve(lines)
    print("\n".join(result))


if __name__ == "__main__":
    main()
