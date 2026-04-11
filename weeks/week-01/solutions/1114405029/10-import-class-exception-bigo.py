# 10 模組、類別、例外與 Big-O (底層邏輯與效能篇)

# === 1. 模組匯入 (Importing Tools) ===
# 好的程式設計不需要「重新造輪子」，而是學會選擇對的工具。
import heapq                # 為了 Top-N 與優先佇列 (高效能)
from collections import deque, Counter, defaultdict  # 為了優化 list 與統計

# 💡 實戰心得：
# - 用 Counter(list) 瞬間完成統計 (Task 3)。
# - 用 defaultdict(int) 解決 key 不存在會報錯的問題。

# === 2. 類別與物件 (Class & Object) ===
# 類別就像「模具」，物件是「成品」。
class User:
    def __init__(self, user_id):
        self.user_id = user_id  # self 代表「這個物件自己」的屬性

# 應用情境：當資料不只是單純的數字，而是像「使用者」這樣有名字、有行為的個體時使用。
user = User("d1114405029")
print(user.user_id)  # 存取物件屬性

# === 3. 例外處理 (Exception Handling) ===
# 語法：try (嘗試做做看) / except (出事了怎麼辦)
val = "abc"
try:
    num = int(val)
except ValueError:
    num = 0  # 如果轉型失敗，給一個預設值，防止程式直接崩潰 (Crash)

# 💡 實戰連結 (Task 2 & 3)：
# 在處理 sys.stdin.read() 時，若遇到空輸入或格式錯誤，
# 使用 try-except 包起來能確保程式「優雅地結束」，這在作業評分中是強健性 (Robustness) 的關鍵。

# === 4. 基本 Big-O 觀念 (效能門檻) ===
# Big-O 是衡量「資料變多時，程式變慢的速度」。
# 
# | 複雜度 | 術語 | 例子 | 實戰感受 |
# | :--- | :--- | :--- | :--- |
# | O(1) | 常數時間 | dict[key], deque.popleft() | 極快！不管資料多大都瞬間完成 |
# | O(log N) | 對數時間 | heapq.heappush() | 非常快，適合處理巨量資料的排序 |
# | O(N) | 線性時間 | for x in list, sum(list) | 資料變兩倍，時間就變兩倍 |
# | O(N log N) | 排序時間 | sorted(list), list.sort() | 內建排序的標準速度 |

# === 5. 實戰工具選擇對照表 ===

# [Case A] 在清單最前面新增/刪除資料：
# - 使用 list.insert(0, x) -> O(N) (超慢，因為後面的人都要往後移)
# - 使用 deque.appendleft(x) -> O(1) (超快，專門處理兩端操作)

# [Case B] 找出一千萬筆資料中的前 10 名：
# - 使用 sorted(list)[:10] -> O(N log N) (把所有資料排好，太浪費了)
# - 使用 heapq.nlargest(10, list) -> O(N log K) (只維護 10 個人的小圈圈，省時省記憶體)