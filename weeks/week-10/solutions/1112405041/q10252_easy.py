import sys

def solve():
    """
    UVA 10252 魔改版：找出一點 P 使得與 N 個點的距離之和最小
    解法：
    在二維平面上，若距離定義為 L1 距離 (Manhattan distance: |x1-x2| + |y1-y2|)，
    則最優的 P 點之 (x, y) 座標分別為所有給定點 x 座標與 y 座標的中位數。
    1. 讀取測試組數 T。
    2. 對每組測資，讀取 N 個點。
    3. 分別對 X, Y 座標排序。
    4. 找出中位數範圍內的整數解個數與最小距離和。
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    ptr = 0
    T = int(input_data[ptr])
    ptr += 1

    for _ in range(T):
        N = int(input_data[ptr])
        ptr += 1

        xs = []
        ys = []
        for _ in range(N):
            xs.append(int(input_data[ptr]))
            ys.append(int(input_data[ptr+1]))
            ptr += 2

        xs.sort()
        ys.sort()

        # 中位數位置
        m1 = (N - 1) // 2
        m2 = N // 2

        # 最優 x, y 範圍 (若 N 為奇數，m1==m2)
        best_x = xs[m1]
        best_y = ys[m1]

        # 計算最小距離和
        min_dist = 0
        for x in xs:
            min_dist += abs(x - best_x)
        for y in ys:
            min_dist += abs(y - best_y)

        # 計算可能的整數解數量
        # 整數解數量 = (x 範圍內的整數) * (y 範圍內的整數)
        count_x = xs[m2] - xs[m1] + 1
        count_y = ys[m2] - ys[m1] + 1
        total_solutions = count_x * count_y

        print(f"{min_dist} {total_solutions}")

if __name__ == "__main__":
    solve()
