SHIFT = 3

def enc(c, base):
    return chr((ord(c) - ord(base) + SHIFT) % 26 + ord(base))

def caesar_encrypt(text):
    out = ""
    for ch in text:
        if 'a' <= ch <= 'z':
            out += enc(ch, 'a')
        elif 'A' <= ch <= 'Z':
            out += enc(ch, 'A')
        else:
            out += ch
    return out

def main():
    import sys
    s = sys.stdin.readline()
    if s:
        print(caesar_encrypt(s.rstrip('\n')))

if __name__ == "__main__":
    main()
