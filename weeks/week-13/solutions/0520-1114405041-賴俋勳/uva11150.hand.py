import sys


INF = 10 ** 18


def mat_mul(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
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
    matrix = [[INF] * size for _ in range(size)]
    for i in range(size - 1):
        matrix[i][i + 1] = 0
    for j in range(0, size - minimum_jump + 1):
        if 0 <= j < size:
            matrix[size - 1][j] = landing_cost
    return matrix


def advance(state: list[int], transition: list[list[int]], steps: int) -> list[int]:
    if steps <= 0:
        return state
    return mat_vec_mul(mat_pow(transition, steps), state)


def solve_case(length: int, minimum_jump: int, maximum_jump: int, stones: list[int]) -> int:
    size = maximum_jump
    zero_transition = build_transition(size, minimum_jump, maximum_jump, 0)
    stone_transition = build_transition(size, minimum_jump, maximum_jump, 1)

    state = [INF] * size
    state[-1] = 0
    current_position = 0

    targets = [stone for stone in stones if stone < length]
    targets.sort()
    targets.append(length + maximum_jump - 1)

    for target in targets:
        gap = target - current_position - 1
        state = advance(state, zero_transition, gap)
        current_position += gap

        if target < length:
            state = mat_vec_mul(stone_transition, state)
            current_position = target
        else:
            state = advance(state, zero_transition, target - current_position)
            current_position = target

    return min(state)


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    index = 0
    output = []
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