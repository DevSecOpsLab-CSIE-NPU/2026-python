# Test Cases

## Task 1：Sequence Clean

1. **範例輸入**
   - 輸入：`5 3 5 2 9 2 8 3 1`
   - 預期輸出：
     - dedupe: 5 3 2 9 8 1
     - asc: 1 2 2 3 3 5 5 8 9
     - desc: 9 8 5 5 3 3 2 2 1
     - evens: 2 2 8

2. **空輸入**
   - 輸入：空字串
   - 預期：全部列表為空

3. **包含負數且重複**
   - 輸入：`-1 -1 0 2 -1 2`
   - 預期：
     - dedupe: -1 0 2
     - asc: -1 -1 -1 0 2 2
     - desc: 2 2 0 -1 -1 -1
     - evens: 0 2 2

## Task 2：Student Ranking

1. **範例輸入**
   - 輸入：
     ```text
     6 3
     amy 88 20
     bob 88 19
     zoe 92 21
     ian 88 19
     leo 75 20
     eva 92 20
     ```
   - 預期輸出前 3 名：
     - eva 92 20
     - zoe 92 21
     - bob 88 19

2. **同分同年齡，姓名排序**
   - 輸入：
     ```text
     4 4
     alice 90 18
     aaron 90 17
     bob 90 17
     carol 90 18
     ```
   - 預期：aaron 90 17 會在 bob 90 17 之前

3. **k 值邊界**
   - k = 0 → 回傳空列表
   - k > n → 回傳全部學生

## Task 3：Log Summary

1. **範例輸入**
   - 輸入：
     ```text
     8
     alice login
     bob login
     alice view
     alice logout
     bob view
     bob view
     chris login
     bob logout
     ```
   - 預期：
     - bob 4
     - alice 3
     - chris 1
     - top_action: login 3

2. **多個 top action 相同次數**
   - 當有多個 action 出現次數一樣多時，選擇字母序最小的一個

3. **空紀錄**
   - m = 0 時，使用者列表為空，top_action 為空字串與 0
