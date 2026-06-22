"""
解題檔：任意進位的數字根（Base-13 Digital Root）- 第三題

核心任務：
1. 進位轉換 - 將十進位數字轉換成 Base-13 進位
2. 計算數字根 - 迭代求和各位數字直到變成一位數
3. 輸出結果 - 以十進位格式輸出最終的數字根
"""


def digital_root_base13(n):
    """
    計算 Base-13 進位下的數字根
    
    Args:
        n: 十進位整數
    
    Returns:
        Base-13 進位下的數字根（十進位表示）
    
    算法：
    - 重複計算各位數字和直到結果小於 13
    - 利用模運算 (n % 13) 和整除 (n // 13) 進行進位轉換
    """
    if n == 0:
        return 0
    
    # 反覆計算位數和直到一位數（< 13）
    while n >= 13:
        digit_sum = 0
        # 進位轉換：提取各位數字並求和
        while n > 0:
            digit_sum += n % 13  # 提取最低位數字
            n //= 13             # 移除最低位
        n = digit_sum  # 更新 n 為位數和
    
    return n


def main():
    """主程序 - 讀取輸入直到 EOF 並輸出數字根"""
    try:
        while True:
            try:
                line = input()
                num = int(line)
                result = digital_root_base13(num)
                print(result)
            except EOFError:
                # 遇到 EOF 時終止
                break
    except Exception as e:
        pass


if __name__ == "__main__":
    main()
