import sys

def solve():
    # 使用 sys.stdin 讀取輸入，直到遇到 EOF (檔案結尾)
    # 這是處理 UVA 或 ZeroJudge 多筆測資的標準寫法
    for line in sys.stdin:
        try:
            # 將讀入的一行字串切分，並轉換為整數 S (起始人數) 與 D (目標天數)
            parts = line.split()
            if not parts:
                continue
            
            S = int(parts[0])
            D = int(parts[1])
            
            # current_day_total: 用來記錄目前所有旅行團總共住過的累計天數
            # current_group_size: 目前正在住宿的旅行團人數
            current_day_total = 0
            current_group_size = S
            
            # 開始模擬旅行團入住的過程
            while True:
                # 根據規則：人數為 n 的團體會住 n 天
                # 所以我們直接將當前團體的人數加進「累計天數」中
                current_day_total += current_group_size
                
                # 檢查目前的累計天數是否已經涵蓋了我們要找的第 D 天
                if current_day_total >= D:
                    # 如果當前累計天數大於或等於 D，代表第 D 天就發生在這一團住宿期間
                    print(current_group_size)
                    break
                
                # 如果還沒到第 D 天，下一團的人數會比這一團多 1 人
                current_group_size += 1
                
        except EOFError:
            # 碰到檔案結尾，安全退出
            break

if __name__ == "__main__":
    solve()
