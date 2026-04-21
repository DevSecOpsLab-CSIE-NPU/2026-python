import sys


def main() -> None:
    # 先把所有輸入行讀進來，因為旋轉時要一次看完整個矩陣。
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    # 找出最長的一列，這就是旋轉後每一欄要補空白的基準寬度。
    max_width = max(len(line) for line in lines)
    line_count = len(lines)

    result = []

    # 旋轉 90 度順時針：
    # 原本最左邊的欄位，會變成輸出最上面的那一列。
    for column in range(max_width):
        chars = []

        # 由下往上讀原本的每一行，拼成新的橫列。
        for row in range(line_count - 1, -1, -1):
            text = lines[row]
            if column < len(text):
                chars.append(text[column])
            else:
                # 原本這一行較短，就補空白維持矩形。
                chars.append(' ')

        result.append(''.join(chars))

    # 不要用 rstrip，因為題目要求保留右側空白。
    sys.stdout.write('\n'.join(result) + ('\n' if result else ''))


if __name__ == '__main__':
    main()