import sys


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    n = int(lines[0])

    # 26 個英文字母計數器
    freq = [0] * 26

    for i in range(1, min(n + 1, len(lines))):
        text = lines[i].upper()
        for ch in text:
            if "A" <= ch <= "Z":
                freq[ord(ch) - ord("A")] += 1

    result = []
    for i in range(26):
        if freq[i] > 0:
            result.append((chr(ord("A") + i), freq[i]))

    # 次數大到小；次數相同按字母小到大
    result.sort(key=lambda item: (-item[1], item[0]))

    for c, count in result:
        print(c, count)


if __name__ == "__main__":
    main()
