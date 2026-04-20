# R10. 去重且保序（1.10）

# 定義一個函式 dedupe，用於從序列中移除重複元素，同時保持元素的原始順序。
# 這個函式是一個生成器函式，它會惰性地產生不重複的元素。
def dedupe(items):
    # 創建一個空集合 seen，用於儲存已經見過的元素。
    seen = set()
    # 遍歷輸入序列 items 中的每個元素。
    for item in items:
        # 檢查當前元素是否已經在 seen 集合中。
        if item not in seen:
            # 如果元素未見過，則使用 yield 將其產生。
            # yield 會暫停函式執行並回傳值，下次呼叫時從這裡繼續。
            yield item
            # 將這個新見過的元素添加到 seen 集合中。
            seen.add(item)
    print(f"  (dedupe 內部) 處理完成。") # 函式內部處理完成的提示。

# 定義一個更通用的函式 dedupe2，它允許指定一個 key 函式來決定如何判斷元素的唯一性。
def dedupe2(items, key=None):
    # 創建一個空集合 seen，用於儲存已經見過的「判斷鍵」。
    seen = set()
    # 遍歷輸入序列 items 中的每個元素。
    for item in items:
        # 根據 key 參數決定用於判斷唯一性的值 (val)。
        # 如果 key 為 None，則直接使用元素本身作為判斷鍵。
        # 否則，呼叫 key 函式來獲取判斷鍵。
        val = item if key is None else key(item)
        # 檢查判斷鍵是否已經在 seen 集合中。
        if val not in seen:
            # 如果判斷鍵未見過，則產生原始元素。
            yield item
            # 將判斷鍵添加到 seen 集合中。
            seen.add(val)
    print(f"  (dedupe2 內部) 處理完成。") # 函式內部處理完成的提示。

print("--- dedupe 函式示範 (基本去重) ---")
# 測試 dedupe 函式。
list1 = [1, 5, 2, 1, 9, 1, 5, 10]
print(f"原始列表 list1: {list1}") # 顯示原始列表。
# 將 dedupe 生成器轉換為列表以便印出所有結果。
deduped_list1 = list(dedupe(list1))
print(f"去重並保序後的列表: {deduped_list1}\n") # 顯示去重後的列表。

print("--- dedupe2 函式示範 (根據特定鍵去重) ---")
# 測試 dedupe2 函式，用於處理字典列表。
list2 = [
    {'x': 1, 'y': 2},
    {'x': 1, 'y': 3},
    {'x': 2, 'y': 2},
    {'x': 1, 'y': 2},
]
print(f"原始字典列表 list2: {list2}") # 顯示原始字典列表。

# 使用 dedupe2 根據字典的 'x' 鍵進行去重。
# lambda d: d['x'] 作為 key 函式，表示只考慮 'x' 的值來判斷唯一性。
deduped_list2_by_x = list(dedupe2(list2, key=lambda d: d['x']))
print(f"根據 'x' 鍵去重並保序後的列表: {deduped_list2_by_x}") # 顯示根據 'x' 鍵去重後的列表。

# 使用 dedupe2 根據字典的 'y' 鍵進行去重。
deduped_list2_by_y = list(dedupe2(list2, key=lambda d: d['y']))
print(f"根據 'y' 鍵去重並保序後的列表: {deduped_list2_by_y}") # 顯示根據 'y' 鍵去重後的列表。
