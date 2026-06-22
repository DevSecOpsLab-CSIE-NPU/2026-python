import sys

def caesar_cipher_encrypt(text: str, shift: int) -> str:
    """
    AI 簡單版 - 凱撒密碼加密：
    1. 將位移量同餘化至 0-25 之間。
    2. 逐一處理字元，大寫在 A-Z 循環，小寫在 a-z 循環，其餘字元保留。
    """
    result = []
    # 確保位移量在 0-25 之間
    shift = shift % 26
    
    for char in text:
        if 'a' <= char <= 'z':
            # 小寫字母：將字元轉換為 0-25 的索引，位移後再轉回 ASCII
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            # 大寫字母：將字元轉換為 0-25 的索引，位移後再轉回 ASCII
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            # 非英文字元原樣保留
            result.append(char)
            
    return "".join(result)

def main():
    while True:
        # 讀取整行，讀到 EOF 時會回傳空字串
        line = sys.stdin.readline()
        if not line:
            break
            
        # 移除行尾的換行符（如 \n 或 \r\n）以防影響列印
        stripped_line = line.rstrip('\r\n')
        
        # 依學號計算出的位移量 SHIFT = 6 進行加密
        encrypted_line = caesar_cipher_encrypt(stripped_line, 6)
        
        # 印出加密後的單行
        print(encrypted_line)

if __name__ == '__main__':
    main()
