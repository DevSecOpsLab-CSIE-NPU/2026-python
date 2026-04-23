import sys

# 乳牛排序 - 大一最基礎版
# 題目邏輯：我們知道每頭牛前面有多少頭牛比它編號小。
# 最簡單的作法是從最後一頭牛開始推算，因為最後一頭牛前面有多少比它小的，
# 就能直接決定它是「剩下還沒被挑走的編號中」的第幾個。

def main():
    # 讀取所有輸入
    data = sys.stdin.read().split()
    if not data:
        return

    # 第一個數字是牛的總數 N
    n = int(data[0])

    # 後面的數字是從第 2 頭牛到第 N 頭牛的「前面比它小」的數量
    # 第 1 頭牛前面一定是 0，所以我們手動加上去
    counts = [0]
    for i in range(1, n):
        counts.append(int(data[i]))

    # 我們建立一個清單，存放所有可用的編號 1 到 N
    available_numbers = []
    for i in range(1, n + 1):
        available_numbers.append(i)

    # 建立一個結果清單，用來存放最後排好的牛編號
    results = [0] * n

    # 關鍵邏輯：從最後一頭牛（索引 n-1）往回推算到第一頭牛
    for i in range(n - 1, -1, -1):
        # 題目說「前面有 k 個比它小」，表示它是目前剩下數字中「第 k+1 小」的
        # 因為程式的清單索引是從 0 開始，所以直接拿 counts[i] 當索引就好
        k = counts[i]

        # 從可用編號清單中取出對應位置的編號
        chosen_number = available_numbers.pop(k)

        # 放入結果中
        results[i] = chosen_number

    # 最後依照順序印出結果
    for num in results:
        print(num)

if __name__ == "__main__":
    main()
