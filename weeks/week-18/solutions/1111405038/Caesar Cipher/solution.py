"""
解題檔：凱撒密碼（Caesar Cipher）- 第二題

核心任務：
1. 讀取文本 - 逐行讀入直到 EOF
2. 進行加密 - 使用 SHIFT=9 位移對字母進行加密
3. 保留非字母 - 空白、數字、標點符號保持不變
"""


def caesar_encrypt(text, shift=9):
    """
    凱撒密碼加密函數
    
    Args:
        text: 輸入文字
        shift: 位移數（預設為9）
    
    Returns:
        加密後的文字
    """
    result = []
    
    for char in text:
        if 'A' <= char <= 'Z':
            # 大寫字母：位移並使用模運算實現繞回
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        elif 'a' <= char <= 'z':
            # 小寫字母：位移並使用模運算實現繞回
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        else:
            # 非字母字符：直接保留
            result.append(char)
    
    return ''.join(result)


def main():
    """主程序 - 讀取輸入直到 EOF 並輸出加密結果"""
    try:
        while True:
            try:
                line = input()
                encrypted = caesar_encrypt(line, 9)
                print(encrypted)
            except EOFError:
                # 遇到 EOF 時終止
                break
    except KeyboardInterrupt:
        # 遇到中斷時正常終止
        pass


if __name__ == '__main__':
    main()
