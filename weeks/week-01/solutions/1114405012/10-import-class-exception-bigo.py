# 10 模組、類別、例外與 Big-O（最低門檻）範例

# 從標準函式庫 collections 匯入 deque。
# deque 是雙向佇列，適合做兩端快速加入/移除。
from collections import deque

# 建立一個最多只能放 2 個元素的 deque。
# 如果超過長度，最舊的元素會被自動移除。
q = deque(maxlen=2)
q.append(1)
q.append(2)
q.append(3)  # 加入 3 後，最前面的 1 會被丟掉。


class User:
    # __init__ 是初始化方法，當你建立物件時會自動呼叫。
    def __init__(self, user_id):
        # self.user_id 是這個物件自己的屬性。
        self.user_id = user_id


# 建立 User 類別的物件（實例）。
u = User(42)

# 透過「物件.屬性」取得資料。
uid = u.user_id


# 例外處理
def is_int(val):
    # try 區塊內放「可能出錯」的程式。
    # 如果 int(val) 成功，表示 val 可以轉成整數。
    try:
        int(val)
        return True
    # ValueError: 例如 int('abc')
    # TypeError: 例如 int(None)
    except (ValueError, TypeError):
        return False


def run_examples():
    """執行這個檔案時，示範匯入、類別、例外與時間複雜度概念。"""
    print('deque q 的內容 =', list(q))
    print('因為 maxlen=2，所以依序加入 1、2、3 後，只會保留最後兩個元素 [2, 3]')
    print()

    print('建立 User(42) 後，u.user_id =', uid)
    print()

    test_values = ['123', '12.5', 'abc', None]
    for value in test_values:
        print(f'is_int({value!r}) =', is_int(value))
    print()

    print('Big-O 觀念提示：')
    print('list.append 通常是 O(1)，代表資料量變大時，單次加入尾端的成本通常不會跟著線性增加。')
    print('list 切片通常是 O(N)，因為建立切片時，通常需要把元素複製到新的串列中。')


if __name__ == '__main__':
    run_examples()
