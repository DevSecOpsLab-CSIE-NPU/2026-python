"""
R02：例外處理基本用法（記憶層 — 直接複製可執行）

對應 Cookbook：
- 14.6 處理多個例外
- 14.7 捕獲所有例外
- 14.8 建立自定義例外

涵蓋的主題：
  A. try/except/else/finally 完整結構
  B. 14.6 用 tuple 處理多種例外 vs 多個 except 子句
  C. try/else：沒拋例外時才執行
  D. try/finally：無論如何都要清理資源
  E. 14.7 except Exception vs 裸 except:
  F. 14.8 自定義例外類別與繼承層級
  G. raise from：例外鏈（包裝底層錯誤）
  H. bare raise：在 except 區塊中重新拋出

執行：
    python R02-exceptions-basic.py
"""
import traceback
import sys


# ==========================================================
# A — 完整的 try/except/else/finally 結構
# Python 的例外處理語法可以組合四種區塊
# ==========================================================
def demo_try_structure(filename):
    """展示 try/except/else/finally 的完整流程。

    try:     可能拋例外的危險操作
    except:  發生例外時的处理
    else:    沒有發生例外時執行（可省略）
    finally: 無論有沒有例外都會執行（可省略）
    """
    try:
        f = open(filename, "r")
        content = f.read()
    except FileNotFoundError:
        print(f"[A] 檔案 {filename} 不存在")
        return None
    except PermissionError:
        print(f"[A] 沒有權限讀取 {filename}")
        return None
    else:
        # 只有當 try 區塊成功完成（沒拋例外）時才會進 else
        print(f"[A] 成功讀取 {filename}，共 {len(content)} 字元")
        return content
    finally:
        # 不管有沒有例外，finally 一定會執行
        # 適合用來關閉檔案、釋放資源
        print(f"[A] finally：清理資源（{filename}）")


# ==========================================================
# B — 14.6 處理多種例外
# 兩種寫法：（1）同一 except 用 tuple  （2）多個 except 子句
# ==========================================================

def parse_value_tuple(s):
    """用 tuple 把多種例外寫在同一個 except 裡。
    適用於：不同例外要做「相同處理」（例如都回傳 None 並印 log）。"""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        # int("abc")    → ValueError
        # int(None)     → TypeError
        print(f"[B/tuple] 解析失敗 {type(e).__name__}: {e}")
        return None


def parse_value_multi(s):
    """用多個 except 子句分別處理不同的例外。
    適用於：不同例外要做「不同處理」。"""
    try:
        return int(s)
    except ValueError:
        # 格式錯誤（例如 "abc"）→ 提示使用者檢查格式
        print(f"[B/multi] 格式錯誤：無法將 '{s}' 轉為數字")
        return 0
    except TypeError:
        # 型別錯誤（例如 None）→ 回傳預設值
        print(f"[B/multi] 型別錯誤：不支援的型別 {type(s).__name__}")
        return -1


def divide_numbers(a, b):
    """示範 except 子句的順序很重要：
    子類別要寫在前面，父類別寫在後面。
    如果父類別先被比對到，子類別的 except 就永遠不會被執行。"""
    try:
        result = a / b
    except ZeroDivisionError:
        # ZeroDivisionError 是 ArithmeticError 的子類別
        # 一定要寫在 ArithmeticError 前面
        print("[B/順序] 除以零！")
        return float("inf")
    except ArithmeticError:
        # 其他算術錯誤（如 OverflowError）
        print(f"[B/順序] 其他算術錯誤")
        return None
    else:
        return result


# ==========================================================
# C — try/else：沒有拋例外時才執行
# else 區塊只在 try 完全成功時執行，except 區塊則跳過
# ==========================================================

def process_data(data):
    """else 區塊的典型用途：成功後的後續處理。"""
    try:
        value = int(data)
    except (ValueError, TypeError) as e:
        print(f"[C] 轉換失敗: {e}")
        return None
    else:
        # 只有當 int(data) 成功時才會執行這裡
        print(f"[C] 轉換成功，value = {value}")
        return value * 2


# ==========================================================
# D — try/finally：無論如何都要清理資源
# finally 總是會執行，即使 try 或 except 中有 return/break/continue
# ==========================================================

def demo_finally():
    """示範 finally 在 return 之後仍然會執行。"""
    try:
        print("[D] try：準備回傳 42")
        return 42
    finally:
        # 注意：return 42 雖然會執行，但 finally 會搶在 return 生效前先跑
        print("[D] finally：return 之前我一定會執行！")


