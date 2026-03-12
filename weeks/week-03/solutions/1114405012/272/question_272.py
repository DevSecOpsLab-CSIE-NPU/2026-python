"""
UVA 272 - TEX Quotes（正式版）

題目重點：
把輸入文字中的一般雙引號 \", 依出現順序交替替換成：
1. 開始引號：``
2. 結束引號：''

規則說明：
- 第一個遇到的 \" 要換成 ``
- 第二個遇到的 \" 要換成 ''
- 第三個再換成 ``，第四個再換成 ''，依此類推
- 其他所有字元（包含換行、空白、標點）都必須原樣保留
"""

from __future__ import annotations


def convert_tex_quotes(text: str) -> str:
    """
    將一般雙引號轉為 TeX 方向性引號。

    參數：
    - text: 原始輸入全文（可包含多行）

    回傳：
    - 轉換後的全文字串
    """
    result_chars = []

    # True 表示下一個遇到的雙引號要當「開引號」``
    # False 表示下一個遇到的雙引號要當「閉引號」''
    use_open_quote = True

    for ch in text:
        if ch == '"':
            if use_open_quote:
                result_chars.append("``")
            else:
                result_chars.append("''")
            use_open_quote = not use_open_quote
        else:
            result_chars.append(ch)

    return "".join(result_chars)


def solve_text(text: str) -> str:
    """供評測使用的入口函式。"""
    return convert_tex_quotes(text)


if __name__ == "__main__":
    import sys

    data = sys.stdin.read()
    if data:
        # end="" 可避免 print 額外再補一個換行，確保輸出與規格一致
        print(solve_text(data), end="")
