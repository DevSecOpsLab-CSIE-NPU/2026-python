# 主題 01：變數與指定（Assignment）- 正式版

def get_point():
    """返回座標點"""
    return 4, 9

def demonstrate_assignment():
    """展示變數指定的基本用法"""
    x = 10
    name = 'ACME'
    x, y = 3, 5
    px, py = get_point()
    
    return {
        'x': x,
        'name': name,
        'y': y,
        'px': px,
        'py': py
    }

if __name__ == '__main__':
    result = demonstrate_assignment()
    print(result)
