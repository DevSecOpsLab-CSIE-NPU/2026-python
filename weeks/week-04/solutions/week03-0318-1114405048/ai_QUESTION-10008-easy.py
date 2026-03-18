import sys


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    n = int(lines[0])

    # cnt[0] 對應 A，cnt[25] 對應 Z
    cnt = [0] * 26

    for i in range(1, n + 1):
        if i >= len(lines):
            break
        for ch in lines[i].upper():
            if 'A' <= ch <= 'Z':
                cnt[ord(ch) - ord('A')] += 1

    data = []
    for i in range(26):
        if cnt[i] > 0:
            data.append((chr(i + ord('A')), cnt[i]))

    # 先比次數(降序)，再比字母(升序)
    data.sort(key=lambda x: (-x[1], x[0]))

    for c, k in data:
        print(c, k)


if __name__ == "__main__":
    main()