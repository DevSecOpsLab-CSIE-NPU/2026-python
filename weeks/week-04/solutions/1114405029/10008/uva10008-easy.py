def solve(data: str) -> str:
    # 將整份輸入依照換行切開
    lines = data.splitlines()

    # 第一行表示後面共有幾行文字需要分析
    n = int(lines[0])

    # 使用字典來統計每個英文字母出現的次數
    # 例如 counts["A"] = 3，代表 A 出現 3 次
    counts = {}

    # 逐行處理後面的 n 行文字
    for i in range(1, n + 1):
        line = lines[i]

        # 題目要求大小寫視為相同，所以先全部轉成大寫
        line = line.upper()

        # 逐字元檢查
        for ch in line:
            # 只統計英文字母 A 到 Z
            if "A" <= ch <= "Z":
                if ch not in counts:
                    counts[ch] = 0
                counts[ch] += 1

    # 將字典轉成串列，方便排序
    # 每個元素會長成 (字母, 次數)
    items = list(counts.items())

    # 排序規則：
    # 1. 次數由大到小
    # 2. 若次數相同，字母由小到大
    items.sort(key=lambda item: (-item[1], item[0]))

    # 把排序後的結果組成題目要求的輸出格式
    result_lines = []
    for letter, count in items:
        result_lines.append(f"{letter} {count}")

    # 每筆結果用換行串起來
    return "\n".join(result_lines)


if __name__ == "__main__":
    import sys

    # 讀取標準輸入，交給 solve 處理，再輸出答案
    input_data = sys.stdin.read()
    print(solve(input_data))