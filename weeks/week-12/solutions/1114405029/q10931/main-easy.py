import sys


def main():

    # 逐行讀取輸入
    for line in sys.stdin:

        # 將輸入轉成整數
        n = int(line.strip())

        # 如果輸入是 0
        # 代表輸入結束
        if n == 0:
            break

        # 用來儲存二進位字元
        binary = []

        # 用來記錄 1 的個數
        count = 0

        # 暫存目前數字
        current = n

        # 不斷除以 2
        while current > 0:

            # 取得最低位元
            bit = current % 2

            # 加入二進位結果
            binary.append(str(bit))

            # 如果是 1
            # parity 加 1
            if bit == 1:
                count += 1

            # 去掉目前最低位元
            current //= 2

        # 因為剛剛是反向加入
        # 所以需要反轉
        binary.reverse()

        # 組成完整二進位字串
        binary_string = "".join(binary)

        # 按照題目格式輸出
        print(
            f"The parity of {binary_string} is {count} (mod 2)."
        )


if __name__ == "__main__":
    main()