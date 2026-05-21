# A02. with 語句與 Context Manager
# 「借東西要還」——確保資源一定會被釋放，就算程式出錯也一樣
# 對應 Bloom's Taxonomy：應用（Apply）— 能設計並使用自訂的 with 區塊
#
# 本題核心：
# with 語句用來管理「需要使用後釋放」的資源。
#
# 常見資源包含：
# 1. 檔案
# 2. 網路連線
# 3. 資料庫連線
# 4. 暫時修改的系統設定
# 5. 計時器
# 6. 測試時暫時截取輸出
#
# with 的精神可以想成：
# 「進入區塊時借用資源，離開區塊時一定歸還資源。」
#
# 就算 with 區塊裡面發生錯誤，
# Python 也會確保離開時執行清理動作。
#
# Context Manager 中文常翻成「情境管理器」或「上下文管理器」。
# 它的工作就是定義：
# 1. 進入 with 區塊時要做什麼
# 2. 離開 with 區塊時要做什麼

# ── 為什麼需要 with？ ─────────────────────────────────────
# 沒有 with 的開檔方式：如果中途發生例外，close() 可能永遠不會被呼叫
#
# 開檔是一種典型的「借資源」行為。
# 程式向作業系統借用檔案資源，
# 使用完後應該要關閉檔案。
#
# 如果忘記 close()，
# 可能造成：
# 1. 檔案內容沒有正確寫入
# 2. 檔案被鎖住
# 3. 系統資源被浪費
# 4. 程式長時間執行時累積太多未關閉檔案

# 不好的寫法
# f = open("demo.txt", "w")
# f.write("hello")
# f.close()   # 如果 write 出錯，這行就不會執行了
#
# 上面這種寫法的問題是：
# 如果 f.write("hello") 發生錯誤，
# 程式會直接中斷或跳到錯誤處理流程，
# 下面的 f.close() 就可能不會被執行。
#
# 所以這種寫法在安全性與穩定性上比較差。

# 正確的寫法：with 會自動呼叫 close()，即使出錯也一樣
#
# 這裡示範用 with 開檔。
# 當程式進入 with 區塊時，檔案會被打開。
# 當程式離開 with 區塊時，檔案會自動關閉。
print("=== with 開檔：自動關閉 ===")

# open("/tmp/week13_demo.txt", "w")：
# 以寫入模式開啟 /tmp/week13_demo.txt。
#
# "w" 代表 write，也就是寫入模式。
# 如果檔案不存在，Python 會建立新檔案。
# 如果檔案已存在，原本內容會被覆蓋。
#
# as f：
# 把開啟後的檔案物件命名為 f，
# 讓 with 區塊內可以使用 f 寫入資料。
with open("/tmp/week13_demo.txt", "w") as f:
    # 將文字寫入檔案。
    # \n 代表換行符號。
    f.write("Hello from Week 13\n")

# 上面的 with 區塊結束後，
# 檔案已經自動關閉。
#
# 接著再用讀取模式 "r" 開啟同一個檔案。
#
# "r" 代表 read，也就是讀取模式。
with open("/tmp/week13_demo.txt", "r") as f:
    # f.read() 會讀取整個檔案內容。
    #
    # strip() 會移除字串前後的空白與換行，
    # 讓輸出結果更乾淨。
    print(f.read().strip())

# ── 自己寫 Context Manager（用 class）────────────────────
# 需要實作兩個方法：
#   __enter__：進入 with 區塊時執行，回傳值會被 as 接收
#   __exit__ ：離開 with 區塊時執行（不管有沒有出錯）
#
# 如果想自己設計可以搭配 with 使用的物件，
# 就要讓這個物件具備 Context Manager 的能力。
#
# 在 class 寫法中，主要靠兩個特殊方法：
#
# 1. __enter__(self)
#    - 進入 with 區塊時自動執行
#    - 通常用來初始化、取得資源、開始計時
#    - return 的值會交給 as 後面的變數
#
# 2. __exit__(self, exc_type, exc_val, exc_tb)
#    - 離開 with 區塊時自動執行
#    - 不管 with 裡面有沒有發生錯誤，都會執行
#    - 通常用來釋放資源、關閉檔案、結束計時、還原狀態
#
# __exit__ 的三個錯誤相關參數：
# exc_type：錯誤類型
# exc_val ：錯誤物件或錯誤訊息
# exc_tb  ：錯誤追蹤資訊 traceback
#
# 如果 with 區塊裡沒有錯誤，
# 這三個值通常會是 None。

import time

# 匯入 time 模組。
#
# time.time() 可以取得目前時間戳記。
# 常用來計算兩個時間點之間相差多少秒。

