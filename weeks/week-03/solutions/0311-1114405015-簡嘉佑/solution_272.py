"""
UVA 272 - TEX Quotes（正式版）

題意摘要：
  把輸入文字中的一般雙引號 (") 依序替換成 TeX 方向引號：
    - 第 1、3、5... 個 " 變成 ``
    - 第 2、4、6... 個 " 變成 ''
  其他字元一律不改。

關鍵觀念：
  只需要一個布林狀態 `is_open` 記錄下一個雙引號應該是開引號還是關引號。
  每遇到一次雙引號就切換狀態。
"""

from __future__ import annotations

import sys


def convert_tex_quotes(text: str, is_open: bool = True) -> tuple[str, bool]:
    """
    轉換單行（或單段）文字中的雙引號。

    :param text: 要處理的字串
    :param is_open: 下一個 " 是否該替換成 ``
    :return: (轉換後字串, 更新後狀態)

    規則：
      - 當字元不是 "：原樣保留
      - 當字元是 "：
          is_open=True  -> ``
          is_open=False -> ''
        並且反轉 is_open 狀態
    """
    out: list[str] = []

    for ch in text:
        if ch == '"':
            if is_open:
                out.append("``")
            else:
                out.append("''")
            is_open = not is_open
        else:
            out.append(ch)

    return "".join(out), is_open


def convert_lines(lines: list[str]) -> list[str]:
    """
    轉換多行文字（共用同一個引號狀態）。

    :param lines: 每行輸入（不含換行）
    :return: 每行轉換結果

    注意：UVA 272 是整份輸入直到 EOF，因此引號狀態要跨行延續。
    """
    is_open = True
    result: list[str] = []

    for line in lines:
        converted, is_open = convert_tex_quotes(line, is_open)
        result.append(converted)

    return result


def main() -> None:
    """逐行讀取標準輸入，輸出轉換後文字。"""
    is_open = True

    for raw_line in sys.stdin:
        line = raw_line.rstrip("\n")
        converted, is_open = convert_tex_quotes(line, is_open)
        print(converted)


if __name__ == "__main__":
    main()
