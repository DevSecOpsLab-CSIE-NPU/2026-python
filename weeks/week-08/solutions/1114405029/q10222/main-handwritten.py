import sys


def build_mapping():
    rows = [
        "`1234567890-=",
        "qwertyuiop[]\\",
        "asdfghjkl;'",
        "zxcvbnm,./"
    ]

    mapping = {}

    for row in rows:
        for i in range(1, len(row)):
            mapping[row[i]] = row[i - 1]

    return mapping


def decode_text(text, mapping):
    text = text.lower()

    result = []

    for ch in text:
        if ch == " ":
            result.append(" ")
        else:
            result.append(mapping.get(ch, ch))

    return "".join(result)


def main():
    mapping = build_mapping()
    lines = sys.stdin.read().splitlines()

    outputs = []

    for line in lines:
        outputs.append(decode_text(line, mapping))

    print("\n".join(outputs))


if __name__ == "__main__":
    main()