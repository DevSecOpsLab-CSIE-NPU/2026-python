"""
UVA 118 / ZeroJudge c082 - Martian Robots（火星機器人）
========================================================
【題目概要】
  在一個矩形網格（左下角 (0,0)，右上角 (max_x, max_y)）上，
  依序控制多個機器人執行指令。

【指令集】
  L → 原地左轉 90 度
  R → 原地右轉 90 度
  F → 往面向方向前進一格

【掉落與標記（Scent）機制】
  - 機器人走出邊界即「掉落（LOST）」，並在掉落前的最後位置留下 scent。
  - 後續機器人若站在有 scent 的位置，且下一步 F 會離開邊界，
    則該 F 指令被忽略（機器人安全留在原地）。

【輸出格式】
  正常：x y 方向
  掉落：x y 方向 LOST

【方向系統】
  N（北）= y+1，S（南）= y-1，E（東）= x+1，W（西）= x-1
  左轉順序：N → W → S → E → N
  右轉順序：N → E → S → W → N
"""

import sys

# ── 方向常數 ──────────────────────────────────────────────────────────────────
# 按「右轉」順序排列，方便用索引計算轉向
DIRS = ['N', 'E', 'S', 'W']

# 各方向對應的座標位移 (dx, dy)
MOVE = {
    'N': (0,  1),   # 北：y 增加
    'E': (1,  0),   # 東：x 增加
    'S': (0, -1),   # 南：y 減少
    'W': (-1, 0),   # 西：x 減少
}


# ─────────────────────────────────────────────────────────────────────────────
def turn_left(d: str) -> str:
    """
    將方向 d 向左轉 90 度並回傳新方向。

    【轉向原理】
      DIRS = ['N', 'E', 'S', 'W']，依右轉順序排列。
      左轉與右轉相反，所以索引 -1（往左移一格）即為左轉結果。
      對 4 取餘數是為了讓 'N'（索引 0）左轉後繞回 'W'（索引 3），
      而不是變成索引 -1（Python 雖然支援負索引，但 % 4 更清晰）。

      左轉對照表：
        N(0) → W(3)    E(1) → N(0)
        S(2) → E(1)    W(3) → S(2)

    參數：
        d (str): 目前方向，'N' / 'E' / 'S' / 'W'

    回傳：
        str: 左轉後的新方向
    """
    return DIRS[(DIRS.index(d) - 1) % 4]


def turn_right(d: str) -> str:
    """
    將方向 d 向右轉 90 度並回傳新方向。

    【轉向原理】
      DIRS = ['N', 'E', 'S', 'W']，本身就是依右轉順序排列的，
      所以索引 +1 即為右轉結果。
      對 4 取餘數是為了讓 'W'（索引 3）右轉後繞回 'N'（索引 0）。

      右轉對照表：
        N(0) → E(1)    E(1) → S(2)
        S(2) → W(3)    W(3) → N(0)

    參數：
        d (str): 目前方向，'N' / 'E' / 'S' / 'W'

    回傳：
        str: 右轉後的新方向
    """
    return DIRS[(DIRS.index(d) + 1) % 4]


# ─────────────────────────────────────────────────────────────────────────────
def run_robot(x: int, y: int, d: str, cmds: str,
              max_x: int, max_y: int, scents: set) -> tuple:
    """
    模擬單一機器人執行完整指令集。

    【處理流程】
      1. 逐字元讀取 cmds
      2. L/R：直接轉向，不影響位置
      3. F：
         a. 計算下一個座標 (nx, ny)
         b. 若 (nx, ny) 在邊界內 → 移動過去
         c. 若超出邊界，且目前位置有 scent → 忽略此 F
         d. 若超出邊界，且目前位置無 scent → 記錄 scent、標記 LOST、停止

    參數：
        x, y  (int): 初始座標
        d     (str): 初始方向
        cmds  (str): 指令字串
        max_x (int): 網格 x 最大值
        max_y (int): 網格 y 最大值
        scents (set): 已有 scent 的座標集合（會被修改）

    回傳：
        tuple: (x, y, d, lost)
          x, y (int) : 最終座標（或掉落前最後座標）
          d    (str) : 最終方向
          lost (bool): True 表示機器人掉落
    """
    for cmd in cmds:
        if cmd == 'L':
            d = turn_left(d)                    # 原地左轉
        elif cmd == 'R':
            d = turn_right(d)                   # 原地右轉
        elif cmd == 'F':
            dx, dy = MOVE[d]
            nx, ny = x + dx, y + dy             # 計算下一格座標

            if 0 <= nx <= max_x and 0 <= ny <= max_y:
                # 在邊界內，正常前進
                x, y = nx, ny
            else:
                # 下一格超出邊界
                if (x, y) in scents:
                    # 目前位置有 scent：忽略這個 F 指令，保持不動
                    pass
                else:
                    # 無 scent：機器人掉落
                    scents.add((x, y))          # 在目前位置留下 scent
                    return x, y, d, True        # 回傳掉落前的最後狀態

    # 所有指令執行完畢，機器人存活
    return x, y, d, False


# ─────────────────────────────────────────────────────────────────────────────
def solve(input_text: str) -> str:
    """
    解析完整輸入，回傳對應的輸出字串。

    【輸入格式】
      第一行：max_x max_y
      之後每兩行為一組機器人：
        行 1：x y 方向
        行 2：指令字串

    【輸出格式】
      每個機器人一行：
        存活 → "x y 方向"
        掉落 → "x y 方向 LOST"

    參數：
        input_text (str): 完整輸入文字

    回傳：
        str: 完整輸出文字
    """
    # 過濾空行，避免解析錯誤
    lines = [l.strip() for l in input_text.strip().splitlines() if l.strip()]
    idx = 0

    # 第一行：讀取網格右上角座標
    max_x, max_y = map(int, lines[idx].split())
    idx += 1

    scents  = set()     # 儲存掉落過的座標，讓後續機器人參考
    results = []        # 收集每個機器人的輸出行

    # 逐組處理機器人（每組佔兩行）
    while idx + 1 < len(lines):
        # 第奇數行：初始位置與方向
        parts = lines[idx].split()
        x, y, d = int(parts[0]), int(parts[1]), parts[2]
        idx += 1

        # 第偶數行：指令字串
        cmds = lines[idx]
        idx += 1

        # 模擬機器人執行指令
        fx, fy, fd, lost = run_robot(x, y, d, cmds, max_x, max_y, scents)

        if lost:
            # 掉落：輸出「最後位置 + 方向 + LOST」
            results.append(f"{fx} {fy} {fd} LOST")
        else:
            # 存活：只輸出「最終位置 + 方向」
            results.append(f"{fx} {fy} {fd}")

    # 將所有輸出行用換行符串接，結尾不加多餘換行
    return "\n".join(results)


# ── 直接執行時：從 stdin 讀入，輸出至 stdout ─────────────────────────────────
if __name__ == "__main__":
    print(solve(sys.stdin.read()))
