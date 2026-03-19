def is_jolly(sequence: list[int]) -> bool:
    # 取得序列長度
    n = len(sequence)

    # 若只有 1 個數字，沒有相鄰差值，
    # 依題意可視為 Jolly
    if n == 1:
        return True

    # 用集合儲存所有相鄰兩數的絕對差
    diffs = set()

    # 從第 2 個數字開始，逐一和前一個數字做差
    for i in range(1, n):
        diff = abs(sequence[i] - sequence[i - 1])

        # 合法差值必須介於 1 到 n-1
        # 若超出範圍，直接不是 Jolly
        if diff < 1 or diff >= n:
            return False

        # 把差值加入集合
        diffs.add(diff)

    # 若是 Jolly，則差值集合中應剛好有 n-1 種不同差值
    return len(diffs) == n - 1


def solve(data: str) -> str:
    # 用來儲存每組測資的答案
    answers = []

    # 逐行處理輸入
    for line in data.strip().splitlines():
        # 把這一行切開並轉成整數串列
        parts = list(map(int, line.split()))

        # 第一個數字是 n，表示此序列長度
        n = parts[0]

        # 後面 n 個數字就是實際序列
        sequence = parts[1:1 + n]

        # 判斷是否為 Jolly Jumper
        if is_jolly(sequence):
            answers.append("Jolly")
        else:
            answers.append("Not jolly")

    # 每組答案以換行連接
    return "\n".join(answers)


if __name__ == "__main__":
    import sys

    # 讀取整份標準輸入後交給 solve 處理
    input_data = sys.stdin.read()
    print(solve(input_data))