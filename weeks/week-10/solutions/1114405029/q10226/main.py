import sys


def parse_cases(lines):
    # 第一行是測資數量
    t = int(lines[0].strip())
    index = 1

    # 跳過第一個空白行（如果有）
    if index < len(lines) and lines[index] == "":
        index += 1

    cases = []

    for _ in range(t):
        trees = []

        # 讀到空白行或 EOF 為止，這些行都屬於同一筆測資
        while index < len(lines) and lines[index] != "":
            trees.append(lines[index])
            index += 1

        cases.append(trees)

        # 跳過測資之間的空白行
        if index < len(lines) and lines[index] == "":
            index += 1

    return cases


def solve_case(trees):
    counter = {}
    total = 0

    # 統計每個樹種出現次數
    for name in trees:
        counter[name] = counter.get(name, 0) + 1
        total += 1

    output_lines = []

    # 題目要求依字典順序輸出
    for name in sorted(counter):
        percentage = counter[name] * 100.0 / total
        output_lines.append(f"{name} {percentage:.4f}")

    return output_lines


def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return

    cases = parse_cases(lines)
    all_outputs = []

    for i, trees in enumerate(cases):
        if i > 0:
            all_outputs.append("")

        all_outputs.extend(solve_case(trees))

    print("\n".join(all_outputs))


if __name__ == "__main__":
    main()