import sys

# 機率計算 - 大一最基礎版
# 我們要計算在 N 個玩家中，第 i 個玩家獲勝的機率

def main():
    # 讀取輸入
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # 第一個數字是測試組數
    num_tests = int(input_data[0])
    current_idx = 1

    for _ in range(num_tests):
        # 玩家人數 N
        n = int(input_data[current_idx])
        # 成功機率 p
        p = float(input_data[current_idx + 1])
        # 目標玩家序號 i
        i = int(input_data[current_idx + 2])
        current_idx += 3

        # 特殊情況：如果成功機率是 0，那誰都不會贏，機率就是 0
        if p == 0:
            print("0.0000")
            continue

        # 失敗機率 q = 1 - p
        q = 1.0 - p

        # 根據無窮等比級數公式：
        # 第 i 個玩家第一次就贏的機率是 p * q^(i-1)
        # 所有人輪完一圈都沒贏的機率是 q^n
        # 最終勝率 = (第一次就贏的機率) / (1 - 所有人輪完一圈都沒贏的機率)
        # 公式： [p * q^(i-1)] / [1 - q^n]

        numerator = p * (q ** (i - 1))
        denominator = 1.0 - (q ** n)

        result = numerator / denominator

        # 印出結果，並強制保留四位小數
        # 加入 1e-9 是為了防止浮點數精準度導致四捨五入出錯（資工系的小技巧！）
        print("{:.4f}".format(result + 1e-9))

if __name__ == "__main__":
    main()
