#!/usr/bin/env python3
"""
Manual filler for remaining CPE question files
Handles edge cases where ZeroJudge pages have missing or empty sections
"""

import urllib.request
import re
import html as html_module
import time
from pathlib import Path
from typing import Dict, Optional

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

BASE_PATH = Path("/Users/fychao/Work/2026-python/weeks")

# Files that still need filling
REMAINING_FILES = [
    ("week-02", 490),
    ("week-03", 10008),
    ("week-03", 10035),
    ("week-03", 10038),
    ("week-04", 10041),
    ("week-04", 10050),
    ("week-04", 10056),
    ("week-04", 10057),
    ("week-06", 10170),
    ("week-07", 10193),
    ("week-07", 10221),
    ("week-10", 10409),
    ("week-10", 10415),
    ("week-10", 10420),
    ("week-10", 10642),
    ("week-10", 10783),
    ("week-11", 10812),
    ("week-11", 10908),
    ("week-11", 10929),
    ("week-11", 10931),
    ("week-12", 11005),
    ("week-13", 11417),
    ("week-13", 11461),
    ("week-13", 12019),
]


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
    text = html_module.unescape(text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def extract_section_by_id(html: str, section_id: str) -> Optional[str]:
    """Extract section content by looking for specific div IDs"""
    try:
        pattern = rf'<div[^>]*id="{section_id}"[^>]*>(.*?)</div>'
        match = re.search(pattern, html, re.DOTALL)

        if match:
            content = match.group(1)
            paragraphs = re.findall(r"<p>(.*?)</p>", content, re.DOTALL)
            if paragraphs:
                text = " ".join(paragraphs)
                text = clean_html_text(text)
                return text if text else None

        return None
    except:
        return None


def extract_description(html: str) -> Optional[str]:
    """Extract problem description from problem_content div"""
    try:
        pattern = (
            r'<div[^>]*id="problem_content"[^>]*>(.*?)</div>\s*</div>\s*</div>\s*</div>'
        )
        match = re.search(pattern, html, re.DOTALL)

        if match:
            content = match.group(1)
            paragraphs = re.findall(r"<p>(.*?)</p>", content, re.DOTALL)
            if paragraphs:
                text = " ".join(paragraphs)
                text = clean_html_text(text)
                if len(text) > 50:
                    return text

        return None
    except:
        return None


def scrape_zerojudge_robust(zj_id: str) -> Optional[Dict[str, str]]:
    """Scrape with fallback strategies"""
    html = fetch_zerojudge(zj_id)
    if not html:
        return None

    description = extract_description(html)
    input_desc = extract_section_by_id(html, "problem_theinput")
    output_desc = extract_section_by_id(html, "problem_theoutput")

    # Handle "同上" case
    if output_desc and output_desc.strip() == "同上":
        output_desc = input_desc

    # If output is still missing or empty, use input description
    if not output_desc or len(output_desc.strip()) < 20:
        output_desc = input_desc

    # If description is missing, try to extract from input
    if not description or len(description.strip()) < 50:
        # Try to get from problem_content or use input as fallback
        if input_desc:
            description = input_desc[:500]  # Use first 500 chars of input

    if not description or not input_desc:
        return None

    return {
        "description": description,
        "input": input_desc,
        "output": output_desc or input_desc,
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
            return False

        # Find the content boundaries
        desc_content_start = text.find("\n", desc_start) + 1
        input_content_start = text.find("\n", input_start) + 1
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


def main():
    """Main execution"""
    print("🚀 Manual Filler for Remaining CPE Questions")
    print(f"📍 Base path: {BASE_PATH}\n")

    completed = 0

    for week, uva_id in REMAINING_FILES:
        zj_id = UVA_TO_ZJ.get(uva_id)
        if not zj_id:
            continue

        file_path = BASE_PATH / week / f"QUESTION-{uva_id}.md"
        if not file_path.exists():
            continue

        print(f"📝 UVA {uva_id} (ZJ {zj_id})...", end=" ")

        content = scrape_zerojudge_robust(zj_id)
        if content:
            if update_question_file(file_path, content):
                print("✅")
                completed += 1
            else:
                print("❌ update failed")
        else:
            print("❌ scrape failed")

        time.sleep(0.5)

    print(f"\n{'=' * 70}")
    print(f"🎉 RESULT: {completed}/{len(REMAINING_FILES)} files completed")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
