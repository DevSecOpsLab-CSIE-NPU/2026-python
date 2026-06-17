# Week 02 PR Evaluation Framework

**Overview**: Complete guide for evaluating all 67 week-02 student submissions labeled with `week02`

---

## 📚 Documentation Structure

This evaluation framework consists of 3 documents:

### 1. **WEEK02_EVALUATION_QUICKSTART.md** ⚡ (START HERE)
**For**: Quick reference during PR reviews  
**Length**: 5 minutes to read  
**Contains**:
- TL;DR scoring rubric
- Command cheat sheet
- Merge/request changes decision tree
- Red flags checklist
- PR comment templates (copy & paste ready)

**When to use**: 
- First time evaluating a week-02 PR
- Need quick decision on approve/changes/close
- Want to understand concepts to look for

---

### 2. **WEEK02_SCORECARD.md** 📋
**For**: Filling out during actual PR review  
**Length**: Printable 2-page form  
**Contains**:
- File structure checklist
- Code quality rubric (syntax, logic, style)
- Testing verification checklist
- Documentation assessment
- Concept mastery grid
- Scoring table (0-50 points)
- Grade scale (A-F)
- Feedback summary template

**When to use**:
- Reviewing a specific PR
- Want to score systematically
- Need to track evaluation time
- Want consistent feedback format

**How to use**:
```bash
# Print for physical review (if preferred)
# OR use digital version in editor
# Fill checkbox as you review each PR
# Write final feedback in comments section
```

---

### 3. **WEEK02_EVALUATION_GUIDE.md** 📖 (Reference)
**For**: Deep understanding of evaluation criteria  
**Length**: Comprehensive reference (~30 min read)  
**Contains**:
- Expected submission structure
- Detailed scoring rubric (5 categories, 50 points)
- Per-category breakdown:
  - Submission Completeness (5 points)
  - Code Quality (15 points: correctness, data structures, style)
  - Testing & Verification (10 points)
  - Documentation (10 points: README, AI_USAGE)
  - Week 02 Concept Mastery (10 points)
- Evaluation workflow (5 steps)
- Common issues & scoring guidance
- PR comment template
- Quality standards (merge-ready, needs revision, resubmit)
- Expected student learning outcomes

**When to use**:
- First time establishing evaluation standards
- Disagreement on scoring → refer to criteria
- Creating custom evaluation for your context
- Understanding why specific rubric choices

---

## 🎯 How to Use This Framework

### For First-Time Evaluators
1. **Read** `WEEK02_EVALUATION_QUICKSTART.md` (5 min)
2. **Print/Open** `WEEK02_SCORECARD.md` (for reference)
3. **Evaluate** each PR following the scorecard
4. **Reference** `WEEK02_EVALUATION_GUIDE.md` if unsure about scoring

### For Experienced Evaluators  
1. Use `WEEK02_SCORECARD.md` as checklist
2. Reference `WEEK02_EVALUATION_QUICKSTART.md` for quick decisions
3. Consult `WEEK02_EVALUATION_GUIDE.md` for edge cases

### For Consistent Team Evaluation
1. **Everyone reads** `WEEK02_EVALUATION_GUIDE.md` first (alignment)
2. **Everyone uses** `WEEK02_SCORECARD.md` (consistency)
3. **Share feedback** using templates from quickstart

---

## 📊 Quick Reference Table

| Document | Read Time | Purpose | Format |
|---|---|---|---|
| **Quickstart** | 5 min | Decision making | Bullets, tables, templates |
| **Scorecard** | 25 min (while reviewing) | Systematic evaluation | Checklist, rubric, grid |
| **Guide** | 30 min | Understanding standards | Detailed criteria, examples |

---

## 🔍 Evaluation Summary

### Week 02 Learning Objectives
Students should demonstrate understanding of:
- **Sequences**: `list`, unpacking, slicing, `*args`
- **Dictionaries**: `dict`, `defaultdict`, `Counter`
- **Sorting**: `sorted()` with custom keys
- **Grouping**: `groupby()`, aggregation patterns
- **Efficiency**: Avoiding O(n²), using built-ins

### Submission Patterns (67 PRs to evaluate)
| Pattern | Count | Example |
|---|---|---|
| **Task-based** | ~50 | 3 tasks + docs + tests |
| **Bloom examples** | ~15 | 30 example files (R01-U10) |
| **Mixed** | ~2 | Both approaches combined |

### Grading Scale
| Score | Grade | Status | Action |
|---|---|---|---|
| 45-50 | A | Excellent | ✅ Merge |
| 40-44 | B | Good | ✅ Merge + praise |
| 35-39 | C | Satisfactory | ⚠️ Request changes |
| 30-34 | D | Below expectation | ❌ Request major changes |
| <30 | F | Incomplete | ❌ Resubmit |

---

## 🚀 Getting Started: Step-by-Step

### Before You Start
```bash
# Get the PR number
gh pr list --label week02 --state closed | head -20

# Clone the PR locally
git fetch origin pull/<PR#>/head:review-<PR#>
git checkout review-<PR#>

# List files to check structure
find weeks/week-02/solutions -type f -name "*.py" | head -15
```

### During Evaluation (25 min process)
```
1. Check files exist (2 min)
   └─ Use SCORECARD "File Structure" section
   
2. Run tests (3 min)
   └─ cd weeks/week-02/solutions/<student-id>
      python -m pytest tests/ -v
      
3. Review code (10 min)  
   └─ Read task*.py files
      Check: data structures, algorithm efficiency, style
      
4. Check documentation (5 min)
   └─ README.md: approach explanation
      AI_USAGE.md: integrity check
      TEST_LOG.md: test results
      
5. Score & feedback (5 min)
   └─ Fill SCORECARD
      Write PR comment using QUICKSTART template
```

