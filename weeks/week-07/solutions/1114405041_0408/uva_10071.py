import sys


def displacement_after_round_trip(velocity: int, time_value: int) -> int:
    """根據等速直線運動公式，答案為 2 * v * t。"""
    return 2 * velocity * time_value


def solve(data: str) -> str:
    outputs = []

    for line in data.splitlines():
        stripped = line.strip()
        if not stripped:
            continue

        velocity, time_value = map(int, stripped.split())
        outputs.append(str(displacement_after_round_trip(velocity, time_value)))

    return "\n".join(outputs)


def main() -> None:
    # 每行一組 v 與 t，直到 EOF 結束。
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()