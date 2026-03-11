import sys

def convert(input_text):
    QUOTES = ['``', "''"]
    text = input_text
    i = 0
    while '"' in text:
        text = text.replace('"', QUOTES[i % 2], 1)
        i += 1
    return text

if __name__ == "__main__":
    print(convert(sys.stdin.read()), end='')