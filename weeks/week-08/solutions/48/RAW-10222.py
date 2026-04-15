import sys


def main():
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./",
    ]

    decode = {}
    for row in rows:
        for index in range(1, len(row)):
            decode[row[index]] = row[index - 1]

    text = sys.stdin.read()
    result = []

    for ch in text:
        result.append(decode.get(ch, ch))

    sys.stdout.write(''.join(result))


if __name__ == '__main__':
    main()
