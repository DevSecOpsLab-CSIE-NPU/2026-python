# test1_sequence_clean 測試資料
## 一般情況
### 輸入
1 2 3 4 5 6 7 8 9
### 預期輸出
dedupe:
1 2 3 4 5 6 7 8 9
asc:
1 2 3 4 5 6 7 8 9
desc:
9 8 7 6 5 4 3 2 1
evens:
2 4 6 8
### 實際輸出
dedupe:
1 2 3 4 5 6 7 8 9
asc:
1 2 3 4 5 6 7 8 9
desc:
9 8 7 6 5 4 3 2 1
evens:
2 4 6 8
### 是否通過
是

## 邊界
### 輸入
空輸入 : " "
### 預期輸出
dedupe:

asc:

desc:

evens:

### 實際輸出
dedupe:

asc:

desc:

evens:

### 是否通過
是

## 重複值
### 輸入
1 1 3 6 3 5 8 8 6
### 預期輸出
dedupe:
1 3 6 5 8
asc:
1 3 5 6 8
desc:
8 6 5 3 1
evens:
6 8
### 實際輸出
dedupe:
1 3 6 5 8
asc:
1 3 5 6 8
desc:
8 6 5 3 1
evens:
6 8
### 是否通過
是

## 反例
### 輸入
重複空輸入 : "  "
1  5 9 4 1 3 5  5 
### 預期輸出
dedupe:
1 5 9 4 3
asc:
1 3 4 5 9
desc:
9 5 4 3 1
evens:
4
### 實際輸出
dedupe:
1 5 9 4 3
asc:
1 3 4 5 9
desc:
9 5 4 3 1
evens:
4
### 是否通過
是

## 我認為最容易出錯的一組
重複空輸入 : "  " 資料:1  5 9 4 1 3 5  5
這筆資料中間呈不規則的空白令我不太確定可不可以通過 

# test2_student_ranking 測試資料
## 一般情況
### 輸入
6 3
amy 88 20
bob 88 19
zoe 92 21
ian 88 19
leo 75 20
eva 92 20
### 預期輸出
學生排序結果:
eva 92 20
zoe 92 21
bob 88 19
### 實際輸出
學生排序結果:
eva 92 20
zoe 92 21
bob 88 19
### 是否通過
是

## 邊界
### 輸入 - 只有一筆
1 1
amy 90 18
### 預期輸出
amy 90 18
### 實際輸出
amy 90 18
### 是否通過
是

## 重複值 - 同分排序
### 輸入
4 4
amy 90 20
bob 90 18
chris 90 19
dora 90 18
### 預期輸出
amy 90 20
bob 90 18
chris 90 19
dora 90 18
### 實際輸出
bob 90 18
dora 90 18
chris 90 19
amy 90 20
### 是否通過
是

## 反例 - 名字排序
### 輸入
5 5
zoe 88 19
amy 88 19
ian 88 19
bob 88 19
leo 88 19
### 預期輸出
amy 88 19
bob 88 19
ian 88 19
leo 88 19
zoe 88 19
### 實際輸出
amy 88 19
bob 88 19
ian 88 19
leo 88 19
zoe 88 19
### 是否通過
是

## 我認為最容易出錯的一組
反例 - 名字排序
在撰寫的過程中不斷地關注升/降冪的排序也以為sorted()只能進行數字的排序而忘了名字也要做排序

# test3_log_summary 測試資料
## 一般情況
### 輸入
8
alice login
bob login
alice view
alice logout
bob view
bob view
chris login
bob logout
### 預期輸出
bob 4
alice 3
chris 1
top_action: login 3
### 實際輸出
統計結果:
bob: 4
alice: 3
chris: 1
Top action: login 3
### 是否通過
是

## 邊界
### 輸入 - 空輸入
0
### 預期輸出
top_action: None 0
### 實際輸出
Error
Traceback (most recent call last):
  File "D:\Edwin\program\program-python\2026-python\weeks\week-02\solutions\1114405014\tests\test_task3.py", line 19, in <module>
    print(f"Top action: {top_action[0][0]} {top_action[0][1]}")
                         ~~~~~~~~~~^^^
IndexError: list index out of range
### 是否通過
否

## 重複值 - 比user名稱
### 輸入
4
bob login
alice view
bob logout
alice login
### 預期輸出
alice 2
bob 2
top_action: login 2
### 實際輸出
bob: 2
alice: 2
Top action: login 2
### 是否通過
否 (名字未按照字母排列)

## 反例 - action統計
### 輸入
6
alice login
bob view
alice view
chris view
bob logout
dora view
### 預期輸出
alice 2
bob 2
chris 1
dora 1
top_action: view 4
### 實際輸出
alice: 2
bob: 2
chris: 1
dora: 1
Top action: view 4
### 是否通過
是

## 我認為最容易出錯的一組
邊界 - 空輸入
在這題中我和Copilot進行Refactor討論時有增加空輸入的情況進行考慮但整體沒特別做觀察沒想到在做測資時就發生了錯誤