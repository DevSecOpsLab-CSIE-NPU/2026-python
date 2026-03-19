# U10. zip 為何只能用一次（1.8）
"""
本範例說明為什麼 zip() 回傳的是一個「一次性可迭代物件」（iterator），
也就是說只能被消費（iterate）一次。

zip() 會將多個可迭代物件逐一配對，並且在每次取值後就前進。
一旦迭代完成，zip 物件就會變成空的，後續再取值就得不到任何元素。

常見錯誤：
- 先呼叫 min(zip_obj) 取得結果，再呼叫 max(zip_obj) 或 list(zip_obj)，
  這會得到空結果，因為 zip_obj 已被消耗。

如果需要多次使用配對結果，可以先把 zip 的結果轉成 list，
或重新呼叫 zip() 建立新的迭代器。
"""

prices = {'A': 2.0, 'B': 1.0}
# zip 回傳的是 iterator，不會立即建立整個 list
z = zip(prices.values(), prices.keys())

# 下面這行會消耗掉整個 iterator
min(z)  # OK（消耗掉迭代器）

# 這行會失敗，因為 z 已經被消耗完了
# max(z)

