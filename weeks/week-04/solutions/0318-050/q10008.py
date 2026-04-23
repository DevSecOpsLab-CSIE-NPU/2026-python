import sys
from collections import Counter

def analyze_crypto(lines):
    """
    分析多行字串中英文字母的出現頻率。
    回傳一個字串串列，格式為 ["字母 次數", ...]
    """
    # 建立一個 Counter 物件來方便且快速地計算字元出現次數
    counter = Counter()
    
    for line in lines:
        for char in line:
            # 題目要求：只統計英文字母，忽略標點符號、數字與空白
            if char.isalpha():
                # 題目要求：大小寫視為相同，因此統一轉換為大寫進行統計
                counter[char.upper()] += 1
                
    # 雙重條件排序核心技巧：
    # x 代表 counter.items() 裡的每一組 tuple，例如 ('A', 3) -> x[0] 是字母, x[1] 是次數
    # 條件 1: -x[1] 加上負號代表依照「次數」做降冪排序 (由大排到小)
    # 條件 2: x[0]  如果次數相同時，依照「字母」做升冪排序 (A 在 B 前面)
    sorted_counts = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    
    # 將排序後的結果格式化成題目要求的字串清單 ["A 3", "B 2"]
    return [f"{char} {count}" for char, count in sorted_counts]

if __name__ == '__main__':
    # 一次性讀取所有標準輸入，並以換行符號切分成串列
    input_data = sys.stdin.read().splitlines()
    
    if input_data:
        # 第一行是數字 n，代表接下來有幾行密文。
        n = int(input_data[0].strip())
        
        # 將接下來的 n 行交給 analyze_crypto 處理並印出結果
        for result in analyze_crypto(input_data[1:n+1]):
            print(result)