import sys

# 無限旅館問題 - 大一入門版
# 規則：
# 第一天有 S 人，住 S 天。
# 接下來變 S+1 人，住 S+1 天。
# 我們要找第 D 天時，住的是幾個人的團。

def main():
    # 讀取所有輸入
    lines = sys.stdin.readlines()

    for line in lines:
        parts = line.split()
        if not parts: continue

        s = int(parts[0]) # 起始人數
        d = int(parts[1]) # 目標天數

        # 我們用一個變數 current_days 來累計目前過了好幾天
        current_days = 0
        current_group_size = s

        # 只要累計天數還沒到達目標天數 D，就繼續下一個團
        # 邏輯：
        # 第 1 團住 s 天
        # 第 2 團住 s+1 天
        # ...
        # 這裡我們可以用數學公式優化，但為了「好懂」，我們用 while 迴圈
        while current_days < d:
            current_days += current_group_size
            if current_days >= d:
                # 找到了！目前這一團的人數就是答案
                print(current_group_size)
                break
            current_group_size += 1

if __name__ == "__main__":
    main()
