"""
UVA 11063 — XYZ 色彩轉換 程式模組（詳細繁體中文註解）

本模組包含兩個主要功能：
- `convert_rgb_to_xyz(pixels)`：將像素列表（每個元素為 (R,G,B)）轉換為題目要求的輸出字串列表。
- `parse_input_and_process(stdin_text)`：解析題目輸入格式（第一行 n，接下來 n 行每行 n 個像素），並呼叫轉換函式。

輸出格式與規則提醒：
- 對每個像素輸出一行，格式為 "X Y Z"，每個值需四捨五入到小數第 4 位。
- 在輸出所有像素後，再輸出一行："The average of Y is <avg>"，其中 <avg> 也四捨五入到小數第 4 位。

此檔也支援以命令列直接執行（從 stdin 讀入整個輸入內容並輸出結果），方便本地測試或線上 judge 使用。
"""

from typing import List, Tuple


def convert_rgb_to_xyz(pixels: List[Tuple[int, int, int]]) -> List[str]:
    """
    將像素列表轉換為題目要求的輸出行清單。

    參數：
    - pixels: List[Tuple[int,int,int]]，每個像素為 (R,G,B)，R/G/B 範圍為 0..255。

    回傳：
    - List[str]：每個元素為一行輸出字串，最後一行為平均 Y，皆已格式化為小數第 4 位。
    """
    lines: List[str] = []
    Ys: List[float] = []

    # 逐像素計算 XYZ
    for (R, G, B) in pixels:
        # 依題目所給的係數計算 X, Y, Z
        # 這裡直接用浮點數乘法，題目容許誤差 1e-4
        X = 0.5149 * R + 0.3244 * G + 0.1607 * B
        Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
        Z = 0.0248 * R + 0.1248 * G + 0.8504 * B

        Ys.append(Y)

        # 格式化到小數第 4 位（Python 的格式化會做四捨五入）
        lines.append(f"{X:.4f} {Y:.4f} {Z:.4f}")

    # 計算平均 Y，保護性地處理空列表情況
    avgY = sum(Ys) / len(Ys) if Ys else 0.0
    lines.append(f"The average of Y is {avgY:.4f}")
    return lines


def parse_input_and_process(stdin_text: str) -> List[str]:
    """
    解析題目輸入文字並回傳要輸出的行清單。

    輸入文字格式：
      第一個數字為 n（影像寬/高），接著有 n*n 個像素，每個像素由三個整數 R G B 組成，
      像素間與數字間以空白分隔。範例：

      2
      255 3 192 0 0 0
      128 128 128 255 255 255

    解析流程：
    1. 以 whitespace 分割所有 token（包括換行、空格）。
    2. 第一個 token 轉成整數 n，接著逐三個 token 讀入一個像素，總共 n*n 個像素。
    3. 若 token 數不足，會拋出 ValueError 提醒輸入格式錯誤。

    最後呼叫 `convert_rgb_to_xyz` 產生輸出行並回傳。
    """
    parts = stdin_text.strip().split()
    if not parts:
        return []
    it = iter(parts)
    try:
        n = int(next(it))
    except StopIteration:
        raise ValueError("輸入為空或格式錯誤，找不到 n")
    except ValueError:
        raise ValueError("第一個 token 需為整數 n")

    pixels: List[Tuple[int, int, int]] = []
    # 預期像素數量
    expected = n * n
    for i in range(expected):
        try:
            R = int(next(it))
            G = int(next(it))
            B = int(next(it))
        except StopIteration:
            raise ValueError(f"輸入格式不完整：預期 {expected} 個像素，但資料不足 (在第 {i+1} 個像素讀取時失敗)")
        pixels.append((R, G, B))

    return convert_rgb_to_xyz(pixels)


if __name__ == "__main__":
    import sys

    # 從標準輸入讀取整個輸入內容，方便在 judge 或測試時以檔案重定向或貼上輸入
    text = sys.stdin.read()
    lines = parse_input_and_process(text)
    for line in lines:
        print(line)
