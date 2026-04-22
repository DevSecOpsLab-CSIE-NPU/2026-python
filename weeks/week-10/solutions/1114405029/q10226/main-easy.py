import sys


def parse_cases(lines):
    # 第一行是測資數量
    t = int(lines[0].strip())

    # index 用來記錄目前讀到哪一行
    index = 1

    # 題目格式中，測資數量後面通常會有一個空白行
    # 如果有，就先跳過
    if index < len(lines) and lines[index] == "":
        index += 1

    cases = []

    # 一共要讀 t 筆測資
    for _ in range(t):
        trees = []

        # 同一筆測資會一直讀到空白行為止
        while index < len(lines) and lines[index] != "":
            trees.append(lines[index])
            index += 1

        cases.append(trees)

        # 讀完一筆後，如果下一行是空白行，就跳過
        if index < len(lines) and lines[index] == "":
            index += 1

    return cases


def solve_case(trees):
    # 用字典統計每個樹種出現幾次
    counter = {}

    # total 記錄這筆測資總共有幾棵樹
    total = 0

    for name in trees:
        counter[name] = counter.get(name, 0) + 1
        total += 1

    result = []

    # 題目要求依照樹名字典順序輸出
    for name in sorted(counter):
        percentage = counter[name] * 100.0 / total
        result.append(f"{name} {percentage:.4f}")

    return result


def main():
    # 一次把所有輸入行讀進來
    lines = sys.stdin.read().splitlines()

    if not lines:
        return

    # 先把所有測資切出來
    cases = parse_cases(lines)

    outputs = []

    for i, trees in enumerate(cases):
        # 不同測資之間要空一行
        if i > 0:
            outputs.append("")

        outputs.extend(solve_case(trees))

    print("\n".join(outputs))


if __name__ == "__main__":
    main()