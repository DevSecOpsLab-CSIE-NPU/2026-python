import sys


def encrypt_caesar(text: str, shift: int = 1) -> str:
    """凱撒密碼位移加密：
    1. 僅英文字母進行位移，其餘字元保留不變
    2. 大寫英文字母 (A-Z) 在其範圍內循環
    3. 小寫英文字母 (a-z) 在其範圍內循環
    """
    result = []
    for char in text:
        if "A" <= char <= "Z":
            # 轉換至 0-25 範圍進行位移，再轉回 ASCII
            new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            result.append(new_char)
        elif "a" <= char <= "z":
            # 轉換至 0-25 範圍進行位移，再轉回 ASCII
            new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            result.append(new_char)
        else:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    # 處理多行輸入至 EOF
    for line in sys.stdin:
        # 去除結尾換行符號、加密、並重組輸出
        sys.stdout.write(encrypt_caesar(line.rstrip("\r\n"), 1) + "\n")
