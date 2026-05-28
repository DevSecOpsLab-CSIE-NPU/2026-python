"""
R02：例外處理基本用法（記憶層）

對應 Cookbook：
- 14.6 處理多個例外
- 14.7 捕獲所有例外
- 14.8 建立自定義例外

執行：
    python R02-exceptions-basic.py
"""

# traceback 模組：
# 用來印出完整的錯誤追蹤資訊，也就是「錯誤發生的位置與呼叫流程」
#
# 平常 Python 發生錯誤時，終端機會顯示 Traceback
# 這個模組可以讓我們在 except 裡面手動印出類似的錯誤堆疊資訊
import traceback


# ---------- 14.6 多個例外 ----------
# parse_value(s)：
# 功能：
#   嘗試把傳入的 s 轉換成整數 int
#
# 這個範例重點：
#   示範如何在同一個 except 裡面
#   同時處理多種可能發生的例外
def parse_value(s):

    # 函式說明字串 docstring
    # 說明這個函式示範：
    #   在 except 後面使用 tuple
    #   一次列出多個要捕捉的例外類別
    """同一個 except 用 tuple 列出多種例外類別"""

    # try 區塊：
    # 放「可能會發生錯誤」的程式碼
    try:

        # int(s)：
        # 嘗試把 s 轉成整數
        #
        # 可能成功：
        #   int("123") → 123
        #
        # 可能失敗：
        #   int("abc") 會產生 ValueError
        #   int(None) 會產生 TypeError
        return int(s)

    # except (ValueError, TypeError) as e：
    # 同時捕捉 ValueError 與 TypeError
    #
    # ValueError：
    #   資料型態可以處理，但內容不合法
    #   例如 int("abc")
    #
    # TypeError：
    #   資料型態本身不適合
    #   例如 int(None)
    #
    # as e：
    #   把捕捉到的例外物件存到變數 e
    except (ValueError, TypeError) as e:

        # type(e).__name__：
        # 取得例外類別的名稱
        # 例如 ValueError 或 TypeError
        #
        # {e}：
        # 取得例外訊息本身
        #
        # 這行會印出錯誤類型與錯誤原因
        print(f"[14.6] 解析失敗 {type(e).__name__}: {e}")

        # 發生錯誤時回傳 None
        # 代表這次解析失敗，但程式不中斷
        return None


# ---------- 14.7 捕獲所有例外 ----------
# safe_run(func, *args)：
# 功能：
#   安全地執行某個函式 func
#   如果 func 執行成功，就回傳執行結果
#   如果 func 發生例外，就捕捉錯誤並印出訊息
#
# 這個範例重點：
#   示範 except Exception as e
#   用來捕捉大多數一般程式錯誤
def safe_run(func, *args):

    # 函式說明字串 docstring
    #
    # except Exception：
    #   會捕捉大多數一般例外
    #
    # 裸 except：
    #   指的是直接寫 except:
    #   這樣會連 KeyboardInterrupt、SystemExit 這類特殊中斷也抓到
    #   通常不建議這樣寫
    """except Exception，而不是裸 except:（裸 except 會抓到 KeyboardInterrupt）"""

    # try 區塊：
    # 嘗試執行傳進來的函式
    try:

        # func(*args)：
        # 呼叫 func，並把 args 裡面的參數拆開傳進去
        #
        # 例如：
        #   safe_run(pow, 2, 3)
        #
        # 等同於：
        #   pow(2, 3)
        return func(*args)

    # except Exception as e：
    # 捕捉大多數一般程式執行錯誤
    #
    # 例如：
    #   ZeroDivisionError
    #   ValueError
    #   TypeError
    #   FileNotFoundError
    #
    # 注意：
    #   Exception 不會捕捉所有 BaseException 的子類別
    #   例如 KeyboardInterrupt 通常不會被這裡攔住
    except Exception as e:

        # 印出錯誤類型與錯誤訊息
        print(f"[14.7] 發生例外 {type(e).__name__}: {e}")

        # traceback.print_exc()：
        # 印出完整錯誤追蹤資訊
        #
        # 可以看到：
        #   1. 錯誤發生在哪一行
        #   2. 呼叫流程
        #   3. 最後的例外類型與訊息
        #
        # 這在除錯時非常有用
        traceback.print_exc()


# ---------- 14.8 自定義例外 ----------
# 自定義例外：
#   自己建立專案需要的錯誤類別
#
# 好處：
#   1. 錯誤分類更清楚
#   2. 上層程式可以針對不同錯誤做不同處理
#   3. 比單純使用 ValueError / RuntimeError 更有語意
#
# 這裡建立一組和「網路連線」相關的例外類別


# NetworkError：
# 所有網路相關錯誤的共同父類別
#
# 繼承 Exception：
#   表示它是一般程式錯誤
#
# 不繼承 BaseException：
#   因為 BaseException 是更底層的例外基底
#   KeyboardInterrupt、SystemExit 也屬於 BaseException
#   一般自定義例外通常應該繼承 Exception
class NetworkError(Exception):

    # 類別說明字串 docstring
    # 說明這個類別是所有網路錯誤的基底類別
    """所有網路錯誤的基底類別；繼承 Exception 而不是 BaseException"""


# HostnameError：
# 表示主機名稱相關錯誤
#
# 繼承 NetworkError：
#   代表 HostnameError 也是一種 NetworkError
#
# 因此：
#   except NetworkError
# 可以捕捉 HostnameError
class HostnameError(NetworkError):

    # 類別說明字串 docstring
    # 說明這個錯誤代表找不到主機或主機名稱不合法
    """找不到主機"""


