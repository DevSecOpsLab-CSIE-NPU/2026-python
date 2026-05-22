"""
簡易版：UVA 11063 — XYZ 色彩轉換（-easy）

目的：提供最簡潔、容易記憶的實作，讓學生能快速理解轉換步驟。

說明重點：
- 使用一個簡單的函式 `convert_rgb_to_xyz`（名稱與正規版一致，便於呼叫），
  直接對每個像素用內建的浮點運算計算 X、Y、Z，最後回傳已格式化的字串列表。
- 若要在測試或其他程式中載入此檔（因檔名包含 '-'），請使用 `importlib.util.spec_from_file_location` 動態載入。
"""

def convert_rgb_to_xyz(pixels):
    """
    簡單直觀的轉換函式（無 type hints，易於背誦）：

    參數：
      pixels: list of (R,G,B) tuples

    回傳：
      list of strings，每個元素為一行輸出（最後一行為平均 Y）
    """
    lines = []
    Ys = []

    for R, G, B in pixels:
        X = 0.5149 * R + 0.3244 * G + 0.1607 * B
        Y = 0.2654 * R + 0.6704 * G + 0.0642 * B
        Z = 0.0248 * R + 0.1248 * G + 0.8504 * B

        Ys.append(Y)
        # 格式化到小數第 4 位
        lines.append("{:.4f} {:.4f} {:.4f}".format(X, Y, Z))

    avgY = sum(Ys) / len(Ys) if Ys else 0.0
    lines.append("The average of Y is {:.4f}".format(avgY))
    return lines


if __name__ == "__main__":
    # 互動示範：簡單跑一個像素
    print(convert_rgb_to_xyz([(255, 3, 192)]))