class Timer:
    """計時器：進入 with 時開始，離開時印出經過時間"""

    def __enter__(self):
        # __enter__ 會在進入 with 區塊的瞬間自動被呼叫。
        #
        # 這裡把目前時間記錄在 self.start。
        # self.start 代表計時開始的時間點。
        self.start = time.time()

        # 印出提示訊息，表示開始計時。
        print("⏱  開始計時")

        # return self 的意思是：
        # 把目前這個 Timer 物件本身回傳給 as 後面的變數。
        #
        # 例如：
        # with Timer() as t:
        #
        # 這裡的 t 就會接收到 self，
        # 也就是這個 Timer 物件。
        return self   # 這個值會被 as 接收，例如 as t

    def __exit__(self, exc_type, exc_val, exc_tb):
        # __exit__ 會在離開 with 區塊時自動被呼叫。
        #
        # 不管 with 區塊是正常結束，
        # 還是因為錯誤而離開，
        # __exit__ 都會執行。
        #
        # time.time() - self.start：
        # 用目前時間減去開始時間，
        # 得到 with 區塊執行花了幾秒。
        elapsed = time.time() - self.start

        # 用格式化字串印出經過時間。
        #
        # {elapsed:.4f} 代表顯示到小數點後 4 位。
        print(f"⏱  結束：{elapsed:.4f} 秒")

        # return False 的意思是：
        # 如果 with 區塊裡發生錯誤，
        # 不要把錯誤吃掉，讓錯誤繼續往外傳。
        #
        # 這通常是比較安全的做法，
        # 因為錯誤不應該被偷偷忽略。
        return False  # False = 不吃掉例外（讓錯誤繼續往外傳）

# 印出自訂計時器的測試標題。
print("\n=== 自訂計時器 ===")

# 使用自訂的 Timer 搭配 with。
#
# 進入 with 時會執行 Timer.__enter__()。
# 離開 with 時會執行 Timer.__exit__()。
#
# as t 會接收 __enter__ 回傳的 self。
with Timer() as t:
    # sum(range(1_000_000)) 會計算：
    # 0 + 1 + 2 + ... + 999999
    #
    # 這裡用來模擬一段需要花一點時間的運算。
    total = sum(range(1_000_000))

# 離開 with 後，Timer 已經印出執行時間。
#
# 接著印出計算結果。
print(f"計算結果：{total}")

# ── 更簡單的寫法：@contextmanager ─────────────────────────
# 不用寫 class，用 yield 分隔「進入前」和「離開後」
#
# 如果 Context Manager 的邏輯比較簡單，
# 不一定要寫完整 class。
#
# Python 的 contextlib 提供 @contextmanager 裝飾器，
# 可以用一個 generator 函數快速建立 Context Manager。
#
# @contextmanager 的基本概念：
# 1. yield 前面的程式碼 = 進入 with 前要執行的事情
# 2. yield 本身 = with 區塊執行的位置
# 3. yield 後面的程式碼 = 離開 with 後要執行的事情

from contextlib import contextmanager

# 從 contextlib 模組匯入 contextmanager。
#
# contextmanager 可以把含有 yield 的函數，
# 轉換成可以搭配 with 使用的 Context Manager。

@contextmanager
def section(title):
    """印出有邊框的區段標題"""

    # yield 前的程式碼會在進入 with 區塊前執行。
    #
    # 這裡先印出一個空行和一條由 = 組成的分隔線。
    print(f"\n{'='*40}")

    # 印出傳入的區段標題。
    print(f"  {title}")

    # 再印出一條分隔線，形成標題框。
    print(f"{'='*40}")

    # yield 是分界點。
    #
    # 執行到 yield 時，
    # 程式會暫時把控制權交給 with 區塊內的程式碼。
    yield           # ← with 區塊的程式碼在這裡執行

    # with 區塊執行完後，
    # 會回到 yield 後面繼續執行。
    #
    # 這裡印出結尾分隔線。
    print(f"{'─'*40}")

# 印出空行，讓輸出格式比較清楚。
print()

# 使用 section() 這個自訂 Context Manager。
#
# 進入 with 前會先印出標題框。
# with 裡面的內容會被包在這個區段之中。
# 離開 with 後會印出結尾線。
with section("Week 13 CPE 模擬考"):
    print("  題目：UVA 11005 Cheapest Base")
    print("  時間限制：20 分鐘")

# ── CPE 應用：截取 stdout，方便測試輸出 ─────────────────
# 有些 CPE 題目會直接 print 答案
# 測試時可以截取 print 的輸出來比對
#
# 很多競程或 CPE 題目會要求直接印出答案。
# 但在寫單元測試時，如果函數只 print 不 return，
# 就比較不方便直接比對結果。
#
# 這時可以暫時把 sys.stdout 換成 io.StringIO()。
#
# sys.stdout：
# 代表 Python 預設輸出的地方，通常是終端機。
#
# io.StringIO()：
# 代表一個像檔案一樣的記憶體字串緩衝區。
#
# 把 sys.stdout 改成 StringIO 後，
# print() 的內容就不會直接出現在終端機，
# 而是被存進這個字串緩衝區。
#
# 測試結束後，一定要把 sys.stdout 改回原本的值，
# 否則後面的 print 可能會全部被截走。

