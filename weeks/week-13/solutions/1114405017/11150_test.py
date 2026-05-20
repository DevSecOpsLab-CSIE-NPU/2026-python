import io
import sys

# 這裡放入你剛剛寫好的解題邏輯（將原本的 print 改為 return 或捕捉輸出）
# 為了測試方便，我們讓 solve 接受輸入字串，並回傳結果


def solve(input_string):
    data = list(map(int, input_string.split()))
    if not data:
        return 0

    L, S, T, M = data[0], data[1], data[2], data[3]
    stones = sorted(data[4 : 4 + M])

    if S == T:
        return sum(1 for x in stones if x % S == 0)

    pos = [0] + stones + [L]
    new_stones = set()
    curr = 0

    for i in range(1, len(pos)):
        diff = pos[i] - pos[i - 1]
        curr += min(diff, 90)
        if i < len(pos) - 1:
            new_stones.add(curr)

    new_L = curr
    dp = [0] + [float("inf")] * (new_L + T)

    for i in range(1, new_L + T + 1):
        # 預防切片索引變成負數，與 0 取 max
        start = max(0, i - T)
        end = max(0, i - S + 1)

        if start >= end:  # 如果找不到合法的上一步
            dp[i] = float("inf")
        else:
            dp[i] = min(dp[start:end]) + (1 if i in new_stones else 0)

    return min(dp[new_L : new_L + T + 1])


# ==============================================================================
# 自動化測試測試程式
# ==============================================================================
def run_tests():
    # 定義測試用例：(測試名稱, 輸入資料, 預期輸出)
    test_cases = [
        (
            "範例測試 1 (基本動態規劃)",
            """10
             2 3 5
             2 3 5 6 7""",
            2,
        ),
        (
            "範例測試 2 (步長固定特判)",
            """10
             3 3 2
             3 5""",
            1,  # 只有 3 是 3 的倍數，5 不是
        ),
        (
            "範例測試 3 (超長距離壓縮)",
            """1000000000
             2 3 1
             500000000""",
            0,  # 只有一顆石子且步長靈活，可以完美避開
        ),
        (
            "範例測試 4 (多顆極遠石子)",
            """1000000000
             2 3 3
             100 500000 999999900""",
            0,
        ),
        (
            "範例測試 5 (起點周圍密集石子)",
            """20
             2 3 4
             1 2 3 4""",
            1,  # 踩到 2 或 3
        ),
    ]

    print("開始執行自動化測試...\n" + "-" * 40)

    passed_count = 0
    for name, input_data, expected in test_cases:
        # 執行程式並取得答案
        actual = solve(input_data)

        # 比對結果
        if actual == expected:
            print(f"✅ [{name}] 通過！")
            passed_count += 1
        else:
            print(f"❌ [{name}] 失敗！")
            print(f"   預期輸出: {expected}")
            print(f"   實際輸出: {actual}")

    print("-" * 40)
    print(f"測試結束：總共 {len(test_cases)} 個測試，通過 {passed_count} 個。")


if __name__ == "__main__":
    run_tests()