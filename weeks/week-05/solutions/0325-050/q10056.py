import sys

def calculate_probability(n, p, i):
    """
    計算第 i 個玩家獲勝的機率。
    利用無窮等比級數公式： S = a / (1 - r)
    - 首項 a = p * (1-p)**(i-1) (在前 i-1 個人都失敗後，第 i 個人成功)
    - 公比 r = (1-p)**n (一整輪 n 個人都失敗的機率)
    """
    # 陷阱防呆：如果單次成功的機率是 0，任何人都贏不了
    # 而且如果不提早 return，底下的 1 - r 會變成 1 - 1 = 0，導致除以零錯誤！
    if p == 0.0:
        return "0.0000"
    
    # 首項 a
    a = p * ((1 - p) ** (i - 1))
    # 公比 r
    r = (1 - p) ** n
    
    # 代入無窮等比級數求和公式
    prob = a / (1 - r)
    
    # 格式化為小數點後四位字串
    return f"{prob:.4f}"

if __name__ == '__main__':
    # 讀取標準輸入，將所有輸入用空白/換行切分成一個一維陣列
    input_data = sys.stdin.read().split()
    if input_data:
        S = int(input_data[0])  # 測資筆數
        idx = 1
        for _ in range(S):
            N = int(input_data[idx])
            p = float(input_data[idx+1])
            i = int(input_data[idx+2])
            idx += 3
            
            print(calculate_probability(N, p, i))