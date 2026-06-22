import sys

STUDENT_ID = "1114405017"


def get_shift(student_id: str) -> int:
    """根據學號末位計算凱撒位移 SHIFT。"""
    u = int(student_id[-1])
    return u % 25 + 1


def caesar_shift(text: str, shift: int) -> str:
    """對輸入文字進行凱撒加密，僅變更英文字母，其他字元原樣輸出。"""
    result = []
    for ch in text:
        if "A" <= ch <= "Z":
            result.append(chr((ord(ch) - ord("A") + shift) % 26 + ord("A")))
        elif "a" <= ch <= "z":
            result.append(chr((ord(ch) - ord("a") + shift) % 26 + ord("a")))
        else:
            result.append(ch)
    return "".join(result)


def main() -> None:
    shift = get_shift(STUDENT_ID)
    for line in sys.stdin:
        print(caesar_shift(line.rstrip("\n"), shift))


if __name__ == "__main__":
    main()
