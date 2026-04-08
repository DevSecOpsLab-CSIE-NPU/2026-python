import sys
from collections import Counter

def solve():
    # 讀取輸入並轉換為整數列表
    data = list(map(int, sys.stdin.read().split()))
    if not data: return
    
    n, s = data[0], data[1:]
    
    # 使用 Counter 直接統計 a + b + c 的所有可能結果與出現次數
    # 這裡使用生成式來取代三層迴圈
    lhs_counts = Counter(a + b + c for a in s for b in s for c in s)
    
    # 計算 f - d - e 並從 Counter 中直接取得對應次數加總
    # 若 key 不存在，Counter 會自動回傳 0
    ans = sum(lhs_counts[f - d - e] for f in s for d in s for e in s)
    
    print(ans)

if __name__ == "__main__":
    solve()