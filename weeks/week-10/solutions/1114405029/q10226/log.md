# UVA 10226 — Hardwood Species

## 題目敘述
給定多筆測資，每筆測資包含一份森林中樹木的紀錄。  
每一行是一種樹的名稱，同一種樹可能出現很多次。

對於每筆測資，要統計每一種樹出現的百分比，並依照樹名字典順序輸出。

百分比公式為：

`某樹種出現次數 / 總樹木數量 × 100`

輸出時每個百分比都要保留到小數點後四位。

---

## 輸入格式
- 第一行是一個整數 `T`，表示有幾筆測資
- 接著有一個空白行
- 每筆測資由若干行樹名組成
- 遇到空白行表示該筆測資結束
- 最後一筆測資也可能直接到 EOF 結束

---

## 輸出格式
對每筆測資：

- 依照樹名字典順序輸出
- 每行格式為：

`樹名 百分比`

其中百分比保留小數點後四位。

不同測資之間要輸出一個空白行。

---

## 解題思路（詳細繁體中文）

### 一、這題要做什麼
每一筆測資都會給你很多行字串，每行代表一棵樹的種類名稱。

例如某筆測資可能是：

Red Alder  
Ash  
Ash  
Aspen

那麼這筆測資總共有 4 棵樹，其中：

- Red Alder 出現 1 次
- Ash 出現 2 次
- Aspen 出現 1 次

我們要算出每個樹種所佔百分比，再按照字典順序輸出。

---

### 二、最直接的做法：計數
這題最標準的做法就是用字典（dictionary）或雜湊表（hash map）統計次數。

對每一筆測資：

1. 準備一個字典 `counter`
2. 讀到一個樹名，就做：
   - `counter[name] += 1`
3. 同時記錄總樹數 `total`

這樣最後就能知道：

- 每個樹種出現幾次
- 總共有幾棵樹

---

### 三、如何計算百分比
對某個樹種 `name`：

`percentage = counter[name] / total * 100`

題目要求保留小數點後四位，所以輸出時用：

`{percentage:.4f}`

---

### 四、為什麼要排序
題目要求按照樹名字典順序輸出，所以不能直接照輸入順序印。

做法是：

- 取出所有樹名字串
- 用 `sorted(counter)` 排序
- 再依序輸出

---

### 五、輸入格式是這題的重點
這題真正比較麻煩的不是演算法，而是輸入格式。

輸入會長這樣：

第一行：測資數量 `T`  
第二行：空白行  
之後每筆測資之間也用空白行分隔

所以我們在讀資料時要注意：

- 第一行先讀 `T`
- 跳過中間那個空白行
- 之後每筆測資一直讀到空白行為止
- 最後一筆也可能沒有空白行，而是直接 EOF

因此最穩定的做法是：

- 一次把所有行讀進來
- 用索引去控制目前讀到哪裡
- 每筆測資讀到空白行就停止

---

### 六、時間複雜度
假設某筆測資總共有 `n` 行樹名，不同樹種有 `k` 種。

- 統計次數：`O(n)`
- 排序樹名：`O(k log k)`

所以整體時間複雜度是：

`O(n + k log k)`

這對本題完全足夠。

---

## 解題代碼
請見：
- `main.py`
- `main-easy.py`
- `main-handwritten.py`

---

## 測試用例

### 測試用例 1
輸入：
1

Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak
Poplan
Sassafras
Sycamore
Black Walnut
Willow

輸出：
Ash 13.7931
Aspen 3.4483
Basswood 3.4483
Beech 3.4483
Black Walnut 3.4483
Cherry 3.4483
Cottonwood 3.4483
Cypress 3.4483
Gum 3.4483
Hackberry 3.4483
Hard Maple 3.4483
Hickory 3.4483
Pecan 3.4483
Poplan 3.4483
Red Alder 3.4483
Red Elm 3.4483
Red Oak 6.8966
Sassafras 3.4483
Soft Maple 3.4483
Sycamore 3.4483
White Oak 10.3448
Willow 3.4483
Yellow Birch 3.4483

---

### 測試用例 2
輸入：
1

Oak
Oak
Pine
Pine
Pine

輸出：
Oak 40.0000
Pine 60.0000

---

### 測試用例 3
輸入：
1

Maple

輸出：
Maple 100.0000

---

### 測試用例 4
輸入：
2

Oak
Oak

Pine
Oak
Pine

輸出：
Oak 100.0000

Oak 33.3333
Pine 66.6667