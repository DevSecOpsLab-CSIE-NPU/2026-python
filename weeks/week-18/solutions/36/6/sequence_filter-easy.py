"""
簡易版本：序列處理
功能：去重 → 篩選能被4整除 → 排序

這個版本的特點：
1. 代碼簡潔易懂
2. 邏輯清晰分步驟
3. 變數名稱直觀
4. 適合初學者理解
"""


def process_sequence_easy(numbers):
    """
    簡易版：處理單個數列
    
    步驟說明：
    1. 去重（保留第一次出現的順序）
    2. 篩選能被4整除的數
    3. 排序結果
    
    參數：
        numbers (list): 整數列表
    
    返回值：
        list: 排序後的結果列表
        str: "NONE"（若無符合條件的數）
    """
    
    # ==== 步驟 1：去重 ====
    # 使用一個集合記錄已見過的數字
    seen_set = set()
    unique_numbers = []
    
    # 遍歷原始列表，只保留第一次出現的數字
    for number in numbers:
        if number not in seen_set:
            seen_set.add(number)
            unique_numbers.append(number)
    
    # 現在 unique_numbers 是去重後的序列
    print(f"去重後：{unique_numbers}")
    
    # ==== 步驟 2：篩選 ====
    # 創建新列表，只放入能被4整除的數字
    filtered_numbers = []
    
    for number in unique_numbers:
        if number % 4 == 0:  # 判斷能否被4整除
            filtered_numbers.append(number)
    
    # 現在 filtered_numbers 只包含能被4整除的數字
    print(f"篩選後（能被4整除）：{filtered_numbers}")
    
    # ==== 步驟 3：檢查結果 ====
    # 如果沒有符合條件的數字，返回 "NONE"
    if len(filtered_numbers) == 0:
        return "NONE"
    
    # ==== 步驟 4：排序 ====
    # 使用內建的 sorted() 函式排序（由小到大）
    result = sorted(filtered_numbers)
    
    print(f"排序後：{result}")
    
    return result


def main_easy():
    """
    簡易版主程式
    """
    
    while True:
        # 讀取第一行：數列的長度
        n = int(input("輸入數列長度 n（0 表示結束）："))
        
        # 如果 n = 0，表示輸入結束
        if n == 0:
            print("程式結束")
            break
        
        # 讀取第二行：n 個整數，用空白分隔
        number_line = input(f"輸入 {n} 個整數（用空白分隔）：")
        numbers = list(map(int, number_line.split()))
        
        print(f"\n原始數列：{numbers}")
        
        # 處理數列
        result = process_sequence_easy(numbers)
        
        # 輸出結果
        if result == "NONE":
            print(f"最終結果：NONE\n")
        else:
            output_string = ' '.join(map(str, result))
            print(f"最終結果：{output_string}\n")


if __name__ == '__main__':
    main_easy()
