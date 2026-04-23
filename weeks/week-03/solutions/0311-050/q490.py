import sys

def rotate_sentences(lines):
    """
    將傳入的多行字串進行順時針 90 度旋轉。
    由下往上、由左至右讀取字元；若遇缺字則補空白。
    """
    if not lines:
        return []
        
    # 1. 找出最長字串的長度，這將決定我們旋轉後「總共有幾列 (輸出幾行)」
    max_len = max(len(line) for line in lines)
    
    result = []
    # 2. i 代表目前正在處理哪個索引位置 (從第 0 個字元到最後一個字元)
    for i in range(max_len):
        row_chars = []
        # 3. 旋轉的核心：從「最後一行」開始「往上」讀取到「第一行」
        for line in reversed(lines):
            # 如果該行字串的長度足夠，就取出該位置的字元
            if i < len(line):
                row_chars.append(line[i])
            else:
                # 如果該行字串太短，就在這個位置補上空白 (UVA 490 的經典陷阱)
                row_chars.append(" ")
        # 4. 把收集到的字元拼成一個完整字串，存入結果中
        result.append("".join(row_chars))
        
    return result

if __name__ == '__main__':
    # 讀取標準輸入的所有行，並去除每一行結尾的換行符號
    if input_data := sys.stdin.read().splitlines():
        output = rotate_sentences(input_data)
        for line in output:
            print(line)