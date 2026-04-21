"""UVA 948 金條銀行假幣判定。

這份標準版使用「枚舉硬幣編號 + 枚舉假幣是偏重或偏輕」的方式，
逐一檢查每一次秤重是否都能被同一顆假幣解釋。
"""

import sys


def next_nonempty(lines, index):
    """跳過空白列，回傳下一個有效位置。"""
    while index < len(lines) and not lines[index].strip():
        index += 1
    return index


def candidate_valid(weighings, coin_id, is_heavier):
    """檢查某顆硬幣若是偏重/偏輕，是否可解釋全部秤重結果。"""
    for left, right, result in weighings:
        if coin_id in left:
            predicted = ">" if is_heavier else "<"
        elif coin_id in right:
            predicted = "<" if is_heavier else ">"
        else:
            predicted = "="

        if predicted != result:
            return False
    return True


def solve():
    lines = sys.stdin.buffer.read().splitlines()
    index = 0
    index = next_nonempty(lines, index)
    if index >= len(lines):
        return

    case_count = int(lines[index].decode())
    index += 1
    answers = []

    for case_index in range(case_count):
        index = next_nonempty(lines, index)
        n, k = map(int, lines[index].split())
        index += 1

        weighings = []
        for _ in range(k):
            parts = list(map(int, lines[index].split()))
            index += 1
            p = parts[0]
            left = set(parts[1 : 1 + p])
            right = set(parts[1 + p : 1 + 2 * p])
            result = lines[index].decode().strip()
            index += 1
            weighings.append((left, right, result))

        possible = set()
        for coin_id in range(1, n + 1):
            if candidate_valid(weighings, coin_id, True) or candidate_valid(weighings, coin_id, False):
                possible.add(coin_id)

        answers.append(str(next(iter(possible)) if len(possible) == 1 else 0))

    sys.stdout.write("\n\n".join(answers))


if __name__ == "__main__":
    solve()