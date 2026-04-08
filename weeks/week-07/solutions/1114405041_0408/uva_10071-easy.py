import sys


def solve(data: str) -> str:
    """
    簡單版記法：
    題目本質是在問「如果速度一直都是 v，而且時間是 2t，那位移是多少？」
    所以每筆資料直接算 2 * v * t 就好。
    """
    answers = []

    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue

        v, t = map(int, line.split())
        answers.append(str(2 * v * t))

    return "\n".join(answers)


def main() -> None:
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()