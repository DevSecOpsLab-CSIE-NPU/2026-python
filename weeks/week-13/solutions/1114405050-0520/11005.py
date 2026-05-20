import sys

def get_cheapest_bases(costs, number):
    """
    計算指定數字在 2 到 36 進位制中的印刷成本，並回傳成本最低的進位制列表。
    
    參數:
    costs (list): 一個長度為 36 的串列，儲存 0~9 與 A~Z 的對應印刷成本。
    number (int): 欲計算成本的十進位整數。
    """
    # 特例處理：當數字為 0 時，無論在哪種進位制下，印出來的結果都是 '0'。
    # 既然輸出的字元都只有一個 '0'，那麼每個進位制的成本都會相同（皆為 costs[0]），
    # 也就是全部都是最低成本。因此直接回傳 2 到 36 的所有進位制。
    if number == 0:
        return list(range(2, 37))

    min_cost = float('inf')  # 將初始最低成本設定為無限大，確保後續任何計算出來的成本都能順利取代它
    best_bases = []          # 用來儲存符合目前「最低成本」的所有進位制

    # 遍歷從 2 進位到 36 進位（range 的結尾不包含 37，所以會執行到 36）
    for base in range(2, 37):
        current_cost = 0  # 紀錄在目前進位制 (base) 下的總印刷成本
        temp = number     # 用一個暫存變數來做除法，避免破壞原始的 number
        
        # 使用「短除法」的概念將十進位數字轉換成特定進位制
        while temp > 0:
            digit = temp % base           # 取餘數，取得目前最低位的數值 (即代表該位數對應哪個字元)
            current_cost += costs[digit]  # 將該字元對應的成本累加到總成本中
            temp //= base                 # 將數字整除進位制，繼續處理下一個較高位數字

        # 檢查剛計算完的這個進位制成本，是不是目前為止最低的
        if current_cost < min_cost:
            min_cost = current_cost       # 更新最低成本的紀錄
            best_bases = [base]           # 因為找到了更低的成本，所以清空之前的紀錄，只留下這一個進位制
        elif current_cost == min_cost:
            best_bases.append(base)       # 如果成本和目前的最低成本一樣，代表有並列最低的狀況，加入清單中

    return best_bases

def main():
    # 一次性讀取所有的標準輸入 (包含多行資料)，並利用空白或換行符號將所有資料切割成一個一維的字串串列。
    # 這樣的做法在處理 CPE 這種輸入格式可能夾雜多個空白或不規則換行的題目時，非常方便且穩定。
    input_data = sys.stdin.read().split()
    if not input_data:
        return  # 如果沒有輸入資料，直接結束程式
    
    # 讀取第一筆資料：測試資料的總組數
    num_cases = int(input_data[0])
    idx = 1  # 建立一個索引指標，用來記錄目前讀取到 input_data 的哪一個位置
    
    # 依序處理每一組測試資料
    for case_num in range(1, num_cases + 1):
        # 根據題目要求，相鄰兩組測試資料的輸出之間必須空一行，
        # 但第一組測試資料的前面不需要空行。
        if case_num > 1:
            print()
            
        # 讀取 36 個字元（0-9, A-Z）的印刷成本
        # 利用 list comprehension 一次讀取接下來的 36 個整數並轉為 int
        costs = [int(input_data[idx + i]) for i in range(36)]
        idx += 36  # 指標往後移動 36 格，準備讀取下一個資料
            
        print(f"Case {case_num}:")
        
        num_queries = int(input_data[idx])
        idx += 1   # 指標往後移動 1 格
        
        # 處理每一筆查詢
        for _ in range(num_queries):
            query = int(input_data[idx])
            idx += 1  # 指標往後移動 1 格，為下一次讀取做準備
            
            # 呼叫函式計算最低成本的進位制
            best_bases = get_cheapest_bases(costs, query)
            
            # 格式化輸出結果：將 best_bases 串列裡的數字轉換為字串，並用空格串接起來
            print(f"Cheapest base(s) for number {query}: {' '.join(map(str, best_bases))}")

if __name__ == '__main__':
    main()