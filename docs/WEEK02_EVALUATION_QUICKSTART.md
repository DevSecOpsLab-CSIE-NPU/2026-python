# Week 02 PR Evaluation — Quick Start (5 min Overview)

## 🚀 TL;DR: How to Evaluate Week 02 PRs

### What Students Submit
✅ **3 Tasks** in `weeks/week-02/solutions/{student-id}/`:
1. `task1_sequence_clean.py` — Clean/dedupe sequences
2. `task2_student_ranking.py` — Sort & rank students
3. `task3_log_summary.py` — Count & aggregate logs

Plus docs: README.md, AI_USAGE.md, TEST_CASES.md, TEST_LOG.md, tests/

OR

✅ **30 Bloom Examples** (R01-R20 + U01-U10): Python examples from course

---

## ⏱️ Evaluation Time Budget

| Step | Time | Action |
|---|---|---|
| **1. Verify files** | 2 min | Check if all required files exist |
| **2. Run tests** | 3 min | `python -m pytest tests/ -v` |
| **3. Review code** | 10 min | Read task*.py files (data structures, style) |
| **4. Check docs** | 5 min | README.md, AI_USAGE.md, TEST_LOG.md |
| **5. Score & feedback** | 5 min | Fill scorecard, write PR comment |
| **TOTAL** | **~25 min** | Per PR |

---

## 📊 Quick Scoring (1-Minute Version)

```
Missing files? → -10 points
Tests fail? → -5 to -20 points  
Code uses Counter/dict/sorted? → +10 bonus
Uses O(n) algorithm? → +5 bonus
No comments or unclear names? → -3 to -5
Transparent AI disclosure? → Integrity ✅
```

**Result**: 
- **45-50** = Merge ✅
- **35-44** = Request changes ⚠️
- **<35** = Resubmit ❌

---

## 🔧 Command Cheat Sheet

```bash
# List PR files
gh pr view <PR#> --json files -q '.files[].path' | grep week-02

# Clone & test locally
git fetch origin pull/<PR#>/head:test-<PR#>
git checkout test-<PR#>

# Quick syntax check
python -m py_compile weeks/week-02/solutions/*/task*.py

# Run tests
cd weeks/week-02/solutions/<student-id>
python -m pytest tests/ -v

# View README
cat weeks/week-02/solutions/<student-id>/README.md

# Leave review  
gh pr review <PR#> --comment -b "Your feedback here"
```

---

## ✅ Merge Criteria (Make/Break)

### ✅ MERGE IF:
- [x] All required files present
- [x] No syntax errors
- [x] Tests pass 80%+
- [x] Uses Week 02 data structures (dict, Counter, sorted, deque, etc.)
- [x] Code is readable (PEP 8 names, clear logic)
- [x] AI_USAGE.md discloses any AI usage
- [x] Documentation explains approach

### ❌ REQUEST CHANGES IF:
- [ ] Missing 1-2 files
- [ ] <80% tests pass
- [ ] Code has poor style but logic is correct
- [ ] Documentation incomplete
- [ ] Data structure choices suboptimal
- [ ] Minor bugs in non-critical code

### ❌ CLOSE + RESUBMIT IF:
- [ ] Missing 3+ files or entire sections
- [ ] Code doesn't run (syntax errors)
- [ ] <50% tests pass
- [ ] No AI_USAGE.md (integrity concern)
- [ ] Wholesale copying (obvious plagiarism)

---

## 📝 PR Comment Template (Copy & Paste)

**For Approve:**
```markdown
## ✅ 審核通過 (Approved)

**分數**: 45/50 分 (Grade A)

**優點**:
- 清晰的程式碼結構
- 正確使用 Counter 和 defaultdict
- 完整的測試覆蓋

[APPROVE & MERGE]
```

**For Changes Requested:**
```markdown
## ⚠️ 需要修改 (Changes Requested)

**分數**: 38/50 分 (Grade C)

**需要改進**:
- [ ] Task 2 test case 失敗: 預期輸出與實際不符
- [ ] AI_USAGE.md 缺少細節說明
- [ ] Task 3 使用 O(n²) 排序，建議改用 sorted()

請修改後重新提交。

[REQUEST CHANGES]
```

