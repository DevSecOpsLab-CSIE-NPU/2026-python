import sys

# 題目提供的範例輸入，方便直接驗證程式正確性。
SAMPLE_INPUT = """5 3
1 1 E
RFRFRFRF
3 2 N
FRRFLLFFRRFLL
0 3 W
LLFFFLFLFL
"""

# 題目對應的範例輸出。
SAMPLE_OUTPUT = """1 1 E
3 3 N LOST
2 3 S"""

# 依照順時針方向排列，方便處理左右轉。
DIRECTIONS = ["N", "E", "S", "W"]

# 每個方向前進一格時，x、y 的變化量。
MOVES = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def turn_left(direction: str) -> str:
    # 左轉等於在方向陣列中往前退一格。
    return DIRECTIONS[(DIRECTIONS.index(direction) - 1) % 4]


def turn_right(direction: str) -> str:
    # 右轉等於在方向陣列中往前進一格。
    return DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]


def move_forward(x: int, y: int, direction: str) -> tuple[int, int]:
    # 依照目前方向計算前進後的新座標。
    dx, dy = MOVES[direction]
    return x + dx, y + dy


def simulate_robot(
    x: int,
    y: int,
    direction: str,
    commands: str,
    max_x: int,
    max_y: int,
    scents: set[tuple[int, int, str]],
) -> tuple[int, int, str, bool]:
    # lost 用來記錄這台機器人是否掉出地圖。
    lost = False

    for command in commands:
        if command == "L":
            direction = turn_left(direction)
        elif command == "R":
            direction = turn_right(direction)
        elif command == "F":
            next_x, next_y = move_forward(x, y, direction)

            # 若前進後仍在地圖內，直接更新位置。
            if 0 <= next_x <= max_x and 0 <= next_y <= max_y:
                x, y = next_x, next_y
                continue

            # 若這個位置與方向曾留下標記，代表此危險動作要被忽略。
            scent_key = (x, y, direction)
            if scent_key in scents:
                continue

            # 第一次在此位置面朝此方向跌落，留下標記並結束。
            scents.add(scent_key)
            lost = True
            break

    return x, y, direction, lost


def format_robot_state(x: int, y: int, direction: str, lost: bool) -> str:
    # 依題目格式組合輸出字串。
    result = f"{x} {y} {direction}"
    if lost:
        result += " LOST"
    return result


def solve(text: str) -> str:
    # 先去除空白行，避免解析輸入時出錯。
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return ""

    max_x, max_y = map(int, lines[0].split())
    scents: set[tuple[int, int, str]] = set()
    output = []

    index = 1
    while index < len(lines):
        x_str, y_str, direction = lines[index].split()
        commands = lines[index + 1]

        x, y, direction, lost = simulate_robot(
            int(x_str),
            int(y_str),
            direction,
            commands,
            max_x,
            max_y,
            scents,
        )
        output.append(format_robot_state(x, y, direction, lost))
        index += 2

    return "\n".join(output)


def run_sample_test() -> None:
    # 用題目範例進行快速自我檢查。
    result = solve(SAMPLE_INPUT)
    print(result)
    assert result == SAMPLE_OUTPUT, "範例測試未通過"


if __name__ == "__main__":
    # 若沒有從標準輸入讀到資料，就改跑內建範例測試。
    if sys.stdin.isatty():
        run_sample_test()
    else:
        data = sys.stdin.read()
        if not data.strip():
            sys.exit(0)
        print(solve(data))
