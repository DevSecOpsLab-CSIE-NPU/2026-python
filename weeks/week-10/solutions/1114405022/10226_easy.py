"""UVA 10226 - Hardwood Species

好記版（-easy）：
1. 先把整份輸入切成「每一筆測資一塊」
2. 每塊直接做次數統計
3. 排序後輸出百分比

這個版本的重點是流程非常固定，方便考場快速回想。
"""

from collections import Counter
import sys


def solve(data: str) -> str:
    # 把 Windows 的換行 \r\n 統一成 \n，避免分割時出現平台差異。
    text = data.replace("\r\n", "\n")

    # 去掉開頭/結尾多餘空白，避免 split 後多出空區塊。
    text = text.strip()
    if not text:
        return ""

    # 第一行是測資數量，先切出第一個換行位置。
    first_newline = text.find("\n")
    if first_newline == -1:
        return ""

    t = int(text[:first_newline].strip())

    # 剩下內容通常是「空行 + 測資內容」，先去掉前面空白再處理。
    rest = text[first_newline + 1 :].lstrip("\n")

    # UVA 10226 每筆測資之間以空行分隔。
    # 因此可直接用 "\n\n" 分割成每一筆。
    blocks = rest.split("\n\n") if rest else []

    # 保險做法：只取前 t 筆，避免尾端異常空白造成多餘區塊。
    blocks = blocks[:t]

    answers = []

    for block in blocks:
        # 每一行就是一個樹種名稱（名稱可能有空白，所以不能再 split 空白）。
        trees = [line for line in block.split("\n") if line != ""]

        # Counter 一次完成次數統計。
        freq = Counter(trees)
        total = len(trees)

        # 題目要求字典序輸出。
        lines = []
        for tree in sorted(freq.keys()):
            percent = freq[tree] * 100.0 / total
            lines.append(f"{tree} {percent:.4f}")

        answers.append("\n".join(lines))

    # 不同測資之間要空一行。
    return "\n\n".join(answers)


def main() -> None:
    # 一次讀完整個標準輸入，最適合這題空行分隔格式。
    data = sys.stdin.read()
    output = solve(data)
    if output:
        print(output)


if __name__ == "__main__":
    main()
