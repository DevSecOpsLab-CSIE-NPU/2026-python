import sys

# 詳細繁體中文註解說明：
# 這題的重點在於減少運算次數。
# 直接找六個數會太慢，所以我們把公式拆成兩邊。
# 左邊：a + b + c
# 右邊：f - d - e
# 只要左邊的和等於右邊的差，這六個數就成立。

def solve():
    # 讀取所有的數字
    data = sys.stdin.read().split()
    if not data:
        return
        
    # 第一個數字是數量 N
    n = int(data[0])
    # 後面 N 個數字是集合 S 的內容
    s = []
    for i in range(1, n + 1):
        s.append(int(data[i]))
        
    # 用一個字典 (dict) 來存「和」出現的次數
    # 這樣查找的速度會非常快 (接近 O(1))
    sum_map = {}
    
    # 枚舉前三個數的所有組合
    for a in s:
        for b in s:
            for c in s:
                total = a + b + c
                # 如果這個和已經出現過，次數加 1
                if total in sum_map:
                    sum_map[total] += 1
                else:
                    sum_map[total] = 1
                    
    ans = 0
    # 枚舉後三個數的組合，觀察 f - d - e
    for f in s:
        for d in s:
            for e in s:
                diff = f - d - e
                # 如果這個「差」有在字典裡，表示找到了匹配的 a, b, c
                if diff in sum_map:
                    ans += sum_map[diff]
                    
    # 輸出最後結果
    print(ans)

if __name__ == "__main__":
    solve()