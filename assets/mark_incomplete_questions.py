#!/usr/bin/env python3
"""
CPE 題目系統 - 標記無法爬取的題目並優雅降級

策略：
1. 對於成功爬取的題目（14 題）：保持原樣
2. 對於 ZJ 500 錯誤的題目（18 題）：添加「【待補充】」標記和連結提示
3. 對於部分缺失的題目（17 題）：填補缺失的欄位
"""

import re
from pathlib import Path
from typing import Tuple

PROJECT_ROOT = Path(__file__).parent
WEEKS_DIR = PROJECT_ROOT / "weeks"

# 失敗的 ZJ ID（500 錯誤）
FAILED_ZJ_IDS = {
    10035: "a028",
    10038: "a031",
    10050: "a043",
    10056: "a049",
    10057: "a050",
    10170: "a163",
    10221: "a214",
    10409: "a402",
    10415: "a408",
    10420: "a413",
    10642: "a635",
    10783: "a776",
    10812: "a805",
    10908: "a901",
    10929: "a922",
    10931: "a924",
    11005: "a998",
    11417: "b410",
}


def check_file_completion(filepath: Path) -> Tuple[bool, int]:
    """檢查檔案內容完整性"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    desc_match = re.search(r"## 題目敘述\n(.*?)(?=##|\Z)", content, re.DOTALL)
    input_match = re.search(r"## 輸入說明\n(.*?)(?=##|\Z)", content, re.DOTALL)
    output_match = re.search(r"## 輸出說明\n(.*?)(?=##|\Z)", content, re.DOTALL)

    desc_len = len(desc_match.group(1).strip()) if desc_match else 0
    input_len = len(input_match.group(1).strip()) if input_match else 0
    output_len = len(output_match.group(1).strip()) if output_match else 0

    total_len = desc_len + input_len + output_len
    is_complete = total_len > 500

    return is_complete, total_len


def generate_placeholder_content(
    problem_id: int,
    zj_id: str,
) -> str:
    """為無法爬取的題目生成佔位符內容"""
    return f"""# 題目 {problem_id}

**題名**: UVA {problem_id}

> ⚠️ **【待補充】** 此題的內容暫時無法從 ZeroJudge 爬取
>
> 【狀態】題目敘述、輸入說明、輸出說明待補充
>
> 【建議】請參考以下連結自行補充：
> - [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid={zj_id})
> - [UVA Online Judge](https://uva.onlinejudge.org/external/{problem_id}.pdf)
> - [Yui Huang 題解參考](https://yuihuang.com/cpe-level-1/)

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid={zj_id})
- [UVA Online Judge](https://uva.onlinejudge.org/external/{problem_id}.pdf)

## 題目敘述

[【待補充】請從上述連結複製題目敘述]

## 輸入說明

[【待補充】請從上述連結複製輸入說明]

## 輸出說明

[【待補充】請從上述連結複製輸出說明]

---

## 解題思路

*請填入你的解題思路*

## 解題代碼

```python
# 你的代碼這裡
```

## 測試用例

*測試輸入與預期輸出*
"""


def update_incomplete_file(
    problem_id: int,
    week_num: int,
    filepath: Path,
    is_failed: bool,
) -> bool:
    """更新不完整的檔案"""
    if is_failed:
        # 此題目無法爬取，使用佔位符
        zj_id = FAILED_ZJ_IDS.get(problem_id, "unknown")
        content = generate_placeholder_content(problem_id, zj_id)
    else:
        # 讀取現有內容，補充缺失的欄位
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ 保存失敗: {e}")
        return False


def main():
    print("=" * 70)
    print("CPE 題目系統 - 標記無法爬取的題目")
    print("=" * 70)
    print()

    # 掃描所有題目文件
    incomplete_count = 0
    failed_count = 0
    success_count = 0

    for week_dir in sorted(WEEKS_DIR.glob("week-*")):
        if not week_dir.is_dir():
            continue

        week_num = int(week_dir.name.split("-")[1])
        print(f"\n[Week {week_num:02d}]")

        for qfile in sorted(week_dir.glob("QUESTION-*.md")):
            match = re.search(r"QUESTION-(\d+)", qfile.name)
            if not match:
                continue

            problem_id = int(match.group(1))
            is_complete, length = check_file_completion(qfile)

            if is_complete:
                print(f"  ✅ {problem_id}: 完整 ({length} 字)")
                success_count += 1
            elif problem_id in FAILED_ZJ_IDS:
                # 此題無法爬取，更新為佔位符
                print(f"  ⚠️  {problem_id}: 無法爬取 - 設置佔位符", end=" ")
                if update_incomplete_file(problem_id, week_num, qfile, is_failed=True):
                    print("✅")
                    failed_count += 1
                else:
                    print("❌")
            else:
                # 其他不完整的題目
                print(f"  ◐ {problem_id}: 部分填充 ({length} 字)")
                incomplete_count += 1

    print("\n" + "=" * 70)
    print("完成度統計:")
    print("=" * 70)
    print(f"✅ 完整填充: {success_count}/49 ({success_count * 100 // 49}%)")
    print(f"⚠️  待補充:  {failed_count}/49 ({failed_count * 100 // 49}%)")
    print(f"◐ 部分填充: {incomplete_count}/49 ({incomplete_count * 100 // 49}%)")
    print("=" * 70)
    print()
    print("【後續步驟】")
    print("1. 成功填充的 14 題可直接使用")
    print("2. 待補充的 18 題可由老師或學生自行補充")
    print("3. 建議保留待補充題目以激勵學生自主學習")


if __name__ == "__main__":
    main()
