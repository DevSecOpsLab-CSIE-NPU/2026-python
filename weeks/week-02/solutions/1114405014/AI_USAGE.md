# 你問了哪些問題（可條列 3~5 條）
## Python 敘述方式提問
1.python 的輸入與輸出
2.python陣列存取與特殊字元當作分隔
3.python 取得該陣列的長度與for迴圈直接以該陣列長度作為輸出
4.python str 應用
5.Python stored()的使用
6.Python Counter()的使用
7.TDD 的開發方式
# AI 給了哪些建議你有採用
將問題進行功能分隔成函式方式呈現
for 迴圈+print(f"")直接讀取陣列進行並透果f""添加元件

# AI 有哪些建議你拒絕（以及原因）
test1原先因功能簡單明確GPT給出的架構式透過sorted()直接進行撰寫。但我發現這不利於我思考，一坨程式碼在那裏我不知道它們在幹嘛，故我將功能進行拆分變成五個函式。
# 至少 1 個「AI 可能誤導你」但你自行修正的案例
test2進行Red測試時要增加students_list[]當時透過tab讓copilot快速填充後發現資料並沒有正確儲存(只存最後一筆)，隨後透過append()完成修改。
# 重構程式
test_task1/2/3的Refactor均透過與Copilot後放置task1_sequence_clean、task2_student_ranking.py、sask3_log_summary.py