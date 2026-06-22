import sys

def clean_and_filter_data(raw_data: list, divisor: int) -> list:
    """
    手打版本 - 資料清理與篩選：
    1. 去除重複（保留第一次出現的順序）
    2. 只保留能被 divisor 整除的數
    3. 由小到大排序
    """
    seen = set()
    unique_data = []
    for x in raw_data:
        if x not in seen:
            seen.add(x)
            unique_data.append(x)
            
    filtered_data = [x for x in unique_data if x % divisor == 0]
    return sorted(filtered_data)

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
            
        try:
            n = int(line)
        except ValueError:
            sys.stderr.write("Invalid input format\n")
            continue
            
        if n == 0:
            break
            
        elements_line = sys.stdin.readline()
        if not elements_line:
            break
            
        try:
            raw_data = list(map(int, elements_line.split()))
        except ValueError:
            sys.stderr.write("Invalid input format\n")
            continue
            
        result = clean_and_filter_data(raw_data, 3)
        
        if not result:
            print("NONE")
        else:
            print(" ".join(map(str, result)))

if __name__ == '__main__':
    main()
