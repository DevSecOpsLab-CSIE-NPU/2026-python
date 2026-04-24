# -*- coding: utf-8 -*-
# 這是 UVA 10222 (Decode the Mad man) 的簡易好記版 (Easy Version)
import sys

def solve(text):
    """
    簡易好記秘訣：【字串尋找法 str.find()】
    不需要建字典！直接把鍵盤按鍵照順序寫成一個長字串。
    遍歷輸入的每個字元 (轉小寫)：
    1. 用 find() 找出它在鍵盤字串裡的位置 (index)。
    2. 如果找到了 (index >= 2)，就往左退 2 格取字元。
    3. 如果沒找到 (像是空白字元，find 回傳 -1)，就照原樣輸出。
    """
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    result = ""
    
    for char in text.lower():
        idx = keyboard.find(char)
        # find() 如果找不到會回傳 -1，只要 idx >= 2 就是合法的鍵盤字元
        if idx >= 2:
            result += keyboard[idx - 2]
        else:
            result += char
            
    return result

if __name__ == '__main__':
    for line in sys.stdin:
        print(solve(line.rstrip('\n')))