import sys


def check_symmetric(values):
    """
    用最直觀的方式檢查是否為本題要求的對稱矩陣。

    values 是把整個矩陣由左到右、由上到下攤平成的一維串列。

    如果矩陣是中心對稱，代表：
    values[0] 要等於 values[-1]
    values[1] 要等於 values[-2]
    values[2] 要等於 values[-3]

    只要有任何一組不一樣，就不是對稱矩陣。

    另外，如果任何數字是負數，也不是對稱矩陣。
    """

    left = 0
    right = len(values) - 1

    while left <= right:
        # 只要左右任一邊是負數，就不符合題目要求
        if values[left] < 0 or values[right] < 0:
            return False

        # 檢查中心對稱位置是否相等
        if values[left] != values[right]:
            return False

        left += 1
        right -= 1

    return True


def solve(data):
    """
    讀取輸入資料並產生答案。

    這份 easy 版使用比較直觀的寫法：
    1. 先用 split() 切開所有輸入。
    2. 依序讀取測資數量、矩陣大小、矩陣元素。
    3. 呼叫 check_symmetric() 判斷。
    """

    parts = data.split()

    if len(parts) == 0:
        return ""

    t = int(parts[0])
    pos = 1
    output = []

    for case_id in range(1, t + 1):
        # 每組測資開頭格式是 N = n
        # parts[pos] 是 N
        # parts[pos + 1] 是 =
        # parts[pos + 2] 是真正的 n
        n = int(parts[pos + 2])
        pos += 3

        values = []

        for _ in range(n * n):
            values.append(int(parts[pos]))
            pos += 1

        if check_symmetric(values):
            output.append(f"Test #{case_id}: Symmetric.")
        else:
            output.append(f"Test #{case_id}: Non-symmetric.")

    return "\n".join(output)


def main():
    data = sys.stdin.read()
    answer = solve(data)
    print(answer)


if __name__ == "__main__":
    main()