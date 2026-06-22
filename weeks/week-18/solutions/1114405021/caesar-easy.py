import sys

SHIFT = 2


def solve(text: str) -> str:
    result = []
    for ch in text:
        if "A" <= ch <= "Z":
            # 大寫字母循環
            result.append(chr((ord(ch) - ord("A") + SHIFT) % 26 + ord("A")))
        elif "a" <= ch <= "z":
            # 小寫字母循環
            result.append(chr((ord(ch) - ord("a") + SHIFT) % 26 + ord("a")))
        else:
            # 非字母不變
            result.append(ch)
    return "".join(result)


def main():
    lines = sys.stdin.read().splitlines()
    out = [solve(line) for line in lines]
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
