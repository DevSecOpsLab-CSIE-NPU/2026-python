"""
UVA 10931 — Parity 簡易版（含繁體中文詳細註解）

這個版本的目標是把想法寫得更短、更好記。
核心做法只有兩步：
1. 把十進位整數轉成二進位字串。
2. 直接數二進位字串裡有幾個 '1'。

題目輸出格式：
The parity of B is P (mod 2).
其中 B 是二進位字串，P 是 '1' 的個數。

本檔保留最精簡、最好背的寫法，同時加上完整中文註解方便理解。
"""


def parity_easy(num: int) -> tuple[str, int]:
    """回傳整數的二進位字串，以及其中 '1' 的個數。

    參數：
    - num: 輸入的正整數

    回傳：
    - (binary_str, ones)
      binary_str: 去掉 '0b' 前綴後的二進位字串
      ones: 二進位字串中 '1' 的數量，也就是 parity

    例子：
    - 1  -> '1'     -> 1
    - 2  -> '10'    -> 1
    - 10 -> '1010'  -> 2
    - 21 -> '10101' -> 3
    """
    # bin(num) 會回傳像 '0b10101' 這樣的字串
    # 其中前兩個字元 '0b' 只是表示這是二進位，不是數字內容
    # 用 [2:] 把前綴切掉，就能得到乾淨的二進位字串
    binary_str = bin(num)[2:]

    # 直接用字串的 count('1') 方法統計 '1' 的個數
    # 這一步就是題目要的 parity
    ones = binary_str.count('1')

    # 回傳二進位字串和 1 的個數
    return binary_str, ones


def parse_and_run() -> None:
    """從標準輸入讀入多行整數，遇到 0 就停止，並輸出題目格式。

    輸入格式：
    - 每行一個整數
    - 最後以 0 結束

    輸出格式：
    - 對每個輸入數字，輸出：
      The parity of B is P (mod 2).
    """
    import sys

    # 先把所有輸出結果收集到列表中，最後一次輸出
    # 這樣比較好控制格式，也比較容易測試
    out_lines = []

    # 逐行讀取標準輸入
    for line in sys.stdin:
        # 去掉前後空白與換行符號
        text = line.strip()

        # 如果是空行，就直接跳過
        if not text:
            continue

        # 將字串轉成整數
        num = int(text)

        # 題目指定：遇到 0 就停止，不處理 0 本身
        if num == 0:
            break

        # 計算二進位字串與 parity
        binary_str, ones = parity_easy(num)

        # 按照題目規定組裝輸出字串
        out_lines.append(f"The parity of {binary_str} is {ones} (mod 2).")

    # 用換行字元把所有結果串起來，完整寫到標準輸出
    sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
    # 當檔案直接執行時，啟動 CLI 模式
    parse_and_run()
