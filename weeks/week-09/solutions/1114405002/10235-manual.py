# 手打程式：手動讀取網格並輸出佔位符，加上繁體中文註解

# 讀取測試輸入

with open('test_input_10235.txt', 'r') as f:

    data = f.read().split()

index = 0

# 測試案例數

T = int(data[index])

index +=1

# 輸出記錄

with open('10235-manual_test.log', 'w') as log:

    for case in range(T):

        # 讀取 N 和 M

        N = int(data[index])

        M = int(data[index+1])

        index +=2

        # 讀取網格

        grid = []

        for i in range(N):

            row = []

            for j in range(M):

                row.append(int(data[index]))

                index +=1

            grid.append(row)

        # 佔位符

        log.write(f"Case {case+1}: 0\n")