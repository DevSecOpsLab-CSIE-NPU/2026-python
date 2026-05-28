# Week 02 PR Evaluation Guide

**標題**: 資料結構基礎：序列與字典、排序與計數  
**期間**: 115/03/02 - 115/03/08  
**題號**: UVA 100, 118, 272, 299, 490  
**標籤**: `week02`

---

## 📋 Submission Structure

### Expected Directory Layout
```
weeks/week-02/solutions/{student-id}/
├── README.md                  # 作業說明與實現思路
├── AI_USAGE.md               # AI 使用透明度聲明
├── TEST_CASES.md             # 測試輸入與預期輸出
├── TEST_LOG.md               # 實際測試執行結果
│
├── task1_sequence_clean.py   # 任務1：序列處理
├── task2_student_ranking.py  # 任務2：學生排名系統
├── task3_log_summary.py      # 任務3：日誌分析統計
│
└── tests/
    ├── test_task1.py         # 單元測試
    ├── test_task2.py
    └── test_task3.py
```

### Alternative: Bloom Examples Structure
```
weeks/week-02/solutions/{student-id}/
├── R01-sequence-unpack.py     # 記憶階段 (Bloom Level 1)
├── R02-star-unpack.py
├── R03-deque.py
├── ... (R01-R20)
│
├── U01-unpack-mismatch.py     # 理解階段 (Bloom Level 2)
├── U02-star-unpack-list.py
├── ... (U01-U10)
```

---

## ✅ Evaluation Checklist

### 1️⃣ **Submission Completeness** (5 points)
- [ ] All 3 task files present (`task1_*.py`, `task2_*.py`, `task3_*.py`)
  - **OR** All 30 Bloom example files present (R01-R20, U01-U10)
- [ ] README.md exists and explains the solution
- [ ] AI_USAGE.md exists (documents AI usage if any)
- [ ] TEST_CASES.md exists (shows expected inputs/outputs)
- [ ] TEST_LOG.md exists (actual test results)
- [ ] tests/ directory with unit tests (if task-based)

**Scoring**:
- ✅ Complete (all required files): **5/5**
- ⚠️  Missing 1-2 files: **3-4/5**
- ❌ Missing 3+ files or docs: **0-2/5**

---

### 2️⃣ **Code Quality** (15 points)

#### 2.1 **Correctness** (5 points)
- [ ] Code runs without syntax errors
- [ ] Functions/logic match task requirements
- [ ] Edge cases handled (empty inputs, single item, duplicates)
- [ ] No hardcoded test values

**Scoring**:
- ✅ All test cases pass, clean code: **5/5**
- ⚠️  1-2 test failures or minor issues: **3-4/5**
- ❌ Multiple failures or logic errors: **0-2/5**

#### 2.2 **Data Structures (Core to Week 02)** (5 points)
- [ ] Appropriate use of:
  - `list`, `dict`, `set`, `deque`
  - `Counter`, `defaultdict`, `OrderedDict`
  - `heapq`, `sorted()`, `groupby()`
- [ ] Avoids unnecessary loops where built-ins exist
- [ ] Efficient algorithms (not O(n²) sorting, etc.)

**Scoring**:
- ✅ Excellent data structure usage, O(n) or O(n log n): **5/5**
- ⚠️  Good usage but some inefficiency: **3-4/5**
- ❌ Poor choices or inefficient (O(n²+)): **0-2/5**

#### 2.3 **Style & Readability** (5 points)
- [ ] Follows PEP 8 naming (snake_case, meaningful names)
- [ ] Proper indentation and spacing
- [ ] Comments on complex logic
- [ ] Functions are focused (single responsibility)
- [ ] No magic numbers (use constants)

**Scoring**:
- ✅ Clean, professional code: **5/5**
- ⚠️  Mostly good, minor style issues: **3-4/5**
- ❌ Poor naming, messy structure: **0-2/5**

---

### 3️⃣ **Testing & Verification** (10 points)

