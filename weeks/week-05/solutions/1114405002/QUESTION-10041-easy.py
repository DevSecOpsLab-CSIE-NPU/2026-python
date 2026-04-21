import sys


def solve(data: bytes) -> str:
    # 把所有輸入一次讀完並切成整數，方便逐一取用。
    nums = list(map(int, data.split()))
    if not nums:
        return ""

    # 第一個數字是測資組數。
    t = nums[0]
    idx = 1
    ans = []

    for _ in range(t):
        # 每組先讀親戚數量 r，再讀 r 個門牌。
        r = nums[idx]
        idx += 1
        homes = nums[idx:idx + r]
        idx += r

        # 關鍵：把房子位置排序後，選中位數位置當新家，
        # 會讓「到所有親戚的距離總和」最小。
        homes.sort()
        best = homes[r // 2]

        # 計算所有親戚到 best 的距離總和。
        total = 0
        for h in homes:
            total += abs(h - best)

        ans.append(str(total))

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
