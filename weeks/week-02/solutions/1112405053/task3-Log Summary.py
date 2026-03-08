# 從 collections 模組匯入 Counter
# Counter 是一種專門用來「統計次數」的資料結構
from collections import Counter

# 匯入 sys
import sys


# 讀取第一行輸入：紀錄總數 m
# 例如輸入 8，代表後面會有 8 行 user action 紀錄
m = int(input())


# 建立一個 Counter 用來統計「每個使用者出現幾次」
# 例如：alice 3 次、bob 4 次
user_count = Counter()

# 建立另一個 Counter 用來統計「每種 action 出現幾次」
# 例如：login 3 次、view 3 次
action_count = Counter()


# 迴圈讀取 m 行資料
for _ in range(m):

    # 讀取一行輸入並用空白切割
    # 例如輸入： alice login
    # split() 之後會變成 ["alice", "login"]
    user, action = input().split()

    # 統計使用者出現次數
    # 如果 user 第一次出現，Counter 會自動從 0 開始
    user_count[user] += 1

    # 統計 action 出現次數
    action_count[action] += 1


# 將 user_count 轉成 list 並排序
# user_count.items() 會變成：
# [('alice',3), ('bob',4), ('chris',1)]

# 排序規則：
# 1️⃣ 先按照次數由大到小排序 → -x[1]
# 2️⃣ 如果次數相同 → 按 user 名稱字母排序 → x[0]
result = sorted(user_count.items(), key=lambda x: (-x[1], x[0]))


# 輸出排序後的結果
# 例如：
# bob 4
# alice 3
# chris 1
for user, count in result:
    print(user, count)


# 如果 action_count 不是空的（代表有資料）
if action_count:

    # most_common(1) 會找出出現最多次的 action
    # 回傳格式：[('login',3)]
    action, count = action_count.most_common(1)[0]

    # 輸出最常見的 action
    # 例如：
    # top_action: login 3
    print(f"top_action: {action} {count}")