#### 3.1 **Test Coverage** (5 points)
- [ ] TEST_CASES.md includes:
  - Normal case (happy path)
  - Edge case (empty, single item)
  - Boundary case (large input, special values)
  - Multiple test cases per task (3+ minimum)
- [ ] TEST_LOG.md shows execution with actual output

**Scoring**:
- ✅ 3+ comprehensive cases, all passing: **5/5**
- ⚠️  2-3 cases or 1-2 failures: **3-4/5**
- ❌ <2 cases or >2 failures: **0-2/5**

#### 3.2 **Unit Tests (if applicable)** (5 points)
- [ ] tests/test_*.py files exist
- [ ] Tests import from task modules correctly
- [ ] 3+ assertions per test file
- [ ] Tests pass (shown in TEST_LOG.md)

**Scoring**:
- ✅ Complete, all passing: **5/5**
- ⚠️  Partial or 1-2 failures: **3-4/5**
- ❌ Missing or broken: **0-2/5**

---

### 4️⃣ **Documentation** (10 points)

#### 4.1 **README.md** (5 points)
- [ ] Explains the problem for each task
- [ ] Shows the solution approach (algorithm, data structures used)
- [ ] Lists any assumptions or limitations
- [ ] Written in clear Traditional Chinese (繁體中文)
- [ ] Proper Markdown formatting

**Scoring**:
- ✅ Clear, comprehensive explanation: **5/5**
- ⚠️  Adequate but missing some details: **3-4/5**
- ❌ Vague or poorly structured: **0-2/5**

#### 4.2 **AI_USAGE.md** (5 points)
- [ ] Transparently documents AI tool usage (ChatGPT, Copilot, etc.)
- [ ] If none used: clearly states "No AI used"
- [ ] If used: specifies:
  - Which tools
  - What parts (debugging, code generation, testing, etc.)
  - Modifications made to generated code
- [ ] Shows intellectual integrity

**Scoring**:
- ✅ Clear, honest disclosure: **5/5**
- ⚠️  Present but vague: **3-4/5**
- ❌ Missing or misleading: **0-2/5**

---

### 5️⃣ **Week 02 Concept Mastery** (10 points)

#### Core Concepts (check alignment with course objectives)
- [ ] **Sequences**: Uses appropriate sequence operations (unpacking, slicing, sorting)
- [ ] **Dictionaries**: Uses dict/defaultdict for aggregation, lookup
- [ ] **Sorting & Counting**: Uses `sorted()`, `Counter`, `groupby()` appropriately
- [ ] **Collections**: Uses `deque`, `namedtuple`, or `OrderedDict` if relevant

**Scoring**:
- ✅ Demonstrates mastery of 3+ concepts: **10/10**
- ⚠️  Shows understanding of 2 concepts: **6-9/10**
- ❌ Weak or missing concept understanding: **0-5/10**

---

## 📊 Total Score Calculation

| Category | Max | Student |
|---|---|---|
| Submission Completeness | 5 | ___ |
| Code Quality | 15 | ___ |
| Testing & Verification | 10 | ___ |
| Documentation | 10 | ___ |
| Week 02 Concept Mastery | 10 | ___ |
| **TOTAL** | **50** | **___** |

### Grade Scale
- **45-50**: A (Excellent - ready for Week 03)
- **40-44**: B (Good - minor improvements needed)
- **35-39**: C (Satisfactory - needs revision before Week 03)
- **30-34**: D (Below expectations - discuss with instructor)
- **<30**: F (Incomplete - resubmit)

---

## 🔍 Evaluation Workflow

### Step 1: Verify Submission Completeness (2 min)
```bash
# Check file structure
gh pr view <PR_NUMBER> --json files -q '.files[].path' | grep "week-02/solutions"

# List files to verify structure
```

### Step 2: Review Code Quality (10 min)
```bash
# Clone PR branch locally
git fetch origin pull/<PR_NUMBER>/head:week02-review-<PR_NUMBER>
git checkout week02-review-<PR_NUMBER>

# Read task files
cat weeks/week-02/solutions/<student-id>/task1_sequence_clean.py

# Check if Python syntax is valid
python -m py_compile weeks/week-02/solutions/<student-id>/task*.py
```

