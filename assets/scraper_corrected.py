#!/usr/bin/env python3
"""
CPE Question Content Scraper - Corrected Version
Fetches missing content from ZeroJudge and fills QUESTION-*.md files
"""

import urllib.request
import urllib.error
import re
import time
import html as html_module
from pathlib import Path
from typing import Dict, Optional

# UVA to ZeroJudge ID mapping
UVA_TO_ZJ = {
    272: "c007",
    490: "c045",
    10008: "c044",
    10035: "c014",
    10038: "d097",
    10041: "a737",
    10050: "e579",
    10056: "e510",
    10057: "e606",
    10170: "a041",
    10193: "a084",
    10221: "e483",
    10222: "e484",
    10409: "b025",
    10415: "c011",
    10420: "d016",
    10642: "e619",
    10783: "e837",
    10812: "a680",
    10908: "a853",
    10929: "a875",
    10931: "a877",
    11005: "a901",
    11417: "c080",
    11461: "d224",
    12019: "e652",
}

# Priority 1: Week 2-4 (CORRECTED WEEKS)
PRIORITY_1 = {
    "week-02": [272, 490],
    "week-03": [10008, 10035, 10038],
    "week-04": [10041, 10050, 10056, 10057],
}

# Priority 2: Week 6-7
PRIORITY_2 = {
    "week-06": [10170],
    "week-07": [10193, 10221, 10222],
}

# Priority 3: Week 9-13 (CORRECTED WEEKS)
PRIORITY_3 = {
    "week-10": [10409, 10415, 10420, 10642, 10783],
    "week-11": [10812, 10908, 10929, 10931],
    "week-12": [11005],
    "week-13": [11417, 11461, 12019],
}

BASE_PATH = Path("/Users/fychao/Work/2026-python/weeks")


def fetch_zerojudge(zj_id: str) -> Optional[str]:
    """Fetch HTML content from ZeroJudge"""
    url = f"https://zerojudge.tw/ShowProblem?problemid={zj_id}"

    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"},
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"  ❌ Network error: {e}")
        return None


def clean_html_text(text: str) -> str:
    """Clean HTML entities and tags from text"""
    # Decode HTML entities
    text = html_module.unescape(text)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Clean whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_section_by_id(html: str, section_id: str) -> Optional[str]:
    """Extract section content by looking for specific div IDs"""
    try:
        # Look for div with id="problem_theinput", "problem_theoutput", etc.
        pattern = rf'<div[^>]*id="{section_id}"[^>]*>(.*?)</div>'
        match = re.search(pattern, html, re.DOTALL)

        if match:
            content = match.group(1)
            # Extract text from paragraphs
            paragraphs = re.findall(r"<p>(.*?)</p>", content, re.DOTALL)
            if paragraphs:
                text = " ".join(paragraphs)
                text = clean_html_text(text)
                return text if text else None

        return None
    except Exception as e:
        print(f"  ⚠️  Parse error for {section_id}: {e}")
        return None


def extract_description(html: str) -> Optional[str]:
    """Extract problem description from problem_content div"""
    try:
        # Look for problem_content div
        pattern = (
            r'<div[^>]*id="problem_content"[^>]*>(.*?)</div>\s*</div>\s*</div>\s*</div>'
        )
        match = re.search(pattern, html, re.DOTALL)

        if match:
            content = match.group(1)
            # Extract text from paragraphs
            paragraphs = re.findall(r"<p>(.*?)</p>", content, re.DOTALL)
            if paragraphs:
                text = " ".join(paragraphs)
                text = clean_html_text(text)
                if len(text) > 50:
                    return text

        return None
    except Exception as e:
        print(f"  ⚠️  Parse error for description: {e}")
        return None


