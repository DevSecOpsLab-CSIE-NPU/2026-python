import sys


def solve(data: bytes) -> str:
    nums = list(map(int, data.split()))
    p = 0
    ans = []

    while p < len(nums):
        n = nums[p]
        p += 1
        if p + n > len(nums):
            break

        values = nums[p:p + n]
        p += n
        values.sort()

        # 絕對值總和最小時，A 一定落在中位數區間。
        # n 為奇數：只有一個中位數。
        # n 為偶數：介於兩個中位數之間的整數都可達最小值。
        left_mid = values[(n - 1) // 2]
        right_mid = values[n // 2]

        # 第二個輸出：有多少個 Xi 落在 [left_mid, right_mid]。
        # 這些值都可以當作達最小值時的代表數。
        cnt = 0
        for x in values:
            if left_mid <= x <= right_mid:
                cnt += 1

        # 第三個輸出：可行的 A 有幾種整數值。
        ways = right_mid - left_mid + 1

        # 第一個輸出慣例取 left_mid。
        ans.append(f"{left_mid} {cnt} {ways}")

    return "\n".join(ans)


if __name__ == "__main__":
    print(solve(sys.stdin.buffer.read()))
