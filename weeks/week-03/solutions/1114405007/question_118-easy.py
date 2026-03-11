"""UVA 118 - 好記版本（-easy）。

這版把重點濃縮成一個主迴圈：
1. 轉向就改方向
2. 前進先判斷會不會出界
3. 會出界時看 scent，決定忽略或 LOST
"""

DIRECTIONS = "NESW"
STEP = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


def main() -> None:
    import sys

    # 先把所有行讀進來，方便成對處理（位置行 + 指令行）。
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    max_x, max_y = map(int, lines[0].split())

    # scent 記錄 (x, y, dir)：表示曾有機器人從此狀態往前掉落。
    scent = set()

    i = 1
    while i + 1 < len(lines):
        x, y, d = lines[i].split()
        x = int(x)
        y = int(y)
        commands = lines[i + 1]
        lost = False

        for cmd in commands:
            if cmd == "L":
                d = DIRECTIONS[(DIRECTIONS.index(d) - 1) % 4]
            elif cmd == "R":
                d = DIRECTIONS[(DIRECTIONS.index(d) + 1) % 4]
            else:
                dx, dy = STEP[d]
                nx, ny = x + dx, y + dy

                # 若下一步會掉出地圖，依 scent 決定是否忽略。
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    key = (x, y, d)
                    if key in scent:
                        continue
                    scent.add(key)
                    lost = True
                    break

                x, y = nx, ny

        if lost:
            print(f"{x} {y} {d} LOST")
        else:
            print(f"{x} {y} {d}")

        i += 2


if __name__ == "__main__":
    main()
