def solve(data):
    lines = data.splitlines()
    if not lines:
        return ""

    total_lines = int(lines[0].strip())
    counts = {}

    # 逐行掃描，忽略非英文字母，大小寫一律轉成大寫後統計。
    for line in lines[1 : 1 + total_lines]:
        for char in line.upper():
            if "A" <= char <= "Z":
                counts[char] = counts.get(char, 0) + 1

    # 先按字母排序，再按次數由大到小排序，就能符合題目規則。
    ordered = sorted(counts.items())
    ordered.sort(key=lambda item: item[1], reverse=True)

    answers = []
    for letter, count in ordered:
        answers.append(f"{letter} {count}")
    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    print(solve(sys.stdin.read()), end="")