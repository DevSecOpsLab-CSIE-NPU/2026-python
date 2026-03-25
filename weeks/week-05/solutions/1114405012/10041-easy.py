import sys

# 題目：UVA 10041 - Vito's Family
# 目標：找一個門牌位置，讓到所有親戚門牌的距離總和最小。
#
# 核心觀念：
# 在一維數線上，若要最小化「絕對距離總和」，最佳位置是「中位數」。
# 因此每組測資只要排序後取中位數，再加總到中位數的距離即可。

# 1) 一次讀完整份輸入，並全部轉成整數。
#    使用 split() 可同時處理空白與換行。
nums = list(map(int, sys.stdin.read().split()))

# 若沒有任何輸入資料，直接結束程式。
if not nums:
    raise SystemExit

# 2) 第一個數字 t 代表有幾組測資。
t = nums[0]

# idx 是「讀取指標」，用來追蹤目前讀到 nums 的哪個位置。
idx = 1

# answers 用來收集每組測資的答案，最後一次輸出。
answers = []

for _ in range(t):
    # 3) 讀取本組資料：
    #    r = 親戚數量
    #    接著有 r 個整數是親戚門牌
    r = nums[idx]
    idx += 1

    # 切片取出本組的 r 個門牌
    addresses = nums[idx:idx + r]
    idx += r

    # 4) 排序後取中位數（最小總距離的關鍵步驟）
    #    - 若 r 為奇數：中間那個值就是唯一中位數
    #    - 若 r 為偶數：中間兩個值都可達最小總距離
    #      這裡取 addresses[r // 2] 即可（任取其一都正確）
    addresses.sort()
    median = addresses[r // 2]

    # 5) 計算本組最小總距離：
    #    sum(|x - median|) for x in addresses
    total = sum(abs(x - median) for x in addresses)
    answers.append(str(total))

# 6) 依題目要求，每組答案輸出一行。
print("\n".join(answers))
