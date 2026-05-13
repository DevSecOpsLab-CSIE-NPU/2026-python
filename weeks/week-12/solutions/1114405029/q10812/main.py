import sys


# 此函式負責處理單一測試資料
# total：兩隊分數總和
# diff：兩隊分數差
def solve_case(total, diff):

    # 如果差比分數總和還大
    # 代表較小分數一定會變成負數
    # 例如：
    # total = 20
    # diff = 40
    #
    # low = (20 - 40) / 2 = -10
    #
    # 分數不可能是負數，因此輸出 impossible
    if diff > total:
        return "impossible"

    # 根據公式：
    #
    # high = (total + diff) / 2
    # low  = (total - diff) / 2
    #
    # 分數必須是整數
    # 因此 total + diff 必須能被 2 整除
    #
    # 若 total + diff 為奇數
    # 就無法得到整數答案
    if (total + diff) % 2 != 0:
        return "impossible"

    # 計算較大的分數
    high = (total + diff) // 2

    # 計算較小的分數
    low = (total - diff) // 2

    # 回傳答案
    return f"{high} {low}"


def main():

    # 一次讀取所有輸入資料
    # strip()：移除前後空白與換行
    # split()：依照空白切割成串列
    data = sys.stdin.read().strip().split()

    # 如果沒有輸入資料
    # 直接結束程式
    if not data:
        return

    # 第一個數字代表測試資料組數
    t = int(data[0])

    # index 用來追蹤目前讀到哪個位置
    index = 1

    # 用來儲存所有答案
    answers = []

    # 逐組處理測試資料
    for _ in range(t):

        # 讀取總和與差
        total = int(data[index])
        diff = int(data[index + 1])

        # 移動到下一組資料
        index += 2

        # 計算答案後加入串列
        answers.append(solve_case(total, diff))

    # 使用換行符號把所有答案接起來
    # 一次輸出效率較好
    sys.stdout.write("\n".join(answers))


# Python 主程式入口
if __name__ == "__main__":
    main()