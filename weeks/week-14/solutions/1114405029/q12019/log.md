# UVA 12019 — Doom's Day Algorithm

## 題目重點

本題要判斷 2011 年中的某個日期是星期幾。

雖然題目名稱是 Doom's Day Algorithm，但這題不需要真的推導任意年份的 Doomsday。

題目已經固定在 2011 年，而且給出了每個月份對應的 Doomsday 日期。

2011 年的 Doomsday 是 Monday。

也就是說，每個月表格中的日期都剛好是 Monday。

---

## 重要修正

本題 UVA 12019 是 2011 年，不是 2012 年。

以下這些日期在 2011 年都是 Monday：

1/10
2/21
3/7
4/4
5/9
6/6
7/11
8/8
9/5
10/10
11/7
12/12

所以程式應該以 Monday 當作基準日。

---

## 輸入格式

第一行是一個整數 T，代表測試資料組數。

接下來 T 行，每行有兩個整數：

m d

m 代表月份。
d 代表日期。

---

## 輸出格式

每組測試資料輸出一行英文星期名稱。

可能答案有：

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday

---

## 解題思路

每個月份都有一個已知的 Doomsday 日期。

例如：

1 月的 Doomsday 是 1/10。
4 月的 Doomsday 是 4/4。
12 月的 Doomsday 是 12/12。

在 2011 年，這些 Doomsday 日期都是 Monday。

因此，若要判斷某個日期是星期幾，只需要計算它和該月份 Doomsday 日期差幾天。

例如：

1/10 是 Monday。

所以：

1/11 是 Tuesday。
1/12 是 Wednesday。
1/9 是 Sunday。
1/8 是 Saturday。

用公式表示：

diff = day - doomsday_date[month]

weekday = diff % 7

如果 diff % 7 = 0，代表 Monday。
如果 diff % 7 = 1，代表 Tuesday。
如果 diff % 7 = 2，代表 Wednesday。
依此類推。

---

## 演算法流程

1. 建立每個月份的 Doomsday 日期表。
2. 建立星期名稱表：
   - Monday
   - Tuesday
   - Wednesday
   - Thursday
   - Friday
   - Saturday
   - Sunday
3. 讀取測試資料組數 T。
4. 對每組 month day：
   - 找出該月份的 Doomsday 日期。
   - 計算 day 和 Doomsday 日期差幾天。
   - 用差值對 7 取餘數。
   - 找出對應星期。
5. 輸出答案。

---

## 範例說明

假設輸入：

1 10

1 月的 Doomsday 是 10。

1/10 在 2011 年是 Monday。

所以輸出：

Monday

---

假設輸入：

1 11

1/11 比 1/10 晚一天。

Monday 往後一天是 Tuesday。

所以輸出：

Tuesday

---

假設輸入：

1 9

1/9 比 1/10 早一天。

Monday 往前一天是 Sunday。

所以輸出：

Sunday

---

## 容易錯的地方

### 1. 年份不要看錯

這題是 2011 年。

如果用 2012 年去算，答案會錯。

---

### 2. Doomsday 是 Monday

表格中的日期在 2011 年全部是 Monday。

所以星期表要從 Monday 開始。

---

### 3. 可以使用負數取餘數

例如：

1/9 比 1/10 早一天。

diff = 9 - 10 = -1

Python 中：

-1 % 7 = 6

星期表中 index 6 是 Sunday。

所以可以正確得到答案。

---

### 4. 不需要處理閏年

題目固定在 2011 年，不需要另外判斷閏年。

---

## 時間複雜度

每組測試資料只做固定次數計算。

時間複雜度：

O(1)

---

## 空間複雜度

只使用固定大小的月份表和星期表。

空間複雜度：

O(1)

---

## 測試用例

### 測試 1：Doomsday 日期

輸入：

4
1 10
4 4
8 8
12 12

輸出：

Monday
Monday
Monday
Monday

---

### 測試 2：Doomsday 前一天

輸入：

3
1 9
4 3
12 11

輸出：

Sunday
Sunday
Sunday

---

### 測試 3：Doomsday 後一天

輸入：

3
1 11
4 5
12 13

輸出：

Tuesday
Tuesday
Tuesday

---

### 測試 4：2011 年第一天

輸入：

1
1 1

輸出：

Saturday

---

### 測試 5：2011 年最後一天

輸入：

1
12 31

輸出：

Saturday

---

### 測試 6：多筆不同月份

輸入：

5
1 6
2 28
3 15
7 4
11 11

輸出：

Thursday
Monday
Tuesday
Monday
Friday

---

### 測試 7：連續一週

輸入：

7
10 10
10 11
10 12
10 13
10 14
10 15
10 16

輸出：

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday