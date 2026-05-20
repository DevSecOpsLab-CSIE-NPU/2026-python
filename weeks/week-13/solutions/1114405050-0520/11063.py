import sys

def rgb_to_xyz(r, g, b):
    """
    根據題目給定的轉換矩陣，將 RGB 數值轉換為 XYZ 數值。
    這個公式主要用於色彩空間轉換。
    """
    x = 0.5149 * r + 0.3244 * g + 0.1607 * b
    y = 0.2654 * r + 0.6704 * g + 0.0642 * b
    z = 0.0248 * r + 0.1248 * g + 0.8504 * b
    return x, y, z

def main():
    # sys.stdin.read().split() 會讀取所有標準輸入，並使用空白字元（包含空格、換行）進行切割
    # 這樣可以忽略測資中多餘的換行或空格，非常適合處理解題系統的雜亂輸入。
    input_data = sys.stdin.read().split()
    if not input_data:
        return  # 若沒有任何輸入則直接結束
        
    # 將字串列表轉換成一個迭代器 (iterator)
    # 之後只要呼叫 next(tokens) 就能依序取得下一個字串，不需要再手動維護索引值 (index)
    tokens = iter(input_data)
    
    # ZeroJudge 可能會有多組測試資料，所以我們利用 while 迴圈處理到 EOF
    while True:
        try:
            # 嘗試讀取下一組測資的維度 N
            n_str = next(tokens)
        except StopIteration:
            break  # 如果 next() 丟出 StopIteration 錯誤，代表所有資料都讀取完了，結束迴圈
            
        n = int(n_str)
        total_pixels = n * n  # 影像大小是 N x N，所以共有 N平方個像素
        sum_y = 0.0           # 紀錄所有像素的亮度 (Y) 總和，用於最後計算平均
        
        # 依序讀取每一個像素的 RGB 值
        for _ in range(total_pixels):
            r = int(next(tokens))
            g = int(next(tokens))
            b = int(next(tokens))
            
            # 呼叫自訂函式進行轉換
            x, y, z = rgb_to_xyz(r, g, b)
            sum_y += y  # 將轉換出的 Y 值累加到總和中
            
            # 格式化輸出轉換結果
            # ':.4f' 表示將浮點數格式化為小數點後 4 位的字串（會自動進行四捨五入）
            print(f"{x:.4f} {y:.4f} {z:.4f}")
            
        # 當一組影像的所有像素都處理完後，計算 Y 的平均值
        # 注意這裡不用擔心除以零，因為通常測資 N 會大於 0
        avg_y = sum_y / total_pixels
        
        # 印出平均值，一樣取到小數點後 4 位
        print(f"The average of Y is {avg_y:.4f}")

if __name__ == '__main__':
    main()