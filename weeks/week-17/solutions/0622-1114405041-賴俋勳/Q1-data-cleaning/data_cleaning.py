"""
題目：資料清理 (Data Cleaning) - 30分

步驟①「準保底」：①份競賽數據，依次去掉重複資料、分出訓練集和測試集

輸入說明：
- 輸入包含多行組別數據
- 每組首行是 n (0 ≤ n ≤ 10^9)
- 接著一行包含 n 個整數
- 最後輸入 0 表示 EOF

輸出說明：
- 對每組測量資料輸出一行：清理後的數列、數字間以空白分隔，最後無任何符號

範例 (D = 2)：
Sample Input:
8
4 7 4 2 9 2 6 7
3
1 3 5
0

Sample Output:
2 4 6
NONE
"""


def data_cleaning(input_data):
    """
    實作資料清理功能
    
    Args:
        input_data: 輸入資料列表
    
    Returns:
        str: 清理後的結果字符串
    """
    results = []
    i = 0
    
    while i < len(input_data):
        n = input_data[i]
        i += 1
        
        if n == 0:
            break
        
        # 取得這一組的數據
        numbers = input_data[i]
        i += 1
        
        # 去重並排序
        unique_numbers = sorted(set(numbers))
        
        if unique_numbers:
            results.append(' '.join(map(str, unique_numbers)))
        else:
            results.append('NONE')
    
    return '\n'.join(results)


if __name__ == '__main__':
    data_cleaning()
