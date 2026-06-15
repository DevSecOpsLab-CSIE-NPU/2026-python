# 主題 11：Hello World - 正式版

def hello_world():
    """回傳 Hello World 字串"""
    return 'Hello, World!'

def hello_with_name(name):
    """以名字問候"""
    return f'Hello, {name}!'

if __name__ == '__main__':
    print(hello_world())
    print(hello_with_name('World'))
