# -*- coding: utf-8 -*-
"""
凱撒密碼（Caesar Cipher）－ AI 教學版（簡單好記寫法）
學號 1114405055 的參數：SHIFT = 6

這一版的核心想法：
    不用每個字元自己算 ord()/chr()，而是先把「整套 26 個大寫字母」
    和「整套 26 個小寫字母」各自做好「位移後對照表」（translate table），
    之後不管多長的字串，呼叫一次 str.translate() 就能整行轉換完畢。
    這種「先建表、再查表」的寫法比逐字元手算 ord/chr 更不容易出錯，
    也比較好記：只要記得「位移後的字母表」要怎麼拼出來就好。
"""
import sys
import string

SHIFT = 6


def _build_shift_table(shift: int) -> dict:
    """
    建立位移對照表（給 str.translate 用）。

    做法：
    1. string.ascii_uppercase 是 "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       把它往左切掉 shift 個字母，再接到後面，就變成「位移後的字母順序」。
       例如 shift=6 時：原本 "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
       切成 "ABCDEF" + "GHIJKLMNOPQRSTUVWXYZ"，
       重組成 "GHIJKLMNOPQRSTUVWXYZABCDEF"。
       也就是說「原本排第 0 位的 A，對照到新表第 0 位的 G」，
       剛好就是 A 位移 6 之後變成 G，邏輯一致。
    2. 小寫字母用同樣方法處理 string.ascii_lowercase。
    3. str.maketrans(原字串, 新字串) 會回傳一個對照表，
       之後 line.translate(表) 就會把 line 裡每個出現在「原字串」中的字元，
       換成「新字串」中對應位置的字元；不在表中的字元（標點、數字、空白）
       完全不受影響，自動原樣保留，不用額外寫 if 判斷。
    """
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase

    shifted_upper = upper[shift:] + upper[:shift]
    shifted_lower = lower[shift:] + lower[:shift]

    return str.maketrans(upper + lower, shifted_upper + shifted_lower)


# 程式一啟動就把對照表建好，之後每一行都重複使用同一張表，不用重算
_SHIFT_TABLE = _build_shift_table(SHIFT)


def encrypt_line(line: str) -> str:
    """
    用事先建好的對照表，把整行字串一次轉換完成。
    非英文字母字元（空白、數字、標點）因為不在對照表裡，
    translate() 會自動保留原樣，不需要額外處理。
    """
    return line.translate(_SHIFT_TABLE)


def main() -> None:
    """
    讀取輸入直到 EOF（檔案結尾）為止：
    for line in sys.stdin 會一直讀下一行，
    直到真的沒有輸入了（EOF）才自然結束迴圈，
    跟「讀到某個特定數值就停止」的寫法不同，這裡完全不需要判斷終止條件。
    """
    for line in sys.stdin:
        # line 結尾會帶有換行符 '\n'，要先去掉，避免印出時多一行空白
        print(encrypt_line(line.rstrip('\n')))


if __name__ == '__main__':
    main()
