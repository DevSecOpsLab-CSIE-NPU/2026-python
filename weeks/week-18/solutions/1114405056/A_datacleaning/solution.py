"""第一題：資料清理 (Data Cleaning)

學號末兩碼為 56，個位數 u = 6，
所以 D = 4（整除常數）。

本題需要進行以下操作：
1. 保序去重（保留第一次出現的元素）
2. 篩選能被 D 整除的數
3. 排序並輸出，或輸出 "NONE"
"""

import sys

D = 4  # 整除常數


def dedupe(items):
    """保序去重：產生器，依序產出第一次出現的項目。"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def main():
    """主程式：讀取多組測資並輸出結果。
    
    輸入格式：多組測資，每組先一個整數 n，接著 n 個整數；
    遇到 n == 0 則結束。
    """
    data = sys.stdin.buffer.read().split()
    i = 0
    out_lines = []

    while i < len(data):
        n = int(data[i])
        i += 1
        
        if n == 0:
            break

        # 讀取該組的 n 個整數
        group = list(map(int, data[i:i+n]))
        i += n

        # 保序去重，然後篩選能被 D 整除的數
        keep = [x for x in dedupe(group) if x % D == 0]
        keep.sort()
        
        # 輸出結果
        out_lines.append(" ".join(map(str, keep)) if keep else "NONE")

    print("\n".join(out_lines))


if __name__ == "__main__":
    main()
