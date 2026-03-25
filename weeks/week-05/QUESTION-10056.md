# 題目 10056

**題名**: UVA 10056

>
> 【狀態】題目敘述、輸入說明、輸出說明待補充
>
> 【建議】請參考以下連結自行補充：
> - [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a049)
> - [UVA Online Judge](https://uva.onlinejudge.org/external/10056.pdf)
> - [Yui Huang 題解參考](https://yuihuang.com/cpe-level-1/)

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid=a049)
- [UVA Online Judge](https://uva.onlinejudge.org/external/10056.pdf)

## 題目敘述


機率一直是電腦演算法不可或缺的一部分。
在確定性算法無法在短時間內解決問題的地方，概率性算法已應運而生。
在這個問題上，我們不處理任何概率算法。
我們將僅嘗試確定某個玩家的獲勝機率。
我們透過類似擲骰子的方式來玩這個遊戲 (他不像普通骰子一樣有六個面)。
如果某個特定事件發生在玩家擲骰子時 (例如獲得數字3，獲得綠色的一面或其他任何東西)，則宣佈為獲勝者。
此遊戲可以有N個玩家。
第一個玩家將擲骰子，然後第二個玩家，最後是第N個玩家，再來是第一個玩家，依此類推。
當玩家獲得期望的結果時，宣佈為獲勝者，比賽停止。
您必須確定其中一名 (第i名) 的獲勝機率。

## 輸入說明


一開始有一個整數S (S ≤ 1000)，表示接下來有多少組輸入。
接下來的S行。
每行包含一個整數N (N ≤ 1000)，一個浮點數p，一個整數i。
N表示玩家數，p表示一次成功事件發生的機率，i (i ≤ N) 表示要確定獲勝機率的玩家的序列 (序列號碼從1到N)。
(如果成功事件代表獲得數字3，則p是在一次投擲的獲得數字3的機率)。
例如：一個正常骰子，獲得數字3的機率為1/6輸入不會有不合理的 p 值。

## 輸出說明


對於每組輸入，輸出第i個玩家獲勝的機率。
機率精確到小數點後四位。

---

## 解題思路

N 個玩家輪流擲骰子，成功機率 p，第 i 個玩家獲勝的機率。

第 i 個玩家獲勝的條件：前 i-1 個玩家失敗，第 i 個成功。

由於是循環的，使用幾何級數公式：

P_i = p * (1-p)^{i-1} / (1 - (1-p)^N)

需要處理邊界情況，如 p=0 或 p=1。

輸出四捨五入到小數點後四位。

時間複雜度 O(1) 每組。

## 解題代碼

```python
import sys

def calculate_probability(N, p, i):
    """
    計算第 i 個玩家獲勝機率
    參數：N - 玩家數, p - 成功機率, i - 玩家編號 (1-based)
    返回：機率
    """
    if p == 0:
        return 0.0
    q = 1 - p
    if q ** N == 1:
        # 如果 q=0, p=1, 第一個玩家總是贏
        return 1.0 if i == 1 else 0.0
    prob = p * (q ** (i - 1)) / (1 - q ** N)
    return prob

def main():
    """
    主函數：讀取輸入並處理每一組測試資料
    """
    input_data = sys.stdin.read().split()
    S = int(input_data[0])
    index = 1
    for _ in range(S):
        N = int(input_data[index])
        p = float(input_data[index + 1])
        i = int(input_data[index + 2])
        index += 3
        prob = calculate_probability(N, p, i)
        print(f"{prob:.4f}")

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
