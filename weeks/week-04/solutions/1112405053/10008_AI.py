import sys

def solve():
    # 讀取標準輸入的所有內容並去除頭尾空白
    input_str = sys.stdin.read().strip()
    # 如果輸入不為空
    if input_str:
        # 印出 "hello, " 加上輸入的字串
        print(f"hello, {input_str}")

if __name__ == "__main__":
    solve()
