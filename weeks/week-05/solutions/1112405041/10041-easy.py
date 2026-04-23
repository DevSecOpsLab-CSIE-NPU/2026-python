import sys

# 這是一個專門為大一新鮮人設計的簡單版本
# 我們會使用最基礎的迴圈與清單來解決 Vito 老大的問題

def main():
    # 讀取所有的輸入內容並將它們切割成一個一個的字串
    # 這樣我們就可以一個一個處理數字了
    input_data = sys.stdin.read().split()

    # 如果完全沒有資料，就直接結束程式
    if not input_data:
        return

    # 第一個數字代表總共有多少組測試資料
    test_cases_count = int(input_data[0])

    # 用一個變數來追蹤我們目前讀取到 input_data 的哪個位置
    current_index = 1

    # 針對每一組測試資料進行處理
    for _ in range(test_cases_count):
        # 第一個數字是親戚的數量
        relatives_count = int(input_data[current_index])
        current_index += 1

        # 接下來的 relatives_count 個數字是親戚們的門牌號碼
        # 我們把這些號碼存進一個清單（陣列）裡面
        house_numbers = []
        for i in range(relatives_count):
            house_numbers.append(int(input_data[current_index]))
            current_index += 1

        # 為了找出距離所有親戚最近的位置，最簡單的邏輯就是找出門牌的中位數
        # 首先我們必須先把門牌號碼從小到大排好
        house_numbers.sort()

        # 找出中間位置的門牌（這就是 Vito 老大應該住的地方）
        # 使用整數除法 // 來取得中間的索引
        median_index = relatives_count // 2
        vito_house = house_numbers[median_index]

        # 接下來計算 Vito 的新家到所有親戚家的距離總和
        total_distance = 0
        for number in house_numbers:
            # 計算距離（絕對值），並累加到總和中
            distance = number - vito_house
            if distance < 0:
                distance = -distance
            total_distance += distance

        # 最後將結果印出到螢幕上
        print(total_distance)

# 執行主程式
if __name__ == "__main__":
    main()
