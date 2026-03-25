# 題目 10050

**題名**: UVA 10050

>
> 【狀態】題目敘述、輸入說明、輸出說明待補充
>
> 【建議】請參考以下連結自行補充：
> - [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a043)
> - [UVA Online Judge](https://uva.onlinejudge.org/external/10050.pdf)
> - [Yui Huang 題解參考](https://yuihuang.com/cpe-level-1/)

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a043)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10050.pdf)

## 題目敘述


一個社會研究組織採用了一組簡單的參數來模擬我們國家政黨運作的行為。
參數之一是一個正整數h，h稱為罷會(hartal)參數，它表示同一個政黨連續兩次連續罷會的間隔天數。
儘管該參數有點過於簡單，但還是能用於預測政黨罷會造成的影響。
以下範例為您說明：考慮現在有三個政黨。
假設h1 = 3，h2 = 4，h3 = 8，其中hi是第i方的罷會參數。
現在，我們將模擬這三個方在N = 14天的罷會行為。
模擬的起始天一定是星期天，並假設在每週的假日(星期五和星期六)不會有任何罷會情形。
上面的模擬顯示，在14天內將會罷會5天(分別在第3、4、8、9和12天)。
第6天沒有罷會，因為它屬於假日(星期五)。
由此可知我們在2週內損失了5個工作天。
在這個問題中，考慮到多個政黨的罷會參數和天數N，您的工作是計算出這N天內我們因為罷會損失多少工作天。

## 輸入說明


輸入第一行有一個整數T，代表有T組測資。
每組測資第一行包含一個整數N (7 ≤ N ≤ 3650)，N代表模擬的天數。
下一行包含一個整數P (1 ≤ P ≤ 100)，表示有幾個政黨。
接下來的P行，第i行包含一個正整數hi(永遠不會是7的倍數)，代表第i個政黨的罷會參數。

## 輸出說明

對於每組測資，輸出這N天內因為罷會損失多少工作天。


---

## 解題思路

需要計算 N 天內，因為政黨罷會造成的工作日損失。

- 星期從星期天開始：第1天日，第2天一，... 第7天六，第8天日。
- 假日：星期五（6）和星期六（7）。
- 工作日：其他天（1-5）。
- 罷會天：每個政黨的 h_i 倍數。
- 損失：罷會且為工作日的天數。

模擬每一天，檢查條件。

時間複雜度 O(N * P)，N<=3650, P<=100，可行。

## 解題代碼

```python
import sys

def is_working_day(day):
    """
    判斷某一天是否為工作日
    星期：1=日, 2=一, 3=二, 4=三, 5=四, 6=五, 7=六
    假日：五六 (6,7)
    工作日：日一二三四 (1-5)
    """
    weekday = ((day - 1) % 7) + 1
    return weekday not in [6, 7]

def has_hartal(day, hartals):
    """
    檢查某一天是否有罷會
    參數：day - 天數, hartals - 政黨的罷會參數列表
    返回：是否有罷會
    """
    for h in hartals:
        if day % h == 0:
            return True
    return False

def calculate_lost_days(N, hartals):
    """
    計算損失的工作天數
    參數：N - 總天數, hartals - 罷會參數列表
    返回：損失天數
    """
    lost = 0
    for day in range(1, N + 1):
        if is_working_day(day) and has_hartal(day, hartals):
            lost += 1
    return lost

def main():
    """
    主函數：讀取輸入並處理每一組測試資料
    """
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    index = 1
    for _ in range(T):
        N = int(input_data[index])
        index += 1
        P = int(input_data[index])
        index += 1
        hartals = []
        for i in range(P):
            hartals.append(int(input_data[index]))
            index += 1
        result = calculate_lost_days(N, hartals)
        print(result)

if __name__ == "__main__":
    main()
```

## 解題代碼

```python
# 你的代碼這裡
```

## 測試用例

*測試輸入與預期輸出*
