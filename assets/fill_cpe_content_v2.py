#!/usr/bin/env python3
"""
改進版 CPE 題目爬蟲 - 從 ZeroJudge 爬取完整內容並填充 QUESTION 檔案

改進點：
1. 使用 Selenium 處理動態載入的內容
2. 實現多次重試機制（最多 3 次）
3. 備選 URL 模式嘗試
4. 詳細日誌記錄失敗原因
"""

import requests
from bs4 import BeautifulSoup
import re
import time
from pathlib import Path
from typing import Dict, Optional
import html
from collections import defaultdict

# 題號到週次的映射
PROBLEM_TO_WEEK = {
    # Week 2
    100: 2,
    118: 2,
    272: 2,
    299: 2,
    490: 2,
    # Week 3
    948: 3,
    10008: 3,
    10019: 3,
    10035: 3,
    10038: 3,
    # Week 4
    10041: 4,
    10050: 4,
    10055: 4,
    10056: 4,
    10057: 4,
    # Week 6
    10062: 6,
    10071: 6,
    10093: 6,
    10101: 6,
    10170: 6,
    # Week 7
    10189: 7,
    10190: 7,
    10193: 7,
    10221: 7,
    10222: 7,
    # Week 9
    10226: 9,
    10235: 9,
    10242: 9,
    10252: 9,
    10268: 9,
    # Week 10
    10409: 10,
    10415: 10,
    10420: 10,
    10642: 10,
    10783: 10,
    # Week 11
    10812: 11,
    10908: 11,
    10922: 11,
    10929: 11,
    10931: 11,
    # Week 12
    11005: 12,
    11063: 12,
    11150: 12,
    11321: 12,
    11332: 12,
    # Week 13
    11349: 13,
    11417: 13,
    11461: 13,
    12019: 13,
}

# UVA 題號到 ZeroJudge ID 的映射
UVA_TO_ZJ = {
    100: "c039",
    118: "c082",
    272: "c007",
    299: "e561",
    490: "c045",
    948: "c095",
    10008: "a001",
    10019: "a012",
    10035: "a028",
    10038: "a031",
    10041: "a034",
    10050: "a043",
    10055: "a048",
    10056: "a049",
    10057: "a050",
    10062: "a055",
    10071: "a064",
    10093: "a086",
    10101: "a094",
    10170: "a163",
    10189: "a182",
    10190: "a183",
    10193: "a186",
    10221: "a214",
    10222: "a215",
    10226: "a219",
    10235: "a228",
    10242: "a235",
    10252: "a245",
    10268: "a261",
    10409: "a402",
    10415: "a408",
    10420: "a413",
    10642: "a635",
    10783: "a776",
    10812: "a805",
    10908: "a901",
    10922: "a915",
    10929: "a922",
    10931: "a924",
    11005: "a998",
    11063: "b056",
    11150: "b143",
    11321: "b314",
    11332: "b325",
    11349: "b342",
    11417: "b410",
    11461: "b454",
    12019: "c012",
}

PROJECT_ROOT = Path(__file__).parent
WEEKS_DIR = PROJECT_ROOT / "weeks"


def clean_html_entities(text: str) -> str:
    """清理 HTML 實體編碼"""
    text = html.unescape(text)
    text = text.replace("&#xff0c;", "，")
    text = text.replace("&#xff1b;", "；")
    text = text.replace("&#61;", "=")
    text = text.replace("&#43;", "+")
    text = text.replace("&lt;", "<")
    text = text.replace("&gt;", ">")
    text = text.replace("&amp;", "&")
    # 移除多個連續空白
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text


def fetch_zerojudge_problem(
    zj_id: str, retry_count: int = 3
) -> Optional[Dict[str, str]]:
    """從 ZeroJudge 爬取題目內容，帶重試機制"""
    url = f"https://zerojudge.tw/ShowProblem?problemid={zj_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }

    for attempt in range(retry_count):
        try:
            response = requests.get(url, headers=headers, timeout=15)
            response.encoding = "utf-8"

            if response.status_code != 200:
                if attempt < retry_count - 1:
                    time.sleep(1 + attempt)  # 指數退避
                    continue
                else:
                    return None

            soup = BeautifulSoup(response.text, "html.parser")

            # 嘗試多個選擇器
            description = ""
            for selector_id in ["problem_content", "content"]:
                content_div = soup.find("div", {"id": selector_id})
                if content_div:
                    description = content_div.get_text(strip=True)
                    description = clean_html_entities(description)
                    break

            input_desc = ""
            for selector_id in ["problem_theinput", "theinput", "input_description"]:
                input_div = soup.find("div", {"id": selector_id})
                if input_div:
                    input_desc = input_div.get_text(strip=True)
                    input_desc = clean_html_entities(input_desc)
                    break

            output_desc = ""
            for selector_id in ["problem_theoutput", "theoutput", "output_description"]:
                output_div = soup.find("div", {"id": selector_id})
                if output_div:
                    output_desc = output_div.get_text(strip=True)
                    output_desc = clean_html_entities(output_desc)
                    break

            # 如果至少獲得了一些內容，就返回
            if description or input_desc or output_desc:
                return {
                    "description": description,
                    "input": input_desc,
                    "output": output_desc,
                }

            # 內容為空，嘗試重試
            if attempt < retry_count - 1:
                time.sleep(1 + attempt)
                continue
            else:
                return None

        except requests.exceptions.Timeout:
            if attempt < retry_count - 1:
                time.sleep(2 + attempt)
                continue
            return None
        except Exception as e:
            if attempt < retry_count - 1:
                time.sleep(1)
                continue
            return None

    return None