def scrape_zerojudge(zj_id: str) -> Optional[Dict[str, str]]:
    """Scrape problem content from ZeroJudge"""
    html = fetch_zerojudge(zj_id)
    if not html:
        return None

    # Extract sections
    description = extract_description(html)
    input_desc = extract_section_by_id(html, "problem_theinput")
    output_desc = extract_section_by_id(html, "problem_theoutput")

    # Handle "同上" case - if output is "同上", use input description
    if output_desc and output_desc.strip() == "同上":
        output_desc = input_desc

    if not description or not input_desc or not output_desc:
        print(
            f"  ⚠️  Missing sections: desc={bool(description)}, input={bool(input_desc)}, output={bool(output_desc)}"
        )
        return None

    return {
        "description": description,
        "input": input_desc,
        "output": output_desc,
    }


def update_question_file(file_path: Path, content: Dict[str, str]) -> bool:
    """Update QUESTION-*.md file with scraped content"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Find section positions
        desc_start = text.find("## 題目敘述")
        input_start = text.find("## 輸入說明")
        output_start = text.find("## 輸出說明")

        if desc_start == -1 or input_start == -1 or output_start == -1:
            print(f"  ❌ Cannot find section markers")
            return False

        # Find the content boundaries (between headers)
        desc_content_start = text.find("\n", desc_start) + 1
        desc_content_end = input_start

        input_content_start = text.find("\n", input_start) + 1
        input_content_end = output_start

        output_content_start = text.find("\n", output_start) + 1
        output_content_end = text.find("\n---", output_start)
        if output_content_end == -1:
            output_content_end = len(text)

        # Build new content
        new_text = (
            text[:desc_content_start]
            + "\n"
            + content["description"]
            + "\n\n"
            + text[input_start:input_content_start]
            + "\n"
            + content["input"]
            + "\n\n"
            + text[output_start:output_content_start]
            + "\n"
            + content["output"]
            + "\n\n"
            + text[output_content_end:]
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_text)

        return True
    except Exception as e:
        print(f"  ❌ File update error: {e}")
        return False


def process_priority(priority_dict: Dict[str, list], priority_name: str) -> int:
    """Process all files in a priority level"""
    completed = 0
    total = sum(len(ids) for ids in priority_dict.values())

    for week, uva_ids in priority_dict.items():
        for uva_id in uva_ids:
            zj_id = UVA_TO_ZJ.get(uva_id)
            if not zj_id:
                print(f"⚠️  No ZJ mapping for UVA {uva_id}")
                continue

            file_path = BASE_PATH / week / f"QUESTION-{uva_id}.md"
            if not file_path.exists():
                print(f"⚠️  File not found: {file_path}")
                continue

            print(f"📝 UVA {uva_id} (ZJ {zj_id})...", end=" ")

            content = scrape_zerojudge(zj_id)
            if content:
                if update_question_file(file_path, content):
                    print("✅")
                    completed += 1
                else:
                    print("❌ update failed")
            else:
                print("❌ scrape failed")

            time.sleep(0.5)  # Rate limiting

    return completed


def main():
    """Main execution"""
    print("🚀 CPE Question Content Scraper - Corrected Version")
    print(f"📍 Base path: {BASE_PATH}\n")

    total_completed = 0

    # Priority 1
    print("=" * 70)
    print("PRIORITY 1: Week 2-4 (9 questions)")
    print("=" * 70)
    completed = process_priority(PRIORITY_1, "Priority 1")
    total_completed += completed
    print(f"✅ Priority 1: {completed}/9 completed\n")

    # Priority 2
    print("=" * 70)
    print("PRIORITY 2: Week 6-7 (4 questions)")
    print("=" * 70)
    completed = process_priority(PRIORITY_2, "Priority 2")
    total_completed += completed
    print(f"✅ Priority 2: {completed}/4 completed\n")

    # Priority 3
    print("=" * 70)
    print("PRIORITY 3: Week 10-13 (13 questions)")
    print("=" * 70)
    completed = process_priority(PRIORITY_3, "Priority 3")
    total_completed += completed
    print(f"✅ Priority 3: {completed}/13 completed\n")

    print("=" * 70)
    print(f"🎉 FINAL RESULT: {total_completed}/26 files completed")
    print("=" * 70)


if __name__ == "__main__":
    main()
