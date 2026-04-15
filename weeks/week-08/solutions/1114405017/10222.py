import sys

def solve():
    # 1. 建立鍵盤佈局字串 (依照 QWERTY 順序)
    # 包含數字排、英文三排以及標點符號
    # 這些字元的順序必須嚴格遵守鍵盤上從左到右的排列
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    
    # 2. 持續讀取輸入，直到沒有資料為止
    for line in sys.stdin:
        # 將輸入字串轉為小寫，因為解碼後的結果通常不分大小寫
        line = line.lower()
        
        # 用來儲存解碼後的字元列表
        result = []
        
        # 3. 逐字遍歷輸入的字串
        for char in line:
            # 如果是空格或換行符號，直接保留，不進行解碼
            if char == ' ' or char == '\n':
                result.append(char)
            else:
                # 在鍵盤字串中尋找該字元的位置 (索引值)
                index = keyboard.find(char)
                
                # 如果找到了該字元 (index 不等於 -1)
                if index != -1:
                    # 進行解碼位移
                    # 根據你的題目需求：向左移動 3 個按鍵 (index - 3)
                    # 注意：如果原本是 UVA 10222 標準題意，則通常是 index - 2
                    decoded_char = keyboard[index - 3]
                    result.append(decoded_char)
                else:
                    # 如果字元不在鍵盤定義中，則原樣輸出
                    result.append(char)
        
        # 4. 將列表中的字元合併成字串並印出
        # 使用 end="" 是因為 line 本身已經包含換行符號
        print("".join(result), end="")

if __name__ == "__main__":
    solve()