### After Evaluation
```
1. Save scorecard (optional but recommended)
2. Leave PR comment with feedback
3. Click [APPROVE & MERGE] or [REQUEST CHANGES]
```

---

## 📋 File Location Quick Links

All evaluation documents in `/docs/`:
```
docs/
├── COURSE_PLAN.md                          # Course schedule (read first)
├── WEEK02_EVALUATION_README.md             # THIS FILE
├── WEEK02_EVALUATION_QUICKSTART.md         # ⭐ Start here
├── WEEK02_SCORECARD.md                     # Use while reviewing
├── WEEK02_EVALUATION_GUIDE.md              # Reference guide
└── analysis/
    ├── FINAL_SUMMARY.md
    └── VERIFICATION_REPORT.md
```

---

## 💡 Key Decisions

### What counts as "Complete"?
✅ Either of these is acceptable:
- **Task-based** (3 tasks): task1_*.py, task2_*.py, task3_*.py + docs + tests
- **Bloom examples** (30 files): All R01-R20 and U01-U10 files

### What's acceptable for AI disclosure?
✅ **GOOD**:
- "I used ChatGPT to debug Task 2, modified 30% of generated code"
- "Used GitHub Copilot for syntax suggestions, wrote logic myself"
- "No AI tools used, all original work"

❌ **NOT ACCEPTABLE**:
- No AI_USAGE.md file at all
- "Used AI" with no detail
- Evidence of AI but not disclosed

### What if tests don't pass?
- **1-2 failures** out of 20+ tests → 3-4/5 (request fixes)
- **3-5 failures** → 2-3/5 (request major fixes)
- **>50% failing** → F grade (resubmit)

### What if code is inefficient?
- **O(n log n) or better** → Full points
- **O(n²) but correct** → 2/5 on efficiency (suggest optimization)
- **O(n³+) or wrong algorithm** → 0/5 (request rewrite)

---

## 🎓 Learning Outcomes Checklist

After Week 02, students should:

### Remember (Bloom Level 1)
- [ ] Identify when to use `deque` vs `list`
- [ ] Name `Counter` and `defaultdict` use cases
- [ ] Explain difference between `sort()` and `sorted()`

### Understand (Bloom Level 2)
- [ ] Explain tradeoffs between data structure choices
- [ ] Describe why `O(n log n)` is better than `O(n²)`
- [ ] Apply `groupby()` to aggregate data

### Apply (Bloom Level 3+)
- [ ] **Task 1**: Clean sequences using list operations ✅
- [ ] **Task 2**: Rank items using sorting + counting ✅
- [ ] **Task 3**: Analyze data using grouping + aggregation ✅

---

## 🔧 Troubleshooting

### "I'm not sure if this deserves A or B"
→ Read WEEK02_EVALUATION_GUIDE.md section "Total Score Calculation"

### "The code works but I think it's inefficient"
→ Check data structure choice in QUICKSTART section "Week 02 Core Concepts"

### "Student used AI but didn't clearly disclose it"
→ See QUICKSTART red flags or GUIDE integrity section

### "Tests fail but code logic seems right"
→ Might be edge case handling (common for week-02)
→ Score as 3-4/5, suggest specific test fixes

### "PR has files but structure looks different"
→ Check EVALUATION_GUIDE for "Alternative: Bloom Examples Structure"

---

## 📈 After All PRs Are Evaluated

### Summary Statistics to Collect
```
Total PRs evaluated: 67
Grade distribution:
  A (45-50): ___
  B (40-44): ___
  C (35-39): ___
  D (30-34): ___
  F (<30):   ___

Most common issues:
  - [issue]: ___ occurrences
  - [issue]: ___ occurrences
  
Most commonly used data structures:
  - Counter: ___ PRs
  - defaultdict: ___ PRs
  - sorted(): ___ PRs
```

### Feedback to Instructors
- Which concepts need clarification (Week 03 prep)
- Which assignments worked well
- Suggestions for next iteration

---

## 📞 Contact & Updates

**Questions about this framework?**
- Review WEEK02_EVALUATION_GUIDE.md first
- Ask instructor if criteria unclear

**Found an issue?**
- Note the problem
- Suggest improvement to framework maintainer

**Want to adapt this?**
- Copy structure to WEEK03_EVALUATION_*.md
- Adjust categories for week-3 concepts
- Share improvements back

---

## 📝 Version History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-04-09 | Initial framework created |
| | | - Evaluation guide (50-point rubric) |
| | | - Printable scorecard |
| | | - Quick-start reference |
| | | - This README |

---

## ✨ Key Principles of This Framework

1. **Clear criteria**: 50 points, 5 categories, specific rubrics
2. **Actionable feedback**: Students know exactly what to improve
3. **Consistent**: Same evaluation across all evaluators
4. **Efficient**: 25 min per PR evaluation
5. **Fair**: Rubric accounts for both bloom-example and task-based submissions
6. **Transparent**: AI usage, integrity, effort all visible

---

**Start here**: Open `WEEK02_EVALUATION_QUICKSTART.md`

**Print this**: Open `WEEK02_SCORECARD.md`

**Reference**: Open `WEEK02_EVALUATION_GUIDE.md`

Good luck with your evaluations! 🎉
