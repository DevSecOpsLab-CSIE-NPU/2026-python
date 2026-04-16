"""UVA 272 - TeX Quoting

題意：
- 將普通雙引號 " 轉換成 TeX 引號。
- 奇數個 " (1st, 3rd, 5th...) 轉換為 `` （開啟引號）。
- 偶數個 " (2nd, 4th, 6th...) 轉換為 '' （關閉引號）。
- 其他文字保持不變。
- 引號計數跨越多行連續進行（不在每行重置）。
"""

import sys


def main() -> None:
    """讀入所有行，累計引號計數並進行轉換。"""
    quote_count = 0
    result = []

    for line in sys.stdin:
        # 移除尾端換行符，方便處理
        line = line.rstrip('\n')
        converted_line = ""

        for char in line:
            if char == '"':
                # 計數引號出現次數
                quote_count += 1
                # 奇數次用 ``，偶數次用 ''
                if quote_count % 2 == 1:
                    converted_line += "``"
                else:
                    converted_line += "''"
            else:
                # 其他字元直接保留
                converted_line += char

        result.append(converted_line)

    # 輸出所有行
    sys.stdout.write("\n".join(result) + "\n")


if __name__ == "__main__":
    main()
