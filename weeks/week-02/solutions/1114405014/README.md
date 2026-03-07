# 完成題目清單
task1_suquence_clean
task2_student_ranking
task3_log_summary

# 執行方式

## 程式執行指令
python3 <檔案名.py>
## 測試執行指令
python3 <檔案名.py>

# 資料結構

## task1_suquence_clean
我將 去重化、升冪、降冪、取偶數、輸出分為五個功能分別寫成四個函式
先用去重化得出的函示結果再放入升冪、降冪及取偶數進行運算隨後使用輸出進行顯示

## task2_student_ranking
我先創建 students_list 進行儲存所有學生的資料
隨後運用sorted函式進行三個條件的排序後再輸出

## task3_log_summary
我先用判斷式判斷歷史紀錄的資料合不合理
後創建 data_list 蒐集歷史紀錄清單
運用 Counter 進行次數運算
並輸出使用者的操作歷史紀錄數及最常操作的方式

# 錯誤與修正方式
進行 task3 時最後要輸出"最常操作方式"時原本使用 most_common()進行輸出
但該方式只能顯示操作方式不能顯示次數
我透過將該資料存入 top_action 透過 print(f"")進行顯示

# Red 、 Green and Refactor

## task1_suquence_clean
這一題功能十分明確因此我先將四個功能進行拆分(去重、升/降冪、取偶數)分別撰寫先進行Red的嘗試後，再進行組合成Green。但我發現輸出的方式十分冗長故在增加output函式統一進行輸出。之後將檔案給Copilot進行Refactor並瞭解重構的內容以及格式如何撰寫會更好。

## task2_student_ranking
我先分別將姓名、分數、年齡分別做排序進行Red嘗試。隨後發現只需調整key lambda 的參數就可將三者合在一起形成Green。之後將檔案給Copilot進行Refactor並瞭解重構的內容以及格式如何撰寫會更好。

## task3_log_summary
我先進行Counter的Red嘗試了解這個函式的使用方式，隨後將逐漸將判斷式、輸入、輸出組合成簡單的Green。之後將檔案給Copilot進行Refactor並瞭解重構的內容以及格式如何撰寫會更好。