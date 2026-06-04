# README — UVA 11417 GCD (0603)

此資料夾為學號 `1114405003` 的 Week-15 0603 練習答案。

## 檔案
- [test_gcd.py](test_gcd.py) — 單元測試（包含 3 個案例：n=1, n=2, n=10）。
- [gcd.py](gcd.py) — `sum_of_gcd(n)` 的實作（naive O(n^2) 演算法）。
- [AI_LOG.md](AI_LOG.md) — AI 協助紀錄與 PR 模板。

## 啟動與測試
在本資料夾執行：

```bash
python -m unittest test_gcd.py
```

預期輸出：
```
Ran 3 tests in ...

OK
```

## 函式說明
- `sum_of_gcd(n: int) -> int`：計算所有 1 ≤ i < j ≤ n 的 `gcd(i, j)` 總和。實作採用兩層迴圈並使用 `math.gcd`。

複雜度：時間 O(n^2)，空間 O(1)。在題目限制 n ≤ 500 時可接受。

## Commit / PR 建議
範例 git 流程：

```bash
git checkout -b feature/wk15-0603-1114405003
git add solutions/1114405003/0603/test_gcd.py solutions/1114405003/0603/gcd.py solutions/1114405003/0603/AI_LOG.md solutions/1114405003/0603/README.md
git commit -m "test: add failing tests for UVA 11417 GCD"
# 若測試一開始為紅燈，實作後再 commit
git commit -m "feat: implement UVA 11417 GCD"
git push -u origin feature/wk15-0603-1114405003
```

建議 PR 標題與描述請參考 `AI_LOG.md` 中的範本。

## 注意事項
- 本實作為單純解題版本；若需優化可使用數論技巧（例如用歐拉函數的方法降低複雜度）。
- 請確保在自己的 fork 與 feature 分支上建立 PR（不要直接 push 到課程 repo 的 main）。

---

需要我幫你產生可直接貼到 GitHub 的 PR 描述文字嗎？