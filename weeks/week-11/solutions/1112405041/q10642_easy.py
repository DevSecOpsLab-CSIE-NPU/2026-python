# AI Easy 版: 10642 Can You Solve It?
import sys

def get_pos_value(x, y):
    """
    計算 (x, y) 座標在路徑上的序號。
    公式：該點所在斜線層數為 x+y。
    前 (x+y) 層點數總和為 (x+y)*(x+y+1)//2。
    當前層 (斜線) 從 y 軸開始，x 座標每增加 1 就前進一步，
    所以再加上 x 偏移量。
    """
    layer = x + y
    base_count = layer * (layer + 1) // 2
    return base_count + x

def solve():
    raw_input = sys.stdin.read().split()
    if not raw_input: return

    try:
        t_cases = int(raw_input[0])
    except ValueError: return

    ptr = 1
    for i in range(1, t_cases + 1):
        x1, y1 = int(raw_input[ptr]), int(raw_input[ptr+1])
        x2, y2 = int(raw_input[ptr+2]), int(raw_input[ptr+3])
        ptr += 4

        steps = get_pos_value(x2, y2) - get_pos_value(x1, y1)
        print(f"Case {i}: {steps}")

if __name__ == "__main__":
    solve()
