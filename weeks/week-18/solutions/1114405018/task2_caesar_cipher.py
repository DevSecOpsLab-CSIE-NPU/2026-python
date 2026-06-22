def caesar_encrypt(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(ch)
    return ''.join(result)


def solve_caesar(data: str, shift: int) -> str:
    lines = data.splitlines()
    out_lines = [caesar_encrypt(line, shift) for line in lines]
    return '\n'.join(out_lines)


def main():
    import sys
    data = sys.stdin.read()
    sys.stdout.write(solve_caesar(data, 9))


if __name__ == '__main__':
    main()
