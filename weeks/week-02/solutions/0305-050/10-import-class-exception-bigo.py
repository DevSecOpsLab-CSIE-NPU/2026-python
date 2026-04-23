# 10 模組、類別、例外與 Big-O 基礎範例 (Modules, Classes, Exceptions, and Big-O Basics)

# --- 模組匯入 (Modules & Imports) ---
# 從內建的 collections 模組中匯入 deque (雙向佇列) 類別。
from collections import deque

# 建立一個最大長度為 2 的雙向佇列 (Double-ended queue)。
# maxlen 參數的作用是：當佇列滿了以後，再加入新元素時，會自動從另一端擠掉最舊的元素。
q = deque(maxlen=2)
# 將整數 1 加入佇列的右側。目前佇列內容: deque([1])
q.append(1)
# 將整數 2 加入佇列的右側。目前佇列內容: deque([1, 2])
q.append(2)
# 將整數 3 加入佇列。因為設定了 maxlen=2，容量已滿，所以最舊的元素 (1) 會被自動擠掉 (popleft)。
# 執行後佇列內容會變成: deque([2, 3])
q.append(3)

# --- 類別與物件導向 (Classes & OOP) ---
# 定義一個名為 User 的類別 (Class)，用來產生與管理使用者物件。
class User:
    # 定義 __init__ 方法，這是類別的「建構子 (Constructor)」。
    # 當我們建立一個新的 User 物件時，這個方法會被自動呼叫。
    # self 代表物件本身，user_id 是建立物件時需要傳入的參數。
    def __init__(self, user_id):
        # 將傳入的 user_id 參數，存入物件本身的屬性 (Attribute) 內。
        self.user_id = user_id

# 實例化 (Instantiate) 一個 User 物件，並將 42 作為 user_id 傳入，最後指派給變數 u。
u = User(42)
# 透過「點 (.)」運算子來存取物件 u 的 user_id 屬性，這裡 uid 的值將會是 42。
uid = u.user_id

# --- 例外處理 (Exception Handling) ---
# 定義一個函式 is_int，用來檢查傳入的值 val 是否能被成功轉換成整數。
def is_int(val):
    # 使用 try 區塊包圍「可能會發生錯誤 (拋出例外)」的程式碼。
    try:
        # 嘗試將 val 轉換為整數 (int)。
        int(val)
        # 如果上一行轉換成功，沒有發生任何錯誤，就會執行這行，回傳 True。
        return True
    # except 區塊用來「捕捉」特定的錯誤。
    # ValueError 是 int() 轉換失敗時 (例如 int('abc')) 會拋出的例外類型。
    except ValueError:
        # 當捕捉到 ValueError 時，程式不會當掉，而是會執行這行，回傳 False。
        return False

# --- Big-O 複雜度觀念提示 (Big-O Notation Basics) ---
# Big-O 用來描述演算法的時間複雜度 (執行時間隨資料量增長的速度) 或空間複雜度。
# list.append 通常是 O(1): 常數時間複雜度。不管串列有多長，把元素加到尾端所花的時間幾乎是一樣且非常快的。
# list 切片 (例如 list[a:b]) 是 O(N): 線性時間複雜度。切片的長度 (N) 越長，複製資料所需的記憶體和時間就越多。
