"""
UVA 10057 - A mid-summer night's dream
測試程式版本

用途說明：
這份程式主要用來做本地測試。
程式將核心計算邏輯獨立成函式，
方便檢查答案是否正確，也方便後續維護與除錯。
"""


def find_median_info(numbers):
    """
    計算本題要求的三個答案：
    1. 最小可行中位數
    2. 原資料中落在可行中位數範圍內的數值個數
    3. 可作為中位數的整數個數

    參數：
        numbers (list[int])：輸入的整數資料列表

    回傳：
        tuple[int, int, int]：
            (最小可行中位數, 符合範圍的資料個數, 可行中位數個數)

    解題觀念：
        將資料排序後：
        1. 若資料筆數為奇數，只有正中間那個值可作為中位數
        2. 若資料筆數為偶數，介於中間兩個值之間的所有整數都可作為中位數
    """

    # 先將資料排序，方便找出中間位置
    numbers.sort()

    # 取得資料筆數
    data_count = len(numbers)

    # 若為奇數筆資料
    if data_count % 2 == 1:
        # 正中間的值就是唯一可行中位數
        median_value = numbers[data_count // 2]

        # 統計該中位數在原資料中出現幾次
        median_count = 0
        for value in numbers:
            if value == median_value:
                median_count += 1

        # 奇數筆時，可行中位數只有一個
        median_range_count = 1

        return median_value, median_count, median_range_count

    # 若為偶數筆資料
    # 找出排序後中間兩個值
    low = numbers[data_count // 2 - 1]
    high = numbers[data_count // 2]

    # 統計原資料中有多少數值落在 [low, high] 範圍內
    median_count = 0
    for value in numbers:
        if low <= value <= high:
            median_count += 1

    # 可作為中位數的整數個數為 high - low + 1
    median_range_count = high - low + 1

    # 最小可行中位數為 low
    return low, median_count, median_range_count


def solve():
    """
    依照 UVA 題目的輸入格式讀取資料並輸出答案。

    注意：
    本題沒有先給測試資料組數，
    會重複輸入多組資料直到 EOF 為止。
    """

    try:
        while True:
            # 讀入資料筆數
            line = input().strip()

            # 若遇到空行，則跳過不處理
            if not line:
                continue

            data_count = int(line)

            # 依照資料筆數讀入所有整數
            numbers = []
            for _ in range(data_count):
                numbers.append(int(input().strip()))

            # 呼叫函式計算答案
            answer_value, answer_count, answer_range = find_median_info(numbers)

            # 依題目要求輸出三個結果
            print(answer_value, answer_count, answer_range)

    except EOFError:
        # 當讀到輸入結束時，正常結束程式
        pass


# 程式進入點
if __name__ == "__main__":
    solve()