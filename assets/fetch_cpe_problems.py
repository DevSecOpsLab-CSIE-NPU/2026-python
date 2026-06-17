#!/usr/bin/env python3
"""
CPE 題目管理系統 - 按週次分類
從預定義的題號映射自動建立題目骨架檔案
"""

import time
from pathlib import Path
from typing import Dict, List

# 題號到週次的映射表
PROBLEM_TO_WEEK = {
    # Week 2 - 資料結構基礎
    100: 2,
    118: 2,
    272: 2,
    299: 2,
    490: 2,
    # Week 3 - 字串處理
    948: 3,
    10008: 3,
    10019: 3,
    10035: 3,
    10038: 3,
    # Week 4 - 數字與日期
    10041: 4,
    10050: 4,
    10055: 4,
    10056: 4,
    10057: 4,
    # Week 6 - 迭代器應用
    10062: 6,
    10071: 6,
    10093: 6,
    10101: 6,
    10170: 6,
    # Week 7 - 檔案 I/O 基礎
    10189: 7,
    10190: 7,
    10193: 7,
    10221: 7,
    10222: 7,
    # Week 9 - 資料編碼
    10226: 9,
    10235: 9,
    10242: 9,
    10252: 9,
    10268: 9,
    # Week 10 - 函式進階
    10409: 10,
    10415: 10,
    10420: 10,
    10642: 10,
    10783: 10,
    # Week 11 - 類別與模組
    10812: 11,
    10908: 11,
    10922: 11,
    10929: 11,
    10931: 11,
    # Week 12 - 網路與共時
    11005: 12,
    11063: 12,
    11150: 12,
    11321: 12,
    11332: 12,
    # Week 13 - 綜合專案
    11349: 13,
    11417: 13,
    11461: 13,
    12019: 13,
}

# 基礎配置
BASE_URL = "https://yuihuang.com"
PROJECT_ROOT = Path(__file__).parent
WEEKS_DIR = PROJECT_ROOT / "weeks"


def organize_problems(problems: List[int]) -> Dict[int, List[int]]:
    """將問題按週次分類"""
    week_problems = {}
    for prob_id in problems:
        week = PROBLEM_TO_WEEK.get(prob_id)
        if week:
            if week not in week_problems:
                week_problems[week] = []
            week_problems[week].append(prob_id)
    return week_problems


def save_problem_template(problem_id: int, week_num: int) -> Path:
    """將題目樣板保存為 Markdown"""
    week_dir = WEEKS_DIR / f"week-{week_num:02d}" / "solutions"
    week_dir.mkdir(parents=True, exist_ok=True)

    # 以題號為檔名
    filename = f"{problem_id:05d}.md"
    filepath = week_dir / filename

    # 構造 Markdown 內容
    content = f"""# 題目 {problem_id}

**週次**: Week {week_num}  
**UVA 題號**: {problem_id}  
**官方題目**: https://yuihuang.com/uva-{problem_id}/

## 題目描述

[題目內容請見上方官方連結]

## 解題思路

*請填入解題思路*

## 解題代碼

```python
# 你的代碼這裡
```

## 測試用例

*測試輸入與預期輸出*
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def main():
    """主程式"""
    print("=" * 70)
    print("CPE 題目管理系統 - 按週次分類")
    print("=" * 70)
    print()

    # 使用預定義的題號映射
    problem_ids = list(PROBLEM_TO_WEEK.keys())

    print(f"📋 已配置 {len(problem_ids)} 道題目")
    print(f"   題號範圍: {min(problem_ids):5d} - {max(problem_ids):5d}")
    print()

    # 按週次分類
    print("📊 按週次分類:")
    week_problems = organize_problems(problem_ids)
    for week in sorted(week_problems.keys()):
        problems = week_problems[week]
        print(f"   Week {week:2d}: {len(problems):2d} 題 - {problems}")

    print()
    print("📝 建立題目骨架檔案...")
    print("-" * 70)

    # 建立每個題目的骨架檔案
    total_created = 0
    for week in sorted(week_problems.keys()):
        print(f"\n[Week {week:02d}]")
        for prob_id in week_problems[week]:
            filepath = save_problem_template(prob_id, week)
            print(f"✅ {filepath.name}")
            total_created += 1
            time.sleep(0.01)  # 短暫延遲

    print("\n" + "=" * 70)
    print(f"✅ 完成! 共建立 {total_created} 道題目骨架檔案")
    print()
    print("📌 後續步驟:")
    print("   1. 每個題號現已有對應的 .md 檔案在 week-XX/solutions/ 目錄")
    print("   2. 從 https://yuihuang.com/cpe-level-1/ 複製題目描述")
    print("   3. 在各檔案中填入解題代碼 (.py)")
    print("=" * 70)


if __name__ == "__main__":
    main()
