# 題目分析：凱撒密碼（Caesar Cipher）- 第二題

## 📋 題目概述
- **分值**：25分
- **難度**：A題（保留）
- **相關資源**：week-03/README.md、QUESTION-10222.md
- **技術重點**：用 AI 前向思考與主要操作、邊比/邊併、邊/邊搭或邊界/edge case/邊界等條件

---

## 🎯 題目敘述

### 題目描述
凱撒密碼是將文字中的字母向右移動指定位數，實現加密。本題為學期初已編過的序列/學典題型。

### 核心任務
對輸入的每一行文字，依序完成：
1. **讀取文本** - 逐行讀入直到 EOF
2. **進行加密** - 使用 SHIFT 位移對字母進行加密
3. **保留非字母** - 空白、數字、標點符號保持不變

---

## 📥 輸入說明

```
Line 1 (可能含空白、標點、長度 ≤ 1000)
Line 2
...
EOF
```

- 輸入包含多行
- 每行一個字串，可能含有：
  - 大寫字母（A-Z）
  - 小寫字母（a-z）
  - 空白
  - 數字（0-9）
  - 標點符號
  - 長度最多 1000 字
- 當遇到 EOF（檔案結束）時終止

---

## 📤 輸出說明

對每一行輸入，輸出加密後的字串：
- 加密後的字母（大寫→大寫、小寫→小寫）
- 非字母字符保留原樣
- 保留原有的空白、標點、數字
- 每行輸入對應一行輸出

---

## 📊 範例說明（假設 SHIFT = 9）

### Sample Input
```
Hello, NPU!
abc XYZ
ABCXYZ
```

### Sample Output
```
Qsvvb, WYD!
jkl GHI
JKLGHI
```

### 詳細過程

#### 第1行：`Hello, NPU!`
```
H  e  l  l  o  ,     N  P  U  !
↓  ↓  ↓  ↓  ↓  ↓     ↓  ↓  ↓  ↓
Q  n  u  u  x  ,     W  Y  D  !

Q: H + 9 = Q (H=7, Q=16)
n: e + 9 = n (e=4, n=13)
u: l + 9 = u (l=11, u=20)
u: l + 9 = u
x: o + 9 = x (o=14, x=23)
,: 保留
(空白): 保留
W: N + 9 = W (N=13, W=22)
Y: P + 9 = Y (P=15, Y=24)
D: U + 9 = D (U=20, D=3, 超過Z會繞回)
!: 保留
```

**輸出**：`Qsvvb, WYD!`

#### 第2行：`abc XYZ`
```
a  b  c     X  Y  Z
↓  ↓  ↓     ↓  ↓  ↓
j  k  l     G  H  I

j: a + 9 = j (a=0, j=9)
k: b + 9 = k (b=1, k=10)
l: c + 9 = l (c=2, l=11)
(空白): 保留
G: X + 9 = G (X=23, G=6, 超過Z會繞回)
H: Y + 9 = H (Y=24, H=7, 超過Z會繞回)
I: Z + 9 = I (Z=25, I=8, 超過Z會繞回)
```

**輸出**：`jkl GHI`

#### 第3行：`ABCXYZ`
```
A  B  C  X  Y  Z
↓  ↓  ↓  ↓  ↓  ↓
J  K  L  G  H  I

J: A + 9 = J (A=0, J=9)
K: B + 9 = K (B=1, K=10)
L: C + 9 = L (C=2, L=11)
G: X + 9 = G (X=23, G=6, 超過Z會繞回)
H: Y + 9 = H (Y=24, H=7, 超過Z會繞回)
I: Z + 9 = I (Z=25, I=8, 超過Z會繞回)
```

**輸出**：`JKLGHI`

---

## 🔑 關鍵要點

1. **字母位移的循環性** - 超過 Z 時要繞回到 A（使用模運算 mod 26）
2. **大小寫區分** - 大寫與小寫分別處理，不改變原有大小寫
3. **非字母保留** - 空白、數字、標點、特殊符號都保持不變
4. **EOF 處理** - 逐行讀入直到檔案結束
5. **SHIFT 參數** - 根據題目參數調整（本題 SHIFT=9）

---

## 💡 演算法策略

### 方案1：使用 ASCII 值計算（推薦）
```python
def caesar_encrypt(text, shift=9):
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            # 大寫字母
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        elif 'a' <= char <= 'z':
            # 小寫字母
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
        else:
            # 非字母，保留原樣
            result.append(char)
    return ''.join(result)
```

### 方案2：使用 Python 字元方法
```python
def caesar_encrypt_v2(text, shift=9):
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)
```

---

## 📌 邊界情況（Edge Cases）

- **空行** - 空字符串應直接輸出空字符串
- **純非字母** - 僅含空白、數字、標點的行直接保留並輸出
- **混合內容** - 大小寫混合、含數字和標點的文本
- **邊界字母** - X, Y, Z 加上 SHIFT 需要正確繞回
- **特殊字符** - 換行符、特殊符號需要保留
- **長字符串** - 長度 1000 以下的字串處理
- **SHIFT 超過 26** - 雖然題目通常 SHIFT < 26，但應考慮 SHIFT % 26 的情況

---

## 📚 相關資源參考

- `week-03/README.md` - 相關題目與講解
- `QUESTION-10222.md` - 完整題目敘述
- ASCII 表 - 字元編碼參考

---

## ✅ 實作檢查清單

- [ ] 讀取輸入直到 EOF
- [ ] 實作字母位移邏輯
- [ ] 實作大寫字母加密
- [ ] 實作小寫字母加密
- [ ] 保留非字母字符
- [ ] 正確處理 Z/z 繞回
- [ ] 驗證 SHIFT=9 的正確性
- [ ] 測試所有邊界情況
- [ ] 驗證輸出格式

---

## 📝 SHIFT 參數

**當前設定：SHIFT = 9**

使用此參數時：
- A → J, B → K, C → L, ...
- X → G, Y → H, Z → I（繞回）
- a → j, b → k, c → l, ...
- x → g, y → h, z → i（繞回）
