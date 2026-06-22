import sys

def caesar_cipher(text, shift):
    """
    凱撒密碼加密核心：
    - 大寫 A-Z 內循環
    - 小寫 a-z 內循環
    - 非英文字母原樣保留
    """
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            # 大寫字母循環位移
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        elif 'a' <= char <= 'z':
            # 小寫字母循環位移
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        else:
            # 非字母字元原樣保留
            result.append(char)
    return "".join(result)

def main():
    """
    多行輸入讀取至 EOF 為止
    """
    # 讀取標準輸入的所有內容
    input_text = sys.stdin.read()
    if not input_text:
        return
        
    lines = input_text.splitlines()
    
    for line in lines:
        # 使用學號對應的專屬位移量 SHIFT = 2
        encrypted_line = caesar_cipher(line, shift=2)
        print(encrypted_line)

if __name__ == "__main__":
    main()