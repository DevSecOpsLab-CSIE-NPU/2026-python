import sys

def solve():
    # 一次性讀取所有輸入資料
    text = sys.stdin.read()
    if not text:
        return
        
    # 神奇小技巧：將字串中的 'N' 和 '=' 都替換成空白字元
    # 這樣一來，不論輸入是 'N = 3' 還是 'N=3'，最後分割出來都會只剩下純數字
    text = text.replace('N', ' ').replace('=', ' ')
    tokens = text.split()
    
    # 取得測試資料總筆數 T
    T = int(tokens[0])
    idx = 1
    
    for t in range(1, T + 1):
        # 讀取矩陣維度 n
        n = int(tokens[idx])
        idx += 1
        
        # 讀取 n * n 個元素，利用 List Comprehension 一次存成一維陣列
        length = n * n
        matrix = [int(x) for x in tokens[idx : idx + length]]
        idx += length
        
        # 判斷是否為對稱矩陣：
        # 條件 1: 陣列正著看和反著看要完全一樣 -> matrix == matrix[::-1]
        # 條件 2: 矩陣中所有的數字都必須 >= 0   -> all(x >= 0 for x in matrix)
        if matrix == matrix[::-1] and all(x >= 0 for x in matrix):
            print(f"Test #{t}: Symmetric.")
        else:
            print(f"Test #{t}: Non-symmetric.")

if __name__ == '__main__':
    solve()