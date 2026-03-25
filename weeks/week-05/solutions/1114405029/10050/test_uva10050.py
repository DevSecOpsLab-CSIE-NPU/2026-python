"""
UVA 10050 - Hartals
測試程式版本

用途說明：
這份程式主要用來做本地測試。
程式將核心計算邏輯獨立成函式，
方便檢查答案是否正確，也方便後續維護與除錯。
"""


def count_lost_working_days(days, hartal_parameters):
    """
    計算在指定天數內，因政黨罷工而損失的工作天數。

    參數：
        days (int)：模擬總天數
        hartal_parameters (list[int])：各政黨的罷工週期列表

    回傳：
        int：有效罷工天數（不含假日）

    解題觀念：
        對每個政黨的罷工週期 h，
        從第 h 天開始，每隔 h 天就會罷工一次。
        若罷工日不是每週第 6 天或第 7 天，則記錄下來。
        使用集合可避免重複計算同一天。
    """

    # 使用集合記錄所有有效罷工日，避免重複計算
    hartal_days = set()

    # 逐一處理每個政黨的罷工週期
    for interval in hartal_parameters:
        # 從該政黨第一次罷工日開始，每隔 interval 天罷工一次
        for day in range(interval, days + 1, interval):
            # 若 day % 7 == 6，表示星期五
            # 若 day % 7 == 0，表示星期六
            # 這兩天是假日，不計入損失工作天數
            if day % 7 != 6 and day % 7 != 0:
                hartal_days.add(day)

    # 回傳有效罷工日總數
    return len(hartal_days)


def solve():
    """
    依照 UVA 題目的輸入格式讀取資料並輸出答案。
    """

    # 讀入測試資料組數
    test_case_count = int(input().strip())

    # 逐組處理
    for _ in range(test_case_count):
        # 讀入模擬天數
        days = int(input().strip())

        # 讀入政黨數量
        party_count = int(input().strip())

        # 讀入每個政黨的罷工週期
        hartal_parameters = []
        for _ in range(party_count):
            hartal_parameters.append(int(input().strip()))

        # 計算答案
        answer = count_lost_working_days(days, hartal_parameters)

        # 輸出結果
        print(answer)


# 程式進入點
if __name__ == "__main__":
    solve()