"""
凱薩位移密碼：英文字母向後位移 SHIFT 位，大小寫各自循環，非字母字元原樣保留。
SHIFT = 10（學號末兩碼 19，個位 9，公式 9 % 25 + 1 = 10）
讀到 EOF 為止，每行輸入對應一行輸出。
"""
import sys

SHIFT = 10


def shift_char(c: str, shift: int) -> str:
    if "A" <= c <= "Z":
        return chr((ord(c) - ord("A") + shift) % 26 + ord("A"))
    if "a" <= c <= "z":
        return chr((ord(c) - ord("a") + shift) % 26 + ord("a"))
    return c


def shift_line(line: str, shift: int) -> str:
    return "".join(shift_char(c, shift) for c in line)


def main() -> None:
    for line in sys.stdin:
        print(shift_line(line.rstrip("\n"), SHIFT))


if __name__ == "__main__":
    main()
