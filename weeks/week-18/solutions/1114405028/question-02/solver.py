def caesar_cipher(text: str, shift: int = 3) -> str:
    result = []
    for ch in text:
        if 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        elif 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(ch)
    return ''.join(result)


if __name__ == '__main__':
    import sys
    data = sys.stdin.read().rstrip('\n')
    if not data:
        sys.exit(0)

    lines = data.splitlines()
    text = lines[0] if lines else ''
    shift = 3
    if len(lines) >= 2:
        try:
            shift = int(lines[1].strip())
        except ValueError:
            shift = 3

    print(caesar_cipher(text, shift))
