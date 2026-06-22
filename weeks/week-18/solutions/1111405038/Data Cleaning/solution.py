"""
解題檔：資料清理（Data Cleaning）- 第一題

核心任務：
1. 去除重複 - 保留第一次出現的順序
2. 篩選被D整除的數 - 只保留被D整除的數（D=2）
3. 由小到大排序
"""


def data_cleaning(numbers, divisor=2):
    """
    進行資料清理
    
    Args:
        numbers: 整數列表
        divisor: 整除因子（預設為2）
    
    Returns:
        排序後被整除的不重複數列
    """
    # 步驟1：去除重複，保留第一次出現的順序
    seen = set()
    unique_numbers = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            unique_numbers.append(num)
    
    # 步驟2：篩選被divisor整除的數
    filtered = [num for num in unique_numbers if num % divisor == 0]
    
    # 步驟3：由小到大排序
    filtered.sort()
    
    return filtered


def main():
    """主程序 - 處理多組測資"""
    while True:
        n = int(input())
        
        # 當 n = 0 時終止
        if n == 0:
            break
        
        # 讀取數列
        numbers = list(map(int, input().split()))
        
        # 進行資料清理
        result = data_cleaning(numbers)
        
        # 輸出結果
        if result:
            print(' '.join(map(str, result)))
        else:
            print('NONE')


if __name__ == '__main__':
    main()
