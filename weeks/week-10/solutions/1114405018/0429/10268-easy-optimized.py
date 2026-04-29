import sys


def solve(text):
    """解題主函式（優化版）。

    優化策略：
    1. 使用二分查找找最小試驗次數，而非線性掃描
    2. 提前計算 dp 值，用組合數學加速
    3. 使用更優的邊界檢查
    """
    vals = list(map(int, text.split()))
    if not vals:
        return ""

    it = iter(vals)
    out = []

    while True:
        k = next(it)
        n = next(it)
        if k == 0:
            break

        # ========== 方法 1：使用數學公式計算 ==========
        # 對於 t 次試驗和 k 顆水球，最多能判定的樓層數為：
        # sum(C(t, 1) + C(t, 2) + ... + C(t, min(t, k)))
        # 這等於 sum(C(t, i) for i in range(1, min(t, k) + 1))
        
        def max_floors(t, k):
            """計算 t 次試驗 k 顆水球最多能判定的樓層數"""
            # 使用帕斯卡三角計算組合數
            result = 0
            comb = 1  # C(t, 0)
            
            for i in range(1, min(t, k) + 1):
                # C(t, i) = C(t, i-1) * (t - i + 1) / i
                comb = comb * (t - i + 1) // i
                result += comb
                
                # 提前退出：如果已經超過 n，後續不需計算
                if result >= n:
                    return result
            
            return result

        # ========== 二分查找最小試驗次數 ==========
        # 利用 max_floors(t, k) 單調遞增的性質
        left, right = 1, 63
        ans = "More than 63 trials needed."

        while left <= right:
            mid = (left + right) // 2
            floors = max_floors(mid, k)
            
            if floors >= n:
                # mid 次試驗足夠，嘗試更少的次數
                ans = str(mid)
                right = mid - 1
            else:
                # mid 次試驗不足，需要更多次數
                left = mid + 1

        out.append(ans)

    return "\n".join(out) + "\n"


def main():
    """讀取標準輸入，交給 solve 後直接輸出"""
    sys.stdout.write(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
