from __future__ import annotations

import sys


def solve_case(points: list[tuple[int, int]]) -> tuple[int, int]:
    # 曼哈頓距離可拆成 x 與 y 兩個一維問題。
    xs = sorted(x for x, _ in points)
    ys = sorted(y for _, y in points)

    # 最小值會落在中位數區間；偶數時是一段區間而非單點。
    left_x = xs[(len(xs) - 1) // 2]
    right_x = xs[len(xs) // 2]
    left_y = ys[(len(ys) - 1) // 2]
    right_y = ys[len(ys) // 2]

    # 任取區間內一點都有同樣最小距離和。
    best_distance = sum(abs(x - left_x) for x in xs) + sum(abs(y - left_y) for y in ys)
    count = (right_x - left_x + 1) * (right_y - left_y + 1)
    return best_distance, count


def main() -> None:
    # 讀入 T 組測資，每組 N 個座標點。
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