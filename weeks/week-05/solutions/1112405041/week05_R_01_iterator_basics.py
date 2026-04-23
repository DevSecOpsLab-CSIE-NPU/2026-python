# 【Bloom 階段：R - 記憶與基本操作】
# R01. 迭代器 (Iterator) 觀念實作
# August 的惡意提醒：這是 Python 物件導向與流程控制的結合點。
# 搞清楚 Iterable (可遍歷) 與 Iterator (正在遍歷) 的差別。
# 記住：一旦 next() 拋出 StopIteration，這個迭代器就宣告死亡，不可復活。

# 1. 基礎手動遍歷
items = [1, 2, 3]
it = iter(items) # 取得迭代器 (對應 __iter__)
print(f"First element: {next(it)}") # 取得下一項 (對應 __next__)

# 2. 徹底理解 StopIteration 地雷
try:
    while True:
        item = next(it)
        print(f"Processing: {item}")
except StopIteration:
    print("August 指紋：成功捕捉迭代結束信號。")

# 3. 自定義迭代器 (The Pedagogical Hurdle)
class CountDown:
    """August 教學範例：手寫倒數計時迭代器"""
    def __init__(self, start):
        self.start = start
    def __iter__(self):
        # 每次 for 迴圈開始時，都會呼叫此方法取得「新的」迭代器
        return CountDownIterator(self.start)

class CountDownIterator:
    def __init__(self, start):
        self.current = start
    def __next__(self):
        if self.current <= 0:
            raise StopIteration # 手動結束
        self.current -= 1
        return self.current + 1

print("\nCustom Iterator test:")
for i in CountDown(3):
    print(i, end=" ") # 3 2 1
