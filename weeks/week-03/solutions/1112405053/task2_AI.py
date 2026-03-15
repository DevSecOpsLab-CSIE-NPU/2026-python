import sys


def solve() -> None:
    # 讀入所有非空白行（每台機器人固定佔兩行：初始狀態 + 指令字串）
    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    # 世界右上角座標，左下角固定為 (0, 0)
    max_x, max_y = map(int, lines[0].split())

    # 記錄會導致掉落的座標，後續機器人若在同座標執行會掉落的 F 指令要忽略。
    scent = set()

    # 方向順序：用索引 +1 / -1 來做右轉與左轉
    dirs = ["N", "E", "S", "W"]
    # 各方向前進一格時，座標的變化量
    delta = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }

    # 收集每台機器人的最終輸出
    out = []
    i = 1
    # 每兩行處理一台機器人
    while i + 1 < len(lines):
        x, y, d = lines[i].split()
        x = int(x)
        y = int(y)
        cmd = lines[i + 1]
        i += 2

        lost = False

        for c in cmd:
            if c == "L":
                # 左轉：方向索引 -1
                d = dirs[(dirs.index(d) - 1) % 4]
            elif c == "R":
                # 右轉：方向索引 +1
                d = dirs[(dirs.index(d) + 1) % 4]
            else:  # c == "F"
                # 前進：先計算下一步位置
                dx, dy = delta[d]
                nx, ny = x + dx, y + dy

                # 若前進後越界：
                # 1) 有 scent：忽略這個 F
                # 2) 無 scent：此機器人 LOST，並在目前位置留下 scent
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    if (x, y) in scent:
                        continue
                    scent.add((x, y))
                    lost = True
                    break
 
                # 合法前進就更新位置
                x, y = nx, ny

        # 依題目格式輸出（掉落需加上 LOST）
        if lost:
            out.append(f"{x} {y} {d} LOST")
        else:
            out.append(f"{x} {y} {d}")

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
