# Week 02 PR Evaluation Scorecard

**PR #**: ______  
**Student ID**: ________________  
**Date**: ________________  
**Evaluator**: ________________

---

## 📋 Quick Checklist

### ✅ File Structure (5 min)
```
weeks/week-02/solutions/{student-id}/
├── [ ] README.md
├── [ ] AI_USAGE.md
├── [ ] TEST_CASES.md
├── [ ] TEST_LOG.md
├── [ ] task1_sequence_clean.py
├── [ ] task2_student_ranking.py
├── [ ] task3_log_summary.py
└── tests/
    ├── [ ] test_task1.py
    ├── [ ] test_task2.py
    └── [ ] test_task3.py
```

**Missing Files**: _______________  
**File Status Score**: __/5

---

## 🔍 Code Quality Review (15 min)

### 1. **Correctness** (5 points)
| Aspect | ✅ Good | ⚠️ Minor | ❌ Bad | Score |
|---|---|---|---|---|
| **Syntax** | Runs clean | 1-2 warnings | Errors | _/5 |
| **Logic** | All correct | 1-2 bugs | Multiple bugs | _/5 |
| **Edge Cases** | Handled well | Partial | Missing | _/5 |

**Notes**: _______________________________________

**Correctness Score**: __/5

---

### 2. **Data Structures (Week 02 Focus)** (5 points)
- [ ] Uses `list`, `dict`, `set` appropriately
- [ ] Uses `Counter` or `defaultdict` 
- [ ] Uses `sorted()`, `heapq`, or `groupby()`
- [ ] Avoids unnecessary nested loops
- [ ] Time complexity ≤ O(n log n)

| Aspect | ✅ Excellent | ⚠️ Good | ❌ Poor | Score |
|---|---|---|---|---|
| **Structure Choice** | Right tools | Minor subopt | Wrong tools | _/5 |
| **Efficiency** | O(n) or O(n log n) | O(n²) acceptable | O(n³) or worse | _/5 |

**Data Structures Score**: __/5

---

### 3. **Style & Readability** (5 points)
| Aspect | ✅ Good | ⚠️ Minor | ❌ Poor | Score |
|---|---|---|---|---|
| **Naming** | Clear, snake_case | Some unclear | Bad names | _/5 |
| **Formatting** | PEP 8 compliant | Minor issues | Messy | _/5 |
| **Comments** | Where needed | Minimal | Missing | _/5 |

**Style Score**: __/5

**Code Quality Total**: __/15

---

## 🧪 Testing & Verification (10 min)

### Test Coverage (5 points)
| Case Type | Count | Pass? | Score |
|---|---|---|---|
| **Normal** | __/3+ | ☐ | _/2 |
| **Edge** | __/2+ | ☐ | _/2 |
| **Boundary** | __/1+ | ☐ | _/1 |

**Test Coverage Score**: __/5

---

### Unit Tests (5 points)
| Aspect | ✅ Good | ⚠️ Fair | ❌ Missing |
|---|---|---|---|
| **tests/ directory** | ☐ | ☐ | ☐ |
| **test files** | ☐ 3+ files | ☐ 1-2 files | ☐ none |
| **assertions** | ☐ 3+/file | ☐ 1-2/file | ☐ <1 |
| **Pass rate** | ☐ 100% | ☐ 50-99% | ☐ <50% |

**Unit Tests Score**: __/5

**Testing Total**: __/10

---

## 📖 Documentation (10 min)

### README.md (5 points)
- [ ] Explains problem statement
- [ ] Describes solution approach
- [ ] Lists data structures used
- [ ] Notes assumptions/limitations
- [ ] Written in Traditional Chinese (繁體中文)
- [ ] Proper Markdown formatting

**README Score**: __/5

### AI_USAGE.md (5 points)
- [ ] File exists
- [ ] Clearly states AI usage (yes/no)
- [ ] If yes: names tools (ChatGPT, Copilot, etc.)
- [ ] If yes: specifies what was generated vs modified
- [ ] Demonstrates integrity

**AI Transparency Score**: __/5

**Documentation Total**: __/10

---

## 🎓 Week 02 Concept Mastery (10 min)

Check which concepts are demonstrated:

| Concept | Example in Code | Demonstrated? | Points |
|---|---|---|---|
| **Sequences** | Uses slicing, unpacking, or operations | ☐ | _/2 |
| **Dictionaries** | Uses dict/defaultdict for lookups/aggregation | ☐ | _/2 |
| **Sorting** | Uses sorted() with custom keys | ☐ | _/2 |
| **Counting** | Uses Counter, groupby, or aggregation | ☐ | _/2 |
| **Collections** | Uses deque, namedtuple, or OrderedDict | ☐ | _/2 |

**Concept Mastery Score**: __/10

---

## 📊 Final Scoring

| Category | Max | Score |
|---|---|---|
| **1. Submission Completeness** | 5 | __/5 |
| **2. Code Quality** | 15 | __/15 |
| **3. Testing & Verification** | 10 | __/10 |
| **4. Documentation** | 10 | __/10 |
| **5. Week 02 Concept Mastery** | 10 | __/10 |
| **TOTAL** | **50** | **__/50** |

---

## 🎯 Grade & Recommendation

### Score to Grade Mapping
| Score Range | Grade | Status |
|---|---|---|
| 45-50 | A | ✅ Ready to merge |
| 40-44 | B | ✅ Merge with praise |
| 35-39 | C | ⚠️ Request minor changes |
| 30-34 | D | ❌ Request major changes |
| <30 | F | ❌ Resubmit |

**Final Grade**: _____ (**__/50**)

---

## 💬 Feedback Summary

### Strengths (2-3 points)
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

### Areas for Improvement (2-3 points)
1. _____________________________________________
2. _____________________________________________
3. _____________________________________________

---

## 📝 Detailed Comments

### Task 1: Sequence Clean
**Observation**: _________________________________  
**Feedback**: _________________________________  

### Task 2: Student Ranking
**Observation**: _________________________________  
**Feedback**: _________________________________  

### Task 3: Log Summary
**Observation**: _________________________________  
**Feedback**: _________________________________  

---

## ✅ Review Decision

- [ ] **APPROVE** — Merge to main
- [ ] **REQUEST CHANGES** — Specific improvements needed:
  - _____________________________________________
  - _____________________________________________
  - _____________________________________________
- [ ] **CLOSE** — Needs complete resubmission

---

## 📌 Next Steps for Student

1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

---

**Reviewed by**: ____________________  
**Date**: ____________________  
**Time spent**: ______ minutes  

---

## Quick Tips

### Code Review Commands
```bash
# Clone PR branch
git fetch origin pull/{PR}/head:review-{PR}
git checkout review-{PR}

# Check syntax
python -m py_compile weeks/week-02/solutions/*/task*.py

# Run tests  
cd weeks/week-02/solutions/{student-id}
python -m pytest tests/ -v

# View specific file
cat weeks/week-02/solutions/{student-id}/README.md
```

### Common Issues Quick Reference
| Issue | Score Impact | Fix |
|---|---|---|
| No AI_USAGE.md | -5 points | Request file |
| Syntax error | -3 points | Ask for fix |
| Missing tests | -5 points | Request tests |
| Poor naming | -2 points | Minor feedback |
| Complex O(n²) | -2 points | Suggest optimization |
