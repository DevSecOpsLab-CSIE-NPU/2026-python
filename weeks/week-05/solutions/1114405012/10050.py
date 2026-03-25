import sys


def solve(data: str) -> str:
    """解 UVA 10050（Hartals）並回傳輸出字串。"""
    # 將整份輸入一次讀入並轉為整數串列
    # split() 可同時處理空白與換行
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    # 第一個整數是測資組數 T
    t = nums[0]

    # idx 是目前讀取位置指標
    idx = 1

    # 收集每組測資答案，最後以換行串接
    answers = []

    for _ in range(t):
        # N：模擬天數；P：政黨數量
        n = nums[idx]
        idx += 1
        p = nums[idx]
        idx += 1

        # 讀取 P 個 hartal 參數
        hartals = nums[idx:idx + p]
        idx += p

        # 用集合記錄「實際損失的工作日」
        # 好處：多個政黨落在同一天只會計一次
        lost_days = set()

        for h in hartals:
            # 第 h, 2h, 3h, ... 天為該政黨的罷會日
            for day in range(h, n + 1, h):
                # 題目規則：每週星期五、星期六不計入
                # 已知第 1 天是星期天，故：
                # day % 7 == 6 -> 星期五
                # day % 7 == 0 -> 星期六
                weekday = day % 7
                if weekday == 6 or weekday == 0:
                    continue

                # 其餘工作日若有罷會，記錄為損失日
                lost_days.add(day)

        # 本組答案為損失工作天數
        answers.append(str(len(lost_days)))

    # 依題目要求：每組答案輸出一行
    return "\n".join(answers)


if __name__ == "__main__":
    # 從標準輸入讀取資料並輸出結果
    print(solve(sys.stdin.read()))
