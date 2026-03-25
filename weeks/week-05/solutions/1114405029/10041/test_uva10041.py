"""
UVA 10041 - Vito's Family
測試程式版本

用途說明：
這份程式主要用來做本地測試。
程式將核心計算邏輯獨立成函式，
方便檢查答案是否正確，也方便後續維護與除錯。
"""


def minimum_total_distance(addresses):
    """
    計算所有親戚到最佳住址的最小總距離。

    參數：
        addresses (list[int])：親戚居住的街道號碼列表

    回傳：
        int：最小總距離

    解題觀念：
        若要讓一組數字到某個位置的絕對距離總和最小，
        最佳位置就是中位數（median）。
        因此先將地址排序，再取中位數，
        最後計算所有地址到中位數的距離總和即可。
    """

    # 將地址排序後存成新串列
    # 這裡使用 sorted()，不會直接改到原本傳入的 addresses
    sorted_addresses = sorted(addresses)

    # 取排序後的中位數位置
    # 若資料筆數為奇數，中位數唯一
    # 若資料筆數為偶數，取中間兩個位置之一即可得到最小總距離
    # 這裡直接取索引 len(sorted_addresses) // 2 的元素
    median_address = sorted_addresses[len(sorted_addresses) // 2]

    # 累加所有親戚到中位數的距離
    total_distance = 0
    for address in sorted_addresses:
        total_distance += abs(address - median_address)

    # 回傳最小總距離
    return total_distance


def solve():
    """
    依照 UVA 題目的輸入格式讀取資料並輸出答案。
    """

    # 讀入測試資料組數
    test_case_count = int(input().strip())

    # 逐組處理每一筆測試資料
    for _ in range(test_case_count):
        # 讀入一整行整數資料
        # 格式為：
        # r a1 a2 a3 ... ar
        data = list(map(int, input().split()))

        # 第一個數字代表親戚人數
        relative_count = data[0]

        # 後面 relative_count 個數字才是真正的地址資料
        addresses = data[1:1 + relative_count]

        # 呼叫函式計算最小總距離
        answer = minimum_total_distance(addresses)

        # 輸出答案
        print(answer)


# 程式進入點
if __name__ == "__main__":
    solve()