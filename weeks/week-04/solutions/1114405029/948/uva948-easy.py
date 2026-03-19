"""
UVA 948 簡化版

這個版本保留相同邏輯，
但把流程寫得更直白，方便閱讀與學習。
"""


def is_valid_assumption(coin: int, state: str, weighings: list[tuple[list[int], list[int], str]]) -> bool:
    """
    檢查某顆硬幣是否能在指定狀態下符合所有秤重。

    參數：
    coin      : 假設中的假幣編號
    state     : "heavy" 表示偏重，"light" 表示偏輕
    weighings : 所有秤重紀錄

    回傳：
    True  -> 這個假設成立
    False -> 這個假設不成立
    """
    for left, right, result in weighings:
        if coin in left:
            # 假幣在左盤
            if state == "heavy":
                expected = ">"
            else:
                expected = "<"

        elif coin in right:
            # 假幣在右盤
            if state == "heavy":
                expected = "<"
            else:
                expected = ">"

        else:
            # 假幣不在秤上，應平衡
            expected = "="

        if expected != result:
            return False

    return True


def solve_case(n: int, weighings: list[tuple[list[int], list[int], str]]) -> int:
    """
    解單一測資，回傳唯一假幣編號；
    若無法唯一判定，回傳 0。
    """
    candidates = []

    for coin in range(1, n + 1):
        # 檢查 coin 是否可能偏重或偏輕
        can_be_heavy = is_valid_assumption(coin, "heavy", weighings)
        can_be_light = is_valid_assumption(coin, "light", weighings)

        if can_be_heavy or can_be_light:
            candidates.append(coin)

    if len(candidates) == 1:
        return candidates[0]
    return 0


def solve(data: str) -> str:
    """
    解析整份輸入，並依題目格式輸出答案。
    """
    lines = data.splitlines()
    i = 0

    # 略過最前方空白行
    while i < len(lines) and lines[i].strip() == "":
        i += 1

    t = int(lines[i].strip())
    i += 1

    result_list = []

    for _ in range(t):
        # 略過各組測資前面的空白行
        while i < len(lines) and lines[i].strip() == "":
            i += 1

        n, k = map(int, lines[i].split())
        i += 1

        weighings = []

        for _ in range(k):
            parts = lines[i].split()
            i += 1

            p = int(parts[0])
            left = list(map(int, parts[1:1 + p]))
            right = list(map(int, parts[1 + p:1 + 2 * p]))

            # 略過可能的空白行，再讀結果
            while i < len(lines) and lines[i].strip() == "":
                i += 1

            mark = lines[i].strip()
            i += 1

            weighings.append((left, right, mark))

        answer = solve_case(n, weighings)
        result_list.append(str(answer))

    # 各組答案中間需空一行
    return "\n\n".join(result_list)


if __name__ == "__main__":
    import sys
    print(solve(sys.stdin.read()))