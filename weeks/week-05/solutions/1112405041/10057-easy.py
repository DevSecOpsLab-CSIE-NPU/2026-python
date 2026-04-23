import sys

# 仲夏夜之夢（中位數問題）- 大一入門版
# 我們要找一個數字 A，讓它到所有數字的距離總和最小

def main():
    # 讀取輸入
    # 因為這題是多組測資，且 n 的位置可能不固定，我們用 split() 拿走所有字串
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    current_idx = 0
    # 只要還有資料就繼續跑
    while current_idx < len(input_data):
        # 讀取這組資料有多少個數字
        n = int(input_data[current_idx])
        current_idx += 1

        # 讀取這 n 個數字並存進清單
        numbers = []
        for _ in range(n):
            numbers.append(int(input_data[current_idx]))
            current_idx += 1

        # 1. 為了找中位數，我們先排序
        numbers.sort()

        # 2. 找出中位數
        # 如果 n 是奇數，只有一個中位數
        # 如果 n 是偶數，中間有兩個數字都是中位數候選
        # 我們取這兩個中間位置的索引
        mid1_idx = (n - 1) // 2
        mid2_idx = n // 2

        m1 = numbers[mid1_idx]
        m2 = numbers[mid2_idx]

        # 3. 題目要求輸出三個數字：
        # (1) 最小的中位數 (m1)
        # (2) 在輸入的數字中，有多少個數字等於 m1 或等於 m2 (或是介於中間)
        #     根據數學原理，只要 Xi 等於 m1 或 m2，它就是符合條件的點
        count_in_input = 0
        for x in numbers:
            if x == m1 or x == m2:
                count_in_input += 1

        # (3) 有多少種可能的整數 A 可以讓距離總和最小
        # 答案就是 m2 - m1 + 1 (這區間內的整數都可以)
        possible_a_count = m2 - m1 + 1

        # 印出結果
        print("{} {} {}".format(m1, count_in_input, possible_a_count))

if __name__ == "__main__":
    main()
