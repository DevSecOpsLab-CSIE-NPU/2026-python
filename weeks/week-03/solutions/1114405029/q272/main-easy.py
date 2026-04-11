import sys

# 詳細繁體中文註解說明：
# 這題不需要複雜的演算法，只需要「記住」現在是第幾個引號。
# 我們用一個變數 first 來當開關：
# 如果 first 是 True，代表遇到 " 要換成 ``
# 如果 first 是 False，代表遇到 " 要換成 ''
# 換完之後，就把 True 變 False，或是 False 變 True。

def solve():
    # 一開始遇到的第一個引號一定是「開始引號」
    first = True
    
    # 讀取所有的輸入內容
    # 因為題目說直到檔案結束 (EOF)，所以用 read() 全部讀進來
    data = sys.stdin.read()
    
    # 準備一個空的字串來存結果
    output = ""
    
    # 檢查內容裡的每一個字
    for char in data:
        if char == '"':
            # 如果是第一個引號
            if first:
                output += "``"
                first = False # 下一個就不是第一個了
            else:
                # 如果是第二個引號
                output += "''"
                first = True # 下一個又是新的一組第一個
        else:
            # 不是引號的字，直接照抄
            output += char
            
    # 最後把結果印出來
    print(output, end="")

if __name__ == "__main__":
    solve()