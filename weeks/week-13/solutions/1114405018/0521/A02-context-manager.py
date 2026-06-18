# A02. with 語句與 Context Manager（情境管理器）
# =============================================================================
# 什麼是 Context Manager？
#   Context Manager 是 Python 中「資源管理」的標準模式。
#   核心概念：「借東西要還」—— 確保資源一定會被釋放，就算程式出錯也一樣。
#
# 為什麼需要？
#   當你開啟檔案、連線資料庫、鎖定執行緒⋯⋯這些資源用完必須歸還。
#   如果忘記 close()，或程式在 close() 之前就出錯，資源就會永遠被佔住。
#   with 語句可以保證「無論如何都會執行清理動作」。
#
# 生活比喻：
#   你向圖書館借了一本書（open），看完一定要還（close）。
#   with 就像圖書館的自動還書機：不管你什麼時候離開，
#   它都會自動幫你把書還掉，不用自己擔心。
#
# 對應 Bloom's Taxonomy：應用（Apply）— 能設計並使用自訂的 with 區塊
# =============================================================================


# ═════════════════════════════════════════════════════════════════════════════
# 為什麼需要 with？—— 對比「沒有 with」和「有 with」
# ═════════════════════════════════════════════════════════════════════════════
# 不好的寫法（沒有 with）：
#   f = open("demo.txt", "w")
#   f.write("hello")
#   f.close()   # 如果 write 出錯，這行就不會執行，檔案永遠不會關閉
#
# 錯誤可能發生在 write() 時（例如磁碟空間不足），
# 這時 close() 根本不會被執行，檔案句柄就被浪費了。
# 如果這種情況一直發生，作業系統可能會說「開啟太多檔案」。

# 正確的寫法：with 會自動呼叫 close()，即使出錯也一樣
print("=== with 開檔：自動關閉 ===")
with open("/tmp/week13_demo.txt", "w") as f:
    f.write("Hello from Week 13\n")

with open("/tmp/week13_demo.txt", "r") as f:
    print(f.read().strip())


# ═════════════════════════════════════════════════════════════════════════════
# 自己寫 Context Manager（用 class）
# ═════════════════════════════════════════════════════════════════════════════
# 要讓一個 class 支援 with，必須實作兩個特殊方法：
#
#   __enter__(self)：
#       進入 with 區塊時自動執行。
#       回傳值會被 as 關鍵字接收（例如 as t）。
#       通常回傳 self，或回傳某個需要使用的資源。
#
#   __exit__(self, exc_type, exc_val, exc_tb)：
#       離開 with 區塊時自動執行。
#       三個參數用來接收例外資訊：
#         - exc_type：例外型別（如果沒有例外就是 None）
#         - exc_val：例外實例（如果沒有例外就是 None）
#         - exc_tb：追蹤資訊（如果沒有例外就是 None）
#       回傳值：
#         - True：吃掉例外（不讓錯誤繼續往上傳）
#         - False：不處理例外（讓錯誤繼續往外傳，預設行為）

import time

class Timer:
    """計時器：進入 with 時開始計時，離開時印出經過時間

    使用方式：
        with Timer() as t:
            # 要做的事情
    """

    def __enter__(self):
        """進入 with 區塊時執行：記錄開始時間"""
        self.start = time.time()
        print("⏱  開始計時")
        return self   # 這個值會被 as 接收，例如 as t

    def __exit__(self, exc_type, exc_val, exc_tb):
        """離開 with 區塊時執行：計算並印出經過時間

        注意：
            exc_type, exc_val, exc_tb 只有在發生例外時才有值
            如果正常結束，這三個都是 None
        """
        elapsed = time.time() - self.start
        print(f"⏱  結束：{elapsed:.4f} 秒")
        # 回傳 False 代表「不處理例外」，讓錯誤繼續往上傳
        # 如果回傳 True，例外就會被這裡吃掉，外面 catch 不到
        return False

print("\n=== 自訂計時器 ===")
with Timer() as t:
    total = sum(range(1_000_000))
print(f"計算結果：{total}")


