import sys

def find_fake_coin(n, k, weighings):
    """
    找出假幣的編號。
    利用集合 (Set) 的特性，篩選出符合所有秤重結果的可能假幣。
    """
    # 初始狀態：每個硬幣 (1~n) 都有可能是假幣，且可能是比較輕 ("light") 或比較重 ("heavy")
    # 用 tuple (硬幣編號, 狀態) 來記錄，例如 (3, "light") 代表 3 號硬幣是輕的假幣
    candidates = {(i, w) for i in range(1, n + 1) for w in ["light", "heavy"]}

    for left, right, result in weighings:
        if result == '=':
            # 天平平衡：左右兩盤的硬幣絕對都是真幣，把它們從嫌疑名單中剔除
            candidates = {(c, w) for c, w in candidates if c not in left and c not in right}
        elif result == '<':
            # 左輕右重：假幣必定在左盤(且比較輕) 或是 假幣在右盤(且比較重)
            candidates = {(c, w) for c, w in candidates if (c in left and w == "light") or (c in right and w == "heavy")}
        elif result == '>':
            # 左重右輕：假幣必定在左盤(且比較重) 或是 假幣在右盤(且比較輕)
            candidates = {(c, w) for c, w in candidates if (c in left and w == "heavy") or (c in right and w == "light")}

    # 提取出目前還有嫌疑的硬幣編號 (去掉輕重狀態)
    suspect_coins = {c for c, w in candidates}

    # 如果最終只剩下「唯一」一個硬幣有嫌疑，那它就是我們要找的假幣
    if len(suspect_coins) == 1:
        return suspect_coins.pop()
    else:
        # 資訊不足以確認唯一假幣，或者資料相互矛盾
        return 0

if __name__ == '__main__':
    # 讀取所有輸入並依據空白字元 (包含換行、空格) 切割成一維陣列
    input_data = sys.stdin.read().split()
    
    if input_data:
        M = int(input_data[0])  # 測資筆數
        idx = 1
        
        for t in range(M):
            N = int(input_data[idx])
            K = int(input_data[idx+1])
            idx += 2
            
            weighings = []
            for _ in range(K):
                P = int(input_data[idx])
                idx += 1
                left = [int(x) for x in input_data[idx : idx + P]]
                idx += P
                right = [int(x) for x in input_data[idx : idx + P]]
                idx += P
                result = input_data[idx]
                idx += 1
                weighings.append((left, right, result))
                
            ans = find_fake_coin(N, K, weighings)
            
            # 依據題目要求，多筆測資的輸出之間需要有一行空行
            if t > 0:
                print()
            print(ans)