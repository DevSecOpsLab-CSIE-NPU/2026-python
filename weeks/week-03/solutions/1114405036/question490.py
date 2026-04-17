# UVA 490: Rotate text 90 degrees clockwise
# 將多行文字視為矩陣後旋轉，並以空白補齊短行

def rotate_text(lines):
    max_width = max(len(line) for line in lines) if lines else 0
    padded = [line.ljust(max_width) for line in lines]
    rotated = []
    for col in range(max_width):
        row_chars = []
        for row in range(len(padded) - 1, -1, -1):
            row_chars.append(padded[row][col])
        rotated.append(''.join(row_chars).rstrip())
    return rotated


def solve_490(input_text):
    lines = input_text.splitlines()
    return '\n'.join(rotate_text(lines))


def main():
    import sys
    print(solve_490(sys.stdin.read()))


if __name__ == '__main__':
    main()