# ConnectionTimeout：
# 表示連線逾時錯誤
#
# 繼承 NetworkError：
#   代表 ConnectionTimeout 也是一種 NetworkError
#
# 這個類別有自訂 __init__
# 因為它除了錯誤訊息之外
# 還想額外保存 host 與 seconds 兩個屬性
class ConnectionTimeout(NetworkError):

    # 類別說明字串 docstring
    # 說明這個錯誤會附帶 host / seconds 屬性
    # 方便上層程式判斷是哪個主機、幾秒後逾時
    """連線逾時，附帶 host / seconds 屬性，方便上層判斷"""

    # __init__(self, host, seconds)：
    # 建構子
    #
    # 當建立 ConnectionTimeout(host, seconds) 物件時會自動執行
    #
    # host：
    #   發生逾時的主機名稱
    #
    # seconds：
    #   逾時秒數
    def __init__(self, host, seconds):

        # super().__init__(...)：
        # 呼叫父類別 Exception / NetworkError 的初始化方法
        #
        # 這裡傳入的字串會成為例外訊息
        #
        # 例如：
        #   ConnectionTimeout("slow.com", 0)
        #
        # 錯誤訊息會是：
        #   連線 slow.com 超過 0 秒
        super().__init__(f"連線 {host} 超過 {seconds} 秒")

        # self.host：
        # 把發生錯誤的主機名稱存成物件屬性
        #
        # 之後如果 except ConnectionTimeout as e
        # 就可以透過 e.host 取得 host
        self.host = host

        # self.seconds：
        # 把逾時秒數存成物件屬性
        #
        # 之後可以透過 e.seconds 取得秒數
        self.seconds = seconds


# connect(host, timeout)：
# 功能：
#   模擬連線到某個主機
#
# host：
#   主機名稱
#
# timeout：
#   允許等待的秒數
#
# 這個函式會根據不同錯誤情況
# 丟出不同的自定義例外
def connect(host, timeout):

    # 如果 host 是空字串
    # 代表沒有提供有效主機名稱
    if host == "":

        # raise HostnameError(...)：
        # 主動丟出 HostnameError 例外
        #
        # 因為 HostnameError 繼承 NetworkError
        # 所以可以被 except NetworkError 捕捉
        raise HostnameError("主機名稱為空")

    # 如果 timeout 小於 1
    # 代表等待時間太短，不符合連線需求
    if timeout < 1:

        # raise ConnectionTimeout(host, timeout)：
        # 主動丟出連線逾時錯誤
        #
        # 這個例外會保存：
        #   1. host
        #   2. timeout 秒數
        #   3. 錯誤訊息
        raise ConnectionTimeout(host, timeout)

    # 如果 host 不為空，而且 timeout 合理
    # 就回傳連線成功的字串
    return f"connected to {host}"


# 主程式進入點
#
# 如果這個檔案是直接執行：
#   __name__ 會等於 "__main__"
#
# 如果這個檔案是被其他檔案 import：
#   __name__ 不會等於 "__main__"
#
# 這樣可以避免別人 import 這個檔案時
# 底下的示範程式自動執行
if __name__ == "__main__":

    # 顯示 14.6 範例標題
    print("--- 14.6 ---")

    # 測試 parse_value("abc")
    #
    # "abc" 是字串型態，但內容不是合法整數
    # int("abc") 會發生 ValueError
    #
    # parse_value 會捕捉 ValueError
    # 印出錯誤訊息並回傳 None
    parse_value("abc")

    # 測試 parse_value(None)
    #
    # None 不是可以直接轉成整數的型態
    # int(None) 會發生 TypeError
    #
    # parse_value 會捕捉 TypeError
    # 印出錯誤訊息並回傳 None
    parse_value(None)

    # 顯示 14.7 範例標題
    print("\n--- 14.7 ---")

    # safe_run(lambda: 1 / 0)
    #
    # lambda: 1 / 0：
    #   建立一個匿名函式
    #   執行時會做 1 / 0
    #
    # 1 / 0 會發生 ZeroDivisionError
    #
    # safe_run 會用 except Exception 捕捉這個錯誤
    # 並印出錯誤訊息與 traceback
    safe_run(lambda: 1 / 0)

    # 顯示 14.8 範例標題
    print("\n--- 14.8 ---")

    # for host, t in [...]：
    # 依序測試三組連線資料
    #
    # 第一組：
    #   host = "example.com"
    #   t = 5
    #   應該成功
    #
    # 第二組：
    #   host = ""
    #   t = 5
    #   host 空字串，會丟出 HostnameError
    #
    # 第三組：
    #   host = "slow.com"
    #   t = 0
    #   timeout 小於 1，會丟出 ConnectionTimeout
    for host, t in [("example.com", 5), ("", 5), ("slow.com", 0)]:

        # try：
        # 嘗試執行 connect(host, t)
        try:

            # 如果 connect 成功
            # 就印出連線成功訊息
            print(connect(host, t))

        # except NetworkError as e：
        # 捕捉所有 NetworkError 類型的錯誤
        #
        # 因為 HostnameError 與 ConnectionTimeout
        # 都繼承 NetworkError
        #
        # 所以這兩種錯誤都可以在這裡被統一處理
        except NetworkError as e:

            # type(e).__name__：
            # 取得實際發生的例外類別名稱
            # 可能是：
            #   HostnameError
            #   ConnectionTimeout
            #
            # {e}：
            # 印出例外訊息
            print(f"接到 {type(e).__name__}: {e}")