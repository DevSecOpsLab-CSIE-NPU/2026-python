from __future__ import annotations

import sys


def solve_case(points: list[tuple[int, int]]) -> tuple[int, int]:
    # 這題其實是曼哈頓距離和，所以 x 與 y 可以分開看。
    xs = sorted(x for x, _ in points)
    ys = sorted(y for _, y in points)

    # 偶數個點時，中位數中間那一段所有整數都一樣好。
    left_x = xs[(len(xs) - 1) // 2]
    right_x = xs[len(xs) // 2]
    left_y = ys[(len(ys) - 1) // 2]
    right_y = ys[len(ys) // 2]

    best_distance = sum(abs(x - left_x) for x in xs) + sum(abs(y - left_y) for y in ys)
    count = (right_x - left_x + 1) * (right_y - left_y + 1)
    return best_distance, count


def main() -> None:
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    if not tokens:
        return

    index = 0
    case_count = tokens[index]
    index += 1
    outputs: list[str] = []

    for _ in range(case_count):
        point_count = tokens[index]
        index += 1
        points = []
        for _ in range(point_count):
            x = tokens[index]
            y = tokens[index + 1]
            index += 2
            points.append((x, y))
        best_distance, count = solve_case(points)
        outputs.append(f"{best_distance} {count}")

    sys.stdout.write("\n".join(outputs))


if __name__ == "__main__":
    main()