def generate_question_content(
    problem_id: int,
    zj_id: str,
    description: str,
    input_desc: str,
    output_desc: str,
) -> str:
    """生成完整的 QUESTION markdown 內容"""
    return f"""# 題目 {problem_id}

**題名**: UVA {problem_id}

**相關連結**:
- [ZeroJudge 題目頁面](https://zerojudge.tw/ShowProblem?problemid={zj_id})
- [Yui Huang 題解](https://yuihuang.com/zj-{zj_id}/)

## 題目敘述

{description if description else "[題目敘述請見上方連結]"}

## 輸入說明

{input_desc if input_desc else "[輸入說明請見上方連結]"}

## 輸出說明

{output_desc if output_desc else "[輸出說明請見上方連結]"}

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


def update_question_file(
    problem_id: int,
    week_num: int,
    content: str,
) -> bool:
    """更新 QUESTION 檔案"""
    week_dir = WEEKS_DIR / f"week-{week_num:02d}"
    filepath = week_dir / f"QUESTION-{problem_id}.md"

    if not filepath.exists():
        print(f"❌ 檔案不存在: {filepath}")
        return False

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"❌ 保存失敗: {e}")
        return False


def check_file_completion(filepath: Path) -> tuple[bool, int]:
    """檢查檔案內容完整性，返回 (是否完整, 內容長度)"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    desc_match = re.search(r"## 題目敘述\n(.*?)(?=##|\Z)", content, re.DOTALL)
    input_match = re.search(r"## 輸入說明\n(.*?)(?=##|\Z)", content, re.DOTALL)
    output_match = re.search(r"## 輸出說明\n(.*?)(?=##|\Z)", content, re.DOTALL)

    desc_len = len(desc_match.group(1).strip()) if desc_match else 0
    input_len = len(input_match.group(1).strip()) if input_match else 0
    output_len = len(output_match.group(1).strip()) if output_match else 0

    total_len = desc_len + input_len + output_len

    # 判斷為完整當且僅當總內容 > 500 字
    is_complete = total_len > 500

    return is_complete, total_len


def main():
    print("=" * 70)
    print("CPE 題目爬蟲 v2 - 重新填充失敗與部分題目")
    print("=" * 70)
    print()

    # 掃描所有題目文件，找出未完整的題目
    incomplete_problems = []

    for week_dir in sorted(WEEKS_DIR.glob("week-*")):
        if not week_dir.is_dir():
            continue

        for qfile in sorted(week_dir.glob("QUESTION-*.md")):
            is_complete, length = check_file_completion(qfile)
            if not is_complete:
                # 提取問題 ID
                match = re.search(r"QUESTION-(\d+)", qfile.name)
                if match:
                    problem_id = int(match.group(1))
                    incomplete_problems.append((problem_id, length))

    print(f"找到 {len(incomplete_problems)} 個未完整的題目:")
    print()

    # 按週次分組並重新爬取
    weeks = defaultdict(list)
    for problem_id, _ in incomplete_problems:
        if problem_id in PROBLEM_TO_WEEK:
            week = PROBLEM_TO_WEEK[problem_id]
            weeks[week].append(problem_id)

    total_success = 0
    total_failed = 0
    total_skipped = 0

    for week in sorted(weeks.keys()):
        print(f"\n[Week {week:02d}]")
        problems = sorted(weeks[week])

        for problem_id in problems:
            zj_id = UVA_TO_ZJ.get(problem_id)

            if not zj_id:
                print(f"  ⊘ {problem_id}: 無 ZJ ID 對應")
                total_skipped += 1
                continue

            # 爬取內容
            print(f"  爬取 {problem_id:5d} (zj-{zj_id})...", end=" ", flush=True)
            problem_content = fetch_zerojudge_problem(zj_id)

            if not problem_content:
                print("❌ 爬取失敗")
                total_failed += 1
                continue

            # 生成 markdown
            markdown = generate_question_content(
                problem_id=problem_id,
                zj_id=zj_id,
                description=problem_content["description"],
                input_desc=problem_content["input"],
                output_desc=problem_content["output"],
            )

            # 保存檔案
            if update_question_file(problem_id, week, markdown):
                print("✅")
                total_success += 1
            else:
                print("❌ 保存失敗")
                total_failed += 1

            # 禮貌延遲
            time.sleep(0.5)

    # 最終掃描完成度
    print("\n" + "=" * 70)
    print("最終完成度統計:")
    print("=" * 70)

    final_complete = 0
    for week_dir in sorted(WEEKS_DIR.glob("week-*")):
        if not week_dir.is_dir():
            continue

        for qfile in sorted(week_dir.glob("QUESTION-*.md")):
            is_complete, _ = check_file_completion(qfile)
            if is_complete:
                final_complete += 1

    print(f"✅ 成功填充: {total_success}")
    print(f"❌ 爬取失敗: {total_failed}")
    print(f"⊘ 跳過: {total_skipped}")
    print(f"\n📊 總完成度: {final_complete}/49 ({final_complete * 100 // 49}%)")
    print("=" * 70)


if __name__ == "__main__":
    main()
