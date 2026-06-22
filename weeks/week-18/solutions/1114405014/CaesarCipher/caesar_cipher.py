import sys


# 依照你的學號末碼設定
# 你的學號看起來是 1114405014，末碼 u = 4
# SHIFT = u % 25 + 1 = 5
STUDENT_LAST_DIGIT = 4
SHIFT = STUDENT_LAST_DIGIT % 25 + 1


def caesar_cipher(text: str, shift: int) -> str:
    """
    對一段文字做凱撒密碼加密。

    規則：
    1. 大寫 A-Z 在 A-Z 範圍內循環。
    2. 小寫 a-z 在 a-z 範圍內循環。
    3. 非英文字母原樣保留。
    """
    result = []

    for char in text:
        if "A" <= char <= "Z":
            shifted = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            result.append(shifted)

        elif "a" <= char <= "z":
            shifted = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            result.append(shifted)

        else:
            result.append(char)

    return "".join(result)


def process_text(input_text: str, shift: int) -> str:
    """
    處理多行輸入，保留原本的換行與空行。
    """
    output_lines = []

    for line in input_text.splitlines(keepends=True):
        output_lines.append(caesar_cipher(line, shift))

    return "".join(output_lines)


def main() -> None:
    """
    從標準輸入讀到 EOF，逐行輸出加密後結果。
    """
    input_text = sys.stdin.read()
    output_text = process_text(input_text, SHIFT)
    print(output_text, end="")


if __name__ == "__main__":
    main()