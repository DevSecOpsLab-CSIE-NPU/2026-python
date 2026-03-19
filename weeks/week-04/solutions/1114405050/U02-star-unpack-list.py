# U2. 星號解包為何能處理「不定長」且結果固定是 list（1.2）
"""
本範例說明 Python 中的「星號解包」（star unpacking）如何處理不定長序列，
以及為什麼變數會被包成 list。

星號解包可以用在解包時接收剩餘元素，方便處理元素數量不固定的情況。
"""

record = ('Dave', 'dave@example.com')

# 將前三個變數與其餘元素分開
# name 和 email 會各自取對應位置的元素
# *phones 會收集剩下的所有元素（這裡沒有剩下的，所以會是空列表）
name, email, *phones = record

# 無論剩餘元素有沒有，*phones 一定會被轉成 list
# 例如：
# record = ('Dave', 'dave@example.com', '111-2222')
# name='Dave', email='dave@example.com', phones=['111-2222']
# record = ('Dave', 'dave@example.com', 1, 2, 3)
# phones=[1, 2, 3]

