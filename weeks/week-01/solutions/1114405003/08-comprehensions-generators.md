# 8 容器操作與推導式

你必須已經「不需要解釋」就能看懂：

```python
# 先從序列 data 中挑出符合條件的元素，重新組成一個新的 list。
# 這種寫法稱為 list comprehension，優點是簡潔、直接、可讀性高。
[x for x in data if x > 0]

# 將字典 d 的每個鍵值對重新組裝成新的字典。
# 左邊是新字典的 key，右邊是 value，for 後面負責逐一走訪原本的項目。
{k: v for k, v in d.items()}
```

```python
# generator expression 會建立「產生器」而不是立即建立完整清單。
# 它會在需要時才逐一產生資料，適合搭配 sum / min / max / join 等函式。
(x * x for x in nums)
```

用途（對應第一章範例）：

- 過濾序列（1.16）
- 字典子集（1.17）
- `sum(...)` / `min(...)` / `join(...)`

## 補充說明

這一章最重要的概念，是把「寫迴圈組資料」改寫成「用一行表達資料轉換」。

- list comprehension：會直接回傳 list，適合你接下來就要反覆使用結果的情境。
- dict comprehension：適合做查表、篩選欄位、重新命名 key 的工作。
- generator expression：不會一次把所有結果放進記憶體，適合資料量大、只需要逐步消耗的情況。
- 如果你不確定要用哪一種，先問自己「我是不是要立即拿到完整結果？」如果答案是是，通常用 list comprehension；如果答案是否，優先考慮 generator。

常見錯誤是把 generator 當成 list 使用。generator 只能被迭代一次，迭代完之後內容就被消耗掉了。

```python
# 範例：先建立 generator，再轉成 list 才能看到全部內容。
gen = (x * x for x in nums)
result = list(gen)
```
