# 手打程式：手動實現雞蛋掉落問題，加上繁體中文註解

# 讀取輸入

with open('test_input_10268.txt', 'r') as f:

    data = f.read().split()

index = 0

# 輸出記錄

with open('10268-manual_test.log', 'w') as log:

    while index < len(data):

        k = int(data[index])

        n = int(data[index+1])

        index +=2

        if k == 0:

            break

        # 二分搜尋最小 m

        low = 1

        high = 64

        while low < high:

            mid = (low + high) // 2

            # 計算使用 k 個雞蛋 m 次可以區分的最大樓層

            s = 0

            c = 1

            for i in range(k+1):

                s += c

                if i < k:

                    c = c * (mid - i) // (i + 1)

            if s >= n:

                high = mid

            else:

                low = mid + 1

        if low > 63:

            log.write("More than 63 trials needed.\n")

        else:

            log.write(str(low) + '\n')