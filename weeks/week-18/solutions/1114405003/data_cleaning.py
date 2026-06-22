"""
第一題 資料清理 (Data Cleaning)
學號: 1114405003
D = 5 (個位 3 % 4 + 2 = 5)

步驟：
1. 去除重複 (保留第一次出現的順序)
2. 只保留能被 D 整除的數
3. 由小到大排序
"""


def clean_data(nums: list[int], d: int) -> list[int]:
    """
    資料清理函式

    Args:
        nums: 整數數列
        d: 整除數

    Returns:
        清理後的數列 (去重 -> 篩選 -> 排序)
    """
    # 步驟1: 去除重複 (保留第一次出現的順序)
    seen = set()
    unique_nums = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            unique_nums.append(num)

    # 步驟2: 只保留能被 D 整除的數
    filtered = [num for num in unique_nums if num % d == 0]

    # 步驟3: 由小到大排序
    filtered.sort()

    return filtered


def main():
    """主程式：讀取多組測資並輸出結果"""
    results = []

    while True:
        try:
            line = input().strip()
            if not line:
                continue

            n = int(line)
            if n == 0:
                break

            nums = list(map(int, input().split()))
            D = 5  # 學號 1114405003, 個位 3 % 4 + 2 = 5

            cleaned = clean_data(nums, D)

            if cleaned:
                results.append(" ".join(map(str, cleaned)))
            else:
                results.append("NONE")

        except EOFError:
            break

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
