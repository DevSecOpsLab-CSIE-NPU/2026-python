# UVA 12019 — Doom's Day Algorithm（手打版）
# 計算 2012 年任意日期是星期幾
# 2012 年各月 Doomsday 日期（皆為星期三，2012 是閏年）

DOOMSDAY = [4, 29, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
#          Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

T = int(input())  # 讀取測試組數
for _ in range(T):
    m, d = map(int, input().split())
    # 星期三 = index 2；計算與 Doomsday 的天數差後取模 7
    day_index = (2 + d - DOOMSDAY[m - 1]) % 7
    print(DAYS[day_index])
