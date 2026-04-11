import sys

def run():
    # 讀取第一行，得知後面有幾列文字
    try:
        line_input = sys.stdin.readline()
        if not line_input:
            return
        n = int(line_input.strip())
        
        # 建立字典來存放統計結果，例如 {'A': 5, 'B': 2}
        counts = {}
        
        for _ in range(n):
            # 逐行讀取
            text = sys.stdin.readline()
            for char in text:
                # 只處理英文字母
                if char.isalpha():
                    # 統一轉成大寫
                    c = char.upper()
                    # 如果字母已在字典，次數加 1，否則初始化為 1
                    if c in counts:
                        counts[c] += 1
                    else:
                        counts[c] = 1
        
        # 將字典轉成清單，方便排序
        items = list(counts.items())
        
        # 進行排序
        # -x[1] 代表對「次數」做降序排列（由大到小）
        # x[0] 代表當次數相同時，對「字母」做升序排列（由小到大）
        items.sort(key=lambda x: (-x[1], x[0]))
        
        # 印出結果
        for char, count in items:
            print(f"{char} {count}")
            
    except EOFError:
        pass

if __name__ == "__main__":
    run()