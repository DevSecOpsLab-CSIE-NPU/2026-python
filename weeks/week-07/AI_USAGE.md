# AI_USAGE.md - 赤壁戰役作業

## AI 使用記錄

---

## 1. 詢問的問題

1. **Python 如何使用 namedtuple 定義結構體？**
   - 原因：定義 General 武將資料結構

2. **Counter 和 defaultdict 有什麼差別？**
   - 原因：選擇合適的資料結構統計傷害

3. **如何實現 EOF 結尾的檔案讀取？**
   - 原因：讀取 generals.txt 時要正確處理 EOF

4. **sorted() 的 key 參數如何使用？**
   - 原因：實現按速度排序戰鬥順序

5. **如何實現 ASCII 視覺化進度條？**
   - 原因：美化傷害統計報告輸出

---

## 2. 採納的 AI 建議

1. **使用 namedtuple 定義 General**
   - 建議：General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])
   - 原因：比 dict 更清晰，且不可變更
   - 實際採用：已應用

2. **使用 Counter 統計傷害**
   - 建議：self.stats['damage'] = Counter()
   - 原因：Counter 有 most_common() 方法方便排名
   - 實際採用：已應用

3. **使用 defaultdict(int) 追蹤兵力損失**
   - 建議：self.stats['losses'] = defaultdict(int)
   - 原因：自動初始化為 0，避免 KeyError
   - 實際採用：已應用

4. **sorted(key=lambda g: g.spd, reverse=True)**
   - 建議：用 lambda 取得屬性作為排序 key
   - 原因：清晰且易讀
   - 實際採用：已應用

---

## 3. 拒絕的 AI 建議

1. **使用 dataclass 取代 namedtuple**
   - 拒絕原因：作業要求使用 namedtuple
   - 改用：namedtuple

2. **使用 pandas 處理資料**
   - 拒絕原因：作業要求使用標準庫
   - 改用：Counter, defaultdict

3. **使用 Enum 定義勢力**
   - 拒絕原因：過度複雜
   - 改用：簡單的字串

---

## 4. AI 可能誤導的案例

### 案例：namedtuple 屬性名稱衝突

**AI 建議**：
```python
General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def', 'spd', 'is_leader'])
```

**實際問題**：
Python 中 `def` 是關鍵字，不能作為變數名稱。

**自行修正**：
```python
General = namedtuple('General', ['faction', 'name', 'hp', 'atk', 'def_', 'spd', 'is_leader'])
```

**教訓**：AI 有時會忽略 Python 保留字的限制，需要自己注意。
