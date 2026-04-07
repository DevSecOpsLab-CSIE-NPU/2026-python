import sys

def analyze_text_simple(text):
    """
    簡易版本：分析文本中的字母出現次數
    使用字典手動統計
    """
    letter_counts = {}

    for char in text:
        if char.isalpha():
            upper_char = char.upper()
            if upper_char in letter_counts:
                letter_counts[upper_char] += 1
            else:
                letter_counts[upper_char] = 1

    # 轉為列表並排序
    counts_list = list(letter_counts.items())
    counts_list.sort(key=lambda x: (-x[1], x[0]))

    return counts_list

def main():
    input_lines = sys.stdin.readlines()
    n = int(input_lines[0].strip())
    text_lines = input_lines[1:1+n]
    full_text = ''.join(text_lines)

    result = analyze_text_simple(full_text)

    for letter, count in result:
        print(f"{letter} {count}")

if __name__ == "__main__":
    main()