"""
UVA 11150 - easy 版

這題的關鍵是：
1. 每次可以跳 S 到 T 格，所以「下一個落點」只會依賴前面 T 格內的狀態。
2. 石子很少，但橋很長，所以不能一格一格慢慢算到 L。
3. 於是把「沒有石子的長區間」用 min-plus 矩陣快速冪一次跳過。

state 的意義：
    state[i] 代表目前位置往前看第 i 格的最小踩石數。
最右邊那格代表目前所在的位置。
每往前走一格，就把 state 整體往左平移，最後再算新位置的最小值。
"""

import sys


INF = 10 ** 18


def mat_mul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    """min-plus 矩陣乘法。"""
    size = len(left)
    result = [[INF] * size for _ in range(size)]
    for i in range(size):
        left_row = left[i]
        result_row = result[i]
        for k, left_value in enumerate(left_row):
            if left_value >= INF:
                continue
            right_row = right[k]
            for j, right_value in enumerate(right_row):
                candidate = left_value + right_value
                if candidate < result_row[j]:
                    result_row[j] = candidate
    return result


def mat_vec_mul(matrix: list[list[int]], vector: list[int]) -> list[int]:
    """把矩陣套到 state 上。"""
    size = len(matrix)
    result = [INF] * size
    for i in range(size):
        best = INF
        row = matrix[i]
        for j, value in enumerate(row):
            candidate = value + vector[j]
            if candidate < best:
                best = candidate
        result[i] = best
    return result


def mat_pow(matrix: list[list[int]], power: int) -> list[list[int]]:
    """快速冪，讓長空白區間可以直接跳過。"""
    size = len(matrix)
    result = [[INF] * size for _ in range(size)]
    for i in range(size):
        result[i][i] = 0

    base = matrix
    while power > 0:
        if power & 1:
            result = mat_mul(result, base)
        base = mat_mul(base, base)
        power >>= 1
    return result


def build_transition(size: int, minimum_jump: int, maximum_jump: int, landing_cost: int) -> list[list[int]]:
    """建立「往前一格」的狀態轉移矩陣。"""
    matrix = [[INF] * size for _ in range(size)]

    # 平移 state：前一格會變成下一格的前一格。
    for i in range(size - 1):
        matrix[i][i + 1] = 0

    # 新位置的最小值只會看前面 S~T 格。
    for j in range(0, size - minimum_jump + 1):
        if 0 <= j < size:
            matrix[size - 1][j] = landing_cost
    return matrix


def advance(state: list[int], transition: list[list[int]], steps: int) -> list[int]:
    """把 state 往前推進 steps 格。"""
    if steps <= 0:
        return state
    powered = mat_pow(transition, steps)
    return mat_vec_mul(powered, state)


def solve_case(length: int, minimum_jump: int, maximum_jump: int, stones: list[int]) -> int:
    """計算答案。"""
    size = maximum_jump
    zero_transition = build_transition(size, minimum_jump, maximum_jump, 0)
    stone_transition = build_transition(size, minimum_jump, maximum_jump, 1)

    # 初始時只站在 0 號位置，其他位置都還不可達。
    state = [INF] * size
    state[-1] = 0
    current_position = 0

    # 只需要處理橋上的石子，最後再多推進到 L + T - 1。
    targets = [stone for stone in stones if stone < length]
    targets.sort()
    targets.append(length + maximum_jump - 1)

    for target in targets:
        # 先把中間沒有石子的區段跳過。
        gap = target - current_position - 1
        state = advance(state, zero_transition, gap)
        current_position += gap

        if target < length:
            # 落在石子上，成本 +1。
            state = mat_vec_mul(stone_transition, state)
            current_position = target
        else:
            # 終點後面不會再有石子，只要推到 L + T - 1 即可。
            state = advance(state, zero_transition, target - current_position)
            current_position = target

    return min(state)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    output: list[str] = []
    while index < len(data):
        length = data[index]
        index += 1
        minimum_jump, maximum_jump, stone_count = data[index:index + 3]
        index += 3
        stones = data[index:index + stone_count]
        index += stone_count
        output.append(str(solve_case(length, minimum_jump, maximum_jump, stones)))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()