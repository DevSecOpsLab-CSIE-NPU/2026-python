import sys

def process_line(line):
    result = []
    quote_count = 0
    for char in line:
        if char == '"':
            quote_count += 1
            if quote_count % 2 == 1:
                result.append('``')
            else:
                result.append("''")
        else:
            result.append(char)
    return ''.join(result)

def main():
    for line in sys.stdin:
        print(process_line(line), end='')

if __name__ == "__main__":
    main()