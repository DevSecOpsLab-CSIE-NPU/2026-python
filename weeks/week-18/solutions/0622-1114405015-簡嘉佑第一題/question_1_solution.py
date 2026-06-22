"""
第一題：資料清理 (Data Cleaning) - 30分

題目說明：
- 輸入包含多組資料，每組第一行是 n（資料筆數），第二行是 n 個以空格分隔的整數
- 處理邏輯：
  1. 去重並保留第一次出現的順序
  2. 過濾出能被 D 整除的數字
  3. 將結果由小到大排序
- 輸出：排序後的結果，若沒有符合條件的數字則輸出 NONE

座號：15
D 值：15 % 13 = 2
"""

def solve_data_cleaning(n, numbers, d):
    """
    資料清理函式
    
    Args:
        n: 資料筆數
        numbers: 整數列表
        d: 整除的數字（D值）
    
    Returns:
        處理後的結果字串
    """
    if n == 0 or not numbers:
        return "NONE"
    
    # 步驟1：去重並保留第一次出現的順序
    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)
    
    # 步驟2：過濾出能被 D 整除的數字
    divisible_numbers = [num for num in unique_numbers if num % d == 0]
    
    # 步驟3：如果沒有符合條件的數字，返回 NONE
    if not divisible_numbers:
        return "NONE"
    
    # 步驟4：由小到大排序
    divisible_numbers.sort()
    
    # 步驟5：轉換為字串輸出
    return " ".join(map(str, divisible_numbers))


def main():
    """主程式"""
    d = 2  # 座號15的D值
    
    # 讀取測試用例
    try:
        while True:
            line = input().strip()
            if not line:
                break
            
            n = int(line)
            
            if n == 0:
                print("NONE")
                continue
            
            # 讀取資料列
            numbers_line = input().strip()
            numbers = list(map(int, numbers_line.split()))
            
            # 處理並輸出結果
            result = solve_data_cleaning(n, numbers, d)
            print(result)
    
    except EOFError:
        # 處理文件末尾
        pass


if __name__ == "__main__":
    main()
