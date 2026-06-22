import sys


def encrypt_line(line: str, shift: int) -> str:
    """
    對字串中的英文字母進行 Caesar Cipher 加密。
    
    參數：
        line (str): 待加密的字串
        shift (int): 位移量（0-25）
    
    回傳：
        str: 加密後的字串
    """
    result = []
    
    for char in line:
        if 'A' <= char <= 'Z':
            # 大寫字母：在 A-Z 內循環
            # 計算字母在 A-Z 中的位置（0-25）
            pos = ord(char) - ord('A')
            # 位移後的位置（模 26 保持循環）
            new_pos = (pos + shift) % 26
            # 轉回字元
            new_char = chr(ord('A') + new_pos)
            result.append(new_char)
        elif 'a' <= char <= 'z':
            # 小寫字母：在 a-z 內循環
            pos = ord(char) - ord('a')
            new_pos = (pos + shift) % 26
            new_char = chr(ord('a') + new_pos)
            result.append(new_char)
        else:
            # 非英文字母（空白、數字、標點）原樣保留
            result.append(char)
    
    return ''.join(result)


def solve():
    """
    主程式：讀標準輸入直到 EOF，逐行加密並輸出。
    """
    SHIFT = 6  # 根據學號 1114405006 個位數 = 6
    
    try:
        for line in sys.stdin:
            # 移除行尾的換行符
            line = line.rstrip('\n')
            # 加密該行
            encrypted = encrypt_line(line, SHIFT)
            # 輸出加密後的字串
            print(encrypted)
    except EOFError:
        pass


if __name__ == "__main__":
    solve()
