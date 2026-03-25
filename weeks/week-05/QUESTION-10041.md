# 題目 10041

**題名**: UVA 10041

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a034)
- [Yui Huang 題解](https://yuihuang.com/zj-a034/)

## 題目敘述

世界聞名的黑社會老大 **Vito Deadstone** 要搬到紐約來了。

在那裡他有一個大家族，所有親戚都住在 **Lamafia 大道**上。因為 Vito 時常要拜訪所有的親戚，他想要找一間**距離所有親戚總距離最小**的房子。

他恐嚇你寫一個程式來幫助他解決這個問題。

## 輸入說明

- 第一列有一個整數，代表以下有多少組測試資料。
- 每組測試資料一列，第一個整數 **r**（0 < r < 500），代表他親戚的數目。
- 接下來的 r 個整數 s₁, s₂, …, sᵣ 為這些親戚房子的**門牌號碼**（0 < sᵢ < 30000）。
- 注意：有些親戚的門牌號碼**可能相同**。

## 輸出說明

對每一組測試資料，輸出從他的新家到所有親戚的家**距離總和的最小值**。

兩個門牌號碼 sᵢ、sⱼ 的距離為 |sᵢ - sⱼ| 的絕對值。

---

## 解題思路

這是一個經典的一維中位數問題。為了最小化到所有點的距離總和，最佳位置是所有地址的中位數。

- 將所有地址排序。
- 中位數是排序後的第 (n//2 + 1) 個元素（1-based）。
- 計算所有地址到中位數的絕對距離總和。

時間複雜度 O(n log n) 主要來自排序。

## 解題代碼

```python
import sys

def calculate_min_distance(addresses):
    """
    計算最小距離總和
    參數：addresses - 親戚房子的門牌號碼列表
    返回：最小距離總和
    """
    if not addresses:
        return 0
    # 排序地址
    addresses.sort()
    # 找到中位數（對於偶數個，取任一個中位數）
    n = len(addresses)
    median = addresses[n // 2]
    # 計算總距離
    total_distance = sum(abs(addr - median) for addr in addresses)
    return total_distance

def main():
    """
    主函數：讀取輸入並處理每一組測試資料
    """
    # 讀取所有輸入
    data = sys.stdin.read().split()
    # 第一個數字是測試案例數量
    T = int(data[0])
    index = 1
    for _ in range(T):
        # 讀取親戚數量 r
        r = int(data[index])
        index += 1
        # 讀取 r 個地址
        addresses = []
        for i in range(r):
            addresses.append(int(data[index]))
            index += 1
        # 計算並輸出最小距離
        result = calculate_min_distance(addresses)
        print(result)

if __name__ == "__main__":
    main()
```

## 測試用例

*測試輸入與預期輸出*
