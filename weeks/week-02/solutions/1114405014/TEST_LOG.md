# task1_sequence_clear 測試歷程
總測試數:5  通過次數:1 失敗次數:4

## 第一次測試 - 輸入與輸出
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task1.py
請輸入一行數列並用空格分隔:
1 5 9 7 8
['1', '5', '9', '7', '8']

### 更改方向
將輸出更改為逐項輸出

## 第二次測試 - 功能初步測試
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task1.py
請輸入一行數列並用空格分隔:
5 7 8 9 9 2 4 6
dedupe: 5 7 8 9 2 4 6
asc: [2, 4, 5, 6, 7, 8, 9, 9]
desc: [9, 9, 8, 7, 6, 5, 4, 2]
evens: [8, 6, 4, 2]

### 更改方向
將輸出結果寫為函式進行逐項輸出

## 第三次測試 - 測試輸出
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task1.py
請輸入一行數列並用空格分隔:
4 9 8 6 5 7 1 3
4 9 8 6 5 7 1 3 1 3 4 5 6 7 8 9 9 8 7 6 5 4 3 1 8 6 4 
### 更改方向
將輸出結果後進行換行並添加輸出項目名稱

## 第四次測試 - 功能測試
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task1.py
請輸入一行數列並用空格分隔:
2 4 9 7 3 1 4 5
dedupe:
2 4 9 7 3 1 5 
asc:
1 2 3 4 4 5 7 9 
desc:
9 7 5 4 4 3 2 1
evens:
4 4 2

### 更改方向
先進行dedupe後再進行剩餘排列

## 第五次測試 Green
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task1.py
請輸入一行數列並用空格分隔:
4 8 9 1 6 3 4 2 7
dedupe:
4 8 9 1 6 3 2 7
asc:
1 2 3 4 6 7 8 9
desc:
9 8 7 6 4 3 2 1
evens:
4 8 6 2

# task2_student_ranking 測試歷程

## 第一次測試 -輸入
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task2.py
請輸入學生數量
3
請輸入學生姓名、分數、年齡:(以空格作為分隔符)
Tom 70 11
Cindy 70 10
Judy 50 12
[('Tom', 70, 11), ('Cindy', 70, 10), ('Judy', 50, 12)]

### 更改方向
用for迴圈進行輸出並增加排序

## 第二次測試 -輸出與單一排序
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task2.py
請輸入學生數量
6
請輸入學生姓名、分數、年齡:(以空格作為分隔符)
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
學生排序結果:
bob 88 19
ian 88 19
amy 88 20
leo 75 20
eva 92 20
zoe 92 21

### 更改方向
將三個排序方式同時進行

## 第三次測試 - 多重排序
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task2.py
請輸入學生數量
6
請輸入學生姓名、分數、年齡:(以空格作為分隔符)
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 15 20
eva 92 20
學生排序結果:
eva 92 20
zoe 92 21
bob 88 19
ian 88 19
amy 88 20
leo 15 20

### 更改方向
添加顯示前面特定名次

## 第四次測試 - 完成 Green
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task2.py
請輸入學生數量、顯示名次:
6 
3
請輸入學生姓名、分數、年齡:(以空格作為分隔符)
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
學生排序結果:
eva 92 20
zoe 92 21
bob 88 19

# task3_log_summary 測試歷程

## 第一次測試 -輸入
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task3.py
請輸入紀錄筆數
3
請輸入user、action並以空格分隔
alice login
請輸入user、action並以空格分隔
bob login
請輸入user、action並以空格分隔
alice view
[('alice', 'login'), ('bob', 'login'), ('alice', 'view')]

### 更改方向
將提示詞不要重複出現、顯示以for迴圈呈現、增加判斷式杜絕<=0的可能

## 第二次測試 -輸出
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task3.py
請輸入紀錄筆數
3
請輸入user、action並以空格分隔
alice login
bob login
alice view
alice: login
bob: login
alice: view

### 更改方向
進行統計並排序

## 第三次測試 -統計與排序
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task3.py
請輸入紀錄筆數
4
請輸入user、action並以空格分隔
alice login
bob login
alice view
alice logout
統計結果:
alice: 3
bob: 1
### 更改方向
添加統計最常使用的功能

## 第四次測試 -完成 (Green)
PS D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests> python3 test_task3.py
請輸入紀錄筆數
8
請輸入user、action並以空格分隔
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
統計結果:
bob: 4
alice: 3
chris: 1
Top action: login 3




