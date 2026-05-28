# UVA 12019 — Doom's Day Algorithm（AI 簡單版）
# 用 Conway 的 Doomsday 演算法計算 2012 年任意日期是星期幾
#
# 核心原理：
#   每年有一組「Doomsday 日期」，這些日期全部落在同一個星期幾。
#   2012 年是閏年，Doomsday 是「星期三」。
#   只要算出給定日期與該月 Doomsday 的天數差，就能推算出星期幾。

# 2012 年（閏年）每月的 Doomsday 日期（這些日期全部是星期三）
DOOMSDAY = [4, 29, 7, 4, 9, 6, 11, 8, 5, 10, 7, 12]
#          Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec

# 星期名稱（Monday=0, Tuesday=1, ..., Sunday=6）
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

T = int(input())
for _ in range(T):
    m, d = map(int, input().split())
    # 計算目標日期與 Doomsday 的差距（可能為負，% 7 自動處理）
    diff = d - DOOMSDAY[m - 1]
    # 星期三的 index 是 2，加上差距再取模
    day_index = (2 + diff) % 7
    print(DAYS[day_index])
