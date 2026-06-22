def encrypt_caesar(text: str, shift: int) -> str:
    if not isinstance(shift, int):
        raise TypeError("shift must be an integer")
    
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            # 大寫字母位移
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        elif 'a' <= char <= 'z':
            # 小寫字母位移
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        else:
            # 非字母字元保持不變
            result.append(char)
            
    return "".join(result)
