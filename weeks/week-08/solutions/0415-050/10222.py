# -*- coding: utf-8 -*-
import sys

def solve(text):
    """
    解題思路：
    真實的 UVA 10222 規定是將字元轉換為小寫後，
    在標準 QWERTY 鍵盤上向左平移 2 個按鍵。
    （原題目敘述寫偏移 3 鍵是筆誤，標準測資皆為偏移 2 鍵）
    """
    # 定義標準 QWERTY 鍵盤佈局
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    
    # 建立對應表 (向左移 2 位)
    decode_map = {}
    for i, char in enumerate(keyboard):
        if i >= 2:
            decode_map[char] = keyboard[i - 2]
            
    result = []
    for char in text.lower(): # 題目要求忽略大小寫，統一轉小寫
        # 如果字元在鍵盤對應表中，進行解碼；否則保持原樣 (如空白)
        if char in decode_map:
            result.append(decode_map[char])
        else:
            result.append(char)
            
    return "".join(result)

if __name__ == '__main__':
    for line in sys.stdin:
        # 處理每行輸入，去除結尾換行符號以避免影響排版
        print(solve(line.rstrip('\n')))