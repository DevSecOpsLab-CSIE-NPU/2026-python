import sys

# 罷工天數統計程式 - 大一輕鬆版
# 我們要幫組織算算看，這 N 天裡面到底有多少天因為政黨罷工而沒辦法上班

def main():
    # 先讀取所有的資料
    input_text = sys.stdin.read().split()
    if not input_text:
        return

    # 第一個數字是測資組數
    total_test_cases = int(input_text[0])
    current = 1

    for _ in range(total_test_cases):
        # 讀取模擬總天數
        n_days = int(input_text[current])
        # 讀取政黨數量
        num_parties = int(input_text[current + 1])
        current += 2

        # 讀取每個政黨的罷會週期（hartal 參數）
        party_params = []
        for i in range(num_parties):
            party_params.append(int(input_text[current]))
            current += 1

        # 我們準備一個計數器，來記錄總共損失了幾天
        total_lost_days = 0

        # 從第 1 天開始檢查到第 N 天
        for day in range(1, n_days + 1):
            # 規則 1：星期五和星期六不罷工
            # 根據題目，第 1 天是星期日
            # 星期五是第 6, 13, 20... 天 -> day % 7 == 6
            # 星期六是第 7, 14, 21... 天 -> day % 7 == 0
            if day % 7 == 6 or day % 7 == 0:
                continue

            # 規則 2：如果這一天是任何一個政黨的罷工日，這天就損失了
            # 我們只要看到一個政黨罷工，這天就跳過檢查下一個政黨
            is_hartal_day = False
            for p in party_params:
                if day % p == 0:
                    is_hartal_day = True
                    break # 只要有一黨罷工就算數了，不用再看別黨

            # 如果確定是罷工日，就把計數器加 1
            if is_hartal_day:
                total_lost_days += 1

        # 印出最後的結果
        print(total_lost_days)

if __name__ == "__main__":
    main()
