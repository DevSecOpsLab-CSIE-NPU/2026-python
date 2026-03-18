"""題目 948 附件描述版本：找出唯一可能的假幣編號。"""

import sys


def is_state_valid(
    coin: int,
    is_heavier: bool,
    weighings: list[tuple[list[int], list[int], str]],
) -> bool:
    """檢查某一枚硬幣在某個重量狀態下是否符合所有秤重結果。"""
    for left, right, result in weighings:
        on_left = coin in left
        on_right = coin in right

        # 如果假幣根本不在這次秤重中，天平理論上只能平衡。
        if not on_left and not on_right:
            if result != "=":
                return False
            continue

        if result == "=":
            return False

        # 在左盤或右盤時，重幣與輕幣對應的結果相反。
        if on_left:
            expected = ">" if is_heavier else "<"
        else:
            expected = "<" if is_heavier else ">"

        if result != expected:
            return False

    return True


def find_fake_coin(n: int, weighings: list[tuple[list[int], list[int], str]]) -> int:
    """若只有一枚硬幣可能為假幣，回傳其編號；否則回傳 0。"""
    possible_coins: set[int] = set()

    for coin in range(1, n + 1):
        # 同一枚硬幣只要有一種重量狀態成立，就先列入候選。
        if is_state_valid(coin, True, weighings) or is_state_valid(coin, False, weighings):
            possible_coins.add(coin)

    if len(possible_coins) == 1:
        return possible_coins.pop()
    return 0


def solve(text: str) -> str:
    tokens = text.split()
    if not tokens:
        return ""

    index = 0
    test_cases = int(tokens[index])
    index += 1
    outputs: list[str] = []

    for case_index in range(test_cases):
        n = int(tokens[index])
        k = int(tokens[index + 1])
        index += 2

        # 先把一組測試資料完整解析，再統一判斷答案。
        weighings: list[tuple[list[int], list[int], str]] = []
        for _ in range(k):
            p = int(tokens[index])
            index += 1
            left = list(map(int, tokens[index : index + p]))
            index += p
            right = list(map(int, tokens[index : index + p]))
            index += p
            result = tokens[index]
            index += 1
            weighings.append((left, right, result))

        outputs.append(str(find_fake_coin(n, weighings)))
        if case_index != test_cases - 1:
            outputs.append("")

    return "\n".join(outputs)


if __name__ == "__main__":
    print(solve(sys.stdin.read()))