# ═════════════════════════════════════════════════════════════════════════════
# 更簡單的寫法：@contextmanager 裝飾器
# ═════════════════════════════════════════════════════════════════════════════
# 不用寫 class 和 __enter__ / __exit__，只要：
#   1. 寫一個普通函數
#   2. 加上 @contextmanager 裝飾器
#   3. 用 yield 分隔「進入前」和「離開後」
#
# 原理：
#   yield 之前的程式碼 = __enter__ 要做的事
#   yield 本身的回傳值 = as 要接收的值
#   yield 之後的程式碼 = __exit__ 要做的事（不論有無例外都會執行）

from contextlib import contextmanager

@contextmanager
def section(title):
    """印出有邊框的區段標題

    yield 之前的程式會在進入 with 時執行
    yield 之後的程式會在離開 with 時執行
    """
    print(f"\n{'='*40}")
    print(f"  {title}")
    print(f"{'='*40}")
    yield           # ← with 區塊的程式碼在這裡執行
    print(f"{'─'*40}")

print()
with section("Week 13 CPE 模擬考"):
    print("  題目：UVA 11005 Cheapest Base")
    print("  時間限制：20 分鐘")


# ═════════════════════════════════════════════════════════════════════════════
# CPE 應用：截取 stdout，方便測試輸出
# ═════════════════════════════════════════════════════════════════════════════
# 有些 CPE 題目會直接 print 答案。
# 測試時，我們希望可以「攔截」print 的輸出，跟預期結果比對。
# 用 Context Manager 可以優雅地做到：
#   1. 進入時：把 sys.stdout 換成一個 StringIO 物件
#   2. 離開時：把 sys.stdout 還原回原本的
#   3. 中間所有 print 的內容都會被寫入 StringIO

import io, sys

@contextmanager
def capture_output():
    """暫時把 print 的輸出截取到字串裡

    使用方式：
        with capture_output() as buf:
            print("這段話不會出現在畫面上")
        captured = buf.getvalue()   # 取得截取的內容

    實作細節：
        sys.stdout 是 Python 的「標準輸出」通道
        print() 實際上就是呼叫 sys.stdout.write()
        把 sys.stdout 換成自訂的 buffer，print 的內容就會被導向 buffer
    """
    old_stdout = sys.stdout          # 先保存原本的 stdout
    sys.stdout = buffer = io.StringIO()  # 換成 StringIO 物件
    try:
        yield buffer     # with ... as buf 的 buf 就是這個 buffer
    finally:
        sys.stdout = old_stdout   # 一定要還原，finally 保證一定會執行

def solve_parity(n):
    """UVA 10931 Parity：計算 n 的二進位裡有幾個 1

    題目要求輸出格式：
        "The parity of {二進位字串} is {1 的個數} (mod 2 is {奇偶性})."
    """
    bits = bin(n)[2:]             # bin(10) → '0b1010'，去掉 '0b'
    ones = bits.count('1')        # 計算 1 的個數
    print(f"The parity of {bits} is {ones} (mod 2 is {ones % 2}).")

print("\n=== 截取輸出（測試用）===")
with capture_output() as out:
    solve_parity(10)
    solve_parity(7)

captured = out.getvalue()
print("截取到的輸出：")
print(captured)

# 截取下來的內容可以直接拿來做 assertEqual
lines = captured.strip().split('\n')
print(f"共 {len(lines)} 行輸出")


# ═════════════════════════════════════════════════════════════════════════════
# 記憶重點
# ═════════════════════════════════════════════════════════════════════════════
# 1. __enter__：
#    進入 with 時執行，回傳值被 as 接收
# 2. __exit__：
#    離開 with 時執行（出錯也會執行）
#    三個參數：exc_type, exc_val, exc_tb（沒例外時都是 None）
#    回傳 True 吃掉例外，False 讓例外繼續傳
# 3. @contextmanager + yield：
#    更簡單的寫法，yield 前 = enter，yield 後 = exit
# 4. 常用場景：
#    - 開檔（自動 close）
#    - 計時（自動計算經過時間）
#    - 測試輸出截取（自動還原 stdout）
#    - 資料庫連線（自動歸還連線）
#    - 鎖定（自動解鎖）
# 5. 關鍵觀念：
#    Context Manager 的核心就是「不管怎樣，離開時要做 cleanup」