def safe_divide_with_finally(a, b):
    """finally 常用來關閉資源，確保不會遺漏。"""
    print(f"[D] 計算 {a} / {b}")
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"[D] 捕獲例外: {e}")
        return None
    finally:
        # 不管成功或失敗，這裡都會執行
        # 如果是真實的檔案、網路連線，就在這裡關閉
        print(f"[D] finally：清理完畢")


# ==========================================================
# E — 14.7 捕獲所有例外
# 原則：用 except Exception 而不是裸 except:
# 裸 except: 會捕獲 SystemExit / KeyboardInterrupt 等不該抓的例外
# ==========================================================

def safe_run_good(func, *args):
    """正確寫法：except Exception 只捕獲 Exception 的子類別。
    不會抓到 SystemExit、KeyboardInterrupt、GeneratorExit。"""
    try:
        return func(*args)
    except Exception as e:
        print(f"[E/good] {type(e).__name__}: {e}")
        # traceback.print_exc() 印出完整的呼叫堆疊
        traceback.print_exc()
        return None


def safe_run_bad(func, *args):
    """錯誤寫法：裸 except 會連 KeyboardInterrupt（Ctrl+C）都吃掉，
    導致程式無法被中斷，應該避免。"""
    try:
        return func(*args)
    except:  # 等同於 except BaseException，不建議！
        print("[E/bad] 裸 except: 抓到例外，但不知道是哪一種")
        return None


def safe_run_specific(func, error_callback=None, *args):
    """進階：except Exception + 自訂回呼函式來處理不同例外。"""
    try:
        return func(*args)
    except Exception as e:
        if error_callback:
            error_check(e)
            # 可以依據例外型別做不同處理
            if isinstance(e, ValueError):
                print(f"[E/進階] ValueError 特殊處理")
            elif isinstance(e, ZeroDivisionError):
                print(f"[E/進階] 數學錯誤")
        print(f"[E/進階] 發生例外: {type(e).__name__}")
        traceback.print_exc(limit=1, file=sys.stdout)  # 只印一行
        return None


def error_check(e):
    """檢查例外的輔助函式。"""
    print(f"[E/進階] 回呼：例外類型 = {type(e).__name__}")


# ==========================================================
# F — 14.8 自定義例外類別與繼承層級
# 自訂例外一律繼承 Exception（不是 BaseException）
# 可以建立繼承層級，讓上層用一個 except 捕獲整群例外
# ==========================================================

class NetworkError(Exception):
    """所有網路相關錯誤的基底類別。
    繼承 Exception 而非 BaseException，因為我們不需要抓到 KeyboardInterrupt。"""


class HostnameError(NetworkError):
    """找不到主機時拋出。"""


class ConnectionTimeout(NetworkError):
    """連線逾時，攜帶 host 與 seconds 供上層判斷。"""
    def __init__(self, host, seconds):
        super().__init__(f"連線 {host} 超過 {seconds} 秒")
        self.host = host
        self.seconds = seconds


class ProtocolError(NetworkError):
    """通訊協定錯誤，攜帶 status_code。"""
    def __init__(self, host, status_code):
        super().__init__(f"{host} 回應狀態碼 {status_code}")
        self.host = host
        self.status_code = status_code


class AuthError(NetworkError):
    """認證失敗。"""


def connect(host, timeout):
    """模擬連線：根據不同條件拋出自定義例外。"""
    if host == "" or host is None:
        raise HostnameError("主機名稱為空")
    if timeout < 1:
        raise ConnectionTimeout(host, timeout)
    if host == "badhost.com":
        raise ProtocolError(host, 500)
    if host == "unauthorized.com":
        raise AuthError("認證失敗")
    return f"connected to {host}"


# ==========================================================
# G — raise from：例外鏈
# 在 except 區塊中拋出新例外時，用 raise X from e 保留原始 traceback
# ==========================================================

def fetch_data_from_file(filename):
    """包裝底層例外：把 FileNotFoundError 重新包裝成自定義例外。"""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        # raise from 會把原始例外 e 附在 __cause__ 屬性上
        # 除錯時可以看到完整的例外鏈
        raise RuntimeError(f"無法讀取資料檔案: {filename}") from e
    except PermissionError as e:
        raise RuntimeError(f"沒有權限存取: {filename}") from e


