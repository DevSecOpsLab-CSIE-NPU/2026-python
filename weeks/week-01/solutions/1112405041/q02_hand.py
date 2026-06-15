# 主題 02：基本資料型別 - 正式版

def get_basic_types():
    """取得基本資料型別的例子"""
    x = 7
    y = 3.5
    name = 'ACME'
    ok = True
    return {
        'int': x,
        'float': y,
        'str': name,
        'bool': ok
    }

def convert_types():
    """示範型別轉換"""
    s = '12'
    num = int(s)
    price = float('19.99')
    str_num = str(42)
    
    return {
        'to_int': num,
        'to_float': price,
        'to_str': str_num,
        'original_str': s
    }

if __name__ == '__main__':
    print("基本型別:", get_basic_types())
    print("型別轉換:", convert_types())
