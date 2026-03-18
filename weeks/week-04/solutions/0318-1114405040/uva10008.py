"""
UVA 10008: 密碼分析

統計字母出現次數，按照次數降序、同次數按字母升序排列。
"""

try:
    n = int(input())
    char_count = {}
    
    for _ in range(n):
        line = input()
        for char in line:
            if char.isalpha():
                upper_char = char.upper()
                char_count[upper_char] = char_count.get(upper_char, 0) + 1
    
    # 按照次數降序、字母升序排列
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    for char, count in sorted_chars:
        print(f"{char} {count}")
except EOFError:
    pass