### Step 3: Run Tests (5 min)
```bash
# Run unit tests
cd weeks/week-02/solutions/<student-id>
python -m pytest tests/ -v

# Check TEST_LOG.md for recorded results
cat TEST_LOG.md
```

### Step 4: Review Documentation (5 min)
- Read README.md → Solution approach
- Read AI_USAGE.md → Integrity check
- Read TEST_CASES.md → Coverage verification

### Step 5: Score & Provide Feedback (10 min)
- Fill out evaluation checklist
- Calculate total score
- Write constructive feedback:
  ```markdown
  ### Review Summary
  **Score**: XX/50 (Grade: X)
  
  **Strengths**:
  - [List 2-3 strong points]
  
  **Areas for Improvement**:
  - [List 2-3 improvement areas]
  
  **Specific Comments**:
  - [Task 1]: [feedback]
  - [Task 2]: [feedback]
  - [Task 3]: [feedback]
  
  **Next Steps**:
  - [If revision needed: clear guidance]
  ```

---

## 💡 Common Issues & How to Score

### Issue: Missing test files
- If TEST_CASES.md is thorough → 4/5 on testing
- If only task files exist → 2/5 on testing

### Issue: Code works but uses inefficient algorithms
- Correct but O(n²) sort → 3-4/5 on data structures
- Should use week-02 tools (Counter, groupby, etc.)

### Issue: No AI_USAGE.md file
- If student actually used no AI → still 0/5 (must declare)
- If student used AI but didn't disclose → flag for integrity review

### Issue: Mixed language (English + Chinese)
- Prefer Traditional Chinese (繁體中文) for education consistency
- If mostly English: -1 point on documentation

### Issue: Bloom examples instead of tasks
- Both are valid, score equally:
  - **Completeness**: All 30 files present = 5/5
  - **Code Quality**: Examples are correct + match Bloom definition
  - **Testing**: Examples run = 4/5 (less formal testing)
  - **Concept Mastery**: All examples show understanding

---

## 📝 PR Comment Template

```markdown
## 評分結果 (Evaluation Result)

**總分**: XX/50 分 (Grade: X)

### 檢查清單
- [ ] 提交完整性: X/5
- [ ] 程式碼品質: X/15
- [ ] 測試驗證: X/10
- [ ] 文件品質: X/10
- [ ] Week 02 概念掌握: X/10

### 優點 (Strengths)
- ...

### 改進空間 (Areas for Improvement)
- ...

### 意見反饋 (Specific Feedback)
- **Task 1**: ...
- **Task 2**: ...
- **Task 3**: ...

[MERGED/REQUEST CHANGES based on score]
```

---

## 🚀 Quality Standards

### ✅ Merge-Ready (A/B grade)
- All files present and well-structured
- 90%+ test pass rate
- Clear code following PEP 8
- Comprehensive documentation
- No integrity concerns
- **Action**: ✅ Approve & Merge

### ⚠️ Needs Revision (C grade)
- Missing minor files or tests
- Some failing test cases
- Code works but needs optimization
- Documentation incomplete
- **Action**: Request changes with specific guidance

### ❌ Resubmit (D/F grade)
- Core files missing
- Code doesn't run
- Major test failures
- No documentation
- Integrity concerns
- **Action**: Close with feedback, request resubmission

---

## 🎯 Expected Outcomes

After Week 02, students should demonstrate:

1. **Bloom Level 1 (Remember)**: Know sequence/dict operations
   - Can write `Counter()`, `defaultdict()` usage
   - Understand `sorted()`, `heapq` basics
   
2. **Bloom Level 2 (Understand)**: Explain tradeoffs
   - Why use `deque` vs `list`
   - When to use `defaultdict` vs regular dict
   
3. **Application (Apply)**: Use in real tasks
   - Task 1: Sequence cleaning using list operations
   - Task 2: Ranking using sorting + counting
   - Task 3: Analysis using grouping + aggregation

---

Last Updated: 2026-04-09  
Evaluator: [Your Name]
