import sys

# 增加遞迴深度限制，避免線段樹在 N 較大時發生 RecursionError
sys.setrecursionlimit(200000)

def solve():
    # 讀取所有輸入並過濾掉空白，確保在大數據量下效能穩定
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 第一個數字是 N，代表牛的總數
    n = int(input_data[0])
    
    # 題目給的是第 2 到第 N 隻牛前面比它小的數量
    # 我們在最前面補一個 0，代表第 1 隻牛前面有 0 隻比它小
    # pre_smaller[i] 代表「排在位置 i 的牛，前面有幾頭編號比它小」
    pre_smaller = [0] * n
    for i in range(1, n):
        pre_smaller[i] = int(input_data[i])
    
    # 線段樹陣列：長度通常設為 4*n
    # 每個節點 tree[node] 儲存該區間內「目前還剩下多少個編號」可以使用
    tree = [0] * (4 * n)
    
    def build(node, start, end):
        """ 初始化線段樹：每個編號 (1 到 N) 初始都是可用的 (值為 1) """
        if start == end:
            tree[node] = 1
            return
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        # 父節點的值 = 左子樹可用數 + 右子樹可用數
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query_and_update(node, start, end, k):
        """ 
        在線段樹中尋找「目前剩餘編號」裡的第 k 小值，
        找到後將其移除（值減 1），並回傳該編號。
        """
        # 沿路更新，因為該節點下方一定會有一個編號被選走
        tree[node] -= 1
        
        # 找到葉子節點，代表這就是我們要的編號
        if start == end:
            return start
        
        mid = (start + end) // 2
        left_available = tree[2 * node] # 左子樹目前還剩下多少個編號
        
        if k <= left_available:
            # 如果第 k 小就在左邊，往左子樹找
            return query_and_update(2 * node, start, mid, k)
        else:
            # 如果在右邊，則扣除左邊的數量，往右子樹找第 (k - left_available) 小
            return query_and_update(2 * node + 1, mid + 1, end, k - left_available)

    # 1. 建立線段樹
    build(1, 1, n)
    
    # 2. 準備存儲答案的陣列
    ans = [0] * n
    
    # 3. 逆向推導：
    #    最後一頭牛的資訊是最精準的，因為它看過前面所有的牛。
    #    如果它前面有 k 個比它小，那它就是目前剩餘編號中的「第 k+1 小」。
    for i in range(n - 1, -1, -1):
        rank = pre_smaller[i] + 1
        # 透過線段樹找到編號，同時將該編號從可用名單中移除
        ans[i] = query_and_update(1, 1, n, rank)
        
    # 4. 批次輸出，提升效能
    sys.stdout.write('\n'.join(map(str, ans)) + '\n')

if __name__ == '__main__':
    solve()