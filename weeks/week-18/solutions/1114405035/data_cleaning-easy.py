import sys

def clean_and_filter_data(raw_data: list, divisor: int) -> list:
    """
    AI 簡單版 - 資料清理與篩選：
    1. 去除重複（保留第一次出現的順序）
    2. 只保留能被 divisor 整除的數
    3. 由小到大排序
    """
    # 步驟 1: 去除重複且保留原始順序
    seen = set()
    unique_data = []
    for x in raw_data:
        if x not in seen:
            seen.add(x)
            unique_data.append(x)
            
    # 步驟 2: 篩選出能被整除的數 (x % divisor == 0)
    filtered_data = []
    for x in unique_data:
        if x % divisor == 0:
            filtered_data.append(x)
            
    # 步驟 3: 由小到大進行排序
    sorted_data = sorted(filtered_data)
    
    return sorted_data

def main():
    while True:
        # 讀取數列長度 n
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
            
        try:
            n = int(line)
        except ValueError:
            sys.stderr.write("Invalid input format\n")
            continue
            
        # 當 n = 0 時，終止輸入
        if n == 0:
            break
            
        # 讀取下一行 n 個整數
        elements_line = sys.stdin.readline()
        if not elements_line:
            break
            
        try:
            # 將輸入字串以空白切割並轉換為整數串列
            raw_data = list(map(int, elements_line.split()))
        except ValueError:
            sys.stderr.write("Invalid input format\n")
            continue
            
        # 使用學號計算出的 D = 3 進行清理與過濾
        result = clean_and_filter_data(raw_data, 3)
        
        # 輸出處理後的結果，若為空則輸出 NONE
        if not result:
            print("NONE")
        else:
            print(" ".join(map(str, result)))

if __name__ == '__main__':
    main()
