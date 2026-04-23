import sys

def solve(lines):
    """
    處理多行字串，將雙引號 " 交替替換為 `` 與 ''
    """
    is_first_quote = True  # 記錄下一個遇到的引號是否為「開頭引號」
    result = []
    
    for line in lines:
        new_line = []
        for char in line:
            if char == '"':
                if is_first_quote:
                    new_line.append("``")  # 替換為兩個左單引號
                else:
                    new_line.append("''")  # 替換為兩個右單引號
                is_first_quote = not is_first_quote  # 切換引號狀態
            else:
                new_line.append(char)
        
        result.append("".join(new_line))
        
    return result

if __name__ == '__main__':
    # 一次讀取所有標準輸入內容 (包含多行與空行)
    if input_text := sys.stdin.read():
        for line in solve(input_text.splitlines()):
            print(line)
