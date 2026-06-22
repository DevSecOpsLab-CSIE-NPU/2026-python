import sys

def caesar_cipher(text, shift=2):
    """
    凱撒密碼核心轉換邏輯
    - 大寫字母 A-Z 循環
    - 小寫字母 a-z 循環
    - 標點符號、空白與數字等非英文字母維持原樣
    """
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            # 大寫字母循環：A 的 ascii 是 65
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
            result.append(new_char)
        elif 'a' <= char <= 'z':
            # 小寫字母循環：a 的 ascii 是 97
            new_char = chr((ord(char) - 97 + shift) % 26 + 97)
            result.append(new_char)
        else:
            # 非字母直接原樣保留
            result.append(char)
    return "".join(result)

def main():
    """
    標準輸入處理，支援多行輸入直到 EOF 結束
    """
    # 一次性讀取標準輸入的所有文字
    input_text = sys.stdin.read()
    if not input_text:
        return
        
    # 依行拆分處理
    lines = input_text.splitlines()
    
    for line in lines:
        # 帶入你專屬的考卷參數 SHIFT = 2
        output_line = caesar_cipher(line, shift=2)
        print(output_line)

if __name__ == "__main__":
    main()