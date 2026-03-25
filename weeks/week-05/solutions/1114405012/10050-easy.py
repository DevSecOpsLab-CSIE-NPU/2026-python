import sys

# 題目：UVA 10050 - Hartals（罷工日）
# 目標：計算 N 天內，因政黨罷工而損失的「工作天」數量。
# 注意：每週星期五、星期六是假日，不算損失工作天。

# 1) 一次讀入全部資料，並轉成整數串列。
#    split() 會自動處理空白與換行分隔。
nums = list(map(int, sys.stdin.read().split()))

# 若沒有輸入，直接結束。
if not nums:
    raise SystemExit

# 2) 第一個數字是測資組數 T。
t = nums[0]

# idx 是讀取指標：代表目前讀到 nums 的哪個位置。
idx = 1

# ans 用來收集每組測資的答案，最後一次輸出。
ans = []

for _ in range(t):
    # 3) 讀取本組測資：
    #    n = 模擬天數
    #    p = 政黨數量
    n = nums[idx]
    idx += 1
    p = nums[idx]
    idx += 1

    # 4) 讀取 p 個政黨參數 h（每 h 天罷工一次）
    hs = nums[idx:idx + p]
    idx += p

    # 5) 用集合記錄損失工作天：
    #    若多個政黨在同一天罷工，集合只會保留一次，不會重複計數。
    lost = set()

    for h in hs:
        # 該政黨的罷工日：h, 2h, 3h, ...
        for day in range(h, n + 1, h):
            # 6) 依題意排除假日：
            #    第 1 天是星期天，因此：
            #    day % 7 == 6 -> 星期五
            #    day % 7 == 0 -> 星期六
            #    這兩天不算工作天，不能列入損失。
            if day % 7 in (6, 0):
                continue

            # 工作日發生罷工，加入損失日集合。
            lost.add(day)

    # 7) 本組答案 = 損失工作天總數。
    ans.append(str(len(lost)))

# 8) 依題目格式輸出：每組答案一行。
print("\n".join(ans))
