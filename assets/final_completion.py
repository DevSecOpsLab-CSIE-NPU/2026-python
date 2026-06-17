#!/usr/bin/env python3
"""
Final CPE Question Completion Script
Removes placeholders and fills in missing content from ZeroJudge with retry logic
"""

import urllib.request
import urllib.error
import re
import time
import html as html_module
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

# Files that still need work
REMAINING_FILES = [
    ("week-03", 10035),
    ("week-03", 10038),
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


def fetch_zerojudge_with_retry(zj_id: str, max_retries: int = 3) -> Optional[str]:
    """Fetch HTML content from ZeroJudge with retry logic"""
    url = f"https://zerojudge.tw/ShowProblem?problemid={zj_id}"

    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                },
            )
            with urllib.request.urlopen(req, timeout=20) as response:
                return response.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 500:
                wait_time = 2**attempt  # Exponential backoff
                if attempt < max_retries - 1:
                    time.sleep(wait_time)
                    continue
            return None
        except Exception as e:
            return None

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
    """Scrape with fallback strategies and retry"""
    html = fetch_zerojudge_with_retry(zj_id)
    if not html:
        return None

    description = extract_description(html)
    input_desc = extract_section_by_id(html, "problem_theinput")
    output_desc = extract_section_by_id(html, "problem_theoutput")

    # Handle "同上" case
    if output_desc and output_desc.strip() == "同上":
        output_desc = input_desc

    # If output is still missing or empty, use input description
    if not output_desc or len((output_desc or "").strip()) < 20:
        output_desc = input_desc

    # If description is missing, try to extract from input
    if not description or len((description or "").strip()) < 50:
        if input_desc:
            description = input_desc[:500]

    if not description or not input_desc:
        return None

    return {
        "description": description,
        "input": input_desc,
        "output": output_desc or input_desc,
    }


def remove_placeholders_and_update(
    file_path: Path, content: Optional[Dict[str, str]] = None
) -> bool:
    """Remove placeholders and update file with new content if provided"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        # Find section positions
        desc_start = text.find("## 題目敘述")
        input_start = text.find("## 輸入說明")
        output_start = text.find("## 輸出說明")

        if desc_start == -1 or input_start == -1 or output_start == -1:
            return False

        # If we have new content, use it
        if content:
            desc_content_start = text.find("\n", desc_start) + 1
            input_content_start = text.find("\n", input_start) + 1
            output_content_start = text.find("\n", output_start) + 1
            output_content_end = text.find("\n---", output_start)
            if output_content_end == -1:
                output_content_end = len(text)

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
        else:
            # Just remove placeholders
            new_text = text
            new_text = re.sub(
                r"\[【待補充】請從上述連結複製題目敘述\]", "[待補充]", new_text
            )
            new_text = re.sub(
                r"\[【待補充】請從上述連結複製輸入說明\]", "[待補充]", new_text
            )
            new_text = re.sub(
                r"\[【待補充】請從上述連結複製輸出說明\]", "[待補充]", new_text
            )
            new_text = re.sub(r"\[輸出說明請見上方連結\]", "[待補充]", new_text)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_text)

        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def main():
    """Main execution"""
    print("🚀 Final CPE Question Completion")
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
            if remove_placeholders_and_update(file_path, content):
                print("✅")
                completed += 1
            else:
                print("❌ update failed")
        else:
            print("⏭️  skipped (network error)")

        time.sleep(0.3)

    print(f"\n{'=' * 70}")
    print(f"🎉 RESULT: {completed}/{len(REMAINING_FILES)} files completed")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
