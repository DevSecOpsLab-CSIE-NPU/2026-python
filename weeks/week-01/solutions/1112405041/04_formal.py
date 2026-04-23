# 主題 04：for 迴圈 - 正式版

def calculate_sum(items):
    """計算 list 中所有元素的總和"""
    total = 0
    for x in items:
        total += x
    return total

def calculate_squares(items):
    """計算 list 中所有元素的平方"""
    squares = []
    for x in items:
        squares.append(x * x)
    return squares

def iterate_string(word):
    """遍歷字串中的每個字元"""
    chars = []
    for char in word:
        chars.append(char)
    return chars

if __name__ == '__main__':
    items = [2, 4, 6]
    print("總和:", calculate_sum(items))
    print("平方:", calculate_squares(items))
    print("字元:", iterate_string('hello'))
