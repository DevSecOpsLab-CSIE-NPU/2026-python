# AI_USAGE.md — AI 使用紀錄

## 我問了哪些問題

1. `sorted()` 多鍵排序時，如何用單一 `key` 同時處理「分數降序、年齡升序、姓名升序」？
2. `defaultdict` 和 `Counter` 各自的使用時機是什麼？有沒有更簡潔的寫法？
3. 如何對 `builtins.print` 做 mock，讓 `unittest` 可以捕捉函式的標準輸出？
4. 去重保留順序的慣用寫法有哪些（Python 3.7 以前 vs. 以後）？
5. `Counter.most_common()` 在空 Counter 上呼叫會發生什麼事？

---

## AI 建議我有採用的

- 使用 `key=lambda s: (-s[1], s[2], s[0])` 做多鍵排序，比自訂 `cmp_to_key` 更簡潔。
- 在測試中使用 `unittest.mock.patch("builtins.print")` 擷取輸出，比重導向 `sys.stdout` 更直接。
- `Counter.most_common(1)[0]` 在空 Counter 會拋 `IndexError`，需要加邊界保護。

---

## AI 建議我拒絕的（以及原因）

- **建議**：Task 1 用 `dict.fromkeys(nums)` 去重（Python 3.7+ 保序）。  
  **拒絕原因**：題目限制「不可用 `set` 直接輸出去重結果」，`dict.fromkeys()` 語意過於隱晦，閱卷者可能認為違反精神；改用明確的 `seen` set + 遍歷更符合教學要求。

- **建議**：Task 3 的 user 計數也改用 `Counter`，直接 `Counter(user for line...)` 一行搞定。  
  **拒絕原因**：題目要求「需使用 `defaultdict` 或 `Counter` 至少一種」，兩種都使用可展示理解差異；`defaultdict` 也讓行為更顯式，便於後續擴充（如要計算 user-action 組合）。

---

## AI 可能誤導我的案例（自行修正）

**案例**：AI 建議 `dict.fromkeys(nums).keys()` 作為去重輸出，並聲稱「這在現代 Python 完全等價於順序保留的去重 list」。

**問題**：`dict.fromkeys()` 雖然在 CPython 3.7+ 保序，但回傳的是 `dict_keys` 視圖，直接傳入 `" ".join()` 會失敗（需轉 `list`）。此外當輸入含有不可 hash 的元素時也會出錯。

**我的修正**：保留自己的 `dedupe_ordered()` 實作（遍歷 + `set`），邏輯完全透明，且不依賴 CPython 實作細節；測試 `test_preserves_order` 明確驗證了此行為。
