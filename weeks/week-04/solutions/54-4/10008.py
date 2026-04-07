import sys
from collections import Counter

def analyze_text(text):
    """
    分析文本中的字母出現次數
    參數：text - 輸入的文本字符串
    返回：字母及其出現次數的列表，按照次數降序，次數相同按字母升序
    """
    # 將文本轉為大寫，並過濾出字母
    letters = [char.upper() for char in text if char.isalpha()]

    # 使用 Counter 統計出現次數
    letter_counts = Counter(letters)

    # 排序：先按次數降序，再按字母升序
    sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))

    return sorted_letters

def main():
    input_lines = sys.stdin.readlines()

    # 第一行是測試資料組數
    n = int(input_lines[0].strip())

    # 收集所有輸入行
    text_lines = input_lines[1:1+n]

    # 將所有行合併成一個字符串
    full_text = ''.join(text_lines)

    # 分析文本
    result = analyze_text(full_text)

    # 輸出結果
    for letter, count in result:
        print(f"{letter} {count}")

if __name__ == "__main__":
    main()