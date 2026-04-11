import sys

# 詳細繁體中文註解說明：
# 這題的目的是把文字「順時針轉 90 度」。
# 想像我們把每一行排好，最長的那一行決定了我們要印幾次。
# 第一個位置的字要印在最右邊，最後一個位置的字印在最左邊。

def solve():
    # 讀取所有的行，存到一個清單叫 lines
    lines = []
    for line in sys.stdin:
        # 去掉換行符號，保留內容
        lines.append(line.rstrip('\n'))
    
    if not lines:
        return

    # 第一步：先找出這堆句子裡面，最長的是幾個字
    max_length = 0
    for l in lines:
        if len(l) > max_length:
            max_length = len(l)
            
    # 第二步：我們要逐行印出旋轉後的結果
    # 因為旋轉後，原本句子的「第幾個字」會變成新的「第幾行」
    for char_index in range(max_length):
        # 準備要印出來的這一行字串
        result_row = ""
        
        # 題目要求「最後一行變成最左邊」，所以我們從最後一行往回讀
        for line_index in range(len(lines) - 1, -1, -1):
            current_sentence = lines[line_index]
            
            # 檢查這句話有沒有這麼長
            if char_index < len(current_sentence):
                # 如果有，就拿那個字
                result_row += current_sentence[char_index]
            else:
                # 如果這句話太短，就補一個空白格
                result_row += " "
        
        # 把這行印出來
        print(result_row)

if __name__ == "__main__":
    solve()