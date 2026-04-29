from __future__ import annotations

import sys


def axis_distance(values: list[int], pivot: int) -> int:
    return sum(abs(value - pivot) for value in values)


def solve(data: str) -> str:
    numbers = [int(token) for token in data.split()]
    if not numbers:
        return ""

    iterator = iter(numbers)
    case_count = next(iterator)
    outputs: list[str] = []

    for _ in range(case_count):
        point_count = next(iterator)
        xs = [0] * point_count
        ys = [0] * point_count
        for index in range(point_count):
            xs[index] = next(iterator)
            ys[index] = next(iterator)

        xs.sort()
        ys.sort()

        x_left = xs[(point_count - 1) // 2]
        x_right = xs[point_count // 2]
        y_left = ys[(point_count - 1) // 2]
        y_right = ys[point_count // 2]

        best_distance = axis_distance(xs, x_left) + axis_distance(ys, y_left)
        solution_count = (x_right - x_left + 1) * (y_right - y_left + 1)
        outputs.append(f"{best_distance} {solution_count}")

    return "\n".join(outputs)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()