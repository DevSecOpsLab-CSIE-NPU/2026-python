# R2. 解包數量不固定：星號解包（1.2）
#
# 「星號解包（*unpacking）」用途：
# - 當你不知道中間或尾端會有幾個元素時，用 * 來一次接住「剩下的多個值」。
# - * 變數接到的永遠是 list（即使原本來源是 tuple）。
# - 一個解包式中只能有一個 * 變數。

def drop_first_last(grades):
    # 這行表示：
    # - first 取第一個成績
    # - last  取最後一個成績
    # - middle 取中間所有成績（數量可變，型別是 list）
    # 例如 grades = [98, 87, 91, 75, 88]
    # -> first=98, middle=[87, 91, 75], last=88
    first, *middle, last = grades

    # 回傳「中間成績」的平均。
    # 這種寫法常用在「忽略最高分/最低分」情境。
    # 注意：若 grades 元素太少，middle 可能為空，len(middle)=0 會造成除以零錯誤。
    return sum(middle) / len(middle)


# 一筆聯絡資訊：姓名、email、後面接任意數量電話
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')

# 解包規則：
# - name 取第 1 個
# - email 取第 2 個
# - phone_numbers 用 * 接住剩下全部（可 0 個、1 個或多個）
# 這讓資料欄位長度更有彈性。
name, email, *phone_numbers = record


# * 也可放在左邊，表示「前面全部給 trailing，最後一個給 current」
# -> trailing = [10, 8, 7, 1, 9, 5, 10]
# -> current  = 3
# 常見於時間序列：取最新值 current，其他歸類為歷史資料 trailing。
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]


# 讀懂這份程式的實戰步驟：
# 1. 先找左邊哪個變數前面有 *，它就是「可變長度接收器」。
# 2. 沒有 * 的變數，通常代表固定位置（例如第一個、最後一個）。
# 3. 心中模擬資料分配：先滿足固定位置，剩下都丟給 * 變數。
# 4. 檢查邊界條件：資料太短時，是否會出現空 list 或除以零。
