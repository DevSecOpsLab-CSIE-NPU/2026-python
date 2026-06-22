"""
題目：凱撒密碼 (Caesar Cipher) - 25分

問題描述：
「兩章一保護原文」：用古西凱撒替換每個字元的 SHIFT 位

輸入說明：
- 輸入包含多行，每行一個字串 (可能含行、長度≤1000)
- 請獲得結束 (EOF) 為止

輸出說明：
- 對每一行輸入，輸出加密後的字串 (一行一行)

加密規則 (SHIFT=2，根據學號1114405041)：
- 大寫字母: A-Z 循環移位 2 位 (A→C, Y→A, Z→B)
- 小寫字母: a-z 循環移位 2 位 (a→c, y→a, z→b)
- 其他字元保持不變

範例 (SHIFT = 2)：
Sample Input:
Hello, NPU!
abc XYZ

Sample Output:
Jgnnq, PRW!
cde ZAB
"""


def caesar_cipher(text, shift=2):
    """
    凱撒密碼加密
    
    Args:
        text: 要加密的文字
        shift: 位移量 (預設=2，根據學號1114405041)
    
    Returns:
        str: 加密後的文字
    """
    result = []
    
    for char in text:
        if 'A' <= char <= 'Z':
            # 大寫字母
            shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted)
        elif 'a' <= char <= 'z':
            # 小寫字母
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted)
        else:
            # 其他字元保持不變
            result.append(char)
    
    return ''.join(result)


def main():
    """
    凱撒密碼主程式
    
    讀取多行輸入，對每行進行加密並輸出
    """
    try:
        while True:
            line = input()
            encrypted = caesar_cipher(line)
            print(encrypted)
    except EOFError:
        pass


if __name__ == '__main__':
    main()
