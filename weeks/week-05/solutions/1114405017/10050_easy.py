def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = int(input())
        
        # 1. 用集合記錄所有發生罷會的日子（自動處理重複）
        all_hartals = set()
        for _ in range(P):
            h = int(input())
            # range(start, stop, step) 直接幫你算好倍數
            all_hartals.update(range(h, N + 1, h))
        
        # 2. 用列表推導式過濾掉週五 (6) 和 週六 (0)
        # 剩下的元素個數就是答案
        lost_days = [day for day in all_hartals 
                     if day % 7 != 6 and day % 7 != 0]
        
        print(len(lost_days))

# 執行時記得處理可能的空白行或輸入結束
if __name__ == "__main__":
    solve()