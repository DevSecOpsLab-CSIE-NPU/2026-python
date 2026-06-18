import sys

# AI 建議的簡單版本 - 10812 Beat the Spread!
# 繁體中文註解說明

def solve():
    # 讀取所有輸入內容並依空白分割
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # 第一個數字是測試資料的組數
    n = int(input_data[0])
    idx = 1
    
    # 處理每一組測試資料
    for _ in range(n):
        if idx >= len(input_data):
            break
        s = int(input_data[idx])
        d = int(input_data[idx+1])
        idx += 2
        
        # 判斷是否有解：S必須大於等於D，且 S+D 必須為偶數以確保為整數解
        if s >= d and (s + d) % 2 == 0:
            a = (s + d) // 2
            b = (s - d) // 2
            print(f"{a} {b}")
        else:
            print("impossible")

if __name__ == "__main__":
    solve()
