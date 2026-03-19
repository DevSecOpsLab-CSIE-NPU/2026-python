# R10. 去重且保序（1.10）
# 本程式示範如何實現一個生成器函數來去除序列中的重複元素，同時保持原始順序
# 這對於處理大型數據集或需要保持順序的情況非常有用
# 提供了兩個版本：簡單去重和支援鍵函數的去重

# 定義一個生成器函數 dedupe，用於去除序列中的重複元素並保持順序
# 參數 items：一個可迭代的序列，如列表或元組
# 函數使用集合 seen 來追蹤已經出現過的元素
def dedupe(items):
    # 初始化一個空的集合 seen，用來記錄已經處理過的元素
    # 集合的查找速度很快，適合用來檢查元素是否重複
    seen = set()

    # 遍歷輸入序列中的每個元素
    for item in items:
        # 檢查當前元素是否已經在 seen 集合中
        # 如果不在，表示這是第一次遇到，則處理它
        if item not in seen:
            # 使用 yield 關鍵字將元素返回給調用者
            # 這使得函數成為一個生成器，可以逐個產生結果而不占用大量記憶體
            yield item
            # 將當前元素添加到 seen 集合中，防止之後重複出現
            seen.add(item)

# 定義第二個生成器函數 dedupe2，支援根據鍵函數進行去重
# 參數 items：可迭代序列
# 參數 key：一個函數，用來從每個元素中提取比較的鍵，預設為 None（直接比較元素本身）
# 這允許根據元素的特定屬性進行去重，例如對象列表根據某個欄位去重
def dedupe2(items, key=None):
    # 初始化空的集合 seen，用來記錄已經處理過的鍵值
    seen = set()

    # 遍歷輸入序列中的每個元素
    for item in items:
        # 如果 key 為 None，直接使用元素本身作為比較值
        # 否則，使用 key 函數提取元素的鍵值進行比較
        val = item if key is None else key(item)

        # 檢查提取的鍵值是否已經在 seen 集合中
        if val not in seen:
            # 如果沒有，則產生原始元素（不是鍵值）
            yield item
            # 將鍵值添加到 seen 集合中
            seen.add(val)
