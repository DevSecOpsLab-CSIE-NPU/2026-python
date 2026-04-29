"""UVA 10252 - Common Permutation

簡單版：找兩個字符串的共同排列
"""

from collections import Counter


def common_permutation(s1, s2):
    """
    找兩個字符串的共同排列
    即：兩個字符串都包含的字符，取最小出現次數
    """
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    result = []
    for char in sorted(set(s1) & set(s2)):
        count = min(c1[char], c2[char])
        result.extend([char] * count)
    
    return ''.join(sorted(result))


def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        s1, s2 = line.split()
        result = common_permutation(s1, s2)
        print(result)


if __name__ == "__main__":
    main()
