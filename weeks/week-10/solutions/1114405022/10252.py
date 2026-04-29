"""UVA 10252 - Common Permutation

一般版：更穩健的實現
"""

from collections import Counter
import sys


def common_permutation(s1: str, s2: str) -> str:
    """
    找兩個字符串的共同排列
    規則：
    1. 找兩個字符串都包含的字符
    2. 取每個字符的最小出現次數
    3. 按字母順序排列輸出
    """
    # 計算每個字符的出現次數
    count1 = Counter(s1)
    count2 = Counter(s2)
    
    # 找共同字符
    common_chars = set(s1) & set(s2)
    
    # 構建結果
    result = []
    for char in sorted(common_chars):
        # 取最小出現次數
        min_count = min(count1[char], count2[char])
        result.extend([char] * min_count)
    
    return ''.join(result)


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line or len(line.split()) < 2:
            continue
        
        parts = line.split()
        s1, s2 = parts[0], parts[1]
        
        result = common_permutation(s1, s2)
        print(result)


if __name__ == "__main__":
    main()
