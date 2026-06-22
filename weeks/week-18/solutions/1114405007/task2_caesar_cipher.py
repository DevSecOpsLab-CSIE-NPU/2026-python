def encrypt_line(text, shift):
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(ch)
    return "".join(result)


def solve(input_text, shift):
    lines = input_text.splitlines()
    out = []
    for line in lines:
        out.append(encrypt_line(line, shift))
    return "\n".join(out) + ("\n" if out else "")


def get_shift(student_id):
    u = student_id % 10
    return (u % 4) + 2


def main():
    import sys
    STUDENT_ID = 1114405007
    SHIFT = 8
    input_text = sys.stdin.read()
    output = solve(input_text, SHIFT)
    sys.stdout.write(output)


if __name__ == "__main__":
    main()
