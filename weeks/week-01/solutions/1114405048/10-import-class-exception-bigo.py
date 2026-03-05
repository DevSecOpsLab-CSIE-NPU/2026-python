# 10 模組、類別、例外與 Big-O（最低門檻）範例
# Demonstrates imports, class definition, exception handling, and Big-O notes.

from collections import deque  # 從標準庫 collections 匯入雙端佇列類別 deque

q = deque(maxlen=2)  # 建立一個容量為 2 的先進先出隊列
q.append(1)  # 加入元素 1
q.append(2)  # 加入元素 2
q.append(3)  # 再加入元素 3，因為容量限制，最舊的元素 (1) 會自動被丟棄

class User:
    def __init__(self, user_id):  # 建構子接受 user_id 參數
        self.user_id = user_id  # 將傳入的 id 存到實例屬性

u = User(42)  # 建立一個 User 實例，id 為 42
uid = u.user_id  # 從實例中讀取 user_id 值

# 例外處理

def is_int(val):
    try:
        int(val)  # 嘗試將傳入值轉成整數
        return True  # 轉換成功，視為整數
    except ValueError:  # 若發生值錯誤 (代表無法轉換)
        return False  # 回傳 False

# Big-O 只是觀念提示
# list.append 通常是 O(1)  # 列表尾端附加元素通常是常數時間
# list 切片是 O(N)        # 列表切片需要複制元素，時間與元素數量成線性

print(q)  # 輸出當前的隊列內容 