**For Resubmit:**
```markdown
## ❌ 需要重新提交 (Resubmit)

**分數**: 25/50 分 (Grade F)

**重大問題**:
- [ ] 缺少 tests/ 目錄
- [ ] task2_*.py 無法執行 (ImportError)
- [ ] 無 AI_USAGE.md (誠信問題)

請完成所有要件後重新提交。

[CLOSE]
```

---

## 🎯 Week 02 Core Concepts (Quick Check)

| Concept | Check for | Sample Code |
|---|---|---|
| **Sequences** | Unpacking, slicing, `*args` | `a, b, *rest = items` |
| **Dicts** | `defaultdict()`, `Counter()` | `Counter(items)` |
| **Sorting** | `sorted()` with key function | `sorted(students, key=lambda x: x[1])` |
| **Grouping** | `groupby()`, `defaultdict` aggregation | `groupby(data, key=...)` |
| **Efficiency** | Avoid nested loops, use built-ins | Use `set` for O(1) lookup |

**Look for**: At least 3-4 of these in each task ✅

---

## 📋 Decision Tree

```
Does PR have all required files?
├─ NO → Request files + close (D/F)
└─ YES ↓
  
Does code run without errors?
├─ NO → Request fixes (D/F)  
└─ YES ↓

Do tests pass 80%+?
├─ NO → Request fixes (C/D)
└─ YES ↓

Is AI_USAGE.md present & honest?
├─ NO → Flag integrity issue (resubmit)
└─ YES ↓

Does code use Week 02 concepts?
├─ NO → Weak (C), suggest improvements
└─ YES ↓

Is documentation clear?
├─ NO → Minor feedback (B), suggest better README
└─ YES ↓

→ MERGE ✅ (A/B grade)
```

---

## 🚨 Red Flags (Automatic -20 points)

- [ ] Obvious plagiarism (identical code, copied solutions)
- [ ] No AI_USAGE.md + evidence of AI-generated code
- [ ] Hardcoded test values
- [ ] Broken imports or external dependencies not in requirements
- [ ] Rude/unprofessional commits or comments

---

## 💡 Quick Tips

### For Task 1 (Sequence Clean)
- Should use list operations, unpacking, or comprehensions
- Edge case: empty list, duplicates, single item
- ✅ Good: `list(dict.fromkeys(items))` or `sorted(set(items))`
- ❌ Bad: nested for loops checking duplicates

### For Task 2 (Student Ranking)  
- Should use `sorted()` with custom `key=` parameter
- Edge case: tie scores, large class size
- ✅ Good: `sorted(students, key=lambda x: (-x['score'], x['id']))`
- ❌ Bad: manual bubble sort or multiple sorts

### For Task 3 (Log Summary)
- Should use `Counter()` or `defaultdict(int)`
- Edge case: empty log, single entry, malformed lines
- ✅ Good: `Counter(parse(line) for line in logs)`
- ❌ Bad: manual dict with incrementing

---

## 📞 When to Escalate

**Ask instructor/TA if**:
- Plagiarism suspected (compare with online solutions)
- AI usage unclear (looks AI-generated but not disclosed)
- Grade boundary unclear (37-38 range): discuss rubric
- Special circumstance (illness, extension granted)

---

## ✨ Bonus Points (Optional Enhancements)

Award +5 bonus if PR includes:
- [ ] Performance analysis (Big O explanation)
- [ ] Additional test cases beyond minimum
- [ ] Alternative implementations compared
- [ ] Thoughtful refactoring feedback in comments
- [ ] Professional commit messages

---

## 📊 After Evaluation

1. ✅ **Save scorecard** → docs/evaluations/week02_{PR#}_{date}.md
2. 📝 **Leave PR comment** → Use template above
3. 🔀 **Merge or request changes** → Click button or leave comment
4. 📧 **Optional**: Email student with feedback summary

---

**Remember**: 
- Be constructive, not critical
- Point to specific lines or examples
- Suggest improvements, don't just complain
- Celebrate what they did right! 🎉

---

**Last Updated**: 2026-04-09
