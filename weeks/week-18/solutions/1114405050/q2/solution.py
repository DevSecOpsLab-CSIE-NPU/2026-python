def caesar_cipher(text, shift=2):
    """
    實作凱撒密碼邏輯
    大寫：A-Z 內循環
    小寫：a-z 內循環
    其餘：保留
    """
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            # 小寫字母位移
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        elif 'A' <= char <= 'Z':
            # 大寫字母位移
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            # 非字母字元保留
            result.append(char)
    return "".join(result)
