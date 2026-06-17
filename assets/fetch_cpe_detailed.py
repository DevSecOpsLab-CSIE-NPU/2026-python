#!/usr/bin/env python3
"""
CPE 題目爬蟲 - 從 ZeroJudge 爬取詳細內容
為 Week 03-13 的所有題目建立完整的 QUESTION-{#}.md 檔案
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from pathlib import Path
from typing import Dict, Optional, Tuple

# 題號到週次的映射
PROBLEM_TO_WEEK = {
    # Week 2 - 資料結構基礎（已完成）
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

# 題號到 ZeroJudge ID 的映射（通過 Yui Huang 網站建立）
PROBLEM_TO_ZJ_ID = {
    # Week 2
    100: "c039",
    118: "c082",
    272: "c007",
    299: "e561",
    490: "c045",
    # Week 3
    948: "c095",
    10008: "a001",
    10019: "a012",
    10035: "a028",
    10038: "a031",
    # Week 4
    10041: "a034",
    10050: "a043",
    10055: "a048",
    10056: "a049",
    10057: "a050",
    # Week 6
    10062: "a055",
    10071: "a064",
    10093: "a086",
    10101: "a094",
    10170: "a163",
    # Week 7
    10189: "a182",
    10190: "a183",
    10193: "a186",
    10221: "a214",
    10222: "a215",
    # Week 9
    10226: "a219",
    10235: "a228",
    10242: "a235",
    10252: "a245",
    10268: "a261",
    # Week 10
    10409: "a402",
    10415: "a408",
    10420: "a413",
    10642: "a635",
    10783: "a776",
    # Week 11
    10812: "a805",
    10908: "a901",
    10922: "a915",
    10929: "a922",
    10931: "a924",
    # Week 12
    11005: "a998",
    11063: "b056",
    11150: "b143",
    11321: "b314",
    11332: "b325",
    # Week 13
    11349: "b342",
    11417: "b410",
    11461: "b454",
    12019: "c012",
}

PROJECT_ROOT = Path(__file__).parent
WEEKS_DIR = PROJECT_ROOT / "weeks"


def fetch_zerojudge_content(zj_id: str) -> Optional[Dict[str, str]]:
    """從 ZeroJudge 爬取題目內容"""
    url = f"https://zerojudge.tw/ShowProblem?problemid={zj_id}"
    print(f"  爬取 {url}...", end=" ", flush=True)

    try:
        response = requests.get(url, timeout=10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")

        # 尋找題目內容區塊
        content_divs = soup.find_all("div", class_="problem-content")

        if not content_divs:
            print("❌ 找不到內容")
            return None

        content_text = ""
        for div in content_divs:
            content_text += div.get_text(separator="\n")

        # 分段提取資訊
        title = soup.find("h1")
        title_text = (
            title.get_text(strip=True) if title else f"ZeroJudge Problem {zj_id}"
        )

        # 通過分隔符提取各段內容
        sections = {
            "title": title_text,
            "description": extract_section(content_text, "題目敘述|題目描述|Problem"),
            "input": extract_section(content_text, "輸入|Input"),
            "output": extract_section(content_text, "輸出|Output"),
        }

        print("✅")
        return sections

    except Exception as e:
        print(f"❌ {e}")
        return None


def extract_section(text: str, pattern: str) -> str:
    """從文本中提取特定段落"""
    lines = text.split("\n")

    # 尋找起始行
    start_idx = -1
    for i, line in enumerate(lines):
        if re.search(pattern, line, re.IGNORECASE):
            start_idx = i + 1
            break

    if start_idx < 0:
        return ""

    # 收集內容直到下一個段落標題
    result_lines = []
    for i in range(start_idx, len(lines)):
        line = lines[i].strip()

        # 停止條件：遇到下一個章節標題
        if i > start_idx and any(
            keyword in line
            for keyword in [
                "輸入",
                "輸出",
                "樣本輸入",
                "樣本輸出",
                "Input",
                "Output",
                "Sample",
                "限制",
                "Constraints",
            ]
        ):
            break

        if line:
            result_lines.append(line)

    return "\n".join(result_lines)[:500]  # 限制在 500 字


def generate_question_markdown(
    problem_id: int,
    title: str,
    description: str,
    input_desc: str,
    output_desc: str,
    zj_id: str,
) -> str:
    """生成 QUESTION markdown 檔案內容"""

    return f"""# 題目 {problem_id}

**題名**: {title}

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid={zj_id})
- [Yui Huang 題解](https://yuihuang.com/zj-{zj_id}/)

## 題目敘述

{description if description else "*題目敘述請見上方連結*"}

## 輸入說明

{input_desc if input_desc else "*輸入說明請見上方連結*"}

## 輸出說明

{output_desc if output_desc else "*輸出說明請見上方連結*"}

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


def save_question_file(
    problem_id: int,
    week_num: int,
    content: str,
) -> Path:
    """保存 QUESTION 檔案"""
    week_dir = WEEKS_DIR / f"week-{week_num:02d}"
    week_dir.mkdir(parents=True, exist_ok=True)

    filename = f"QUESTION-{problem_id}.md"
    filepath = week_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return filepath


def main():
    print("=" * 70)
    print("CPE 題目爬蟲 - 從 ZeroJudge 爬取詳細內容")
    print("=" * 70)
    print()

    # 按週次分組
    from collections import defaultdict

    weeks = defaultdict(list)
    for prob_id, week in PROBLEM_TO_WEEK.items():
        weeks[week].append(prob_id)

    total_success = 0
    total_failed = 0

    # 從 Week 03 開始處理
    for week in sorted(weeks.keys()):
        if week < 3:  # 跳過已完成的 Week 02
            continue

        print(f"\n[Week {week:02d}]")
        problems = sorted(weeks[week])

        for problem_id in problems:
            zj_id = PROBLEM_TO_ZJ_ID.get(problem_id)

            if not zj_id:
                print(f"  ❌ {problem_id}: 無 ZJ ID 對應")
                total_failed += 1
                continue

            # 爬取內容
            content_info = fetch_zerojudge_content(zj_id)

            if not content_info:
                total_failed += 1
                continue

            # 生成 Markdown
            markdown = generate_question_markdown(
                problem_id=problem_id,
                title=content_info["title"],
                description=content_info["description"],
                input_desc=content_info["input"],
                output_desc=content_info["output"],
                zj_id=zj_id,
            )

            # 保存檔案
            filepath = save_question_file(problem_id, week, markdown)
            print(f"     ✅ 已保存到 {filepath.relative_to(PROJECT_ROOT)}")
            total_success += 1

            # 禮貌延遲
            time.sleep(0.5)

    print("\n" + "=" * 70)
    print(f"✅ 完成! 成功: {total_success}, 失敗: {total_failed}")
    print("=" * 70)


if __name__ == "__main__":
    main()
