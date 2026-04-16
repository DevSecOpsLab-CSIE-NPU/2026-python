"""
UVA 118 - Mutant Flatworld Explorers
機器人在矩形世界中行走，可能會掉落
"""

# 四個方向：N=北、E=東、S=南、W=西
# 用數字代表方向：0=N, 1=E, 2=S, 3=W（順時針排列）
DIRS = ["N", "E", "S", "W"]

# 每個方向對應的位移量
# N 向北：x 不變，y + 1
# E 向東：x + 1，y 不變
# S 向南：x 不變，y - 1
# W 向西：x - 1，y 不變
DX = [0, 1, 0, -1]  # X 軸位移
DY = [1, 0, -1, 0]  # Y 軸位移


def turn_left(d):
    """
    左轉 90 度

    方向編號：0=N, 1=E, 2=S, 3=W
    左轉 = 往編號變小的方向（逆時針）
    - N(0) 左轉 → W(3)
    - W(3) 左轉 → S(2)
    因此：(d + 3) % 4
    """
    return (d + 3) % 4


def turn_right(d):
    """
    右轉 90 度

    方向編號：0=N, 1=E, 2=S, 3=W
    右轉 = 往編號變大的方向（順時針）
    因此：(d + 1) % 4
    """
    return (d + 1) % 4


def solve():
    """主程式：讀取輸入、模擬機器人移動、輸出結果"""
    import sys

    # 讀取輸入
    # 支援兩種方式：
    # 1. 命令列引數：python week03_118-easy.py input.txt
    # 2. 標準輸入（stdin）
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            # 讀取所有行，並去除空白
            lines = [line.strip() for line in f if line.strip()]
    else:
        lines = [line.strip() for line in sys.stdin if line.strip()]

    # 第一行是世界邊界：右上角座標 (max_x, max_y)
    # 左下角為 (0, 0)
    max_x, max_y = map(int, lines[0].split())

    # 記錄掉落的機器人留下的「氣味」
    # 當機器人從某位置掉出去時，在該位置留下氣味
    # 後續機器人站在有氣味的位置時，會忽略會掉出去的 F 指令
    scents = set()

    # 處理每個機器人
    # 每個機器人用兩行表示：
    # 第 1 行：初始位置（x y 方向）
    # 第 2 行：指令集（L=左轉、R=右轉、F=前進）
    for i in range(1, len(lines), 2):
        # 讀取初始位置
        x, y, d_char = lines[i].split()
        x, y = int(x), int(y)
        d = DIRS.index(d_char)  # 將方向字元轉為數字索引

        # 讀取指令集
        cmds = lines[i + 1]

        # 假設機器人沒有掉落
        lost = False

        # 逐一執行指令
        for cmd in cmds:
            if cmd == "L":
                # 左轉：改變方向，不改變位置
                d = turn_left(d)
            elif cmd == "R":
                # 右轉：改變方向，不改變位置
                d = turn_right(d)
            else:
                # cmd == 'F'：前進
                # 計算前進後的新座標
                nx, ny = x + DX[d], y + DY[d]

                # 檢查是否會掉出邊界
                if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                    # 會掉出去！
                    # 檢查這個位置是否有氣味
                    if (x, y) not in scents:
                        # 沒有氣味，機器人掉落，結束指令執行
                        lost = True
                        scents.add((x, y))  # 記錄氣味
                        break
                    # 有氣味，忽略這個 F 指令，繼續下一個指令

                else:
                    # 在邊界內，正常移動
                    x, y = nx, ny

        # 輸出結果
        # 格式：x y 方向 [LOST]
        result = f"{x} {y} {DIRS[d]}"
        if lost:
            result += " LOST"
        print(result)


# 當直接執行此檔案時才執行 solve()
# 如果被其他檔案 import 則不執行
if __name__ == "__main__":
    solve()
