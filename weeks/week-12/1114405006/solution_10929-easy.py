"""
UVA 10929 — 11 is a (multiple) 簡易版（含繁體中文詳細註解）

問題重點：判斷一個很長的整數（以字串表示）是否為 11 的倍數。

數學技巧（記憶口訣）：把位數從左到右以 1-based 編號，
- 將奇數位的數字相加、再減去偶數位的數字，
- 若差值能被 11 整除，原數即為 11 的倍數。

此檔為簡潔且易記的版本，並補上必要的註解，方便考場快速重現。
"""


def is_multiple_of_11_easy(num_str: str) -> bool:
    """簡潔版：判斷字串表示的數字是否為 11 的倍數。

    實作重點說明：
    1. 先用 `lstrip('0')` 去掉前導零（前導零不改變能否被 11 整除）。
    2. 使用單一變數 `total`，對字串每個字元按位數做加或減：
       - 如果位置是奇數（1,3,5...），就把數字加到 total 上；
       - 如果位置是偶數（2,4,6...），就把數字從 total 減去。
    3. 最後檢查 `total % 11 == 0` 即可。

    例子：
    - '121' -> (1 + 1) - 2 = 0 -> 0 % 11 == 0 -> 是 11 的倍數
    - '123' -> (1 + 3) - 2 = 2 -> 2 % 11 != 0 -> 不是 11 的倍數
    """
    # 去掉前導零（如果全為零則保留一個 '0'）
    num_str = num_str.lstrip('0') or '0'

    # total 採用加減混合計算（奇數位加、偶數位減）
    total = 0
    for index, ch in enumerate(num_str, start=1):
        # 用 ord 轉 int 比 int(ch) 快一點，但可讀性略差
        digit = ord(ch) - 48
        if index % 2 == 1:
            total += digit
        else:
            total -= digit

    # 如果 total 對 11 餘 0，代表原數為 11 的倍數
    return total % 11 == 0


def parse_and_run() -> None:
    """從標準輸入讀取多行數字字串，遇到 '0' 結束，並輸出題目要求格式。

    輸出格式：
    - 若為 11 的倍數："{n} is a multiple of 11." 
    - 否則："{n} is not a multiple of 11." 
    """
    import sys

    out_lines = []
    for line in sys.stdin:
        n = line.strip()
        if not n:
            continue
        if n == '0':
            break

        if is_multiple_of_11_easy(n):
            out_lines.append(f"{n} is a multiple of 11.")
        else:
            out_lines.append(f"{n} is not a multiple of 11.")

    sys.stdout.write("\n".join(out_lines))


if __name__ == '__main__':
    parse_and_run()
