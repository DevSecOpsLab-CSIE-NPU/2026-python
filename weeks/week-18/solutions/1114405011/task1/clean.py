import sys

def clean_data(data_list, d_val):
    """
    資料清理核心邏輯：
    1. 去除重複（保留第一次出現的順序）
    2. 只保留能被 d_val 整除的數
    3. 由小到大排序
    """
    # 步驟 1：去除重複且保持首次出現順序 (利用 dict 保持插入順序特性)
    seen = list(dict.fromkeys(data_list))
    
    # 步驟 2：篩選出能被 d_val 整除的數字
    if d_val == 0:
        raise ValueError("整除數 D 不可為 0")
        
    filtered = [x for x in seen if x % d_val == 0]
    
    # 步驟 3：由小到大排序
    filtered.sort()
    
    return filtered

def main():
    """
    處理標準 I/O 多組測資，直到讀到 n = 0 結束
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    while True:
        try:
            n_str = next(iterator)
            n = int(n_str)
            
            # 當 n = 0 代表輸入結束
            if n == 0:
                break
                
            # 讀取接下來的 n 個整數
            current_group = []
            for _ in range(n):
                current_group.append(int(next(iterator)))
            
            # 使用學號對應的參數 D = 3 進行清理
            result = clean_data(current_group, d_val=3)
            
            # 依據考卷規格輸出：空白分隔；若沒有任何數字符合則輸出 NONE
            if result:
                print(" ".join(map(str, result)))
            else:
                print("NONE")
                
        except (StopIteration, ValueError):
            break

if __name__ == "__main__":
    main()