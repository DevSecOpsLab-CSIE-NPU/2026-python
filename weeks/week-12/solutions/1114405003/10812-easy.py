import sys


def solve():
    # 讀入所有數字，避免一行一行處理造成程式寫法變得零散。
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    # 第一個數字是測試資料筆數。
    test_count = int(data[0])
    index = 1
    answers = []

    for _ in range(test_count):
        # 題目給的是總分 S 和差值 D。
        total = int(data[index])
        diff = int(data[index + 1])
        index += 2

        # 先檢查基本條件：
        # 1. S 必須大於等於 D，否則小分會是負數。
        # 2. S + D 必須是偶數，因為兩隊分分都要是整數。
        if total < diff or (total + diff) % 2 != 0:
            answers.append("impossible")
            continue

        # 大分與小分的公式：
        # 大分 = (S + D) / 2
        # 小分 = (S - D) / 2
        bigger = (total + diff) // 2
        smaller = (total - diff) // 2

        if smaller < 0:
            answers.append("impossible")
        else:
            answers.append(f"{bigger} {smaller}")

    sys.stdout.write("\n".join(answers))


if __name__ == "__main__":
    solve()