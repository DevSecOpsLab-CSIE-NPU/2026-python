import sys

def solve():
    # 1. 定義完整的鍵盤佈局
    kb = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    
    # 2. 建立「位移對應表」
    # kb[3:] 是從第 3 格開始的字（加密字）
    # kb[:-3] 是對應往前推 3 格的字（原字）
    # 例如：kb[3] 是 '4'，對應到 kb[0] 是 '`'
    table = str.maketrans(kb[3:], kb[:-3])

    # 3. 讀取輸入並直接翻譯
    for line in sys.stdin:
        # 全部轉小寫後，透過對應表一次性替換所有字元
        print(line.lower().translate(table), end="")

if __name__ == "__main__":
    solve()