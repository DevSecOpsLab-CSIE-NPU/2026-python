# 6/3 (三)｜TDD + Git PR 流程熱身

> 本日題目（UVA 11417 GCD）會進入期末考 **A 區公開題庫**。

## 學習目標

- 把 Week 14 的 `unittest` 與期末考 SOP 串起來跑一次完整流程
- 在「腦袋已經有答案」的狀態下練習，**降低題目負擔，專注於流程**
- 結束時每人應該有一個合法的 PR

## 本日不評分

只記錄「**有沒有開出 PR**」。沒開 PR 不會被扣分，但 6/22 期末考不會再有第二次練習機會。

---

## 題目：UVA 11417 — GCD

寫一個函式 `sum_of_gcd(n: int) -> int`，計算：

```
G = Σ Σ gcd(i, j)   for 1 ≤ i < j ≤ n
```

- 輸入：正整數 `n`（1 ≤ n ≤ 500）
- 輸出：所有 `gcd(i, j)` 的總和

範例：

| n | 結果 |
|---|------|
| 1 | 0 |
| 2 | 1 |
| 3 | 3 |
| 10 | 67 |

> 完整題目見 [`week-08/QUESTION-11417.md`](../../week-08/QUESTION-11417.md)（如有差異以本檔為準）。

---

## 課堂節奏（90 分鐘）

| 時間 | 內容 | 老師動作 | 學生動作 |
|------|------|----------|----------|
| 0:00–0:10 | 老師示範完整 SOP | 投影一次跑完 branch → test → commit → impl → commit → PR | 看 |
| 0:10–0:25 | 拆 test case | 走動巡視 | 跟 AI 討論，把題目拆成 ≥3 個 test case |
| 0:25–0:35 | 紅燈 commit | 檢查是否真的紅燈 | 寫進 `test_gcd.py`，`git commit -m "test: ..."` |
| 0:35–0:55 | 寫實作到綠燈 | 走動巡視，遇卡關引導 | 跟 AI 寫 `gcd.py`，跑測試直到全綠 |
| 0:55–1:05 | 綠燈 commit + 開 PR | 檢查 PR 是否成立 | `git commit -m "feat: ..."` → push → 開 PR |
| 1:05–1:20 | 全班 PR walkthrough | 點開 3–5 個學生的 PR 現場點評 | 看別人怎麼寫，記錄自己錯在哪 |
| 1:20–1:30 | 發 SOP 檢查表 | 提醒 6/4 要帶來 + 6/4 起要寫 AI_LOG | 收檢查表 |

---

## SOP 步驟（學生照做）

```bash
# 0.（第一次才要做）Fork 課程 repo 到自己的 GitHub，clone 自己的 fork
#    git clone <你的 fork 網址>
#    cd <repo 目錄>
#    git remote add upstream <課程 repo 網址>

# 1. 從 main 開分支
git checkout main && git pull
git checkout -b feature/wk15-0603-<學號>

# 2. 跟 AI 拆 test case，寫進 solutions/<學號>/0603/test_gcd.py
#    至少 3 個案例，包含：
#    - n=2（最小有意義輸入）
#    - n=10（範例驗證）
#    - n=1（edge case：迴圈空轉，結果 0）

# 3. 確認紅燈
python -m unittest test_gcd.py
git add test_gcd.py
git commit -m "test: add failing tests for UVA 11417 GCD"

# 4. 跟 AI 寫 gcd.py，跑到綠燈
python -m unittest test_gcd.py
git add gcd.py
git commit -m "feat: implement UVA 11417 GCD"

# 5. push 到自己的 fork + 開 PR
git push -u origin feature/wk15-0603-<學號>
# 到 GitHub 開 PR：你的 fork <分支> → 課程 repo 的 main
# 描述含：題目摘要 + 測試結果
```

---

## starter 檔

從 [`./0603-starter/`](./0603-starter/) 複製到自己的工作目錄，**不要直接在 starter 修改**。

```bash
cp -r weeks/week-15/in_class/0603-starter weeks/week-15/solutions/<學號>/0603
```

---

## 常見錯誤（老師現場提醒）

| 錯誤 | 後果 | 怎麼救 |
|------|------|--------|
| 在自己 fork 的 main 直接 commit | 期末考此題 0 流程分 | 從 main 開 `feature/...` 分支重做 |
| 忘了 fork，想 push 到課程 repo | 沒權限，push 被拒 | 先 fork 到自己帳號，push 到自己的 fork |
| PR 開錯方向（fork→fork） | 老師收不到、等於沒交 | PR base 選課程 repo 的 main，compare 選自己的分支 |
| 先寫 impl 再補 test | commit 順序錯 → 流程分扣半 | 重來不來得及就接受扣分 |
| test 一開始就綠燈 | 等於沒測 | 故意先讓 impl 留空，看 test 是否紅 |
| commit message 寫「update」 | 流程分扣分 | 養成寫 `test:` / `feat:` 前綴的習慣 |
| 忘了開 PR | 等於沒交 | 期末考也一樣 |
