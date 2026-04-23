# 手打程式：手動計算幾何中位數，加上繁體中文註解

# 讀取輸入

with open('test_input_10252.txt', 'r') as f:

    data = f.read().split()

index = 0

T = int(data[index])

index +=1

# 輸出記錄

with open('10252-manual_test.log', 'w') as log:

    for _ in range(T):

        N = int(data[index])

        index +=1

        # 讀取點

        points = []

        for _ in range(N):

            x = int(data[index])

            y = int(data[index+1])

            index +=2

            points.append((x, y))

        # 排序 x 和 y

        xs = sorted(p[0] for p in points)

        ys = sorted(p[1] for p in points)

        # 確定候選點

        if N % 2 == 1:

            mx = xs[N//2]

            my = ys[N//2]

            candidates = [(mx, my)]

        else:

            mx1 = xs[N//2 -1]

            mx2 = xs[N//2]

            my1 = ys[N//2 -1]

            my2 = ys[N//2]

            candidates = [(mx1, my1), (mx1, my2), (mx2, my1), (mx2, my2)]

        # 計算最小距離和計數

        min_dist = float('inf')

        count = 0

        for cx, cy in candidates:

            dist = sum((cx - x)**2 + (cy - y)**2 for x, y in points)

            if dist < min_dist:

                min_dist = dist

                count = 1

            elif dist == min_dist:

                count +=1

        log.write(f"{min_dist} {count}\n")