# 簡單版本：佔位符

with open('test_input_10235.txt', 'r') as f:

    data = f.read().split()

index = 0

T = int(data[index])

index +=1

with open('10235-easy_test.log', 'w') as log:

    for case in range(T):

        N = int(data[index])

        M = int(data[index+1])

        index +=2

        grid = []

        for i in range(N):

            row = []

            for j in range(M):

                row.append(int(data[index]))

                index +=1

            grid.append(row)

        log.write(f"Case {case+1}: 0\n")