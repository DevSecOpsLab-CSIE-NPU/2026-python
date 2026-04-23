# 簡單版本：二分搜尋

with open('test_input_10268.txt', 'r') as f:

    data = f.read().split()

index = 0

with open('10268-easy_test.log', 'w') as log:

    while index < len(data):

        k = int(data[index])

        n = int(data[index+1])

        index +=2

        if k == 0:

            break

        low = 1

        high = 64

        while low < high:

            mid = (low + high) // 2

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