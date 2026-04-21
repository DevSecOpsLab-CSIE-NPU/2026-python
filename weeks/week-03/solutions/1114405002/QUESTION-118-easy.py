import sys


# 左轉、右轉的對照表，直接查表比自己手算方向快很多。
LEFT_TURN = {"N": "W", "W": "S", "S": "E", "E": "N"}
RIGHT_TURN = {"N": "E", "E": "S", "S": "W", "W": "N"}

# 前進時各方向的位移量。
STEP = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}


def main() -> None:
    # 把所有非空白輸入行讀進來，依序處理每台機器人。
    raw_lines = [line.strip() for line in sys.stdin if line.strip()]
    if not raw_lines:
        return

    # 第一行是矩形世界的右上角座標。
    max_x, max_y = map(int, raw_lines[0].split())

    # scent 會記錄「哪個座標、哪個方向」曾經讓機器人掉落。
    scent_positions = set()
    answers = []
    line_index = 1

    while line_index < len(raw_lines):
        # 第二行：機器人的起點與方向。
        x_str, y_str, direction = raw_lines[line_index].split()
        x = int(x_str)
        y = int(y_str)

        # 第三行：指令字串。
        commands = raw_lines[line_index + 1]
        line_index += 2

        lost = False

        for command in commands:
            if command == "L":
                # 左轉 90 度，只改方向，不改座標。
                direction = LEFT_TURN[direction]
            elif command == "R":
                # 右轉 90 度，只改方向，不改座標。
                direction = RIGHT_TURN[direction]
            elif command == "F":
                # 先試著往前一步，看看會不會超出邊界。
                step_x, step_y = STEP[direction]
                next_x = x + step_x
                next_y = y + step_y

                # 如果超出邊界，要看目前位置和方向是否已有 scent。
                if not (0 <= next_x <= max_x and 0 <= next_y <= max_y):
                    if (x, y, direction) in scent_positions:
                        # 之前有人在這裡掉過，所以忽略這個危險指令。
                        continue

                    # 沒有 scent，代表這台機器人真的會掉下去。
                    scent_positions.add((x, y, direction))
                    lost = True
                    break

                # 沒有掉落，就正式更新座標。
                x = next_x
                y = next_y

        result = f"{x} {y} {direction}"
        if lost:
            result += " LOST"

        answers.append(result)

    sys.stdout.write("\n".join(answers) + ("\n" if answers else ""))


if __name__ == "__main__":
    main()