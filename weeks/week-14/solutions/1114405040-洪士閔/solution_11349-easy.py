# UVA 11349 - Symmetric Matrix
#
# 這是比較簡單、好記的寫法。
#
# 題目要判斷一個 n x n 矩陣是不是「以中心對稱」。
# 注意：這不是一般矩陣的轉置對稱，不是檢查 matrix[i][j] == matrix[j][i]。
# 本題要檢查的是：
#   左上角 == 右下角
#   第二個數 == 倒數第二個數
#   第三個數 == 倒數第三個數
#   依此類推
#
# 所以最直覺的做法是：
# 1. 把所有矩陣數字照輸入順序放進 numbers。
# 2. 檢查 numbers 是否等於 numbers[::-1]。
# 3. 題目另外規定：只要有負數，就一定不是 Symmetric。

t = int(input())

for case in range(1, t + 1):
    header = input().strip()

    # 有些測資中間可能有空白行，所以先略過空白行。
    while header == "":
        header = input().strip()

    # 標頭格式長這樣：N = 3
    # 用 split("=") 切開後，右邊就是矩陣大小 n。
    n = int(header.split("=")[1])

    numbers = []
    ok = True

    # 讀入 n 行矩陣資料。
    for _ in range(n):
        row = list(map(int, input().split()))

        for value in row:
            # 題目規定矩陣內的數字不能是負數。
            if value < 0:
                ok = False

            # 不管數字是多少，都放進 numbers，之後一起檢查頭尾對稱。
            numbers.append(value)

    # numbers[::-1] 是反轉後的串列。
    # 如果原串列和反轉串列一樣，代表整個矩陣以中心對稱。
    if numbers != numbers[::-1]:
        ok = False

    if ok:
        print(f"Test #{case}: Symmetric.")
    else:
        print(f"Test #{case}: Non-symmetric.")
