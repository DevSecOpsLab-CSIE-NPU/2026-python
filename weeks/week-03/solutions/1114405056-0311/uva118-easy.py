import sys


def solve(data: str) -> str:
    """模擬 UVA 118 機器人移動，回傳每台機器人的最終狀態。"""
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return ""

    # 世界邊界：左下固定是 (0,0)，這裡讀右上角座標。
    max_x, max_y = map(int, lines[0].split())

    # 方向順序固定成 N -> E -> S -> W，方便用索引做左右轉。
    dirs = "NESW"
    move = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0),
    }

    # scent 記錄「哪個座標 + 哪個方向」曾經讓機器人掉出去。
    # 之後若又在相同狀態遇到前進指令，直接忽略。
    scent = set()

    out = []
    # 從第 2 行開始，每兩行描述一台機器人：
    # 第 1 行是初始位置與方向，第 2 行是指令字串。
    i = 1
    while i + 1 < len(lines):
        x_str, y_str, d = lines[i].split()
        cmds = lines[i + 1]
        i += 2

        x, y = int(x_str), int(y_str)
        lost = False

        for c in cmds:
            if c == "L":
                # 向左轉：在 NESW 中往前一格（循環）。
                d = dirs[(dirs.index(d) - 1) % 4]
            elif c == "R":
                # 向右轉：在 NESW 中往後一格（循環）。
                d = dirs[(dirs.index(d) + 1) % 4]
            else:  # c == "F"
                # 前進一格：先計算候選新座標，再判斷是否越界。
                dx, dy = move[d]
                nx, ny = x + dx, y + dy

                # 若前進會掉出世界，先檢查是否有 scent。
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    # 同一個「位置 + 方向」已經有人掉過，這次忽略 F。
                    if (x, y, d) in scent:
                        continue

                    # 第一次在這裡掉落：留下 scent，該機器人任務結束。
                    scent.add((x, y, d))
                    lost = True
                    break

                # 沒越界才真正移動。
                x, y = nx, ny

        if lost:
            out.append(f"{x} {y} {d} LOST")
        else:
            out.append(f"{x} {y} {d}")

    return "\n".join(out)


def main() -> None:
    """標準輸入輸出進入點。"""
    data = sys.stdin.read()
    ans = solve(data)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
