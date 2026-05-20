"""
簡易版 Problem 11063（RGB -> XYZ） — 詳細註解版

目的：提供一個結構清晰、容易記憶的實作，讓學生能快速理解題目流程與實作要點。

主要重點：
- `rgb_to_xyz`：單一像素的線性轉換函式，直接對應題目給的係數。
- `process`：負責整個輸入輸出流程，包括 token 化、依序讀取像素、呼叫轉換函式、累加 Y 值以計算平均。

教學註解指南：
- 程式不追求過度微優化，閱讀性優先；變數命名與步驟分明，方便手寫重現。
- 對於競賽或考場，記住兩件事：1) 轉換公式；2) 輸出要格式化到小數點 4 位。

複雜度：解析與計算時間皆為 O(n^2)（每個像素常數時間轉換），記憶體為 O(1) 額外空間（不含輸出緩衝）。
"""

from typing import List, Tuple


def rgb_to_xyz(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """將單一像素 (R,G,B) 轉為 (X,Y,Z)。

    欄位說明：R,G,B 為整數（0..255）。輸出為浮點數。
    直接把題目給的線性組合套上即可。函式不做四捨五入，讓呼叫端統一處理格式化。
    """
    # 直接套用題目提供的係數
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z


def process(input_str: str) -> str:
    """解析輸入並回傳多行輸出字串（每個像素一行 X Y Z，最後一行為 Y 平均）。

    步驟細節：
    1. 把整個輸入用空白拆成 token（這樣可以同時處理每行多個像素或任意換行情況）。
    2. 第一個 token 為整數 n，代表影像為 n x n。
    3. 接下來有 n*n*3 個整數，依序為每個像素的 R G B。
    4. 對每個像素呼叫 `rgb_to_xyz`，累加 Y 值以便最後計算平均。
    5. 輸出時統一用小數點 4 位（四捨五入由 Python 的格式化完成）。

    注意：此實作假設輸入為合法格式（符合題目限制），在競賽/考場環境中可接受。
    """
    tokens = input_str.strip().split()
    if not tokens:
        return ""
    p = 0
    n = int(tokens[p]); p += 1
    total = n * n
    out_lines: List[str] = []
    sum_y = 0.0

    # 逐像素處理：每個像素由三個整數 (R,G,B) 組成
    for _ in range(total):
        # 從 tokens 讀取三個整數，注意 p 的移動
        r = int(tokens[p]); g = int(tokens[p+1]); b = int(tokens[p+2]); p += 3
        x, y, z = rgb_to_xyz(r, g, b)
        sum_y += y
        # 格式化：小數點 4 位，Python f-string 會做四捨五入
        out_lines.append(f"{x:.4f} {y:.4f} {z:.4f}")

    # 計算平均 Y（影像亮度）並格式化
    avg_y = sum_y / total if total > 0 else 0.0
    out_lines.append(f"The average of Y is {avg_y:.4f}")
    return "\n".join(out_lines)


def main():
    import sys
    data = sys.stdin.read()
    print(process(data))


if __name__ == '__main__':
    main()
