import sys

def solve():
    """
    UVA 11349 - Symmetric Matrix
    核心思路：
    將 n x n 的矩陣攤平為一維陣列 (長度為 n*n)。
    判斷中心對稱，只需檢查陣列的第 i 個元素是否等於第 (n*n - 1 - i) 個元素。
    同時檢查所有元素是否 >= 0。
    """
    # 讀取標準輸入的所有資料，並以空白字元（包含換行）分割成一個個的 token
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # 取得測試資料組數 T
    T = int(input_data[0])
    idx = 1
    
    for t in range(1, T + 1):
        # 處理輸入中的 "N = n"
        # 由於測資在以空白分割後可能變成 'N', '=', '3'，所以我們尋找下一個合法數字
        n = 0
        while idx < len(input_data):
            token = input_data[idx]
            idx += 1
            # 若該字串是純字母或等號，則略過
            if token == 'N' or token == '=':
                continue
            if token.startswith('N='):
                n = int(token[2:])
                break
            if token.isdigit():
                n = int(token)
                break
                
        # 讀取 n x n 個矩陣元素，存入一維陣列 matrix 中
        matrix = []
        length = n * n
        for _ in range(length):
            matrix.append(int(input_data[idx]))
            idx += 1
            
        # 判斷是否為對稱矩陣
        is_symmetric = True
        
        # 只需要比對到一半即可（若有負數直接判斷為非對稱）
        for i in range((length // 2) + 1):
            if matrix[i] < 0 or matrix[length - 1 - i] < 0:
                is_symmetric = False
                break
            if matrix[i] != matrix[length - 1 - i]:
                is_symmetric = False
                break
        
        # 輸出對應結果
        if is_symmetric:
            print(f"Test #{t}: Symmetric.")
        else:
            print(f"Test #{t}: Non-symmetric.")

if __name__ == '__main__':
    solve()