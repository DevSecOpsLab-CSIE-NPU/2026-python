# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）

# 情境：record 只有 2 個元素，但我們希望定義一個「phones」變數來接收可能的電話號碼
record = ('Dave', 'dave@example.com')

# 使用星號變數 *phones：
# 1. name 會匹配第一個元素 'Dave'
# 2. email 會匹配第二個元素 'dave@example.com'
# 3. *phones 會「收集」剩下的所有元素
name, email, *phones = record

# 重點特性：
# 即使右側沒有剩餘的元素可以分配，星號變數也會被賦予一個「空的列表 []」。
# 這確保了後續程式碼在處理 phones 時，不需要檢查它是否為 None，
# 且其型別固定為 list，這在處理資料的一致性上非常有幫助。
# 此時 phones == []