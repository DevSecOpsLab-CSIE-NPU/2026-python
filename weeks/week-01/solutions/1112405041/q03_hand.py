# 主題 03：基本容器型別 - 正式版

def manage_containers():
    """示範容器型別的操作"""
    numbers = [1, 2, 3]
    point = (4, 5)
    unique = {1, 2, 3}
    prices = {'AAPL': 150.0, 'MSFT': 320.5}
    
    numbers.append(4)
    unique.add(4)
    prices['GOOGL'] = 2800.0
    
    return {
        'list': numbers,
        'tuple': point,
        'set': unique,
        'dict': prices,
        'first_number': numbers[0],
        'aapl_price': prices['AAPL']
    }

if __name__ == '__main__':
    result = manage_containers()
    print(result)
