import sys

# 詳細繁體中文註解說明：
# 這題的規律是：
# 人數 S 的團住 S 天
# 人數 S+1 的團住 S+1 天
# 我們只要把天數一直扣掉，扣到變 0 或負數的時候，
# 當時的人數就是答案。
# 雖然天數 D 很大，但因為人數也會變大，所以迴圈次數並不會到 10^15 次那麼多。

def solve():
    # 讀取標準輸入的每一行
    for line in sys.stdin:
        # 將讀入的字串轉成數字 S 和 D
        try:
            parts = line.split()
            if not parts:
                break
            
            s = int(parts[0])
            d = int(parts[1])
            
            current_people = s
            # 當 d 還大於 0 的時候，表示我們還沒走到目標天數
            while d > 0:
                # 扣掉當前這一團會住的天數
                d -= current_people
                
                # 如果扣完後 d <= 0，表示第 D 天就在這一團的住宿期間內
                if d <= 0:
                    print(current_people)
                    break
                
                # 換下一團，人數加 1
                current_people += 1
                
        except EOFError:
            break

if __name__ == "__main__":
    solve()