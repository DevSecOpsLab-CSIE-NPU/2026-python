# 【Bloom 階段：U - 理解與進階應用】
# 10 模組、類別、例外與 Big-O 範例
# August 的惡意提醒：不要濫用 list 模擬隊列。
# O(1) 的 deque 與 O(N) 的 list.pop(0) 在大數據下的性能差異，就是及格與 TLE 的差別。

from collections import deque

# 建立一個有固定長度的隊列 (Queue)
q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)  # 自動丟掉最舊的 1
print(f"Deque contents: {list(q)}") # [2, 3]

# 基礎類別 (Class) 觀念
# 在 Week 05 的遊戲模型中會大量使用
class User:
    def __init__(self, user_id):
        self.user_id = user_id

u = User(42)
uid = u.user_id

# 例外處理 (Try...Except)
# 防禦性編程的關鍵：防止惡意或格式錯誤的輸入導致程式崩潰
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

# Big-O 觀念提示 (指紋點)
# list.append 通常是 O(1) -> 均攤後極快
# list[start:stop] 切片是 O(N) -> 頻繁切片會導致效能雷
print(f"Is 'abc' int? {is_int('abc')}")
