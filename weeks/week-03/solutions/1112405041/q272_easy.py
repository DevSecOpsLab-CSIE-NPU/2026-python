# 272_ai_easy.py
# UVA 272：TeX 引號替換 - 簡單版，附詳細繁體中文註解
# 功能：將輸入中的雙引號替換成 TeX 格式的引號

def process_tex_quotes(text):
    """
    處理輸入文字，將雙引號替換成 TeX 引號。
    
    參數：
    text (str): 輸入文字
    
    返回：
    str: 處理後的文字
    """
    result = []
    quote_count = 0  # 記錄引號數量，偶數用 ``，奇數用 ''
    
    for char in text:
        if char == '"':
            if quote_count % 2 == 0:
                result.append('``')  # 左引號
            else:
                result.append("''")  # 右引號
            quote_count += 1
        else:
            result.append(char)
    
    return ''.join(result)

# 主程式：讀取輸入行並處理
if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        # 處理每一行
        processed_line = process_tex_quotes(line.rstrip('\n'))
        print(processed_line)