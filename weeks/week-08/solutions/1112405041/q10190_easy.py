import sys

# 自動傘雨水計算 - 大一小萌新版
# 我們要計算在 T 秒內，有多少雨水會落在人行道上
# 邏輯：先算總共會下多少雨，再扣掉被自動傘擋住（吸走）的雨

def main():
    # 讀取輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # N: 傘的數量, W: 馬路寬度, T: 時間, V: 雨量率
    num_umbrellas = int(input_data[0])
    road_width = int(input_data[1])
    total_time = int(input_data[2])
    rain_rate = int(input_data[3])

    # 1. 先計算如果完全沒有傘，馬路上會有多少雨
    # 體積 = 寬度 * 時間 * 雨量率 (假設人行道長度為單位 1)
    max_rain = road_width * total_time * rain_rate

    # 2. 計算所有傘總共擋住了多少雨
    total_absorbed = 0

    current_idx = 4
    for i in range(num_umbrellas):
        # x: 初始位置, l: 傘的長度, v: 速度
        x = int(input_data[current_idx])
        length = int(input_data[current_idx + 1])
        velocity = int(input_data[current_idx + 2])
        current_idx += 3

        # 關鍵邏輯：不管傘怎麼移動，只要它還在馬路上，
        # 它的長度 L 在每一秒鐘都會擋住 L 單位的雨。
        # 所以 T 秒鐘就會擋住 L * T * rain_rate 的雨量。
        absorbed_by_this_one = length * total_time * rain_rate
        total_absorbed += absorbed_by_this_one

    # 3. 馬路上的雨 = 總雨量 - 被傘擋住的雨
    final_rain = max_rain - total_absorbed

    # 如果傘太多把雨都擋完了，雨量就不會是負的，最小是 0
    if final_rain < 0:
        final_rain = 0.0

    # 印出結果，並保留小數點後兩位
    print("{:.2f}".format(final_rain))

if __name__ == "__main__":
    main()
