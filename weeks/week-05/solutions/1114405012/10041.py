import sys


def min_total_distance(addresses):
    """計算所有親戚到新家的最小總距離。

    說明：
    在一維數線上，若要讓到所有點的絕對距離總和最小，
    最佳位置會落在「中位數」上。
    """
    # 先排序，方便取得中位數位置
    sorted_addresses = sorted(addresses)

    # 取中位數作為 Vito 新家的最佳門牌（偶數筆取其中一個中位數即可）
    median = sorted_addresses[len(sorted_addresses) // 2]

    # 計算所有親戚到中位數位置的距離總和
    return sum(abs(x - median) for x in sorted_addresses)


def solve(data: str) -> str:
    """解析題目輸入並回傳對應輸出字串。"""
    # 將整份輸入切成整數串列（可同時處理空白與換行分隔）
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    # 第一個數字為測資組數
    t = nums[0]
    idx = 1
    answers = []

    for _ in range(t):
        # 每組測資第一個數字 r 代表親戚數量
        r = nums[idx]
        idx += 1

        # 讀取接下來 r 個門牌號碼
        addresses = nums[idx : idx + r]
        idx += r

        # 計算該組測資的最小總距離並轉為字串
        answers.append(str(min_total_distance(addresses)))

    # 依題目要求，每組答案輸出一行
    return "\n".join(answers)


if __name__ == "__main__":
    # 從標準輸入讀取完整資料並印出結果
    input_data = sys.stdin.read()
    print(solve(input_data))