import io, sys

# 匯入 io 和 sys。
#
# io.StringIO 用來建立記憶體中的文字緩衝區。
# sys.stdout 用來控制 print 的輸出位置。

@contextmanager
def capture_output():
    """暫時把 print 的輸出截取到字串裡"""

    # 先把原本的 sys.stdout 存起來。
    #
    # 這一步非常重要，
    # 因為後面離開 with 區塊時要把它還原。
    old_stdout = sys.stdout

    # 建立一個 StringIO 緩衝區，
    # 並把 sys.stdout 改成這個 buffer。
    #
    # 這行使用連續指定：
    # sys.stdout = buffer = io.StringIO()
    #
    # 等同於：
    # buffer = io.StringIO()
    # sys.stdout = buffer
    #
    # 也就是：
    # 1. 建立 buffer
    # 2. 讓 print 輸出到 buffer
    sys.stdout = buffer = io.StringIO()

    try:
        # yield buffer：
        # 把 buffer 回傳給 with ... as 後面的變數。
        #
        # 例如：
        # with capture_output() as out:
        #
        # 這裡的 out 就會是 buffer。
        #
        # with 區塊裡所有 print 的內容，
        # 都會被寫進這個 buffer。
        yield buffer     # with ... as buf 的 buf 就是這個 buffer

    finally:
        # finally 的特色：
        # 不管 try 裡面有沒有發生錯誤，
        # finally 都一定會執行。
        #
        # 因此這裡可以保證 sys.stdout 一定會被還原。
        sys.stdout = old_stdout   # 一定要還原，finally 保證執行

def solve_parity(n):
    """UVA 10931 Parity：計算 n 的二進位裡有幾個 1"""

    # bin(n) 會把整數 n 轉成二進位字串。
    #
    # 例如：
    # bin(10) 會得到 "0b1010"
    #
    # 前面的 "0b" 是 Python 表示二進位的前綴。
    bits = bin(n)[2:]

    # [2:] 表示從索引 2 開始取到最後，
    # 也就是去掉前面的 "0b"。
    #
    # 例如：
    # "0b1010"[2:] 會得到 "1010"。

    # count('1') 會計算 bits 字串中有幾個字元 '1'。
    #
    # 這就是二進位中 1 的個數。
    ones = bits.count('1')

    # 按照 UVA 10931 題目常見格式輸出。
    #
    # ones % 2 是 parity 的奇偶值：
    # 如果 ones 是偶數，ones % 2 為 0。
    # 如果 ones 是奇數，ones % 2 為 1。
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")

# 印出截取輸出測試區塊標題。
print("\n=== 截取輸出（測試用）===")

# 使用 capture_output() 暫時截取 print 的輸出。
#
# 在這個 with 區塊中，
# print 不會直接輸出到終端機，
# 而是被寫進 out 這個 StringIO 緩衝區。
with capture_output() as out:
    # solve_parity() 內部會使用 print。
    # 因為目前 stdout 被改成 out，
    # 所以這些輸出會被截取。
    solve_parity(10)
    solve_parity(7)

# 離開 with 區塊後，
# capture_output() 的 finally 會執行，
# sys.stdout 已經被還原成原本的終端機輸出。
#
# out.getvalue() 可以取得剛剛被截取到的全部文字內容。
captured = out.getvalue()

# 印出提示文字。
print("截取到的輸出：")

# 印出剛剛截取到的內容。
print(captured)

# 可以直接拿來做 assertEqual
#
# 在真正寫 unittest 時，
# 可以把 captured 和預期答案字串拿來比較。
#
# 例如：
# self.assertEqual(captured, expected_output)
lines = captured.strip().split('\n')

# captured.strip()：
# 移除前後多餘空白與換行。
#
# split('\n')：
# 依照換行符號切成多行。
#
# 這樣 lines 就會是一個 list，
# 每個元素代表一行輸出。
print(f"共 {len(lines)} 行輸出")

# 記憶重點 ──────────────────────────────────────────────────
# __enter__ → 進入 with 時執行，回傳值被 as 接收
# __exit__  → 離開 with 時執行（出錯也會執行）
# @contextmanager + yield → 更簡單的寫法，yield 前是 enter，yield 後是 exit
# 常用場景：開檔、計時、測試輸出截取、任何「借了要還」的資源
#
# 總結：
# 1. with 可以確保資源使用完後一定會被釋放。
# 2. open() 搭配 with 可以自動 close 檔案。
# 3. 自訂 Context Manager 可以用 class 寫 __enter__ 和 __exit__。
# 4. 簡單的 Context Manager 可以用 @contextmanager 和 yield 寫。
# 5. __exit__ 回傳 False 代表不隱藏錯誤。
# 6. try/finally 很適合用來保證資源一定會還原。
# 7. 截取 stdout 很適合測試只會 print、不會 return 的競程函數。