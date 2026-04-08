import sys


def answer_easy(s, d):
    """回傳第 d 天入住的旅行團人數（簡單好記版）。

    參數:
    - s: 起始旅行團人數（第一個入住的團）
    - d: 查詢第幾天

    核心想法：
    1. s 人團住 s 天，s+1 人團住 s+1 天，依此類推。
    2. 假設第 d 天屬於 n 人團，則從 s 到 n 的總天數需 >= d。
    """

    # 目標是找最小 n，使：
    #   (1+2+...+n) - (1+2+...+(s-1)) >= d
    # 也就是：
    #   n(n+1)/2 >= d + s(s-1)/2
    need = d + s * (s - 1) // 2

    # 用二分搜尋找「最小可行 n」。
    # left 從 s 開始（答案不可能小於起始團人數），
    # right 給一個足夠大的上界即可。
    left, right = s, 2_000_000_000
    while left < right:
        mid = (left + right) // 2

        # total = 1+2+...+mid
        total = mid * (mid + 1) // 2
        if total >= need:
            # mid 已可行，嘗試往更小的答案收斂
            right = mid
        else:
            # mid 不足，答案一定在右半邊
            left = mid + 1

    # 迴圈結束時 left == right，即最小可行 n
    return left


def solve(text):
    """處理整段輸入文字（多筆測資直到 EOF），回傳多行答案字串。"""

    # split 可同時處理空白與換行，適合 OJ 格式
    nums = [int(x) for x in text.split()]
    out = []

    # 題目輸入是多行，每行一組 (S, D)
    for i in range(0, len(nums) - 1, 2):
        s, d = nums[i], nums[i + 1]
        out.append(str(answer_easy(s, d)))

    # 每筆測資輸出一行
    return "\n".join(out)


def main():
    """競賽入口：從標準輸入讀取，輸出答案。"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