def demo_raise_from():
    """示範 raise from 的例外鏈輸出。"""
    try:
        fetch_data_from_file("/tmp/nonexistent_file_xyz.txt")
    except RuntimeError as e:
        print(f"[G] 捕獲: {e}")
        print(f"[G] 原始原因 (__cause__): {e.__cause__}")
        # 如果想知道完整鏈：traceback.print_exc()


# ==========================================================
# H — bare raise：在 except 區塊中重新拋出同一例外
# 適合：記錄 log 之後讓例外繼續往上傳
# ==========================================================

def process_user_data(data):
    """bare raise 保留完整的 traceback，不中斷例外傳遞。"""
    try:
        return int(data)
    except ValueError:
        # 先記錄錯誤，再讓例外繼續往上拋
        print(f"[H] 記錄：輸入 '{data}' 無法轉為整數，準備重新拋出")
        raise  # bare raise → 原來的 ValueError 繼續往外傳


def wrapper_function(data):
    """包裝函式：呼叫 process_user_data 並處理其例外。"""
    try:
        result = process_user_data(data)
        print(f"[H] 成功: {result}")
    except ValueError:
        print(f"[H] 上層也接到 ValueError")
        # 這裡不能再 bare raise，因為不在 except 區塊中


# ==========================================================
# I — sys.exc_info()：取得當前例外資訊
# 在 except 區塊中呼叫，可以拿到 (type, value, traceback) 三元組
# ==========================================================

def inspect_exception():
    """使用 sys.exc_info() 取得例外詳細資訊。"""
    try:
        1 / 0
    except ZeroDivisionError:
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(f"[I] 例外型別: {exc_type.__name__}")
        print(f"[I] 例外訊息: {exc_value}")
        print(f"[I] traceback 物件: {exc_tb}")
        # traceback 物件可以傳給 traceback 模組進一步處理
        traceback.print_tb(exc_tb)


# ==========================================================
# 主程式：依序展示各節功能
# ==========================================================
if __name__ == "__main__":
    print("=" * 60)
    print("A — 完整的 try/except/else/finally 結構")
    print("=" * 60)
    demo_try_structure("/tmp/nonexistent_file.txt")
    print()

    print("=" * 60)
    print("B — 14.6 多種例外處理")
    print("=" * 60)
    print("--- tuple 寫法 ---")
    parse_value_tuple("abc")
    parse_value_tuple(None)
    print("--- 多個 except 寫法 ---")
    parse_value_multi("abc")
    parse_value_multi(None)
    print("--- except 順序 ---")
    print(f"  10 / 0 = {divide_numbers(10, 0)}")
    print(f"  10 / 2 = {divide_numbers(10, 2)}")
    print()

    print("=" * 60)
    print("C — try/else：沒拋例外才執行 else")
    print("=" * 60)
    process_data("42")
    process_data("abc")
    print()

    print("=" * 60)
    print("D — try/finally：無論如何都執行")
    print("=" * 60)
    result = demo_finally()
    print(f"  finally 執行完後才真正回傳: {result}")
    print()
    safe_divide_with_finally(10, 0)
    print()
    safe_divide_with_finally(10, 2)
    print()

    print("=" * 60)
    print("E — 14.7 捕獲所有例外")
    print("=" * 60)
    print("--- except Exception（正確）---")
    safe_run_good(lambda: 1 / 0)
    print("--- 裸 except（不建議）---")
    safe_run_bad(lambda: 1 / 0)
    print()

    print("=" * 60)
    print("F — 14.8 自定義例外")
    print("=" * 60)
    for host, t in [("example.com", 5), ("", 5), ("badhost.com", 5), ("unauthorized.com", 5), ("slow.com", 0)]:
        try:
            print(f"  connect({host}, {t}) => {connect(host, t)}")
        except HostnameError as e:
            print(f"  接到 HostnameError: {e}")
        except ConnectionTimeout as e:
            print(f"  接到 ConnectionTimeout: host={e.host}, seconds={e.seconds}")
        except ProtocolError as e:
            print(f"  接到 ProtocolError: host={e.host}, status={e.status_code}")
        except AuthError as e:
            print(f"  接到 AuthError: {e}")
    print()

    print("=" * 60)
    print("G — raise from 例外鏈")
    print("=" * 60)
    demo_raise_from()
    print()

    print("=" * 60)
    print("H — bare raise 重新拋出")
    print("=" * 60)
    wrapper_function("42")
    wrapper_function("abc")
    print()

    print("=" * 60)
    print("I — sys.exc_info()")
    print("=" * 60)
    inspect_exception()
