import sys
from collections import Counter


def parse_cases(data):
    """
    將整份輸入資料切成多筆測資。

    UVA 10226 的輸入格式：
    1. 第一行是測資數量 t
    2. 第一行後面通常會有一個空白行
    3. 每筆測資之間也會用空白行隔開
    4. 每筆測資內，每一行代表一棵樹的樹種名稱

    回傳：
    - list[list[str]]
    """
    lines = data.splitlines()

    if not lines:
        return []

    case_count = int(lines[0].strip())

    cases = []
    current_case = []

    for line in lines[1:]:
        # 空白行 → 一筆測資結束
        if line == "":
            if current_case:
                cases.append(current_case)
                current_case = []

                # 已達測資數量就停止
                if len(cases) == case_count:
                    break
        else:
            current_case.append(line)

    # 最後一筆沒有空白行的情況
    if current_case and len(cases) < case_count:
        cases.append(current_case)

    return cases


def solve_case(trees):
    """
    計算單筆測資的結果
    """
    total = len(trees)

    # 防止除以 0
    if total == 0:
        return []

    counter = Counter(trees)

    result = []

    # 依字典順序排序
    for name in sorted(counter):
        percentage = counter[name] * 100 / total
        result.append(f"{name} {percentage:.4f}")

    return result


def main():
    data = sys.stdin.read()
    cases = parse_cases(data)

    output = []

    for i, trees in enumerate(cases):
        if i > 0:
            output.append("")  # 測資間空行

        output.extend(solve_case(trees))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()