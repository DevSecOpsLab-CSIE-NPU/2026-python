"""UVA 10226 - Hardwood Species

一般版：使用逐行掃描的方式解析輸入，
可正確處理多筆測資、空行分隔、以及名稱含空白的樹種。
"""

from collections import defaultdict
import sys


def solve(data: str) -> str:
    # 先把輸入切成行，保留空字串（空行）以便辨識測資分隔。
    lines = data.splitlines()
    if not lines:
        return ""

    # 第一行是測資數量，前後空白要去除再轉整數。
    t = int(lines[0].strip())
    i = 1

    # 讀完測資數量後，常見格式會有一個空行，先略過。
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    outputs = []

    for case_idx in range(t):
        counter = defaultdict(int)
        total = 0

        # 讀取本筆測資直到遇到空行（或檔尾）。
        while i < len(lines) and lines[i].strip() != "":
            tree = lines[i]
            counter[tree] += 1
            total += 1
            i += 1

        # 依字典序輸出樹種，百分比固定四位小數。
        case_lines = []
        for tree in sorted(counter):
            percent = (counter[tree] * 100.0) / total
            case_lines.append(f"{tree} {percent:.4f}")

        outputs.append("\n".join(case_lines))

        # 移到下一筆測資（跳過測資間空行）。
        while i < len(lines) and lines[i].strip() == "":
            i += 1

    # 測資間要空一行。
    return "\n\n".join(outputs)


def main() -> None:
    data = sys.stdin.read()
    result = solve(data)
    if result:
        print(result)


if __name__ == "__main__":
    main()
