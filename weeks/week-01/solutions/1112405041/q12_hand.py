# 主題 12：Python 字串格式化 - 正式版

def format_price(name, price):
    """使用 f-string 格式化價格"""
    return f'{name} price = {price:.2f}'

def format_with_method(name, price):
    """使用 format 方法格式化"""
    return '{} price = {:.2f}'.format(name, price)

def align_number(num, width, align='<'):
    """對齐數字"""
    if align == '<':
        return f'{num:<{width}}'
    elif align == '>':
        return f'{num:>{width}}'
    elif align == '^':
        return f'{num:^{width}}'

def format_precision(value, decimals):
    """格式化浮點數精度"""
    return f'{value:.{decimals}f}'

def number_bases(num):
    """轉換不同進位制"""
    return {
        'decimal': num,
        'hex': f'{num:x}',
        'binary': f'{num:b}',
        'octal': f'{num:o}'
    }

if __name__ == '__main__':
    print("f-string:", format_price('ACME', 91.1))
    print("format:", format_with_method('ACME', 91.1))
    print("精度:", format_precision(3.14159, 2))
    print("進位制:", number_bases(255))
