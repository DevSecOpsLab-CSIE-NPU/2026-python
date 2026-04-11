import sys

# 進階實作版：使用產生器 (Generator) 處理大數據流
# 核心邏輯：逐字讀取並根據布林狀態交替更換引號
def solve():
    # is_opening 用來紀錄目前遇到的引號是否為「開始引號」
    is_opening = True
    
    # 使用 sys.stdin.read() 一次性讀取所有字元 (適用於一般 UVA 測資大小)
    # 若測資極大，可改用 sys.stdin.read(1) 逐字讀取
    content = sys.stdin.read()
    
    result = []
    for char in content:
        if char == '"':
            if is_opening:
                result.append("``")
            else:
                result.append("''")
            # 切換狀態
            is_opening = not is_opening
        else:
            result.append(char)
            
    # 將處理後的字元清單合併並輸出
    sys.stdout.write("".join(result))

if __name__ == "__main__":
    solve()