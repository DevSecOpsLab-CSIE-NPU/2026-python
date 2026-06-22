import time


def binary_search_perf(data: list, target) -> tuple[bool, int, int]:
    """二分搜尋並計算比較次數：
    回傳 (是否找到, index, 比較次數)
    """
    low = 0
    high = len(data) - 1
    cmp_count = 0

    while low <= high:
        mid = (low + high) // 2
        cmp_count += 1
        if data[mid] == target:
            return True, mid, cmp_count
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False, -1, cmp_count


def linear_search_perf(data: list, target) -> tuple[bool, int, int]:
    """線性搜尋並計算比較次數：
    回傳 (是否找到, index, 比較次數)
    """
    cmp_count = 0
    for i in range(len(data)):
        cmp_count += 1
        if data[i] == target:
            return True, i, cmp_count
    return False, -1, cmp_count


if __name__ == "__main__":
    # 產生大型升冪排序數列（規模大於 10^5）
    # 大小為 100,000，皆為偶數
    data = list(range(0, 200000, 2))
    # 搜尋目標 K = 120 (學號末兩碼 20 -> K = 120)
    target = 120

    # 執行二分搜尋並回報比較次數與 index
    found, idx, cmp_binary = binary_search_perf(data, target)

    if found:
        print(f"FOUND {idx} cmp={cmp_binary}")
    else:
        print(f"NOT FOUND cmp={cmp_binary}")

    # 用時間量測線性搜尋的總耗時
    start_lin = time.perf_counter()
    linear_search_perf(data, target)
    end_lin = time.perf_counter()
    t_linear = end_lin - start_lin

    # 用時間量測二分搜尋的總耗時
    start_bin = time.perf_counter()
    binary_search_perf(data, target)
    end_bin = time.perf_counter()
    t_binary = end_bin - start_bin

    # 輸出耗時結果與結論
    print(f"linear : {t_linear:.6f} s")
    print(f"binary : {t_binary:.6f} s")

    if t_binary < t_linear:
        print("=> binary faster")
    else:
        print("=> linear faster")
