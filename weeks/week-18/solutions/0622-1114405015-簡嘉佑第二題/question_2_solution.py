"""
第二題：凱撒密碼 (Caesar Cipher) - 25分

題目說明：
- 輸入：多行字串，每行包含待加密的文字（可能含空白、標點、數字）
- 處理邏輯：
  1. 對每個大寫字母，向後移動 SHIFT 位（Z 之後回到 A）
  2. 對每個小寫字母，向後移動 SHIFT 位（z 之後回到 a）
  3. 空白、標點、數字、非英文字母保持不變
- 輸出：加密後的字串

座號：15
SHIFT 值：15 % 26 = 15
"""

def caesar_cipher(text, shift):
    """
    凱撒密碼加密函式
    
    Args:
        text: 待加密的字串
        shift: 移動位數（0-25）
    
    Returns:
        加密後的字串
    """
    result = []
    
    for char in text:
        if 'A' <= char <= 'Z':
            # 大寫字母：移位並循環
            shifted = (ord(char) - ord('A') + shift) % 26
            result.append(chr(ord('A') + shifted))
        elif 'a' <= char <= 'z':
            # 小寫字母：移位並循環
            shifted = (ord(char) - ord('a') + shift) % 26
            result.append(chr(ord('a') + shifted))
        else:
            # 其他字符保持不變
            result.append(char)
    
    return ''.join(result)


def main():
    """主程式"""
    shift = 15  # 座號15的SHIFT值
    
    # 讀取多行輸入
    try:
        while True:
            line = input()
            encrypted = caesar_cipher(line, shift)
            print(encrypted)
    except EOFError:
        # 處理文件末尾
        pass


if __name__ == "__main__":
    main()
