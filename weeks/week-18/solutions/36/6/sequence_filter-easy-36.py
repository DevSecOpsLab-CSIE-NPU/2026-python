"""
簡易版數列過濾程式

說明：先去除重複元素，再篩選可被 4 整除的數字，最後排序輸出。
"""

def process_sequence(numbers):
    """處理數列：去重、篩選、排序。"""
    seen_set = set()
    unique_numbers = []

    for number in numbers:
        if number not in seen_set:
            seen_set.add(number)
            unique_numbers.append(number)

    print(f"去重後：{unique_numbers}")

    filtered_numbers = []
    for number in unique_numbers:
        if number % 4 == 0:
            filtered_numbers.append(number)

    print(f"篩選後（能被4整除）：{filtered_numbers}")

    if len(filtered_numbers) == 0:
        return "NONE"

    result = sorted(filtered_numbers)
    print(f"排序後：{result}")
    return result


def process_sequence_easy(numbers):
    """簡易版本的包裝函式，直接呼叫 process_sequence。"""
    return process_sequence(numbers)


def main_easy():
    """從標準輸入讀取數列，訊息化輸出中間步驟與最終結果。"""
    while True:
        n = int(input("輸入數列長度 n（0 表示結束）："))

        if n == 0:
            print("程式結束")
            break

        number_line = input(f"輸入 {n} 個整數（用空白分隔）：")
        numbers = list(map(int, number_line.split()))

        print(f"\n原始數列：{numbers}")

        result = process_sequence_easy(numbers)

        if result == "NONE":
            print(f"最終結果：NONE\n")
        else:
            output_string = ' '.join(map(str, result))
            print(f"最終結果：{output_string}\n")


if __name__ == '__main__':
    main_easy()