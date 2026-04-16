"""UVA 118 的簡易版本。

這份版本用更直觀的方式實現：
- 不用類別，改用字典記錄機器人狀態
- 方向管理改用簡單的 list index
- 核心規則用直白的 if-else 實現

適合快速背誦的重點只有三個：
1. 方向是固定的循環：['N', 'E', 'S', 'W']
2. scent 記錄 (x, y, direction) 的三元組
3. LOST 後停止所有指令
"""

from __future__ import annotations


def solve_robots(map_max_x: int, map_max_y: int, robots_data: list[tuple[str, str]]) -> list[str]:
    """簡易版的機器人模擬。
    
    參數：
    - map_max_x, map_max_y：地圖邊界（包含該座標點）
    - robots_data：每個機器人的 (初始狀態, 指令集) tuple 列表
    
    回傳：每個機器人的最終狀態文字。
    
    核心流程：
    1. 每個機器人依序執行指令。
    2. L/R 改變方向，F 嘗試前進。
    3. 前進會掉落時，檢查 scent 決定是否 LOST。
    4. LOST 後停止該機器人的所有指令。
    """

    # 方向的固定循環。N -> E -> S -> W -> N
    # 用 index 的方式讓旋轉變成簡單的 +1 或 -1（模 4）。
    directions = ['N', 'E', 'S', 'W']

    # 全局的 scent 集合，記錄 (x, y, direction) 三元組。
    # 因為所有機器人都在同一個世界裡，scent 是全局共享的。
    scent = set()

    results = []

    # 依序執行每個機器人。前面機器人的 scent 會影響後面的機器人。
    for initial_state_str, commands_str in robots_data:
        # 解析初始狀態字符串：「x y direction」，例如「1 2 N」。
        parts = initial_state_str.split()
        x, y = int(parts[0]), int(parts[1])
        direction = parts[2]

        # 機器人是否已掉落。
        lost = False

        # 依序執行指令。如果 LOST 就提前跳出迴圈。
        for cmd in commands_str:
            # LOST 後停止所有指令。這是 UVA 118 的重要規則。
            if lost:
                break

            if cmd == 'L':
                # 左轉 90 度：找到當前方向在陣列中的位置，往回移一位。
                # 例如 direction='N' 時 idx=0，(0-1)%4=3，所以是 directions[3]='W'。
                idx = directions.index(direction)
                direction = directions[(idx - 1) % 4]

            elif cmd == 'R':
                # 右轉 90 度：找到當前方向在陣列中的位置，往前移一位。
                # 例如 direction='N' 時 idx=0，(0+1)%4=1，所以是 directions[1]='E'。
                idx = directions.index(direction)
                direction = directions[(idx + 1) % 4]

            elif cmd == 'F':
                # 前進：根據當前方向計算新位置。
                if direction == 'N':
                    nx, ny = x, y + 1  # 北方是 y 增加。
                elif direction == 'E':
                    nx, ny = x + 1, y  # 東方是 x 增加。
                elif direction == 'S':
                    nx, ny = x, y - 1  # 南方是 y 減少。
                else:  # 'W'
                    nx, ny = x - 1, y  # 西方是 x 減少。

                # 判斷新位置是否在邊界內。邊界是 [0, max_x] × [0, max_y]。
                if 0 <= nx <= map_max_x and 0 <= ny <= map_max_y:
                    # 在邊界內，正常移動。
                    x, y = nx, ny
                else:
                    # 會掉落（超出邊界）：檢查是否已有 scent。
                    # scent 是以 (x, y, direction) tuple 為鑰匙。
                    # 注意是「掉落前的位置」+ 「掉落時的方向」。
                    scent_key = (x, y, direction)
                    if scent_key not in scent:
                        # 還沒有 scent，這次掉落就留下記號。
                        scent.add(scent_key)
                        # 標記機器人已掉落，後續指令都會被跳過。
                        lost = True
                    # 如果已有 scent，就忽略這個 F 指令，位置和狀態都不改變。

        # 輸出最終狀態。
        if lost:
            results.append(f"{x} {y} {direction} LOST")
        else:
            results.append(f"{x} {y} {direction}")

    return results


def parse_and_solve(text: str) -> str:
    """解析 UVA 118 的輸入並求解。
    
    輸入格式：
    - 第 1 行：地圖邊界 max_x max_y
    - 接下來每 2 行為一個機器人：
      - 初始狀態：x y direction
      - 指令集：由 L/R/F 組成的字串
    
    處理流程：
    1. 分析第一行得到邊界。
    2. 按照每 2 行一組收集機器人資料。
    3. 呼叫 solve_robots 進行模擬。
    4. 把結果組成一個字符串回傳。
    """

    lines = text.strip().splitlines()
    if not lines:
        return ""

    # 第一行是地圖邊界，格式為「max_x max_y」。
    map_parts = lines[0].split()
    map_max_x, map_max_y = int(map_parts[0]), int(map_parts[1])

    # 收集機器人資料。
    # 因為每個機器人占 2 行（初始狀態 + 指令集），所以 i 要 += 2。
    robots_data = []
    i = 1
    while i + 1 < len(lines):
        # 第 i 行是初始狀態，第 i+1 行是指令集。
        robots_data.append((lines[i], lines[i + 1]))
        i += 2

    # 呼叫核心求解函式。
    results = solve_robots(map_max_x, map_max_y, robots_data)
    
    # 把每個機器人的結果用換行連接。
    return "\n".join(results)


if __name__ == "__main__":
    import sys

    input_text = sys.stdin.read()
    if input_text.strip():
        print(parse_and_solve(input_text))
