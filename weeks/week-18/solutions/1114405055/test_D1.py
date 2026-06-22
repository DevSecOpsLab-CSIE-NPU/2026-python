from importlib import import_module

# D1-easy.py 含有破折號不是合法模組名，用 import_module 動態載入
mod = import_module("D1-easy")
process = mod.process

D = 3


def test_sample_1():
    # 工程動機：驗證去重保序的正確性。原始序列 4,7,4,2,9,2,6,7 中
    # 4 與 2、7 皆重複出現，去重後須得 4,7,2,9,6（保留第一次出現順序），
    # 再篩選出可被 d=3 整除者 9,6，最後由小到大排序為 [6, 9]。
    assert process([4, 7, 4, 2, 9, 2, 6, 7], D) == [6, 9]


def test_sample_2():
    # 工程動機：驗證無重複值情境下，流程仍能正確篩選與排序，
    # 確保去重步驟不會在沒有重複值時誤刪或誤改任何元素。
    assert process([1, 3, 5], D) == [3]


def test_edge_case_neg_and_zero():
    # 工程動機：邊界案例，同時驗證三個風險點：
    # (1) 負數整除判斷 -3 % 3 == 0、-9 % 3 == 0 是否正確；
    # (2) 0 % d == 0 恆真，0 必定被視為符合整除條件；
    # (3) 含負數的重複值去重，以及排序時負數需正確排在正數之前。
    assert process([-3, -3, 9, 9, -9, 0], D) == [-9, -3, 0, 9]


def test_none_output():
    # 工程動機：驗證完全沒有元素符合整除條件的極端狀況。
    # process 本身只需正確回傳空列表 []，
    # 將空列表轉換為大寫字串 "NONE" 的格式化責任在主程式 I/O 層，不屬於本函式測試範圍。
    assert process([1, 2, 4, 5, 7], D) == []
