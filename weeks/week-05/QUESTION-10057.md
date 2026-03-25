# 題目 10057

**題名**: UVA 10057

>
> 【狀態】題目敘述、輸入說明、輸出說明待補充
>
> 【建議】請參考以下連結自行補充：
> - [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a050)
> - [UVA Online Judge](https://uva.onlinejudge.org/external/10057.pdf)
> - [Yui Huang 題解參考](https://yuihuang.com/cpe-level-1/)

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a050)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10057.pdf)

## 題目敘述


今年是公元2200年。
在過去的200年中，科學取得了很大進步。
這裡提到了兩百年，因為這個問題是在時光機的幫助下被發送回公元2000年的。
現在可以在人與電腦之間建立直接連接。
人們可以在3D顯示器上觀看別人的夢，就像在看電影一樣。
本世紀最大的一個問題是，人們對電腦的依賴性變得如此之高，以至於他們的分析能力接近於零。
現在，電腦可以讀取問題並自動解決，但是他們只能解決困難的問題(現在已經沒有簡單的問題了)。
我們的首席科學家遇到了很大的麻煩，因為他忘記了密碼。
出於安全原因，當今的電腦無法解決與密碼相關的問題。
在仲夏夜裡，科學家做了一個夢，在那裡他看到許多無號整數飛來飛去。
他在電腦的幫助下記錄了它們，然後他知道如果數字為(X1，X2，...，Xn)。
他需要找到一個整數A(此A為密碼)，使得能夠得到以下式子的最小值。
(|X1 − A| + |X2 − A| + . . . + |Xn − A|)

## 輸入說明


輸入包含多組測資。
每組測資第一行為數字n (0 接下來有n個數字，所有數字都小於65536。

## 輸出說明


對於每組測資，輸出三個整數。
第一個數字是能得到該算式最小值的A。
第二個數字是|Xi − A|為最小值的數量。
第三行數字是可能有幾種最小值。

---

## 解題思路

給定 n 個數字，找 A 使 sum |X_i - A| 最小。

A 應為中位數。

- 排序數字。
- 若 n 奇數，A = nums[n//2]，可能的 A 數 = 1。
- 若 n 偶數，A = nums[n//2 - 1] 或 nums[n//2]，但 sum 相同，輸出一個 A，可能的數 = 2。
- 計算 sum |X_i - A|。

時間複雜度 O(n log n)。

## 解題代碼

```python
import sys

def find_median_and_sum(nums):
    """
    找到中位數和最小距離總和
    參數：nums - 數字列表
    返回：(A, min_sum, possible_A_count)
    """
    if not nums:
        return 0, 0, 0
    nums.sort()
    n = len(nums)
    # 中位數
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = nums[n // 2 - 1]  # 偶數取前一個
    # 最小距離總和
    min_sum = sum(abs(x - median) for x in nums)
    # 可能的 A 數量
    possible = 1 if n % 2 == 1 else 2
    return median, min_sum, possible

def main():
    """
    主函數：讀取多組測試資料直到 n=0
    """
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        nums = list(map(int, sys.stdin.readline().split()))
        A, min_sum, possible = find_median_and_sum(nums)
        print(A, min_sum, possible)

if __name__ == "__main__":
    main()
```

*請填入你的解題思路*

## 解題代碼

```python
# 你的代碼這裡
```

## 測試用例

*測試輸入與預期輸出*
